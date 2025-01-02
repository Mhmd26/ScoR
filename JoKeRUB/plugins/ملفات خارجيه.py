import os
from pathlib import Path

from telethon import events
from telethon.tl.types import InputMessagesFilterDocument

from ..Config import Config
from ..helpers.utils import install_pip
from ..utils import load_module, remove_module
from . import BOTLOG, BOTLOG_CHATID, l313l

plugin_category = "tools"

if Config.PLUGIN_CHANNEL:

    async def install():
        """
        وظيفة لتثبيت المكونات الإضافية من قناة محددة.
        تقوم بتنزيل الملفات وتحميلها إلى النظام.
        """
        documentss = await l313l.get_messages(
            Config.PLUGIN_CHANNEL, None, filter=InputMessagesFilterDocument
        )
        total = int(documentss.total)
        for module in range(total):
            plugin_to_install = documentss[module].id
            plugin_name = documentss[module].file.name
            if os.path.exists(f"JoKeRUB/plugins/{plugin_name}"):
                # إذا كان المكون مثبتًا بالفعل
                return
            downloaded_file_name = await l313l.download_media(
                await l313l.get_messages(Config.PLUGIN_CHANNEL, ids=plugin_to_install),
                "JoKeRUB/plugins/",
            )
            path1 = Path(downloaded_file_name)
            shortname = path1.stem
            flag = True
            check = 0
            while flag:
                try:
                    load_module(shortname.replace(".py", ""))
                    break
                except ModuleNotFoundError as e:
                    # تثبيت الحزم المفقودة تلقائيًا
                    install_pip(e.name)
                    check += 1
                    if check > 5:
                        break
            if BOTLOG:
                await l313l.send_message(
                    BOTLOG_CHATID,
                    f"✎┊‌ تـم تـنصـيب المـلف `{os.path.basename(downloaded_file_name)}` بنجاح ✅.",
                )

    async def uninstall(plugin_name):
        """
        وظيفة لإلغاء تثبيت المكونات الإضافية.
        تقوم بحذف الملف من النظام وإلغاء تحميله.
        """
        plugin_path = f"JoKeRUB/plugins/{plugin_name}"
        if os.path.exists(plugin_path):
            try:
                # إزالة تحميل المكون من النظام
                remove_module(plugin_name)
                # حذف الملف من المجلد
                os.remove(plugin_path)
                if BOTLOG:
                    await l313l.send_message(
                        BOTLOG_CHATID,
                        f"✎┊‌ تـم إزالـة المـلف `{plugin_name}` بنجاح ✅.",
                    )
            except Exception as e:
                if BOTLOG:
                    await l313l.send_message(
                        BOTLOG_CHATID,
                        f"✎┊‌ فشـل فـي إزالة المـلف `{plugin_name}` ❌.\nالخطأ: {str(e)}",
                    )
        else:
            if BOTLOG:
                await l313l.send_message(
                    BOTLOG_CHATID,
                    f"✎┊‌ المـلف `{plugin_name}` غيـر موجـود ❌.",
                )

    @l313l.on(events.NewMessage(pattern=r"^\.الغاء تنصيب$"))
    async def uninstall_command(event):
        """
        أمر لإلغاء تثبيت مكون إضافي باستخدام الرد على ملف فقط.
        """
        # التحقق من وجود رد على ملف
        if not event.reply_to_msg_id:
            await event.reply("✎┊‌ الرجاء الرد على الملف الذي تريد إزالته ❌.")
            return

        reply_message = await event.get_reply_message()
        if not (reply_message and reply_message.file and reply_message.file.name):
            await event.reply("✎┊‌ الرد لا يحتوي على ملف صالح ❌.")
            return

        # الحصول على اسم المكون من الملف
        plugin_name = Path(reply_message.file.name).stem.strip()

        if not plugin_name:
            await event.reply("✎┊‌ لم يتمكن البوت من تحديد اسم الملف ❌.")
            return

        # استدعاء وظيفة الإزالة
        await uninstall(plugin_name)
        await event.reply(f"✎┊‌ جـارٍ إزالة المـلف `{plugin_name}`...")

    # بدء تثبيت المكونات تلقائيًا عند تشغيل البوت
    l313l.loop.create_task(install())
    
