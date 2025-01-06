

import asyncio
import os
from secrets import choice
import random
from urllib.parse import quote_plus
from collections import deque
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.types import InputMessagesFilterVideo, InputMessagesFilterVoice, InputMessagesFilterPhotos

from  JoKeRUB import  l313l

from ..core.logger import logging
from ..Config import Config
from ..core.managers import edit_delete, edit_or_reply
from . import ALIVE_NAME, mention
from ..helpers import get_user_from_event
from ..helpers.utils import _format

from . import reply_id


@l313l.ar_cmd(pattern="حالات$")
async def _(event):
    zzevent = await edit_or_reply(event, "**✎┊‌ جـارِ تحميـل حـالات واتـس ...**")
    try:
        ZTHONR = [
            zlzzl
            async for zlzzl in event.client.iter_messages(
                "@elgraahh", filter=InputMessagesFilterVideo
            )
        ]
        aing = await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(ZTHONR),
            caption=f"**✎┊‌حـالات واتـس قصيـرة **\n\n**[العقرب | 𝐒𝐜𝐨𝐫𝐩𝐢𝐨𝐧  ☑️](https://t.me/Scorpion_scorp)**",
        )
        await zzevent.delete()
    except Exception:
        await zzevent.edit("**✎┊‌ عـذراً .. لـم استطـع ايجـاد المطلـوب **")


@l313l.ar_cmd(pattern="ستوري انمي$")
async def _(event):
    zzevent = await edit_or_reply(event, "**✎┊‌ جـارِ تحميـل الستـوري ...**")
    try:
        ZTHONR = [
            zlzzl
            async for zlzzl in event.client.iter_messages(
                "@AA_Zll", filter=InputMessagesFilterVideo
            )
        ]
        aing = await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(ZTHONR),
            caption=f"**✎┊‌ستـوريات آنمـي قصيـرة **\n\n**[العقرب | 𝐒𝐜𝐨𝐫𝐩𝐢𝐨𝐧  ☑️](https://t.me/Scorpion_scorp)**",
        )
        await zzevent.delete()
    except Exception:
        await zzevent.edit("**✎┊‌ عـذراً .. لـم استطـع ايجـاد المطلـوب **")


@l313l.ar_cmd(pattern="رقيه$")
async def _(event):
    zzevent = await edit_or_reply(event, "**✎┊‌ جـارِ تحميـل الرقيـه ...**")
    try:
        zedgan = [
            zlzzl77
            async for zlzzl77 in event.client.iter_messages(
                "@Rqy_1", filter=InputMessagesFilterVoice
            )
        ]
        aing = await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(zedgan),
            caption=f"**✎┊‌ ◞مقاطـع رقيـه شرعيـة **\n\n**[العقرب | 𝐒𝐜𝐨𝐫𝐩𝐢𝐨𝐧  ☑️](https://t.me/Scorpion_scorp)**",
        )
        await zzevent.delete()
    except Exception:
        await zzevent.edit("**✎┊‌ عـذراً .. لـم استطـع ايجـاد المطلـوب **")


@l313l.ar_cmd(pattern="اولاد رمادي$")
async def _(event):
    zzevent = await edit_or_reply(event, "**✎┊‌ جـارِ تحميـل الافتـار ...**")
    try:
        zedph = [
            zelzal
            async for zelzal in event.client.iter_messages(
                "@shababbbbR", filter=InputMessagesFilterPhotos
            )
        ]
        aing = await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(zedph),
            caption=f"**✎┊‌ ◞افتـارات شبـاب ࢪمـاديه **\n\n**[العقرب | 𝐒𝐜𝐨𝐫𝐩𝐢𝐨𝐧  ☑️](https://t.me/Scorpion_scorp)**",
        )
        await zzevent.delete()
    except Exception:
        await zzevent.edit("**✎┊‌ عـذراً .. لـم استطـع ايجـاد المطلـوب **")


