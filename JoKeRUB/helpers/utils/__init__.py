from .extdl import *
from .paste import *

flag = True
check = 0
while flag:
    try:
        # تأكد من أن الملفات هذه موجودة ومرتبة بشكل صحيح
        from . import format as _format
        from . import tools as _cattools  # تأكد من أن هذا الملف موجود
        from . import utils as _catutils
        from .events import *
        from .format import *
        
        break
    except ModuleNotFoundError as e:
        print(f"خطأ في استيراد {e.name} ... جاري تثبيت المكتبة.")
        install_pip(e.name)
        check += 1
        if check > 5:
            print("فشلت عملية التثبيت بعد 5 محاولات.")
            break
