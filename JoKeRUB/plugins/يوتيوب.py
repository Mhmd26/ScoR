import asyncio
import io
import os
import pathlib
import re
import time
from datetime import datetime

from JoKeRUB.utils import sudo_cmd
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl import types
from telethon.utils import get_attributes
from youtube_dl import YoutubeDL
from urlextract import URLExtract
from wget import download
from JoKeRUB import l313l
from youtube_dl.utils import (
    ContentTooShortError,
    DownloadError,
    ExtractorError,
    GeoRestrictedError,
    MaxDownloadsReached,
    PostProcessingError,
    UnavailableVideoError,
    XAttrMetadataError,
)

from ..helpers.utils import _format
from ..helpers.functions.utube import _mp3Dl, get_yt_video_id, get_ytthumb, ytsearch
from ..core.managers import edit_delete, edit_or_reply
from ..helpers import progress, reply_id

plugin_category = "misc"

audio_opts = {
    "format": "bestaudio",
    "addmetadata": True,
    "key": "FFmpegMetadata",
    "writethumbnail": True,
    "prefer_ffmpeg": True,
    "geo_bypass": True,
    "nocheckcertificate": True,
    "postprocessors": [
        {
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
            "preferredquality": "320",
        }
    ],
    "outtmpl": "%(title)s.mp3",
    "quiet": True,
    "logtostderr": False,
}

video_opts = {
    "format": "best",
    "addmetadata": True,
    "key": "FFmpegMetadata",
    "writethumbnail": True,
    "prefer_ffmpeg": True,
    "geo_bypass": True,
    "nocheckcertificate": True,
    "postprocessors": [{"key": "FFmpegVideoConvertor", "preferedformat": "mp4"}],
    "outtmpl": "%(title)s.mp4",
    "logtostderr": False,
    "quiet": True,
}


async def ytdl_down(event, opts, url):
    try:
        await event.edit("✎┊‌ - يتم جلب البيانات انتظر قليلا")
        with YoutubeDL(opts) as ytdl:
            ytdl_data = ytdl.extract_info(url)
    except DownloadError as DE:
        await event.edit(f"`{str(DE)}`")
        return
    except ContentTooShortError:
        await event.edit("✎┊‌ - عذرا هذا المحتوى قصير جدا لتنزيله ⚠️")
        return None
    except GeoRestrictedError:
        await event.edit(
            "✎┊‌ - الفيديو غير متاح من موقعك الجغرافي بسبب القيود الجغرافية التي يفرضها موقع الويب ❕"
        )
        return None
    except MaxDownloadsReached:
        await event.edit("✎┊‌ - تم الوصول إلى الحد الأقصى لعدد التنزيلات ❕")
        return None
    except PostProcessingError:
        await event.edit("✎┊‌ كان هناك خطأ أثناء المعالجة")
        return None
    except UnavailableVideoError:
        await event.edit("`الوسائط غير متوفرة بالتنسيق المطلوب`")
        return None
    except XAttrMetadataError as XAME:
        await event.edit(f"`{XAME.code}: {XAME.msg}\n{XAME.reason}`")
        return None
    except ExtractorError:
        await event.edit("✎┊‌ حدث خطأ أثناء استخراج المعلومات يرجى وضعها بشكل صحيح ⚠️")
        return None
    except Exception as e:
        await event.edit(f"✎┊‌ حدث خطا : \n__{str(e)}__")
        return None
    return ytdl_data


async def fix_attributes(
    path, info_dict: dict, supports_streaming: bool = False, round_message: bool = False
) -> list:
    """Avoid multiple instances of an attribute."""
    new_attributes = []
    video = False
    audio = False

    uploader = info_dict.get("uploader", "Unknown artist")
    duration = int(info_dict.get("duration", 0))
    suffix = path.suffix[1:]
    if supports_streaming and suffix != "mp4":
        supports_streaming = False

    attributes, mime_type = get_attributes(path)
    if suffix == "mp3":
        title = str(info_dict.get("title", info_dict.get("id", "Unknown title")))
        audio = types.DocumentAttributeAudio(duration, None, title, uploader)
    elif suffix == "mp4":
        width = int(info_dict.get("width", 0))
        height = int(info_dict.get("height", 0))
        for attr in attributes:
            if isinstance(attr, types.DocumentAttributeVideo):
                duration = duration or attr.duration
                width = width or attr.w
                height = height or attr.h
                break
        video = types.DocumentAttributeVideo(
            duration, width, height, round_message, supports_streaming
        )

    if audio and isinstance(audio, types.DocumentAttributeAudio):
        new_attributes.append(audio)
    if video and isinstance(video, types.DocumentAttributeVideo):
        new_attributes.append(video)

    for attr in attributes:
        if (
            isinstance(attr, types.DocumentAttributeAudio)
            and not audio
            or not isinstance(attr, types.DocumentAttributeAudio)
            and not video
            or not isinstance(attr, types.DocumentAttributeAudio)
            and not isinstance(attr, types.DocumentAttributeVideo)
        ):
            new_attributes.append(attr)
    return new_attributes, mime_type


