from JoKeRUB import *
from JoKeRUB import l313l
from JoKeRUB.utils import admin_cmd
from telethon.tl.types import Channel, Chat, User
from telethon.tl import functions, types
from telethon.tl.functions.messages import CheckChatInviteRequest, GetFullChatRequest
from telethon.errors import (ChannelInvalidError, ChannelPrivateError, ChannelPublicGroupNaError, InviteHashEmptyError, InviteHashExpiredError, InviteHashInvalidError)
from telethon.tl.functions.channels import GetFullChannelRequest, GetParticipantsRequest

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
        chat_info = await event.client(GetFullChatRequest(chat))
    except:
        try:
            chat_info = await event.client(GetFullChannelRequest(chat))
        except ChannelInvalidError:
            await event.reply("**✎┊‌ لم يتم العثور على المجموعة او القناة**")
            return None
        except ChannelPrivateError:
            await event.reply("**✎┊‌ لا يمكنني استخدام الامر من الكروبات او القنوات الخاصة**")
            return None
        except ChannelPublicGroupNaError:
            await event.reply("**✎┊‌ لم يتم العثور على المجموعة او القناة**")
            return None
        except (TypeError, ValueError) as err:
            await event.reply("**✎┊‌ رابط الكروب غير صحيح**")
            return None
    return chat_info


def make_mention(user):
    if user.username:
        return f"@{user.username}"
    else:
        return inline_mention(user)


def inline_mention(user):
    full_name = user_full_name(user) or "No Name"
    return f"[{full_name}](tg://user?id={user.id})"


def user_full_name(user):
    names = [user.first_name, user.last_name]
    names = [i for i in list(names) if i]
    full_name = ' '.join(names)
    return full_name


# فريق العقرب 
# علوش @ZS_SQ
# محمد @Zo_r0

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

    s = 0  # عدد المستخدمين الذين تم إضافتهم بنجاح
    f = 0  # عدد المستخدمين الذين حدث خطأ أثناء إضافتهم
    error = 'None'

    # إرسال رسالة بداية العملية
    await roz.edit("**✎┊‌ حـالة الأضافة:**\n\n**✎┊‌ تتـم جـمع معـلومات الـمستخدمين 🔄 **")

    # جمع الأعضاء في المجموعة المستهدفة
    users = [user.id for user in await event.client.iter_participants(JoKeRUB.full_chat.id)]

    # إضافة جميع الأعضاء دفعة واحدة
    for user_id in users:
        try:
            await event.client(functions.channels.InviteToChannelRequest(channel=chat, users=[user_id]))
            s += 1
        except Exception as e:
            error = str(e)
            f += 1

        # تحديث الرسالة بعد كل عملية إضافة
        await roz.edit(f"**✎┊‌ حـالة الأضافة:**\n\n• اضـيف `{s}` \n• خـطأ بأضافـة `{f}` \n\n**× اخـر خـطأ:** `{error}`")

    # إرسال رسالة إتمام العملية
    return await roz.edit(f"**✎┊‌ اكتملت الأضافة ✅**\n\n• تمت بنجاح إضافة `{s}` \n• خطأ في إضافة `{f}`")


@l313l.on(admin_cmd(pattern=r"اضافة_جهاتي ?(.*)"))
async def Hussein(event):
    channel_id = event.chat_id  
    contacts = await event.client(functions.contacts.GetContactsRequest(hash=0))
    added_count = 0 
    for user in contacts.users:
        try:
            await event.client(functions.channels.InviteToChannelRequest(
                channel=channel_id,
                users=[user.id],
            ))
            added_count += 1
        except Exception as e:
            await event.reply(f"**✎┊‌ تم إضافة {added_count} من جهات اتصالي**")
    await event.reply(f"**✎┊‌ تم إضافة {added_count} من جهات اتصالي**")