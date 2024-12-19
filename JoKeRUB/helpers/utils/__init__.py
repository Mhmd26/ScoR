from .extdl import install_pip
from .paste import *

MAX_RETRIES = 5  # الحد الأقصى للمحاولات
retry_count = 0

modules_to_import = {
    "format": "_format",
    "tools": "_cattools",
    "utils": "_catutils",
    "events": None,  # لا حاجة لتعيين اسم مستعار
}

while retry_count < MAX_RETRIES:
    try:
        # استيراد الوحدات المطلوبة
        for module_name, alias in modules_to_import.items():
            module = __import__(f".{module_name}", globals(), locals(), [module_name], 1)
            if alias:
                globals()[alias] = module

        # استيراد إضافي (اختياري)
        from .format import *

        # إذا نجحت جميع الاستيرادات، اكسر الحلقة
        break
    except ModuleNotFoundError as e:
        # تثبيت المكتبة المطلوبة
        print(f"Module {e.name} not found. Attempting to install...")
        install_pip(e.name)
        retry_count += 1
    except Exception as e:
        # التعامل مع أخطاء أخرى (إذا لزم الأمر)
        print(f"Unexpected error: {e}")
        break
else:
    print("Failed to import required modules after multiple attempts.")
