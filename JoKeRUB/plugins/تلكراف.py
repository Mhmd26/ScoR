import requests
import os
from telegraph import Telegraph, upload_file
from JoKeRUB import l313l

plugin_category = "الادوات"

# إعداد Telegraph
telegraph = Telegraph()
telegraph.create_account(short_name="JoKeRUB")

# مفتاح API الخاص بـ ImgBB
imgbb_api_key = "2c13527e292170493a5313151f57ce1c"

# رفع صورة إلى ImgBB
def upload_to_imgbb(image_path):
    try:
        with open(image_path, "rb") as img_file:
            url = "https://api.imgbb.com/1/upload"
            files = {"image": img_file.read()}
            payload = {"key": imgbb_api_key}
            response = requests.post(url, data=payload, files=files)
            result = response.json()
            if response.status_code == 200 and result.get('status') == 200:
                imgbb_url = result['data']['url']
                return imgbb_url
            else:
                error_message = result.get('error', {}).get('message', 'خطأ غير معروف.')
                return f"حدث خطأ أثناء رفع الصورة: {error_message}"
    except Exception as e:
        return f"حدث خطأ: {e}"

# رفع صورة إلى Telegraph
def upload_to_telegraph(image_path):
    try:
        media_urls = upload_file(image_path)
        return f"https://telegra.ph{media_urls[0]}"
    except Exception as e:
        return f"حدث خطأ أثناء رفع الصورة إلى تليجراف: {e}"

# رفع نص إلى Telegraph
def upload_text_to_telegraph(title, content):
    try:
        response = telegraph.create_page(title=title, html_content=content)
        return f"https://telegra.ph/{response['path']}"
    except Exception as e:
        return f"حدث خطأ أثناء رفع النص إلى تليجراف: {e}"

# أمر رفع الصور بالرد
@l313l.ar_cmd(
    pattern="تلكراف ميديا (imgbb|telegraph)$",
    command=("تلكراف ميديا", plugin_category),
    info={
        "header": "لرفع صورة إلى ImgBB أو Telegraph.",
        "الاستخدام": "{tr}تلكراف ميديا <imgbb|telegraph> (بالرد على الصورة)",
    },
)
async def upload_image(event):
    reply = await event.get_reply_message()
    service = event.pattern_match.group(1).strip().lower()  # اختيار الخدمة (ImgBB أو Telegraph)

    if reply and reply.photo:
        await event.edit(f"**✎┊‌انتظر يتم رفع الصورة إلى {service}...**")
        photo = await event.client.download_media(reply.photo, file="temp_image.jpg")
        
        if service == "imgbb":
            link = upload_to_imgbb(photo)
        elif service == "telegraph":
            link = upload_to_telegraph(photo)
        else:
            await event.edit("خدمة غير معروفة. اختر بين `imgbb` أو `telegraph`.")
            os.remove(photo)
            return

        await event.respond(f"رابط الصورة:\n{link}")
        os.remove(photo)  # حذف الصورة المؤقتة بعد الرفع
        await event.delete()
    else:
        await event.edit("يرجى الرد على صورة لاستخدام هذا الأمر.")

# أمر رفع النصوص إلى Telegraph
@l313l.ar_cmd(
    pattern="تلكراف نص(?:\s|$)([\s\S]*)",
    command=("تلكراف نص", plugin_category),
    info={
        "header": "لرفع نص إلى Telegraph.",
        "الاستخدام": "{tr}تلكراف نص <عنوان اختياري> (بالرد على النص)",
    },
)
async def upload_text(event):
    reply = await event.get_reply_message()
    title = event.pattern_match.group(1).strip() or "نص بدون عنوان"  # عنوان النص
    
    if reply and reply.text:
        await event.edit("**✎┊‌انتظر يتم رفع النص إلى Telegraph...**")
        content = reply.text.replace("\n", "<br>")  # تنسيق النص
        link = upload_text_to_telegraph(title, content)
        await event.respond(f"رابط النص:\n{link}")
        await event.delete()
    else:
        await event.edit("يرجى الرد على نص لاستخدام هذا الأمر.")
    