async def _get_file_name(path: pathlib.Path, full: bool = True) -> str:
    return str(path.absolute()) if full else path.stem + path.suffix


@l313l.ar_cmd(
    pattern="تحميل ص(?: |$)(.*)",
    command=("تحميل ص", plugin_category),
    info={
        "header": "To download audio from many sites like Youtube",
        "description": "downloads the audio from the given link (Suports the all sites which support youtube-dl)",
        "examples": [
            "{tr}yta <reply to link>",
            "{tr}yta <link>",
        ],
    },
)
async def download_audio(event):
    """To download audio from YouTube and many other sites."""
    url = event.pattern_match.group(1)
    rmsg = await event.get_reply_message()
    if not url and rmsg:
        myString = rmsg.text
        url = re.search("(?P<url>https?://[^\s]+)", myString).group("url")
    if not url:
        return await edit_or_reply(event, "✎┊‌ - يجب وضع رابط لتحميله ❕")
    catevent = await edit_or_reply(event, "✎┊‌ يتم الاعداد انتظر")
    reply_to_id = await reply_id(event)
    ytdl_data = await ytdl_down(catevent, audio_opts, url)
    if ytdl_data is None:

        return
    await catevent.edit(
        f"✎┊‌ يتم لتحميل الأغنية:\
        \n✎┊‌ {ytdl_data['title']}\
        \nبواسطة ✎┊‌ {ytdl_data['uploader']}"
    )
    f = pathlib.Path(f"{ytdl_data['title']}.mp3".replace("|", "_"))
    catthumb = pathlib.Path(f"{ytdl_data['title']}.mp3.jpg".replace("|", "_"))
    if not os.path.exists(catthumb):
        catthumb = pathlib.Path(f"{ytdl_data['title']}.mp3.webp".replace("|", "_"))
    if not os.path.exists(catthumb):
        catthumb = None
    c_time = time.time()
    ul = io.open(f, "rb")
    uploaded = await event.client.fast_upload_file(
        file=ul,
        progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
            progress(d, t, catevent, c_time, "upload", file_name=f)
        ),
    )
    ul.close()
    attributes, mime_type = await fix_attributes(f, ytdl_data, supports_streaming=True)
    media = types.InputMediaUploadedDocument(
        file=uploaded,
        mime_type=mime_type,
        attributes=attributes,
        thumb=await event.client.upload_file(catthumb) if catthumb else None,
    )
    await event.client.send_file(
        event.chat_id,
        file=media,
        reply_to=reply_to_id,
        caption=ytdl_data["title"],
        supports_streaming=True,
        force_document=False,
    )
    os.remove(f)
    if catthumb:
        os.remove(catthumb)
    await catevent.delete()


@l313l.ar_cmd(
    pattern="تحميل ف(?: |$)(.*)",
    command=("تحميل ف", plugin_category),
    info={
        "header": "To download video from many sites like Youtube",
        "description": "downloads the video from the given link(Suports the all sites which support youtube-dl)",
        "examples": [
            "{tr}ytv <reply to link>",
            "{tr}ytv <link>",
        ],
    },
)
async def download_video(event):
    """To download video from YouTube and many other sites."""
    url = event.pattern_match.group(1)
    rmsg = await event.get_reply_message()
    if not url and rmsg:
        myString = rmsg.text
        url = re.search("(?P<url>https?://[^\s]+)", myString).group("url")
    if not url:
        return await edit_or_reply(event, "✎┊‌ عـليك وضع رابـط اولا ليتـم تنـزيله")
    catevent = await edit_or_reply(event, "✎┊‌ يتم التحميل انتظر قليلا")
    reply_to_id = await reply_id(event)
    ytdl_data = await ytdl_down(catevent, video_opts, url)
    if ytdl_down is None:
        return
    f = pathlib.Path(f"{ytdl_data['title']}.mp4".replace("|", "_"))
    catthumb = pathlib.Path(f"{ytdl_data['title']}.jpg".replace("|", "_"))
    if not os.path.exists(catthumb):
        catthumb = pathlib.Path(f"{ytdl_data['title']}.webp".replace("|", "_"))
    if not os.path.exists(catthumb):
        catthumb = None
    await catevent.edit(
        f"✎┊‌ التحضيـر للـرفع انتظر:\
        \n✎┊‌ {ytdl_data['title']}\
        \nبـواسطة *{ytdl_data['uploader']}*"
    )
    ul = io.open(f, "rb")
    c_time = time.time()
    attributes, mime_type = await fix_attributes(f, ytdl_data, supports_streaming=True)
    uploaded = await event.client.fast_upload_file(
        file=ul,
        progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
            progress(d, t, catevent, c_time, "upload", file_name=f)
        ),
    )
    ul.close()
    media = types.InputMediaUploadedDocument(
        file=uploaded,
        mime_type=mime_type,
        attributes=attributes,
        thumb=await event.client.upload_file(catthumb) if catthumb else None,
    )
    await event.client.send_file(
        event.chat_id,
        file=media,
        reply_to=reply_to_id,
        caption=ytdl_data["title"],
    )
    os.remove(f)
    if catthumb:
        os.remove(catthumb)
    await event.delete()


