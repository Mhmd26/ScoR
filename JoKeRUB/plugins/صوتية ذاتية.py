from telethon import events
from JoKeRUB import *
import os
import datetime
from ..sql_helper.globals import addgvar, delgvar, gvarstatus

Aljoker_Asbo3 = {
    'Monday': 'الاثنين',
    'Tuesday': 'الثلاثاء',
    'Wednesday': 'الأربعاء',
    'Thursday': 'الخميس',
    'Friday': 'الجمعة',
    'Saturday': 'السبت',
    'Sunday': 'الأحد'
}

@l313l.on(admin_cmd(pattern="(البصمات تشغيل|الصوتية تشغيل)"))
async def enable_voice_save(event):
    if gvarstatus("savevoicerecforme"):
        return await edit_delete(event, "**✎┊‌حفظ البصمات الصوتية مفعل بالفعل.**")
    else:
        addgvar("savevoicerecforme", "reda")
        await edit_delete(event, "**✎┊‌تم تفعيل ميزة حفظ البصمات الصوتية بنجاح ✓**")

@l313l.on(admin_cmd(pattern="(البصمات تعطيل|الصوتية تعطيل)"))
async def disable_voice_save(event):
    if gvarstatus("savevoicerecforme"):
        delgvar("savevoicerecforme")
        return await edit_delete(event, "**✎┊‌تم تعطيل حفظ البصمات الصوتية بنجاح ✓**")
    else:
        await edit_delete(event, "**✎┊‌انت لم تفعل حفظ البصمات الصوتية لتعطيلها!**")

def is_voice_note(message):
    """تحقق إذا كانت الرسالة تحتوي على بصمة صوتية."""
    return message.media and message.media.document.mime_type == "audio/ogg"

def is_self_destruct(event):
    """تحقق إذا كانت الرسالة ذاتية الحذف."""
    return event.message.ttl and event.message.ttl > 0

async def save_voice(event, caption):
    """حفظ البصمة الصوتية مع التفاصيل."""
    media = await event.download_media()
    sender = await event.get_sender()
    sender_id = event.sender_id
    voice_date = event.date.strftime("%Y-%m-%d")
    voice_day = Aljoker_Asbo3[event.date.strftime("%A")]
    
    await bot.send_file(
        "me",
        media,
        caption=caption.format(sender.first_name, sender_id, voice_date, voice_day),
        parse_mode="markdown"
    )
    os.remove(media)

@l313l.on(events.NewMessage(func=lambda e: e.is_private and is_voice_note(e) and e.sender_id != bot.uid))
async def handle_voice(event):
    """التعامل مع الرسائل الصوتية."""
    if gvarstatus("savevoicerecforme") and is_self_destruct(event):
        caption = """
        ** 
✎┊‌ تم الحفظ بنجاح ☑️
✎┊‌ أسم المرسل : [{0}](tg://user?id={1})
✎┊‌ التاريخ :  {2}
✎┊‌ يوم :  {3}

        𝗦𝗰𝗼𝗿𝗽𝗶𝗼𝗻 𝗦𝗼𝘂𝗿𝗰𝗲 ✓
        **"""
        await save_voice(event, caption)