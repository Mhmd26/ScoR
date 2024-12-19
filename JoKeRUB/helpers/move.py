from .utils.extdl import install_pip

try:
    from moviepy.editor import VideoFileClip
    print("مكتبة MoviePy مثبتة بالفعل.")
except ModuleNotFoundError:
    print("مكتبة MoviePy غير مثبتة. جارٍ التثبيت...")
    install_pip("moviepy")
    print("تم تثبيت مكتبة MoviePy بنجاح.")
  
