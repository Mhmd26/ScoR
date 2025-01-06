import random
import re
import time
from platform import python_version

from telethon import version, Button, events
from telethon.errors.rpcerrorlist import (
    MediaEmptyError,
    WebpageCurlFailedError,
    WebpageMediaEmptyError,
)
from telethon.events import CallbackQuery

from JoKeRUB import StartTime, l313l, JEPVERSION

from ..Config import Config
from ..core.managers import edit_or_reply
from ..helpers.functions import catalive, check_data_base_heal_th, get_readable_time
from ..helpers.utils import reply_id
from ..sql_helper.globals import addgvar, delgvar, gvarstatus
from . import mention

plugin_category = "utils"

@l313l.on(events.NewMessage(pattern=r'\.event', outgoing=True))
async def my_event_handler(event):
    if event.is_reply:
        replied_message = await event.get_reply_message()
        if replied_message:
            event_info = await client.get_event_info(replied_message)
            with open("event_info.txt", "w") as file:
                file.write(event_info.stringify())
            await l313l.send_file(event.chat_id, "event_info.txt")

@l313l.ar_cmd(
    pattern="المطور$",
    command=("المطور", plugin_category),
    info={
        "header": "لأظهار مطورين السورس",
        "usage": [
            "{tr}المطور",
        ],
    },
)
async def amireallyalive(event):
    "A kind of showing bot details"
    reply_to_id = await reply_id(event)
    uptime = await get_readable_time((time.time() - StartTime))
    _, check_sgnirts = check_data_base_heal_th()
    EMOJI = gvarstatus("ALIVE_EMOJI") or "  - "
    CUSTOM_ALIVE_TEXT = gvarstatus("ALIVE_TEXT")
    CAT_IMG = "https://telegra.ph/file/d619daa249b56eb805eb5.jpg"
    if CAT_IMG:
        CAT = [x for x in CAT_IMG.split()]
        A_IMG = list(CAT)
        PIC = random.choice(A_IMG)
        cat_caption = f"** مطورين سورس العقرب ✍🏻\n\n المطور : [𝗔𝗹𝗹𝗼𝘂𝘀𝗵](t.me/I_e_e_l) \n المطور : [𝗠𝗼𝗵𝗮𝗺𝗺𝗲𝗱](t.me/Zo_r0) \n\n [العقرب | 𝐒𝐜𝐨𝐫𝐩𝐢𝐨𝐧 ☑️](t.me/Scorpion_scorp) ** "
        await event.client.send_file(
            event.chat_id, PIC, caption=cat_caption, reply_to=reply_to_id
        )

@l313l.tgbot.on(CallbackQuery(data=re.compile(b"stats")))
async def on_plug_in_callback_query_handler(event):
    statstext = await catalive(StartTime)
    await event.answer(statstext, cache_time=0, alert=True)
