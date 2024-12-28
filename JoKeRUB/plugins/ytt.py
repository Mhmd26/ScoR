import requests
from yt_dlp import YoutubeDL
from JoKeRUB import l313l
import os

plugin_category = "الادوات"

# البحث عن رابط YouTube
def search_youtube(song_name):
    search_url = f"https://www.youtube.com/results?search_query={song_name.replace(' ', '+')}"
    response = requests.get(search_url).text
    video_id = response.split('{"videoId":"')[1].split('"')[0]
    return f"https://www.youtube.com/watch?v={video_id}"

# تحميل مقطع صوتي من YouTube
def download_audio_from_youtube(video_url):
    ydl_opts = {
        "format": "bestaudio/best",
        "outtmpl": "audio.%(ext)s",
        "postprocessors": [
            {"key": "FFmpegExtractAudio", "preferredcodec": "mp3", "preferredquality": "192"}
        ],
    }
    with YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(video_url, download=True)
        file_path = ydl.prepare_filename(info).replace(".webm", ".mp3").replace(".m4a", ".mp3")
        return file_path, info["title"], int(info["duration"])

# أمر البحث على YouTube
@l313l.ar_cmd(
    pattern="بحث (.+)",
    command=("بحث", plugin_category),
    info={
        "header": "لـ البحث عن رابط YouTube لأغنية",
        "الاستخدام": "{tr}بحث <اسم الأغنية>",
    },
)
async def search_song_on_youtube(event):
    song_name = event.pattern_match.group(1).strip()
    
    if song_name:
        try:
            await event.edit("**✎┊‌انتظر يتم جلب طلبك**")
            youtube_link = search_youtube(song_name)
            await event.respond(f"{youtube_link}")
            await event.delete()
        except Exception as e:
            await event.edit("حدث خطأ أثناء البحث.")
    else:
        await event.edit("يرجى إدخال اسم البحث بعد الأمر.")

# أمر تحميل الصوت من YouTube
@l313l.ar_cmd(
    pattern="يوت (.+)",
    command=("يوت", plugin_category),
    info={
        "header": "تحميل مقطع صوتي من رابط YouTube",
        "الاستخدام": "{tr}يوت <رابط المقطع>",
    },
)
async def download_audio(event):
    video_url = event.pattern_match.group(1).strip()
    
    if video_url:
        try:
            await event.edit("**✎┊‌جاري تحميل الصوت، انتظر قليلاً...**")
            file_path, title, duration = download_audio_from_youtube(video_url)
            caption = (
                f"**✎┊العنوان:** {title}\n"
                f"**✎┊المدة:** {duration} ثوانٍ\n"
            )
            await event.respond(file=file_path, caption=caption)
            os.remove(file_path)  # حذف الملف بعد الإرسال
            await event.delete()
        except Exception as e:
            await event.edit("حدث خطأ أثناء تحميل المقطع.")
    else:
        await event.edit("يرجى إدخال رابط المقطع بعد الأمر.")
