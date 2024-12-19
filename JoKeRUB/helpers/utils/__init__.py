import logging
from importlib import import_module

# استيرادات أساسية
from .extdl import *
from .paste import *

# إعداد تسجيل الأخطاء
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# وحدات مطلوبة
required_modules = {
    "format": "_format",
    "tools": "_cattools",
    "utils": "_catutils",
    "events": "events"
}

# استيراد الوحدات المطلوبة مع التعامل مع الأخطاء
for module_name, alias in required_modules.items():
    try:
        module = import_module(f".{module_name}", package=__name__)
        globals()[alias] = module
        logger.info(f"Successfully imported {module_name} as {alias}")
    except ModuleNotFoundError as e:
        logger.error(f"Module {module_name} not found. Ensure it exists: {e}")
        raise ImportError(f"Could not import {module_name}") from e

# تأكيد استيراد إضافات محددة (مثل الوظائف أو الكلاسات)
try:
    from .format import *
except ImportError as e:
    logger.warning(f"Optional import failed: {e}")
