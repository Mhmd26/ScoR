import os
import shutil
from JoKeRUB import l313l
from ..core.managers import edit_or_reply
from ..helpers.utils import _catutils
plugin_category = "tools"

@l313l.ar_cmd(
    pattern="ملفات العقرب$",
    command=("ملفات العقرب", plugin_category),
    info={
        "header": "To list all plugins in JoKeRUB.",
        "usage": "{tr}plugins",
    },
)
async def _(event):
    "To list all plugins in JoKeRUB"
    cmd = "ls JoKeRUB/plugins"
    o = (await _catutils.runcmd(cmd))[0]
    OUTPUT = f"**[العقرب](tg://need_update_for_some_feature/) الـمـلفـات:**\n{o}"
    await edit_or_reply(event, OUTPUT)

@l313l.ar_cmd(
    pattern="تحميل العقرب$",
    command=("تحميل العقرب", plugin_category),
    info={
        "header": "Compress and send JoKeRUB folder.",
        "usage": "{tr}تحميل العقرب",
    },
)
async def _(event):
    "Compress JoKeRUB folder and send it."
    await edit_or_reply(event, "**✎┊‌ يُجري عملية ضغط المجلد . .**")
    try:
        # تحديد اسم الملف المضغوط
        zip_file = "JoKeRUB.zip"
        
        # ضغط المجلد
        shutil.make_archive("JoKeRUB", "zip", "JoKeRUB")
        
        # إرسال الملف
        await event.client.send_file(event.chat_id, zip_file, caption="**✎┊‌ تم ضغط وإرسال مجلد JoKeRUB بنجاح.**")
        
        # حذف الملف المضغوط بعد الإرسال
        os.remove(zip_file)
        
        await edit_or_reply(event, "**✎┊‌ تم إرسال المجلد المضغوط بنجاح.**")
    except Exception as e:
        await edit_or_reply(event, f"**✎┊‌ حدث خطأ أثناء العملية:**\n`{str(e)}`")
