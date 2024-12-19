from . import fonts
from . import memeshelper as catmemes
from .aiohttp_helper import AioHttp
from .utils import *
from .telegraph_utils import post_to_telegraph
from .time_utils import time_formatter
from .utiles import sanga_seperator
from .times_utils import readable_time
from .media_utils import media_type
from .media_type import *  # إضافة اسم الملف هنا
    # تأكد من أنك قد حصلت على مفتاح API من Telegraph
                            
flag = True
check = 0
while flag:
    try:
        from .chatbot import *
        from .functions import *
        from .memeifyhelpers import *
        from .progress import *
        from .qhelper import process
        from .tools import *
        from .utils import _cattools, _catutils, _format

        break
    except ModuleNotFoundError as e:
        install_pip(e.name)
        check += 1
        if check > 5:
            break
