from .extdl import *
from .paste import *

def install_pip(package_name):
    import subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", package_name])

try:
    # محاولة استيراد الوحدات
    from . import format as _format
    from . import tools as _cattools
    from . import utils as _catutils
    from .events import *
    from .format import *
except ModuleNotFoundError as e:
    print(f"Module {e.name} not found. Attempting to install it...")
    try:
        # محاولة تثبيت الوحدة المفقودة
        install_pip(e.name)
        # إعادة محاولة الاستيراد بعد التثبيت
        from . import format as _format
        from . import tools as _cattools
        from . import utils as _catutils
        from .events import *
        from .format import *
    except ModuleNotFoundError:
        raise ImportError(f"Unable to import {e.name} even after attempting to install it.")
