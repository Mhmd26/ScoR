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
            await msg.delete()
            if video_file_path:
                with open(video_file_path, 'rb') as video_file:
                    await event.respond(file=video_file)
                os.remove(video_file_path)  # حذف الفيديو بعد إرساله
            else:
                await event.edit("**✎┊‌ حدث خطأ أثناء تحميل الفيديو من إنستغرام.**")
        except Exception as e:
            await event.edit("**✎┊‌ حدث خطأ أثناء تحميل الفيديو من إنستغرام.**")
    else:
        await event.edit("**✎┊‌ يرجى إدخال رابط فيديو إنستغرام بعد الأمر.**")


def download_tiktok_video(url):
    try:
        response = requests.get(f"https://www.tikwm.com/api/?url={url}").json()
        video_url = response["data"]["play"]
        return video_url
    except Exception as e:
        print("حدث خطأ:", e)
        return None

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
            await event.edit("**✎┊‌انتظر... جاري التحميل من تيك توك**")
            video_url = download_tiktok_video(tiktok_url)

            if video_url:
                video_content = requests.get(video_url).content
                await event.delete()
                await event.client.send_file(
                    event.chat_id,
                    file=video_content,
                    force_document=False,  # إرسال كفيديو وليس كملف
                    caption=None  # بدون أي نص
                )

            else:
                await event.edit("**✎┊ حدث خطأ أثناء تحميل الفيديو من تيك توك.**")
        except Exception as e:
            await event.edit("**✎┊ حدث خطأ أثناء تحميل الفيديو من تيك توك.**")
    else:
        await event.edit("**✎┊ يرجى إدخال رابط فيديو تيك توك بعد الأمر.**")
        