@l313l.ar_cmd(pattern="بنات رماديه$")
async def _(event):
    zzevent = await edit_or_reply(event, "**✎┊‌ جـارِ تحميـل الافتـار ...**")
    try:
        zedph = [
            zelzal
            async for zelzal in event.client.iter_messages(
                "@banatttR", filter=InputMessagesFilterPhotos
            )
        ]
        aing = await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(zedph),
            caption=f"**✎┊‌ ◞افتـارات بنـات ࢪمـاديه **\n\n**[العقرب | 𝐒𝐜𝐨𝐫𝐩𝐢𝐨𝐧  ☑️](https://t.me/Scorpion_scorp)**",
        )
        await zzevent.delete()
    except Exception:
        await zzevent.edit("**✎┊‌ عـذراً .. لـم استطـع ايجـاد المطلـوب **")


@l313l.ar_cmd(pattern="بيست$")
async def _(event):
    zzevent = await edit_or_reply(event, "**✎┊‌ جـارِ تحميـل الآفتـار **")
    try:
        zedph = [
            zelzal
            async for zelzal in event.client.iter_messages(
                "@Tatkkkkkim", filter=InputMessagesFilterPhotos
            )
        ]
        aing = await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(zedph),
            caption=f"**✎┊‌ ◞افتـارات بيست تطقيـم بنـات **\n\n**[العقرب | 𝐒𝐜𝐨𝐫𝐩𝐢𝐨𝐧  ☑️](https://t.me/Scorpion_scorp)**",
        )
        await zzevent.delete()
    except Exception:
        await zzevent.edit("**✎┊‌ عـذراً .. لـم استطـع ايجـاد المطلـوب **")


@l313l.ar_cmd(pattern="حب$")
async def _(event):
    zzevent = await edit_or_reply(event, "**✎┊‌ جـارِ تحميـل الآفتـار **")
    try:
        zedph = [
            zelzal
            async for zelzal in event.client.iter_messages(
                "@tatkkkkkimh", filter=InputMessagesFilterPhotos
            )
        ]
        aing = await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(zedph),
            caption=f"**✎┊‌ ◞افتـارات حـب تمبلـرࢪ **\n\n**[العقرب | 𝐒𝐜𝐨𝐫𝐩𝐢𝐨𝐧  ☑️](https://t.me/Scorpion_scorp)**",
        )
        await zzevent.delete()
    except Exception:
        await zzevent.edit("**✎┊‌ عـذراً .. لـم استطـع ايجـاد المطلـوب **")


@l313l.ar_cmd(pattern="رياكشن$")
async def _(event):
    zzevent = await edit_or_reply(event, "**✎┊‌ جـارِ تحميـل الرياكشـن ...**")
    try:
        ZTHONR = [
            zlzzl
            async for zlzzl in event.client.iter_messages(
                "@reagshn", filter=InputMessagesFilterVideo
            )
        ]
        aing = await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(ZTHONR),
            caption=f"** ✎┊رياكشـن تحشيـش 😂😁**\n\n**[العقرب | 𝐒𝐜𝐨𝐫𝐩𝐢𝐨𝐧  ☑️](https://t.me/Scorpion_scorp)**",
        )
        await zzevent.delete()
    except Exception:
        await zzevent.edit("**✎┊‌ عـذراً .. لـم استطـع ايجـاد المطلـوب **")


@l313l.ar_cmd(pattern="ادت$")
async def _(event):
    zzevent = await edit_or_reply(event, "**✎┊‌ جـارِ تحميـل مقطـع ادت ...**")
    try:
        ZTHONR = [
            asupan
            async for asupan in event.client.iter_messages(
                "@snje1", filter=InputMessagesFilterVideo
            )
        ]
        aing = await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(ZTHONR),
            caption=f"**✎┊مقاطـع ايـدت منوعـه ✨**\n\n**[العقرب | 𝐒𝐜𝐨𝐫𝐩𝐢𝐨𝐧  ☑️](https://t.me/Scorpion_scorp)**",
        )
        await zzevent.delete()
    except Exception:
        await zzevent.edit("**✎┊‌ عـذراً .. لـم استطـع ايجـاد المطلـوب **")




