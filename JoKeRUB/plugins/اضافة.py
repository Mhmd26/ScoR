import asyncio
from JoKeRUB import *
from JoKeRUB import l313l
from JoKeRUB.utils import admin_cmd
from telethon.tl.types import Channel, Chat, User
from telethon.tl import functions, types
from telethon.errors import (ChannelInvalidError, ChannelPrivateError, ChannelPublicGroupNaError)
from telethon.tl.functions.channels import GetFullChannelRequest

# فريق العقرب
# علوش @ZS_SQ
# محمد @Zo_r0

async def get_chatinfo(event):
    chat = event.pattern_match.group(1)
    chat_info = None
    if chat:
        try:
            chat = int(chat)
        except ValueError:
            pass
    if not chat:
        if event.reply_to_msg_id:
            replied_msg = await event.get_reply_message()
            if replied_msg.fwd_from and replied_msg.fwd_from.channel_id is not None:
                chat = replied_msg.fwd_from.channel_id
        else:
            chat = event.chat_id
    try:
        chat_info = await event.client(GetFullChannelRequest(chat))
    except:
        await event.reply("**✎┊‌ لم يتم العثور على المجموعة او القناة**")
        return None
    return chat_info


@l313l.on(admin_cmd(pattern=r"ضيف ?(.*)"))
async def get_users(event):
    sender = await event.get_sender()
    me = await event.client.get_me()
    
    if not sender.id == me.id:
        roz = await event.reply("**✎┊‌ تتـم العـملية انتظـࢪ قليلا ⏳ ...**")
    else:
        roz = await event.edit("**✎┊‌ تتـم العـملية انتظـࢪ قليلا ⏳ ...**.")
    
    JoKeRUB = await get_chatinfo(event)
    chat = await event.get_chat()

    if event.is_private:
        return await roz.edit("**✎┊‌ لا يمكننـي اضافـة المـستخدمين هـنا**")
    
    s = 0
    f = 0
    error = 'None'
    
    await roz.edit("**✎┊‌ حـالة الأضافة:**\n\n**✎┊‌ تتـم جـمع معـلومات الـمستخدمين 🔄 **")

    users_to_add = []
    async for user in event.client.iter_participants(JoKeRUB.full_chat.id):
        users_to_add.append(user.id)

    # إضافة 5 مستخدمين في كل مرة مع تأخير 10 ثواني بين كل دفعة
    for i in range(0, len(users_to_add), 5):
        batch = users_to_add[i:i+5]  # كل دفعة تحتوي على 5 مستخدمين
        for user_id in batch:
            try:
                await event.client(functions.channels.InviteToChannelRequest(channel=chat, users=[user_id]))
                s += 1
            except Exception as e:
                error = str(e)
                f += 1
        
        # تأخير 10 ثواني بين كل دفعة
        await asyncio.sleep(10)
        
        # تحديث الرسالة بحالة الإضافة بعد كل دفعة
        await roz.edit(f"**✎┊‌ حـالة الأضـافة:**\n\n• تم إضافة `{s}` من الأشخاص بنجاح\n• أخطاء في إضافة `{f}`\n\n**× آخر خطأ:** `{error}`")
    
    return await roz.edit(f"**✎┊‌ أكملت الإضافة ✅**\n\n• تم إضافة `{s}` شخص بنجاح\n• أخطاء في إضافة `{f}`")