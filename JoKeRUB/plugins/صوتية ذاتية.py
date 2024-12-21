from telethon import events
from JoKeRUB import *
import os

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
    addgvar("savevoicerecforme", "reda")
    await edit_delete(event, "**✎┊‌تم تفعيل ميزة حفظ البصمات الصوتية الذاتية بنجاح ✓**")

@l313l.on(admin_cmd(pattern="(البصمات تعطيل|الصوتية تعطيل)"))
async def disable_voice_save(event):
    delgvar("savevoicerecforme")
    await edit_delete(event, "**✎┊‌تم تعطيل حفظ البصمات الصوتية الذاتية بنجاح ✓**")

def is_voice_note(message):
    """تحقق إذا كانت الرسالة تحتوي على بصمة صوتية."""
    return message.media and message.media.document.mime_type == "audio/ogg"

def is_self_destruct(message):
    """تحقق إذا كانت الرسالة ذاتية الحذف."""
    return message.ttl_period is not None  # `ttl_period` يحدد مدة الحذف التلقائي.

async def save_voice(event):
    """حفظ البصمة الصوتية في الرسائل المحفوظة."""
    media = await event.download_media()
    sender = await event.get_sender()
    sender_id = event.sender_id
    voice_date = event.date.strftime("%Y-%m-%d")
    voice_day = Aljoker_Asbo3[event.date.strftime("%A")]

    # صيغة الرسالة المرسلة
    caption = f"""
✎┊‌ تم حفظ البصمة بنجاح ☑️
✎┊‌ أسم المرسل : [{sender.first_name}](tg://user?id={sender_id})
✎┊‌ التاريخ : {voice_date}
✎┊‌ يوم : {voice_day}
    """

    # إرسال البصمة إلى الرسائل المحفوظة
    await bot.send_file("me", media, caption=caption)
    os.remove(media)  # حذف الملف بعد الإرسال

@l313l.on(events.NewMessage(func=lambda e: e.is_private and is_voice_note(e.message) and is_self_destruct(e.message)))
async def handle_voice(event):
    """تعامل مع الرسائل الصوتية ذاتية الحذف."""
    if gvarstatus("savevoicerecforme"):
        await save_voice(event)