import os
import time
from JoKeRUB import l313l

plugin_category = "الادوات"

# قائمة لتتبع أسماء الجروبات النشطة
enabled_groups = []

# أمر نشر في الجروبات
@l313l.ar_cmd(
    pattern=r"نشر (\d+) (\S+)",
    command=("نشر", plugin_category),
    info={
        "header": "لنشر رسالة في أكثر من جروب مع فاصل زمني بين كل نشر بشكل لا نهائي",
        "الاستخدام": "{tr}نشر <الوقت بالثواني> <رابط الجروبات>",
    },
)
async def post_message_in_groups(event):
    delay = int(event.pattern_match.group(1).strip())
    groups_links = event.pattern_match.group(2).strip().split()

    # التأكد من وجود رسالة للرد عليها
    message = await event.get_reply_message()
    if message:
        try:
            await event.edit(f"**✎┊‌سيتم نشر الرسالة في الجروبات المحددة مع فاصل زمني قدره {delay} ثانية بين كل نشر بشكل لا نهائي.**")
            
            # إضافة أسماء الجروبات إلى قائمة النشر المفعل
            for group_link in groups_links:
                if group_link not in enabled_groups:
                    enabled_groups.append(group_link)

            # نشر الرسالة بشكل لا نهائي في الجروبات المحددة
            while enabled_groups:
                for group_link in groups_links:
                    if group_link in enabled_groups:  # النشر فقط إذا كان الجروب لا يزال مفعلًا
                        try:
                            await event.client.send_message(group_link, message.text)
                        except Exception as e:
                            await event.respond(f"**✎┊‌حدث خطأ أثناء النشر في {group_link}: {str(e)}**")
                            enabled_groups.remove(group_link)  # إزالة الجروب من القائمة في حالة وجود خطأ
                        time.sleep(delay)  # الانتظار قبل نشر الرسالة التالية
        except Exception as e:
            await event.edit(f"حدث خطأ أثناء نشر الرسالة: {str(e)}")
    else:
        await event.edit("**✎┊‌لم يتم العثور على رسالة للرد عليها!**")

# أمر إيقاف نشر رسالة في جميع الجروبات
@l313l.ar_cmd(
    pattern=r"إيقاف النشر",
    command=("إيقاف النشر", plugin_category),
    info={
        "header": "لإيقاف نشر الرسائل في جميع الجروبات",
        "الاستخدام": "{tr}إيقاف نشر",
    },
)
async def stop_posting_in_all_groups(event):
    # إيقاف النشر في جميع الجروبات
    enabled_groups.clear()
    await event.edit("**✎┊‌تم إيقاف نشر الرسائل في جميع الجروبات.**")
