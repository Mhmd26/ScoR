import asyncio
import re
from telethon import events
from telethon.errors import ChannelPrivateError, ChatAdminRequiredError
from JoKeRUB import l313l

plugin_category = "misc"

@l313l.ar_cmd(
    pattern=r"حفظ كامل (\d+)",  
    command=("حفظ كامل", plugin_category),
    info={
        "header": "نقل جميع الرسائل من قناة معينة.",
        "description": "ينقل كل المحتوى من قناة معينة إلى المكان الذي يتم كتابة الأمر فيه، مع الحفاظ على الترتيب من الأقدم إلى الأحدث.",
        "usage": "{tr}حفظ_كامل <ID القناة>",
    },
)
async def transfer_channel(event):
    channel_id = event.pattern_match.group(1)  # استلام ID القناة
    if not channel_id:
        return await event.edit("**✎┊‌ يرجى تحديد ID القناة!**")

    await event.edit("**✎┊‌ جاري التحقق من القناة، يرجى الانتظار...**")

    try:
        chat = await l313l.get_entity(int(channel_id))  
    except Exception as e:
        return await event.edit(f"**✎┊‌ حدث خطأ أثناء الحصول على القناة. الخطأ: {str(e)}**")

    chat_id = event.chat_id

    try:
        messages = await l313l.get_messages(chat, limit=5000, reverse=True)

        for msg in messages:
            await asyncio.sleep(1)
            try:
                if msg.media:
                    await l313l.send_file(chat_id, msg.media, caption=msg.text or "")
                else:
                    await l313l.send_message(chat_id, msg.text)
            except Exception as e:
                await l313l.send_message(chat_id, f"✎┊‌ تعذر نقل رسالة بسبب خطأ: {str(e)}")

        await event.edit("**✎┊‌ تم نقل جميع الرسائل بنجاح! ✅**")
    except Exception as e:
        await event.edit(f"✎┊‌ حدث خطأ أثناء جلب الرسائل. الخطأ: {str(e)}")