@l313l.ar_cmd(
    pattern="noo(?: |$)(\d*)? ?([\s\S]*)",
    command=("noo", plugin_category),
    info={
        "header": "To search youtube videos",
        "description": "Fetches youtube search results with views and duration with required no of count results by default it fetches 10 results",
        "examples": [
            "{tr}yts <query>",
            "{tr}yts <1-9> <query>",
        ],
    },
)
async def yt_search(event):
    "Youtube search command"
    if event.is_reply and not event.pattern_match.group(2):
        query = await event.get_reply_message()
        query = str(query.message)
    else:
        query = str(event.pattern_match.group(2))
    if not query:
        return await edit_delete(
            event, "**✎┊‌ قم بالرد على النص او كتابته مع الامر**"
        )
    video_q = await edit_or_reply(event, "**✎┊‌ يتم البحث في اليوتيوب**")
    if event.pattern_match.group(1) != "":
        lim = int(event.pattern_match.group(1))
        if lim <= 0:
            lim = 10
    else:
        lim = 10
    try:
        full_response = await ytsearch(query, limit=lim)
    except Exception as e:
        return await edit_delete(video_q, str(e), time=10, parse_mode=_format.parse_pre)
    reply_text = f"**•  البحث المطلوب:**\n`{query}`\n\n**•  النتائج:**\n{full_response}"
    await edit_or_reply(video_q, reply_text)


@l313l.on(admin_cmd(pattern="انستا(?: |$)(.*)"))
async def _(event):
    if event.fwd_from:
        return
    r_link = event.pattern_match.group(1)
    if "www.instagram.com" not in r_link:
        await event.edit("**✎┊‌يجب وضع رابط الانستا مع الامر اولا **")
    else:
        await event.edit("**✎┊‌تتم المعالجة انتظر قليلا**")
    chat = "@Biobot"  # تغيير اسم البوت إلى البوت المناسب لـ Instagram
    async with bot.conversation(chat) as conv:
        try:
            msg_start = await conv.send_message("/start")
            r = await conv.get_response()
            msg = await conv.send_message(r_link)
            details = await conv.get_response()
            video = await conv.get_response()
        
            await bot.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await event.edit("✎┊‌الغـي حـظر هـذا البـوت و حـاول مجـددا @Biobot")
            return
        await bot.send_file(event.chat_id, video)
        await event.client.delete_messages(
            conv.chat_id, [msg_start.id, r.id, msg.id, details.id, video.id]
        )
        await bot.delete_dialog(conv.chat_id)
        await event.delete()
        
from telethon.errors.rpcerrorlist import YouBlockedUserError

from JoKeRUB import l313l


@l313l.on(admin_cmd(pattern="nooooo(?: |$)(.*)"))
async def _(event):
    if event.fwd_from:
        return
    r_link = event.pattern_match.group(1)
    if "tiktok.com" not in r_link:
        await event.edit("**✎┊‌ يجب وضع رابط الفيديو من التيك توك مع الامر  **")
    else:
        await event.edit("**✎┊‌تتم المعالجة انتظر قليلا**")
    chat = "@LEbot"
    async with bot.conversation(chat) as conv:
        try:
            msg_start = await conv.send_message("/start")
            r = await conv.get_response()
            msg = await conv.send_message(r_link)
            details = await conv.get_response()
            video = await conv.get_response()
            await bot.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await event.edit("✎┊‌الغـي حـظر هـذا البـوت و حـاول مجـددا @LEbot")
            return
        await bot.send_file(event.chat_id, video)
        await event.client.delete_messages(
            conv.chat_id, [msg_start.id, r.id, msg.id, details.id, video.id]
        )
        await bot.delete_dialog(conv.chat_id)
        await event.delete()
                


