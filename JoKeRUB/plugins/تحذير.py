# Copyright (C) 2021 Scorpion TEAM
from telethon.tl.types import User
from JoKeRUB import l313l
plugin_category = "utils"

# تخزين عدد التحذيرات لكل مستخدم
warnings = {}

@l313l.ar_cmd(
    pattern="تحذير(?: (.*))?$",
    command=("تحذير", plugin_category),
    info={
        "header": "To warn a user and ban after 3 warnings.",
        "description": "Warns the user for violations. After 3 warnings, the user will be banned from the group or blocked in private chat.",
        "usage": "{tr}تحذير <reason>",
    },
)
async def warn_user(event):
    "Warn a user and ban after 3 warnings"
    reason = event.pattern_match.group(1)
    reply = await event.get_reply_message()
    
    if not reply or not isinstance(reply.sender, User):
        return await event.edit("**✎┊‌ قم بالرد على رسالة المستخدم لتحذيره.**")
    
    user_id = reply.sender_id
    chat_id = event.chat_id
    
    # إذا لم يتم تحديد سبب
    reason_text = f"السبب: {reason}" if reason else "بدون سبب."
    
    # تحديث عدد التحذيرات
    if user_id not in warnings:
        warnings[user_id] = 0
    warnings[user_id] += 1
    
    # إرسال التحذير
    if warnings[user_id] < 3:
        await event.client.send_message(
            chat_id,
            f"**✎┊‌ تم تحذير المستخدم :** [{reply.sender.first_name}](tg://user?id={user_id})\n"
            f"**عدد التحذيرات :** {warnings[user_id]}/3\n{reason_text}"
        )
    else:
        try:
            # إذا كانت المحادثة خاصة، حظر المستخدم
            if event.is_private:
                await event.client.block_user(user_id)
                action = "تم حظر المستخدم من الرسائل الخاصة."
            else:
                # إذا كانت المحادثة مجموعة، حظر المستخدم من المجموعة
                await event.client.kick_participant(chat_id, user_id)
                action = "تم حظر المستخدم من المجموعة."
            
            await event.client.send_message(
                chat_id,
                f"**✎┊‌ تم حظر المستخدم :** [{reply.sender.first_name}](tg://user?id={user_id}) ✓\n"
                f"**السبب:** تجاوز الحد المسموح للتحذيرات.\n**الإجراء:** {action}"
            )
            # حذف التحذيرات بعد الحظر
            del warnings[user_id]
        except Exception as e:
            await event.edit(f"**خـطأ أثناء محاولة الحظر:**\n`{str(e)}`")


@l313l.ar_cmd(
    pattern="التحذيرات$",
    command=("التحذيرات", plugin_category),
    info={
        "header": "Show all users with warnings.",
        "description": "Displays the list of users who have warnings.",
        "usage": "{tr}قائمة التحذيرات",
    },
)
async def list_warnings(event):
    "List all users with warnings"
    if not warnings:
        return await event.edit("**✎┊‌ لا توجد أي تحذيرات حاليًا.**")
    
    output = "**✎┊‌ قائمة المستخدمين المحذرين:**\n\n"
    for user_id, count in warnings.items():
        output += f"**المعرف:** [{user_id}](tg://user?id={user_id})\n**التحذيرات:** {count}/3\n\n"
    
    await event.edit(output)


@l313l.ar_cmd(
    pattern="ازالة التحذير(?: (.*))?$",
    command=("ازالة التحذير", plugin_category),
    info={
        "header": "Remove warnings for a user.",
        "description": "Clears all warnings for the specified user.",
        "usage": "{tr}ازالة التحذيرات <reply>",
    },
)
async def clear_warnings(event):
    "Clear warnings for a user"
    reply = await event.get_reply_message()
    
    if not reply or not isinstance(reply.sender, User):
        return await event.edit("**✎┊‌ قم بالرد على رسالة المستخدم لإزالة تحذيراته.**")
    
    user_id = reply.sender_id
    
    if user_id in warnings:
        del warnings[user_id]
        await event.edit(f"**✎┊‌ تم إزالة جميع التحذيرات عن المستخدم:** [{reply.sender.first_name}](tg://user?id={user_id})")
    else:
        await event.edit("**✎┊‌ هذا المستخدم ليس لديه أي تحذيرات.**")
            