@l313l.ar_cmd(pattern="معلومه$")
async def _(event):
    zzevent = await edit_or_reply(event, "**✎┊‌ جـارِ تحميـل صـورة ومعلومـة ...**")
    try:
        zedph = [
            zilzal
            async for zilzal in event.client.iter_messages(
                "@A_l3l", filter=InputMessagesFilterPhotos
            )
        ]
        aing = await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(zedph),
            caption=f"**✎┊‌صـورة ومعلومـة 💡**\n\n**[العقرب | 𝐒𝐜𝐨𝐫𝐩𝐢𝐨𝐧  ☑️](https://t.me/Scorpion_scorp)**",
        )
        await zzevent.delete()
    except Exception:
        await zzevent.edit("**✎┊‌ عـذراً .. لـم استطـع ايجـاد المطلـوب **")


@l313l.ar_cmd(pattern="تويت$")
async def _(event):
    zzevent = await edit_or_reply(event, "**✎┊‌ كـت تـويت بالصـور ...**")
    try:
        zedre = [
            zlzz7
            async for zlzz7 in event.client.iter_messages(
                "@twit_selva", filter=InputMessagesFilterPhotos
            )
        ]
        aing = await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(zedre),
            caption=f"**✎┊‌كـت تـويت بالصـور 🌉**\n\n**[العقرب | 𝐒𝐜𝐨𝐫𝐩𝐢𝐨𝐧  ☑️](https://t.me/Scorpion_scorp)**",
        )
        await zzevent.delete()
    except Exception:
        await zzevent.edit("**✎┊‌ عـذراً .. لـم استطـع ايجـاد المطلـوب **")


@l313l.ar_cmd(pattern="ولد انمي$")
async def _(event):
    zzevent = await edit_or_reply(event, "**✎┊‌ جـارِ تحميـل الآفتـار ...**")
    try:
        zedph = [
            zelzal
            async for zelzal in event.client.iter_messages(
                "@dnndxn", filter=InputMessagesFilterPhotos
            )
        ]
        aing = await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(zedph),
            caption=f"**✎┊‌ ◞افتـارات آنمي شبـاب **\n\n**[العقرب | 𝐒𝐜𝐨𝐫𝐩𝐢𝐨𝐧  ☑️](https://t.me/Scorpion_scorp)**",
        )
        await zzevent.delete()
    except Exception:
        await zzevent.edit("**✎┊‌ عـذراً .. لـم استطـع ايجـاد المطلـوب **")


@l313l.ar_cmd(pattern="بنت انمي$")
async def _(event):
    zzevent = await edit_or_reply(event, "**✎┊‌ جـارِ تحميـل الآفتـار ...**")
    try:
        zedph = [
            zelzal
            async for zelzal in event.client.iter_messages(
                "@shhdhn", filter=InputMessagesFilterPhotos
            )
        ]
        aing = await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(zedph),
            caption=f"**✎┊‌ ◞افتـارات آنمي بنـات **\n\n**[العقرب | 𝐒𝐜𝐨𝐫𝐩𝐢𝐨𝐧  ☑️](https://t.me/Scorpion_scorp)**",
        )
        await zzevent.delete()
    except Exception:
        await zzevent.edit("**✎┊‌ عـذراً .. لـم استطـع ايجـاد المطلـوب **")


@l313l.ar_cmd(pattern="بنات$")
async def _(event):
    zzevent = await edit_or_reply(event, "**✎┊‌ جـارِ تحميـل الآفتـار ...**")
    try:
        zedph = [
            zelzal
            async for zelzal in event.client.iter_messages(
                "@banaaaat1", filter=InputMessagesFilterPhotos
            )
        ]
        aing = await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(zedph),
            caption=f"**✎┊‌ ◞افتـارات بنـات تمبلـرࢪ **\n\n**[العقرب | 𝐒𝐜𝐨𝐫𝐩𝐢𝐨𝐧  ☑️](https://t.me/Scorpion_scorp)**",
        )
        await zzevent.delete()
    except Exception:
        await zzevent.edit("**✎┊‌ عـذراً .. لـم استطـع ايجـاد المطلـوب **")


