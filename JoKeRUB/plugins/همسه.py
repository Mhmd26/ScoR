from telethon import events
import random, re
from JoKeRUB.utils import admin_cmd
import asyncio 

# Wespr File by  @lMl10l
# Copyright (C) 2021 JoKeRUB TEAM
@borg.on(
    admin_cmd(pattern="همسة ?(.*)")
)
async def wspr(event):
    if event.fwd_from:
        return
    l313lb = event.pattern_match.group(1)
    rrrd7 = "@nnbbot"
    if event.reply_to_msg_id:
        reply_to_id = await event.get_reply_message()
    tap = await bot.inline_query(rrrd7, l313lb) 
    await tap[0].click(event.chat_id)
    await event.delete()
    
@borg.on(admin_cmd("اوامر الهمسة"))
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit("**✎┊‌ اوامر الهمسه واكس او \n\n✎┊‌الامر  • `.همسة`\n✎┊‌الاستخدام  • لكتابة همسه سرية لشخص في المجموعه \n\n✎┊‌ الامر • `.الهمسة`\n✎┊‌ استخدامه • لعرض كيفية كتابة همسة سرية\n\nالعقرب |  𝗦𝗰𝗼𝗿𝗽𝗶𝗼 🦂**")
        
@borg.on(admin_cmd("الهمسة"))
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit("**✎┊‌ شـرح كيـفية كـتابة همـسة سـرية**\n✎┊‌ اولا اكتب الامر  .همسة  بعدها الرسالة بعدها اكتب معرف الشخص\n✎┊‌ مـثال  :   `.همسة ههلا @Zo_r0.`")
        
@borg.on(
    admin_cmd(
       pattern="اكس او$"
    )
)
# كتابة وتعديل فريق الجوكر  #@lMl10l
async def gamez(event):
    if event.fwd_from:
        return
    jmusername = "@xoBot"
    uunzz = "play"
    if event.reply_to_msg_id:
        await event.get_reply_message()
    tap = await bot.inline_query(jmusername, uunzz)
    await tap[0].click(event.chat_id)
    await event.delete()
