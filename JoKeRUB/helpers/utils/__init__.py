from .extdl import *
from .paste import *

try:
    # محاولة استيراد الوحدات
    from . import format as _format
    from . import tools as _zedtools
    from . import utils as _zedutils
    from .events import *
    from .format import *
    from .tools import *
    from .utils import *
except ModuleNotFoundError as e:
    # تثبيت الوحدة المفقودة إذا لم تكن موجودة
    install_pip(e.name)
    # إعادة المحاولة بعد التثبيت
    try:
        from . import format as _format
        from . import tools as _zedtools
        from . import utils as _zedutils
        from .events import *
        from .format import *
        from .tools import *
        from .utils import *
    except ModuleNotFoundError:
        raise ImportError(f"Unable to import {e.name} even after installing it.")
