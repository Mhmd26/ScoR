import re

from telethon import Button, events
from telethon.events import CallbackQuery

from l313l.razan.resources.assistant import *
from l313l.razan.resources.mybot import *
from JoKeRUB import l313l
from ..core import check_owner
from ..Config import Config

JEP_IC = "https://a.top4top.io/p_3186zos0l0.jpg"
ROE = "[𝗦𝗰𝗼𝗿𝗚𝗣𝗧 | 𝗚𝗲𝗺𝗶𝗻𝗶 🤖](t.me/Scorpion_scorp)\n\n**✎┊‌ اهلا وسهلا بك في قسم الذكاء الاصطناعي \n الخاص بسورس العقرب \n\n✎┊ يمكن تشغيله من خلال ارسال { `.سؤال` } بلاضافة الى سؤالك وسيتم الرد عليك بعد بضع ثوانٍ\n\n✎┊‌ يحوي على دردشة مباشره تتكون من عدة اصدارات منها Gemini Pro + flash ✓‌ \n\n يمكنك الذهاب الى الدردشة من خلال الزر ⬇️**"
if Config.TG_BOT_USERNAME is not None and tgbot is not None:

    @tgbot.on(events.InlineQuery)
    async def inline_handler(event):
        builder = event.builder
        result = None
        query = event.text
        await bot.get_me()
        if query.startswith("26") and event.query.user_id == bot.uid:
            buttons = [
                [Button.url("— 𝗚𝗼 𝗧𝗼 𝗖𝗵𝗮𝘁 —", "https://t.me/ScorGPTbot")],
            ]
            if JEP_IC and JEP_IC.endswith((".jpg", ".png", "gif", "mp4")):
                result = builder.photo(
                    JEP_IC, text=ROE, buttons=buttons, link_preview=False
                )
            elif JEP_IC:
                result = builder.document(
                    JEP_IC,
                    title="JoKeRUB",
                    text=ROE,
                    buttons=buttons,
                    link_preview=False,
                )
            else:
                result = builder.article(
                    title="JoKeRUB",
                    text=ROE,
                    buttons=buttons,
                    link_preview=False,
                )
            await event.answer([result] if result else None)


@bot.on(admin_cmd(outgoing=True, pattern="26"))
async def repo(event):
    if event.fwd_from:
        return
    lMl10l = Config.TG_BOT_USERNAME
    if event.reply_to_msg_id:
        await event.get_reply_message()
    response = await bot.inline_query(lMl10l, "26")
    await response[0].click(event.chat_id)
    await event.delete()
