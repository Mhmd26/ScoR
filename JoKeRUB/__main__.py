import sys
import contextlib
import JoKeRUB
import asyncio
from JoKeRUB import BOTLOG_CHATID, HEROKU_APP, PM_LOGGER_GROUP_ID
from .Config import Config
from .core.logger import logging
from .core.session import l313l
from .utils import (
    add_bot_to_logger_group,
    install_externalrepo,
    load_plugins,
    setup_bot,
    mybot,
    startupmessage,
    verifyLoggerGroup,
    saves,
)

LOGS = logging.getLogger(".")


LOGS.info(JoKeRUB.__copyright__)
LOGS.info(f"Licensed under the terms of the {JoKeRUB.__license__}")

cmdhr = Config.COMMAND_HAND_LER

try:
    LOGS.info("جار بدء بوت العقرب ✓")
    l313l.loop.run_until_complete(setup_bot())
    LOGS.info("تم اكتمال تنصيب البوت ✓")
except Exception as e:
    LOGS.error(f"{str(e)}")
    sys.exit()

try:
    LOGS.info("يتم تفعيل وضع الانلاين")
    l313l.loop.run_until_complete(mybot())
    LOGS.info("تم تفعيل وضع الانلاين بنجاح ✓")
except Exception as jep:
    LOGS.error(f"- {jep}")
    sys.exit()    

async def startup_process():
    await verifyLoggerGroup()
    await load_plugins("plugins")
    await load_plugins("assistant")
    LOGS.info("""
╔══════════════════════════════╗

 ✎┊‌ الانلاين يعمل الان ✓
 تم تشغيل سورس العقرب بنجاح ارسل كلمة فحص للتأكد
 𝗦𝗰𝗼𝗿𝗽𝗶𝗼 𝘄𝗼𝗿𝗸𝘀 𝘀𝘂𝗰𝗰𝗲𝘀𝘀𝗳𝘂𝗹𝗹𝘆 ✅
 
╚══════════════════════════════╝
""")
    await verifyLoggerGroup()
    await saves()
    await add_bot_to_logger_group(BOTLOG_CHATID)
    if PM_LOGGER_GROUP_ID != -100:
        await add_bot_to_logger_group(PM_LOGGER_GROUP_ID)
    await startupmessage()
    return
    

    
async def externalrepo():
    if Config.VCMODE:
        await install_externalrepo("https://github.com/Mhmd26/ScoR", "jepvc", "jepthonvc")

l313l.loop.run_until_complete(externalrepo())
l313l.loop.run_until_complete(startup_process())

    

if len(sys.argv) in {1, 3, 4}:
    with contextlib.suppress(ConnectionError):
        l313l.run_until_disconnected()
else:
        l313l.disconnect()
  
