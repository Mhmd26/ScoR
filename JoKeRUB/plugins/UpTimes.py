import requests
import threading
import time
from JoKeRUB import l313l
from telethon import events

plugin_category = "الادوات"

# إدارة الروابط
urls = []
lock = threading.Lock()  # قفل لحماية البيانات المشتركة

# المدة المبدئية بين الفحص (بالثواني)
keep_alive_interval = 120  # 2 دقيقة

# وظيفة Keep-Alive للتحقق من الروابط
def keep_alive():
    while True:
        with lock:
            for url in urls:
                try:
                    response = requests.get(url, timeout=5)
                    print(f"Keep-alive successful for {url}, Status: {response.status_code}")
                except Exception as e:
                    print(f"Error keeping {url} alive: {e}")
        time.sleep(keep_alive_interval)  # تكرار العملية حسب المدة المحددة

# بدء Keep-Alive في خيط منفصل
keep_alive_thread = threading.Thread(target=keep_alive, daemon=True)
keep_alive_thread.start()

# إضافة رابط
def add_url(url):
    with lock:
        if url in urls:
            return f"**✎┊‌ الرابط موجود بالفعل 🙂 **"
        else:
            urls.append(url)
            return f"**✎┊‌ تم إضافة الرابط بنجاح ✅ \n {url}**"

# إزالة رابط
def remove_url(index):
    with lock:
        if not urls:
            return "**✎┊‌ لاتوجد روابط لإزالتها ✨**"
        if 0 <= index < len(urls):
            removed_url = urls.pop(index)
            return f"**✎┊‌ تم حذف الرابط ✅ \n {removed_url}**"
        else:
            return "**✎┊‌ الرقم المدخل غير صحيح ❌**"

# عرض قائمة الروابط الشغالة
def get_active_urls():
    active_urls = []
    with lock:
        for url in urls:
            try:
                response = requests.get(url, timeout=5)
                if response.status_code == 200:
                    active_urls.append(url)
            except Exception:
                pass
    return active_urls

# أوامر الروابط (إضافة، حذف، قائمة) للـ JoKeRUB
@l313l.ar_cmd(
    pattern="اضافة رابط (.+)",
    command=("اضافة رابط", plugin_category),
    info={
        "header": "لإضافة رابط إلى قائمة المراقبة",
        "الاستخـدام": "{tr}اضافة رابط <الرابط>",
    },
)
async def add_url_command(event):
    url = event.pattern_match.group(1).strip()
    result = add_url(url)
    await event.edit(result)

@l313l.ar_cmd(
    pattern="حذف رابط (\d+)",
    command=("حذف رابط", plugin_category),
    info={
        "header": "لحذف رابط من قائمة المراقبة",
        "الاستخـدام": "{tr}حذف رابط <رقم الرابط>",
    },
)
async def remove_url_command(event):
    try:
        index = int(event.pattern_match.group(1).strip()) - 1
        result = remove_url(index)
        await event.edit(result)
    except ValueError:
        await event.edit("**✎┊‌ يرجى إدخال رقم صحيح ❌**")

@l313l.ar_cmd(
    pattern="قائمة الروابط$",
    command=("قائمة الروابط", plugin_category),
    info={
        "header": "لعرض جميع الروابط الشغالة من قائمة المراقبة",
        "الاستخـدام": "{tr}قائمة الروابط",
    },
)
async def list_active_urls_command(event):
    await event.edit("**✎┊‌جارٍ جلب قائمة الروابط الشغالة...**")
    active_urls = get_active_urls()
    if active_urls:
        response = "**✎┊‌ الروابط الشغالة **\n" + "\n".join(f"- {url}" for url in active_urls)
    else:
        response = "**✎┊‌ لا توجد روابط شغالة حالياً.**"
    await event.edit(response)

# إضافة أمر لتحديد مدة الفحص
@l313l.ar_cmd(
    pattern="تحديد المدة (\d+)",
    command=("تحديد المدة", plugin_category),
    info={
        "header": "لتحديد مدة الفحص (من 1 إلى 600 ثانية)",
        "الاستخـدام": "{tr}تحديد المدة <المدة>",
    },
)
async def set_keep_alive_interval(event):
    global keep_alive_interval
    try:
        interval = int(event.pattern_match.group(1).strip())
        if 1 <= interval <= 600:
            keep_alive_interval = interval
            await event.edit(f"**✎┊‌ تم تغيير مدة الفحص إلى {interval} ثانية ✅**")
        else:
            await event.edit("**✎┊‌ المدة يجب أن تكون بين 1 و 600 ثانية ❌**")
    except ValueError:
        await event.edit("**✎┊‌ يرجى إدخال مدة صحيحة ❌**")

# إضافة أمر مراقب الروابط
@l313l.ar_cmd(
    pattern="مراقب الروابط",
    command=("مراقب الروابط", plugin_category),
    info={
        "header": "مراقبة المواقع | UpTime 🦂",
        "الاستخـدام": "{tr}.مراقب الروابط",
    },
)
async def command_list(event):
    await event.edit(
        "**✎┊ مراقبة المواقع | UpTime 🦂\n\n"
        "-‌ شرح الامر: \n\n"
        "- { `.اضافة رابط` }\n اكتبه ثم اكتب بعده رابط الموقع الذي تريد مراقبته وفحصه\n- مثال { `.اضافة رابط https://web.com` }\n\n"
        "- { `.حذف رابط` }\n لإزالة الرابط من المراقبة والفحص \n- مثال { `.حذف رابط https://web.com` }\n\n"
        "- { `.قائمة الروابط` }\n لرؤية الروابط التي تتم مراقبتها\n\n"
        "- { `.تحديد المدة` }\n لتحديد مدة زيارة الرابط بالثواني من 1 إلى 600 ثانية\n- مثال { `.تحديد المدة 120` }\n\n"
        "- العقرب | 𝗦𝗰𝗼𝗿𝗽𝗶𝗼 🦂**"
    )
    
