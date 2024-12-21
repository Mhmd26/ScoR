from JoKeRUB import l313l
from ..sql_helper.globals import addgvar, delgvar, gvarstatus
import os
from telethon import events
from JoKeRUB import *

# أسماء أيام الأسبوع بالعربية
Aljoker_Asbo3 = {
    'Monday': 'الاثنين',
    'Tuesday': 'الثلاثاء',
    'Wednesday': 'الأربعاء',
    'Thursday': 'الخميس',
    'Friday': 'الجمعة',
    'Saturday': 'السبت',
    'Sunday': 'الأحد'
}

# تفعيل ميزة حفظ البصمات الصوتية
@l313l.on(admin_cmd(pattern="(البصمة تشغيل|بصمة تشغيل)"))
async def enable_save_voice(event):
    if gvarstatus("savevoiceforme"):
        return await edit_delete(event, "**✎┊‌حفظ البصمات مفعل مسبقاً**")
    else:
        addgvar("savevoiceforme", "enabled")
        await edit_delete(event, "**✎┊‌تم تفعيل ميزة حفظ البصمات بنجاح ✓**")

# تعطيل ميزة حفظ البصمات الصوتية
@l313l.on(admin_cmd(pattern="(البصمة تعطيل|بصمة تعطيل)"))
async def disable_save_voice(event):
    if gvarstatus("savevoiceforme"):
        delgvar("savevoiceforme")
        return await edit_delete(event, "**✎┊‌تم تعطيل ميزة حفظ البصمات بنجاح ✓**")
    else:
        await edit_delete(event, "**✎┊‌الميزة معطلة بالفعل!**")

# التحقق من الرسائل الصوتية الذاتية فقط
def is_voice_message(message):
    return (
        message.media and
        hasattr(message.media, 'document') and
        message.media.document.mime_type == 'audio/ogg' and
        message.media.document.attributes[0].voice  # التحقق من أن الملف صوتي ذاتي
    )

# إرسال البصمة مع التفاصيل
async def save_voice_message(event, caption):
    voice = await event.download_media()
    sender = await event.get_sender()
    sender_id = event.sender_id
    voice_date = event.date.strftime("%Y-%m-%d")
    voice_day = Aljoker_Asbo3[event.date.strftime("%A")]
    await bot.send_file(
        "me",
        voice,
        caption=caption.format(sender.first_name, sender_id, voice_date, voice_day),
        parse_mode="markdown"
    )
    os.remove(voice)

# التقاط الرسائل الصوتية الذاتية في المحادثات الخاصة
@l313l.on(events.NewMessage(func=lambda e: e.is_private and is_voice_message(e) and e.sender_id != bot.uid))
async def handle_voice(event):
    if gvarstatus("savevoiceforme"):
        caption = """** 

✎┊‌ تم حفظ البصمة الذاتية بنجاح ☑️
✎┊‌ أسم المرسل : [{0}](tg://user?id={1})
✎┊‌  تاريخ الإرسال :  {2}
✎┊‌  أرسلت في يوم :  {3}

𝗦𝗰𝗼𝗿𝗽𝗶𝗼𝗻 𝗦𝗼𝘂𝗿𝗰𝗲 ✓
        **"""
        await save_voice_message(event, caption)