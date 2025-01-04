from JoKeRUB import l313l
import subprocess
import sys

plugin_category = "الذكاء_الاصطناعي"

# أمر لتثبيت المكتبة المحددة من قبل المستخدم
@l313l.ar_cmd(
    pattern="تثبيت (.+)",
    command=("تثبيت", plugin_category),
    info={
        "header": "لتثبيت مكتبة معينة عبر pip",
        "الاستخدام": "{tr}تثبيت <اسم المكتبة>",
    },
)
async def install_library(event):
    library_name = event.pattern_match.group(1).strip()

    if library_name:
        await event.edit(f"**✎┊‌ جاري تثبيت المكتبة : \n {library_name} ⏳**")  # رسالة انتظار
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", library_name])
            await event.edit(f"**✎┊‌ تم تثبيت المكتبة بنجاح: \n {library_name} ✅**")
        except Exception as e:
            await event.edit(f"**✎┊‌ حدث خطأ أثناء تثبيت المكتبة: {str(e)}**")
    else:
        await event.edit("**✎┊‌ يرجى إدخال اسم المكتبة بعد الأمر.**")
