# فريق العقرب 
# علوش @ZS_SQ
# محمد @Zo_r0
import requests
from validators.url import url
from JoKeRUB import l313l

from ..core.managers import edit_delete, edit_or_reply

plugin_category = "utils"

@l313l.ar_cmd(
    pattern="مصغر(?:\s|$)([\s\S]*)",
    command=("مصغر", plugin_category),
    info={
        "header": "To short the given url.",
        "usage": "{tr}short <url/reply to url>",
        "examples": "{tr}short https://github.com/lMl10l1709/catuserbot",
    },
)
async def _(event):
    "shortens the given link"
    input_str = "".join(event.text.split(maxsplit=1)[1:])
    reply = await event.get_reply_message()
    if not input_str and reply:
        input_str = reply.text
    if not input_str:
        return await edit_delete(
            event, "**✎┊‌  يجـب عليم الرد على الرابط او وضع الرابط مع الامر**")
    check = url(input_str)
    if not check:
        catstr = f"http://" + input_str
        check = url(catstr)
    if not check:
        return await edit_delete(event, "**✎┊‌ هذا الرابط غير مدعوم**")
    if not input_str.startswith("http"):
        input_str = "http://" + input_str
    sample_url = f"https://da.gd/s?url={input_str}"
    response_api = requests.get(sample_url).text
    if response_api:
        await edit_or_reply(
            event, f"**✎┊‌ تـم صنـع رابـط مصغر ✓ **\n الرابط : {response_api}", link_preview=False
        )
    else:
        await edit_or_reply(event, "**✎┊‌  هـنالك شي خطـا حاول لاحقـا**")
