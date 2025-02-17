import base64
from telethon import events
from telethon.tl.functions.messages import ImportChatInviteRequest as Get
from ..sql_helper.memes_sql import get_link, add_link, delete_link, BASE, SESSION, AljokerLink
from JoKeRUB import l313l
from ..helpers.utils import reply_id

plugin_category = "tools"

# ✅ إضافة بصمة جديدة من رابط
@l313l.on(admin_cmd(outgoing=True, pattern=r"ميمز (\S+) (.+)"))
async def add_meme(event):
    url = event.pattern_match.group(1)
    ScoR = event.pattern_match.group(2)

    add_link(ScoR, url)
    await event.edit(f"✅ تم إضافة البصمة **{ScoR}** بنجاح!")

# ✅ استرجاع البصمة المخزونة
@l313l.on(admin_cmd(outgoing=True, pattern="?(.*)"))
async def get_meme(event):
    try:
        ScoR = event.pattern_match.group(1)
        Joker = await reply_id(event)
        url = get_link(ScoR)

        if url:
            await event.client.send_file(event.chat_id, url, reply_to=Joker)
            await event.delete()
        else:
            await event.edit("❌ ماكو هيج بصمة مخزونة!")

    except Exception as e:
        print(f"Error in get_meme: {e}")

# ✅ حذف بصمة معينة
@l313l.on(admin_cmd(outgoing=True, pattern="ازالة(?:\s|$)([\s\S]*)"))
async def delete_meme(event):
    ScoR = event.pattern_match.group(1)
    delete_link(ScoR)
    await event.edit(f"✅ تم حذف البصمة **{ScoR}** بنجاح!")

# ✅ عرض جميع البصمات المخزونة
@l313l.on(admin_cmd(outgoing=True, pattern="قائمة الميمز"))
async def list_memes(event):
    links = SESSION.query(AljokerLink).all()
    if links:
        message = "**📌 قائمة البصمات المخزونة:**\n"
        for link in links:
            message += f"- `{link.key}`\n"
    else:
        message = "❌ لا توجد بصمات مخزونة حتى الآن."
    await event.edit(message)

# ✅ حذف جميع البصمات المخزونة
@l313l.on(admin_cmd(outgoing=True, pattern="ازالة_البصمات"))
async def delete_all_memes(event):
    SESSION.query(AljokerLink).delete()
    await event.edit("🗑️ تم حذف جميع بصمات الميمز!")