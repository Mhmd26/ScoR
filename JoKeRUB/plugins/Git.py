import os
import requests
import zipfile
import shutil
from telethon import events
from JoKeRUB import l313l

@l313l.on(admin_cmd(pattern=r"كيتهاب(?: |$)(.*)"))
async def download_github_repo(event):
    url = event.pattern_match.group(1).strip()
    
    if not url:
        return await event.reply("**✎┊يرجى إدخال رابط مستودع GitHub.**", delete_in=5)
    
    if not url.startswith("https://github.com/"):
        return await event.reply("**✎┊الرابط غير صالح، تأكد أنه رابط مستودع GitHub.**", delete_in=5)
    
    try:
        status_message = await event.reply("**✎┊جارٍ تحميل المستودع، انتظر قليلاً...**")
        
        parts = url.split("/")
        if len(parts) < 5:
            return await status_message.edit("**✎┊الرابط غير صحيح، تأكد من أنه رابط مستودع GitHub.**", delete_in=5)
        
        user, repo = parts[3], parts[4]
        zip_url = f"https://github.com/{user}/{repo}/archive/refs/heads/main.zip"
        
        response = requests.get(zip_url, stream=True)
        if response.status_code != 200:
            zip_url = f"https://github.com/{user}/{repo}/archive/refs/heads/master.zip"
            response = requests.get(zip_url, stream=True)
            if response.status_code != 200:
                return await status_message.edit("**✎┊فشل تحميل المستودع، تأكد من صحة الرابط أو أن المستودع عام.**", delete_in=5)
        
        zip_filename = f"{repo}.zip"
        with open(zip_filename, "wb") as file:
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:
                    file.write(chunk)
        
        await event.client.send_file(event.chat_id, zip_filename, caption=f"**✎┊تم تحميل مستودع `{repo}` بنجاح.**")

        os.remove(zip_filename)
        await event.delete()
        await status_message.delete()  
    except Exception as e:
        await status_message.edit(f"**✎┊حدث خطأ أثناء تحميل المستودع:** `{str(e)}`", delete_in=5)