@l313l.on(admin_cmd(pattern="nooon(?: |$)(.*)"))
async def _(event):
    if event.fwd_from:
        return
    r_link = event.pattern_match.group(1)

    await event.edit("**✎┊‌يتم الاجابه عن سؤالك ⏳**")
    chat = "@ScorGPTbot"
    async with bot.conversation(chat) as conv:
        try:
            await conv.send_message("/start")
            await conv.get_response()
            await conv.send_message(r_link)
            await event.edit("**✎┊‌ 𝐆𝐞𝐭𝐭𝐢𝐧𝐠 𝐫𝐞𝐬𝐩𝐨𝐧𝐬𝐞 ⏳  | 10%**\n\n[ ▀▀────────────────── ]")
            await asyncio.sleep(1)
            await event.edit("**✎┊‌ 𝐆𝐞𝐭𝐭𝐢𝐧𝐠 𝐫𝐞𝐬𝐩𝐨𝐧𝐬𝐞 ⏳  | 20%**\n\n[ ▀▀▀▀──────────────── ]")
            await asyncio.sleep(1)
            await event.edit("**✎┊‌ 𝐆𝐞𝐭𝐭𝐢𝐧𝐠 𝐫𝐞𝐬𝐩𝐨𝐧𝐬𝐞 ⏳  | 30%**\n\n[ ▀▀▀▀▀▀────────────── ]")
            await asyncio.sleep(1)
            await event.edit("**✎┊‌ 𝐆𝐞𝐭𝐭𝐢𝐧𝐠 𝐫𝐞𝐬𝐩𝐨𝐧𝐬𝐞 ⏳  | 40%**\n\n[ ▀▀▀▀▀▀▀▀──────────── ]")
            await asyncio.sleep(1)
            await event.edit("**✎┊‌ 𝐆𝐞𝐭𝐭𝐢𝐧𝐠 𝐫𝐞𝐬𝐩𝐨𝐧𝐬𝐞 ⏳  | 50%**\n\n[ ▀▀▀▀▀▀▀▀▀▀────────── ]")
            await asyncio.sleep(1)
            await event.edit("**✎┊‌ 𝐆𝐞𝐭𝐭𝐢𝐧𝐠 𝐫𝐞𝐬𝐩𝐨𝐧𝐬𝐞 ⏳  | 60%**\n\n[ ▀▀▀▀▀▀▀▀▀▀▀▀──────── ]")
            await asyncio.sleep(1)
            await event.edit("**✎┊‌ 𝐆𝐞𝐭𝐭𝐢𝐧𝐠 𝐫𝐞𝐬𝐩𝐨𝐧𝐬𝐞 ⏳  | 70%**\n\n[ ▀▀▀▀▀▀▀▀▀▀▀▀▀▀────── ]")
            await asyncio.sleep(1)
            await event.edit("**✎┊‌ 𝐆𝐞𝐭𝐭𝐢𝐧𝐠 𝐫𝐞𝐬𝐩𝐨𝐧𝐬𝐞 ⏳  | 80%**\n\n[ ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀──── ]")
            await asyncio.sleep(1)
            await event.edit("**✎┊‌ 𝐆𝐞𝐭𝐭𝐢𝐧𝐠 𝐫𝐞𝐬𝐩𝐨𝐧𝐬𝐞 ⏳  | 90%**\n\n[ ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀── ]")
            await asyncio.sleep(1)
            await event.edit("**✎┊‌ 𝐆𝐞𝐭𝐭𝐢𝐧𝐠 𝐫𝐞𝐬𝐩𝐨𝐧𝐬𝐞 ⏳  | 100%**\n\n[ ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀ ]")
            await asyncio.sleep(1)
            await event.edit("**✎┊‌ شكرا لأنتظارك 🙏🏻**")
            while True:
                await asyncio.sleep(1)
                response = await conv.get_response(timeout=35)

                if "𝗪𝗮𝗶𝘁 𝗺𝗲" not in response.text:
                    await event.edit(f"** ✎┊‌ الجواب : **\n\n {response.text} \n\n [• 𝗦𝗰𝗼𝗿𝗚𝗣𝗧](t.me/Scorpion_scorp)")
                    await bot.delete_dialog(conv.chat_id)
                    break
            
            await bot.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await event.edit("**✎┊‌الغـي حـظر هـذا البـوت و حـاول مجـددا @ScorGPTbot **")
            return
        except Exception as e:
            await event.edit(f"✎┊‌حدث خطأ :\n `{str(e)}` ")
            return
