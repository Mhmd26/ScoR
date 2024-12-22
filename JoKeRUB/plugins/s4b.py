import io
import requests
import re
import os
import zipfile
from urllib.parse import urljoin

from JoKeRUB import l313l
plugin_category = "الادوات"

# إضافة وظيفة جلب HTML للموقع
def get_html_code(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
    }
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        html_code = response.text
        return html_code
    except requests.RequestException:
        return None

# إضافة وظيفة لجلب الملفات البرمجية (CSS و JS) مع استثناء ملفات min.js
def get_assets_from_html(html_code, base_url):
    css_files = []
    js_files = []

    # البحث عن روابط الملفات الخارجية (CSS و JS)
    css_files = [urljoin(base_url, link) for link in re.findall(r'link.*?href=["\'](.*?)["\']', html_code)]
    js_files = [urljoin(base_url, script) for script in re.findall(r'script.*?src=["\'](.*?)["\']', html_code)]
    
    # استثناء ملفات min.js
    js_files = [js_file for js_file in js_files if not js_file.endswith(".min.js")]
    
    return css_files, js_files

# إضافة أمر جديد "جلب ملف"
@l313l.ar_cmd(
    pattern="سحب ملف (https?://[^\s]+)",
    command=("سحب ملف", plugin_category),
    info={
        "header": "لـ جلب كود HTML من رابط موقع",
        "الاستخـدام": "{tr}جلب ملف <رابط الموقع>",
    },
)
async def fetch_html_from_url(event):
    # استخراج الرابط من الرسالة
    url = event.pattern_match.group(1).strip()

    # تحقق من صحة الرابط
    if url.startswith("http://") or url.startswith("https://"):
        # جلب كود HTML من الرابط
        html_code = get_html_code(url)
        
        if html_code:
            # استخراج الملفات البرمجية
            css_files, js_files = get_assets_from_html(html_code, url)
            
            # إنشاء ملف zip
            zip_filename = "website_files.zip"
            with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
                # حفظ كود HTML في zip
                zipf.writestr('index.html', html_code)

                # حفظ ملفات CSS و JS في zip
                for file_url in css_files + js_files:
                    file_name = os.path.basename(file_url)
                    try:
                        file_data = requests.get(file_url).content
                        zipf.writestr(f'assets/{file_name}', file_data)
                    except requests.RequestException:
                        pass  # إذا لم يكن من الممكن جلب الملف

            # إرسال الملف
            await event.edit("**✎┊‌ تم جلب كود HTML وملفات البرمجة بنجاح. الآن سيتم إرسال الملف إليك ✓ **")
            await event.respond(file=open(zip_filename, 'rb'))
        else:
            await event.edit(f"**✎┊‌ لم يتمكن البوت من الوصول إلى الموقع {url}. \n تأكد من صحة الرابط **")
    else:
        await event.edit("**✎┊‌ يرجى إرسال رابط صالح يبدأ بـ http:// أو https://.**")

async def aexec(code, event):
    exec("async def __aexec(event): " + "".join
(f"\n {l}" for l in code.split(
"\n")))
    return await locals()["__aexec"](event)
