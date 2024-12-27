import requests
from JoKeRUB import l313l

plugin_category = "الادوات"

# البحث عن رابط YouTube
def search_youtube(song_name):
    search_url = f"https://www.youtube.com/results?search_query={song_name.replace(' ', '+')}"
    response = requests.get(search_url).text
    video_id = response.split('{"videoId":"')[1].split('"')[0]
    return f"https://www.youtube.com/watch?v={video_id}"

# إضافة أمر جديد "بحث يوت"
@l313l.ar_cmd(
    pattern="بحث (.+)",
    command=("بحث", plugin_category),
    info={
        "header": "لـ البحث عن رابط YouTube لأغنية",
        "الاستخـدام": "{tr}بحث يوت <اسم الأغنية>",
    },
)
async def search_song_on_youtube(event):
    # استخراج اسم الأغنية من الرسالة
    song_name = event.pattern_match.group(1).strip()
    
    if song_name:
        try:
            youtube_link = search_youtube(song_name)
            await event.respond(f"{youtube_link}")
        except Exception as e:
            await event.edit("حدث خطأ أثناء البحث.")
    else:
        await event.edit("يرجى إدخال اسم البحث بعد الأمر.")
