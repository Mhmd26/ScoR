import asyncio
from JoKeRUB import l313l

plugin_category = "utils"
stop_flags = {}  # لتتبع الإيقاف لكل مجموعة
global_stop = False  # علم لإيقاف جميع النشر
active_broadcasts = []  # قائمة للنشر الجاري

@l313l.ar_cmd(
    pattern="نشر(?: (.*))?$",
    command=("نشر", plugin_category),
    info={
        "header": "نشر رسالة إلى مجموعة.",
        "description": "ينشر الرسالة التي تم الرد عليها إلى مجموعة باستخدام الرابط أو المعرف مع تحديد وقت بين كل رسالة.",
        "usage": "{tr}انشر <رابط أو معرف المجموعة> <الوقت بين الرسائل بالثواني>",
    },
)
async def broadcast_message(event):
    "نشر رسالة إلى مجموعة مع وقت انتظار بين الرسائل"
    global global_stop, active_broadcasts
    args = event.pattern_match.group(1)
    
    if not args:
        return await event.edit("**✎┊‌ يرجى إدخال الرابط أو معرف المجموعة والوقت بين الرسائل.**")
    
    try:
        group_link_or_id, delay = args.split()
        delay = int(delay)
    except ValueError:
        return await event.edit("**✎┊‌ التنسيق غير صحيح. يرجى استخدام:\n.انشر <رابط/معرف المجموعة> <الوقت بين الرسائل>**")
    
    reply = await event.get_reply_message()
    if not reply:
        return await event.edit("**✎┊‌ يرجى الرد على رسالة لنشرها.**")
    
    if group_link_or_id.startswith("http"):
        try:
            group_entity = await event.client.get_entity(group_link_or_id)
            group_id = group_entity.id
        except Exception as e:
            return await event.edit(f"**✎┊‌ خـطأ في الحصول على معرف المجموعة من الرابط:**\n`{str(e)}`")
    else:
        group_id = group_link_or_id
    
    if group_id in active_broadcasts:
        return await event.edit("**✎┊‌ عملية النشر لهذه المجموعة قيد التنفيذ بالفعل.**")
    
    stop_flags[group_id] = False
    active_broadcasts.append(group_id)  # إضافة إلى قائمة النشر النشط
    await event.edit("**✎┊‌ بدأ نشر الرسائل...**")
    
    try:
        for _ in range(50):  # يمكنك تغيير العدد
            if global_stop or stop_flags.get(group_id):
                if group_id in active_broadcasts:
                    active_broadcasts.remove(group_id)  # إزالة من قائمة النشر النشط
                await event.edit("**✎┊‌ تم إيقاف النشر بنجاح.**")
                return
            await event.client.send_message(group_id, reply)
            await asyncio.sleep(delay)
        if group_id in active_broadcasts:
            active_broadcasts.remove(group_id)  # إزالة من قائمة النشر النشط بعد الانتهاء
        await event.edit("**✎┊‌ تم نشر الرسائل بنجاح.**")
    except Exception as e:
        if group_id in active_broadcasts:
            active_broadcasts.remove(group_id)  # إزالة من قائمة النشر النشط في حال وجود خطأ
        await event.edit(f"**✎┊‌ خـطأ أثناء نشر الرسالة:**\n`{str(e)}`")

@l313l.ar_cmd(
    pattern="ايقاف نشر(?: (.*))?$",
    command=("ايقاف نشر", plugin_category),
    info={
        "header": "إيقاف نشر الرسائل إلى مجموعة.",
        "description": "يوقف عملية نشر الرسائل المستمرة إلى مجموعة محددة.",
        "usage": "{tr}ايقاف <رابط أو معرف المجموعة>",
    },
)
async def stop_broadcast(event):
    "إيقاف نشر الرسائل إلى مجموعة"
    global active_broadcasts
    args = event.pattern_match.group(1)
    if not args:
        return await event.edit("**✎┊‌ يرجى إدخال الرابط أو معرف المجموعة.**")
    
    if args.startswith("http"):
        try:
            group_entity = await event.client.get_entity(args)
            group_id = group_entity.id
        except Exception as e:
            return await event.edit(f"**✎┊‌ خـطأ في الحصول على معرف المجموعة من الرابط:**\n`{str(e)}`")
    else:
        group_id = args
    
    if group_id in stop_flags:
        stop_flags[group_id] = True
        if group_id in active_broadcasts:
            active_broadcasts.remove(group_id)  # إزالة من قائمة النشر النشط
        await event.edit("**✎┊‌ تم إرسال أمر الإيقاف بنجاح.**")
    else:
        await event.edit("**✎┊‌ لا توجد عملية نشر قيد التشغيل لهذه المجموعة.**")

@l313l.ar_cmd(
    pattern="ايقاف كل النشر$",
    command=("ايقاف كل النشر", plugin_category),
    info={
        "header": "إيقاف جميع عمليات النشر.",
        "description": "يوقف جميع عمليات نشر الرسائل المستمرة إلى أي مجموعة.",
        "usage": "{tr}ايقاف_الكل",
    },
)
async def stop_all_broadcasts(event):
    "إيقاف جميع عمليات النشر"
    global global_stop, active_broadcasts
    global_stop = True
    active_broadcasts.clear()  # تفريغ قائمة النشر النشط
    await event.edit("**✎┊‌ تم إيقاف جميع عمليات النشر بنجاح.**")

@l313l.ar_cmd(
    pattern="قائمة النشر$",
    command=("قائمة النشر", plugin_category),
    info={
        "header": "عرض قائمة المجموعات التي يتم النشر إليها.",
        "description": "يعرض جميع المجموعات التي يتم النشر إليها حاليًا.",
        "usage": "{tr}قائمة_النشر",
    },
)
async def list_active_broadcasts(event):
    "عرض قائمة المجموعات التي يتم النشر إليها حاليًا"
    global active_broadcasts
    if not active_broadcasts:
        return await event.edit("**✎┊‌ لا توجد عمليات نشر نشطة حاليًا.**")
    
    groups_list = "\n".join([str(group) for group in active_broadcasts])
    await event.edit(f"**✎┊‌ قائمة النشر النشط:**\n{groups_list}")
