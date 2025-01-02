from JoKeRUB import l313l
import google.generativeai as genai
import asyncio

plugin_category = "الذكاء_الاصطناعي"

# إعدادات التوليد
generation_config = {
    "temperature": 1.2,
    "top_p": 1,
    "top_k": 50,
    "max_output_tokens": 4096,
}

safety_settings = [
    {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_NONE"},
    {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_NONE"},
    {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_NONE"},
    {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_NONE"},
]

# تعيين مفتاح API مباشرة
def configure_api():
    api_key = "AIzaSyDC83QfhUo5c17dhZUayLOSUHjM3vjy_0c"  # المفتاح الذي قدمته
    genai.configure(api_key=api_key)

# إنشاء محادثة جديدة مع Gemini
async def make_new_gemini_convo():
    loop = asyncio.get_running_loop()

    def create_convo():
        model = genai.GenerativeModel(
            model_name="models/gemini-1.5-flash-latest",
            generation_config=generation_config,
            safety_settings=safety_settings,
        )
        return model.start_chat()

    convo = await loop.run_in_executor(None, create_convo)
    return convo

# إرسال رسالة للنموذج
async def send_message(convo, message):
    loop = asyncio.get_running_loop()

    def get_response():
        convo.send_message(message)
        return convo.last.text

    response = await loop.run_in_executor(None, get_response)
    return response

# أمر التفاعل مع Gemini
@l313l.ar_cmd(
    pattern="سؤال (.+)",
    command=("سؤال", plugin_category),
    info={
        "header": "لـ التفاعل مع Gemini",
        "الاستخدام": "{tr}ذكاء <سؤالك>",
    },
)
async def ask_gemini(event):
    user_input = event.pattern_match.group(1).strip()

    if user_input:
        try:
            await event.edit("**✎┊‌يتم الاجابه عن سؤالك ⏳**")
            convo = await make_new_gemini_convo()
            response = await send_message(convo, user_input)
            await event.respond(f"**✎┊‌ الإجابة : **\n\n{response}\n\n [• 𝗦𝗰𝗼𝗿𝗚𝗣𝗧](t.me/Scorpion_scorp)")
            await event.delete()
        except Exception as e:
            await event.edit("حدث خطأ أثناء التواصل مع الذكاء الاصطناعي.")
    else:
        await event.edit("يرجى إدخال سؤالك بعد الأمر.")

# تهيئة مفتاح API عند بدء البرنامج
configure_api()
