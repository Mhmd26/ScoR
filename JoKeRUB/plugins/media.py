import yt_dlp
import requests
from JoKeRUB import l313l
import os

plugin_category = "الادوات"

# تحميل فيديو من إنستغرام باستخدام yt-dlp
def download_instagram_video(url):
    try:
        ydl_opts = {
            'quiet': True,
            'extractaudio': False,
            'outtmpl': 'instagram_video.%(ext)s',
            'format': 'bestvideo+bestaudio/best',
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=True)
            video_file = ydl.prepare_filename(info_dict).replace(".webm", ".mp4")
            return video_file
    except Exception as e:
        print("حدث خطأ:", e)
        return None

# تحميل فيديو من تيك توك باستخدام API
def download_tiktok_video(url):
    try:
        response = requests.get(f"https://www.tikwm.com/api/?url={url}").json()
        video_url = response["data"]["play"]
        return video_url
    except Exception as e:
        print("حدث خطأ:", e)
        return None

# تحميل فيديو تيك توك وحفظه محليًا
def save_tiktok_video(url, save_path="tiktok_video.mp4"):
    video_url = download_tiktok_video(url)
    if video_url:
        video_content = requests.get(video_url).content
        with open(save_path, 'wb') as f:
            f.write(video_content)
        return save_path
    return None

# أمر تحميل فيديو إنستغرام
@l313l.ar_cmd(
    pattern="انستا (.+)",
    command=("انستا", plugin_category),
    info={
        "header": "لـ تحميل فيديو من إنستغرام",
        "الاستخدام": "{tr}إنستا <رابط إنستغرام>",
    },
)
async def download_instagram(event):
    instagram_url = event.pattern_match.group(1).strip()
    
    if instagram_url:
        try:
            msg = await event.edit("**✎┊‌ انتظر... جاري التحميل من إنستغرام**")
            video_file_path = download_instagram_video(instagram_url)
            if video_file_path:
                with open(video_file_path, 'rb') as video_file:
                    await event.client.send_file(event.chat_id, video_file)
                os.remove(video_file_path)  # حذف الفيديو بعد إرساله
                await msg.delete()  # حذف رسالة الانتظار
            else:
                await msg.edit("**✎┊‌ حدث خطأ أثناء تحميل الفيديو من إنستغرام.**")
        except Exception as e:
            await msg.edit("**✎┊‌ حدث خطأ أثناء تحميل الفيديو من إنستغرام.**")
    else:
        await event.edit("**✎┊‌ يرجى إدخال رابط فيديو إنستغرام بعد الأمر.**")

# أمر تحميل فيديو تيك توك
@l313l.ar_cmd(
    pattern="تيك (.+)",
    command=("تيك", plugin_category),
    info={
        "header": "لـ تحميل فيديو من تيك توك",
        "الاستخدام": "{tr}تحميل <رابط تيك توك>",
    },
)
async def download_tiktok(event):
    tiktok_url = event.pattern_match.group(1).strip()
    
    if tiktok_url:
        try:
            msg = await event.edit("**✎┊‌انتظر... جاري التحميل من تيك توك**")
            saved_video_path = save_tiktok_video(tiktok_url)

            if saved_video_path:
                with open(saved_video_path, 'rb') as video_file:
                    await event.client.send_file(event.chat_id, video_file)
                os.remove(saved_video_path)  # حذف الفيديو بعد إرساله
                await msg.delete()  # حذف رسالة الانتظار
            else:
                await msg.edit("**✎┊‌ حدث خطأ أثناء تحميل الفيديو من تيك توك.**")
        except Exception as e:
            await msg.edit("**✎┊‌ حدث خطأ أثناء تحميل الفيديو من تيك توك.**")
    else:
        await event.edit("**✎┊‌ يرجى إدخال رابط فيديو تيك توك بعد الأمر.**")
                
