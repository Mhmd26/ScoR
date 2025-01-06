import html
import os
import random
from requests import get
from telethon.tl.functions.photos import GetUserPhotosRequest
from telethon.tl.functions.users import GetFullUserRequest
from telethon.utils import get_input_location

from JoKeRUB import l313l
from random import choice
from l313l.razan.resources.strings import *
from telethon import events
from ..Config import Config
from ..core.managers import edit_or_reply
from ..helpers import get_user_from_event, reply_id
from . import spamwatch
from telethon.utils import get_display_name
from ..helpers.utils import reply_id, _catutils, parse_pre, yaml_format, install_pip, get_user_from_event, _format

plugin_category = "utils"



# فريق العقرب 
# علوش @ZS_SQ
# محمد @Zo_r0
rehu = [
    "شكم مره كتلك خلي نفلش الكروب",
    "باع هذا اللوكي شديسوي",
    "** مالك الكروب واحد زباله ويدور بنات **",
    "**اول مره اشوف بنات يدورن ولد 😂 **",
    "**شوف هذا الكرنج دين مضال براسه**",
    "**انته واحد فرخ وتنيج**",
    "** راح اعترفلك بشي طلعت احب اختك 🥺 **",
    "**مالك الكروب والمشرفين وفرده من قندرتك ضلعي**",
    "**هذا واحد غثيث وكلب ابن كلب**",
    "**لتحجي كدامه هذا نغل يوصل حجي**",
    "**هذا المالك واحد ساقط وقرام ويدور حلوين**",
    "**لو ربك يجي ماتنكشف الهمسه 😂😂**",
]

@l313l.on(admin_cmd(pattern="رفع مرتي(?:\s|$)([\s\S]*)"))
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 7115002714:
        return await edit_or_reply(mention, f"**✎┊‌ لكك دي هذا المطور**")
    if user.id == 815010872:
        return await edit_or_reply(mention, f"**✎┊‌ لكك دي هذا المطور **")
    JoKeRUB = user.last_name.replace("\u2060", "") if user.last_name else user.username
    me = await mention.client.get_me()
    my_first = me.first_name
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    await edit_or_reply(mention, f"** ✎┊‌  المستخدم ** [{JoKeRUB}](tg://user?id={user.id}) \n**✎┊‌  تم رفعها مرتك بواسطه  :**{my_mention} 👰🏼‍♀️.\n**✎┊‌  يلا حبيبي امشي نخلف بيبي 👶🏻🤤** ")

@l313l.on(admin_cmd(pattern="رفع جلب(?:\s|$)([\s\S]*)"))
async def permalink(mention):
    """Generates a link to the user's PM with a custom text."""
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 7115002714:
        return await edit_or_reply(mention, f"**✎┊‌ لكك دي هذا المطور**")
    if user.id == 815010872:
        return await edit_or_reply(mention, f"**✎┊‌ لكك دي هذا المطور **")
    JoKeRUB = user.first_name.replace("\u2060", "") if user.first_name else user.username
    me = await mention.client.get_me()
    my_first = me.first_name
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    await edit_or_reply(mention, f"**✎┊‌ المستخدم** [{JoKeRUB}](tg://user?id={user.id}) \n**✎┊‌  تـم رفعـه جلب 🐶 بواسطة :** {my_mention} \n**✎┊‌  خليه ينبح 😂**") 
    
@l313l.on(admin_cmd(pattern="رفع بربوك(?:\s|$)([\s\S]*)"))
async def permalink(mention):
    """Generates a link to the user's PM with a custom text."""
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 7115002714:
        return await edit_or_reply(mention, f"**✎┊‌ لكك دي هذا المطور**")
    if user.id == 815010872:
        return await edit_or_reply(mention, f"**✎┊‌ لكك دي هذا المطور **")
    JoKeRUB = user.first_name.replace("\u2060", "") if user.first_name else user.username
    me = await mention.client.get_me()
    my_first = me.first_name
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    await edit_or_reply(mention, f"**✎┊‌ المستخدم** [{JoKeRUB}](tg://user?id={user.id}) \n**✎┊‌  تم رفعه بربوك بواسطة :** {my_mention} \n**✎┊‌ ها لچ بربووووك بربووء 😂😉  **") 
    
@l313l.on(admin_cmd(pattern="رفع ططوة(?:\s|$)([\s\S]*)"))
async def permalink(mention):
    """Generates a link to the user's PM with a custom text."""
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 7115002714:
        return await edit_or_reply(mention, f"**✎┊‌ لكك دي هذا المطور**")
    if user.id == 815010872:
        return await edit_or_reply(mention, f"**✎┊‌ لكك دي هذا المطور **")
    JoKeRUB = user.first_name.replace("\u2060", "") if user.first_name else user.username
    me = await mention.client.get_me()
    my_first = me.first_name
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    await edit_or_reply(mention, f"**✎┊‌ المستخدم** [{JoKeRUB}](tg://user?id={user.id}) \n**✎┊‌  تم رفعه ططوة بواسطة :** {my_mention} \n**✎┊‌  لك تبقه فگررر وين ما تروح 🐦‍⬛  **") 
    
@l313l.on(admin_cmd(pattern="رفع تيس(?:\s|$)([\s\S]*)"))
async def permalink(mention):
    """Generates a link to the user's PM with a custom text."""
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 7115002714:
        return await edit_or_reply(mention, f"**✎┊‌ لكك دي هذا المطور**")
    if user.id == 815010872:
        return await edit_or_reply(mention, f"**✎┊‌ لكك دي هذا المطور **")
    JoKeRUB = user.first_name.replace("\u2060", "") if user.first_name else user.username
    me = await mention.client.get_me()
    my_first = me.first_name
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    await edit_or_reply(mention, f"**✎┊‌ المستخدم** [{JoKeRUB}](tg://user?id={user.id}) \n**✎┊‌   تم رفعه تيس  بواسطة :** {my_mention} \n**✎┊‌ها لك تيسسس تيووووس اتياااس 😭😂**") 

@l313l.on(admin_cmd(pattern="رفع مصري(?:\s|$)([\s\S]*)"))
async def permalink(mention):
    """Generates a link to the user's PM with a custom text."""
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 7115002714:
        return await edit_or_reply(mention, f"**✎┊‌ لكك دي هذا المطور**")
    if user.id == 815010872:
        return await edit_or_reply(mention, f"**✎┊‌ لكك دي هذا المطور **")
    JoKeRUB = user.first_name.replace("\u2060", "") if user.first_name else user.username
    me = await mention.client.get_me()
    my_first = me.first_name
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    await edit_or_reply(mention, f"**✎┊‌ المستخدم **[{JoKeRUB}](tg://user?id={user.id}) \n**✎┊‌  تـم رفعـه مصري  بواسطة :** {my_mention} \n**✎┊‌  تاكل فسيخ يباشا؟  **")
    
@l313l.on(admin_cmd(pattern="رفع كتكوت(?:\s|$)([\s\S]*)"))
async def permalink(mention):
    """Generates a link to the user's PM with a custom text."""
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 7115002714:
        return await edit_or_reply(mention, f"**✎┊‌ لكك دي هذا المطور**")
    if user.id == 815010872:
        return await edit_or_reply(mention, f"**✎┊‌ لكك دي هذا المطور **")
    JoKeRUB = user.first_name.replace("\u2060", "") if user.first_name else user.username
    me = await mention.client.get_me()
    my_first = me.first_name
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    await edit_or_reply(mention, f"**✎┊‌ الحلو [{JoKeRUB}](tg://user?id={user.id}) \n✎┊‌  تـم رفعـه كتكوت 🐤 بواسطة : {my_mention} \n✎┊‌    كتككووت نسنس 😚🎀** ")

@l313l.on(admin_cmd(pattern="رفع تاج(?:\s|$)([\s\S]*)"))
async def permalink(mention):
    """Generates a link to the user's PM with a custom text."""
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if custom:
        return await edit_or_reply(mention, f"[{custom}](tg://user?id={user.id})")
    JoKeRUB = user.first_name.replace("\u2060", "") if user.first_name else user.username
    me = await mention.client.get_me()
    my_first = me.first_name
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    await edit_or_reply(mention, f"**✎┊‌ المستخدم [{JoKeRUB}](tg://user?id={user.id}) \n✎┊‌  تـم رفعـه تاج بواسطة :** {my_mention} 👑🔥")

@l313l.on(admin_cmd(pattern="رفع سلبوح(?:\s|$)([\s\S]*)"))
async def permalink(mention):
    """Generates a link to the user's PM with a custom text."""
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if custom:
        return await edit_or_reply(mention, f"[{custom}](tg://user?id={user.id})")
    JoKeRUB = user.first_name.replace("\u2060", "") if user.first_name else user.username
    me = await mention.client.get_me()
    my_first = me.first_name
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    await edit_or_reply(mention, f"**✎┊‌ المستخدم **[{JoKeRUB}](tg://user?id={user.id}) \n**✎┊‌  تـم رفعـه سلبوح 🪱 بواسطة :** {my_mention} \n**✎┊‌ ها لك سلبوح 😂**")

@l313l.on(admin_cmd(pattern="رفع بكلبي(?:\s|$)([\s\S]*)"))
async def permalink(mention):
    """Generates a link to the user's PM with a custom text."""
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    JoKeRUB = user.first_name.replace("\u2060", "") if user.first_name else user.username
    me = await mention.client.get_me()
    my_first = me.first_name
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    await edit_or_reply(mention, f"**✎┊‌ الحلو** [{JoKeRUB}](tg://user?id={user.id}) \n**✎┊‌  تـم رفعـه بكلـبك 🤍 بواسطة :** {my_mention} \n**✎┊‌  خشيت گلبي انت 😔💗**")
    
    

@l313l.on(admin_cmd(pattern="رفع سني(?:\s|$)([\s\S]*)"))
async def permalink(mention):
    """Generates a link to the user's PM with a custom text."""
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 7115002714:
        return await edit_or_reply(mention, f"**✎┊‌ لكك دي هذا المطور**")
    if user.id == 815010872:
        return await edit_or_reply(mention, f"**✎┊‌ لكك دي هذا المطور **")
    JoKeRUB = user.first_name.replace("\u2060", "") if user.first_name else user.username
    me = await mention.client.get_me()
    my_first = me.first_name
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    await edit_or_reply(mention, f"**✎┊‌ المستخدم** [{JoKeRUB}](tg://user?id={user.id}) \n**✎┊‌  تـم رفعـه سني بواسطة :** {my_mention} \n**✎┊‌  دير بالك لا يفجرنا 😹  **")
     
# فريق العقرب 
# علوش @ZS_SQ
# محمد @Zo_r0

@l313l.on(admin_cmd(pattern="رفع شيعي(?:\s|$)([\s\S]*)"))
async def permalink(mention):
    """Generates a link to the user's PM with a custom text."""
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 7115002714:
        return await edit_or_reply(mention, f"**✎┊‌ لكك دي هذا المطور**")
    if user.id == 815010872:
        return await edit_or_reply(mention, f"**✎┊‌ لكك دي هذا المطور **")
    JoKeRUB = user.first_name.replace("\u2060", "") if user.first_name else user.username
    me = await mention.client.get_me()
    my_first = me.first_name
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    await edit_or_reply(mention, f"**✎┊‌ المستخدم** [{JoKeRUB}](tg://user?id={user.id}) \n**✎┊‌  تـم رفعـه شيعي بواسطة :** {my_mention} \n**✎┊‌  دير بالك لا يبوگك 😹 **")
    

@l313l.on(admin_cmd(pattern="رفع سادس(?:\s|$)([\s\S]*)"))
async def permalink(mention):
    """Generates a link to the user's PM with a custom text."""
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    JoKeRUB = user.first_name.replace("\u2060", "") if user.first_name else user.username
    me = await mention.client.get_me()
    my_first = me.first_name
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    await edit_or_reply(mention, f"**✎┊‌ المستخدم** [{JoKeRUB}](tg://user?id={user.id}) \n**✎┊‌  تـم رفع المتهم طالب سادس بواسطة :** {my_mention} \n**✎┊‌  لك انتَ الله غاضب عليك 😂**")

@l313l.on(admin_cmd(pattern="رفع وردة(?:\s|$)([\s\S]*)"))
async def permalink(mention):
    """Generates a link to the user's PM with a custom text."""
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    JoKeRUB = user.first_name.replace("\u2060", "") if user.first_name else user.username
    me = await mention.client.get_me()
    my_first = me.first_name
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    await edit_or_reply(mention, f"**✎┊‌ الحلو** [{JoKeRUB}](tg://user?id={user.id}) \n**✎┊‌  تـم رفعها وردة الكروب 🌹 بواسطة :** {my_mention} \n**✎┊‌ عطرك دوخني 🤍🤭 **")

@l313l.on(admin_cmd(pattern="رفع كردي(?:\s|$)([\s\S]*)"))
async def permalink(mention):
    """Generates a link to the user's PM with a custom text."""
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 7115002714:
        return await edit_or_reply(mention, f"**✎┊‌ لكك دي هذا المطور**")
    if user.id == 815010872:
        return await edit_or_reply(mention, f"**✎┊‌ لكك دي هذا المطور **")
    JoKeRUB = user.first_name.replace("\u2060", "") if user.first_name else user.username
    me = await mention.client.get_me()
    my_first = me.first_name
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    await edit_or_reply(mention, f"**✎┊‌ المستخدم** [{JoKeRUB}](tg://user?id={user.id}) \n**✎┊‌  تـم رفعـه كردي بواسطة :** {my_mention} \n**✎┊‌  كاكا اذا انتة لايك خلي كردي 😹**")

@l313l.ar_cmd(
    pattern="رزله(?:\s|$)([\s\S]*)",
    command=("رزله", plugin_category),
)
async def permalink(mention):
    """Generates a link to the user's PM with a custom text."""
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 7115002714:
        return await edit_or_reply(mention, f"**✎┊‌ لكك دي هذا المطور**")
    if user.id == 815010872:
        return await edit_or_reply(mention, f"**✎┊‌ لكك دي هذا المطور **")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(mention, f"✎┊‌ ولك [{tag}](tg://user?id={user.id}) \n✎┊‌  هيو لتندك بسيادك لا بهاي 👞👈 ")

@l313l.on(admin_cmd(pattern="رفع حية(?:\s|$)([\s\S]*)"))
async def permalink(mention):
    """Generates a link to the user's PM with a custom text."""
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 7115002714:
        return await edit_or_reply(mention, f"**✎┊‌ لكك دي هذا المطور**")
    if user.id == 815010872:
        return await edit_or_reply(mention, f"**✎┊‌ لكك دي هذا المطور **")
    JoKeRUB = user.first_name.replace("\u2060", "") if user.first_name else user.username
    me = await mention.client.get_me()
    my_first = me.first_name
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    await edit_or_reply(mention, f"**✎┊‌ المستخدم** [{JoKeRUB}](tg://user?id={user.id}) \n**✎┊‌  تـم رفعـها حية الكروب  بواسطة :** {my_mention} \n**✎┊‌  ها لچ تس تس 🐍😉 **")

@l313l.on(admin_cmd(pattern="رفع حامل(?:\s|$)([\s\S]*)"))
async def permalink(mention):
    """Generates a link to the user's PM with a custom text."""
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 7115002714:
        return await edit_or_reply(mention, f"**✎┊‌ لكك دي هذا المطور**")
    if user.id == 815010872:
        return await edit_or_reply(mention, f"**✎┊‌ لكك دي هذا المطور **")
    JoKeRUB = user.first_name.replace("\u2060", "") if user.first_name else user.username
    me = await mention.client.get_me()
    my_first = me.first_name
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    await edit_or_reply(mention, f"**✎┊‌ المستخدم** [{JoKeRUB}](tg://user?id={user.id}) \n**✎┊‌  تـم رفعـه حامل 🤰 بواسطة :** {my_mention} \n**✎┊‌  بيا شهر 🤰؟😹  **")

@l313l.on(admin_cmd(pattern="رفع اخوة(?:\s|$)([\s\S]*)"))
async def permalink(mention):
    """Generates a link to the user's PM with a custom text."""
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    JoKeRUB = user.first_name.replace("\u2060", "") if user.first_name else user.username
    me = await mention.client.get_me()
    my_first = me.first_name
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    await edit_or_reply(mention, f"**✎┊‌ المستخدم** [{JoKeRUB}](tg://user?id={user.id}) \n**✎┊‌  تم رفعه اخ بواسطه :** {my_mention} \n**✎┊‌   اخوي الزود وحزام الضهر 🤧😂  **")

@l313l.ar_cmd(
    pattern="مصه(?:\s|$)([\s\S]*)",
    command=("مصه", plugin_category),
)
async def permalink(mention):
    """Generates a link to the user's PM with a custom text."""
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 815010872:
        return await edit_or_reply(mention, f"**✎┊‌ لكك دي هذا المطور**")
    if user.id == 7115002714:
        return await edit_or_reply(mention, f"**✎┊‌ لكك دي هذا المطور **")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(mention, f"** ⣠⡶⠚⠛⠲⢄⡀\n⣼⠁      ⠀⠀⠀⠳⢤⣄\n⢿⠀⢧⡀⠀⠀⠀⠀⠀⢈⡇\n⠈⠳⣼⡙⠒⠶⠶⠖⠚⠉⠳⣄\n⠀⠀⠈⣇⠀⠀⠀⠀⠀⠀⠀⠈⠳⣄\n⠀⠀⠀⠘⣆       ⠀⠀⠀⠀⠀⠈⠓⢦⣀\n⠀⠀⠀⠀⠈⢳⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠲⢤\n⠀⠀⠀⠀⠀⠀⠙⢦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢧\n⠀⠀⠀⠀⠀⠀⠀    ⠓⠦⠀⠀⠀⠀**\n**🚹 ¦ تعال مصه عزيزي ** [{tag}](tg://user?id={user.id})")

@l313l.on(admin_cmd(pattern="سورس(?:\s|$)([\s\S]*)"))
async def permalink(mention):
    await edit_or_reply(mention, f"@Scorpion_scorp")

@l313l.on(admin_cmd(pattern="رفع سندرلا(?:\s|$)([\s\S]*)"))
async def permalink(mention):
    """Generates a link to the user's PM with a custom text."""
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 7115002714:
        return await edit_or_reply(mention, f"**✎┊‌ لكك دي هذا المطور**")
    if user.id == 815010872:
        return await edit_or_reply(mention, f"**✎┊‌ لكك دي هذا المطور **")
    JoKeRUB = user.first_name.replace("\u2060", "") if user.first_name else user.username
    me = await mention.client.get_me()
    my_first = me.first_name
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    await edit_or_reply(mention, f"**✎┊‌ الحلو** [{JoKeRUB}](tg://user?id={user.id}) \n**✎┊‌  تـم رفعـها سندرلا 😍 بواسطة :** {my_mention} \n**✎┊‌  لحظه حذائج وكع 👠 🥰😂  **")

@l313l.on(admin_cmd(pattern="رفع بزون(?:\s|$)([\s\S]*)"))
async def permalink(mention):
    """Generates a link to the user's PM with a custom text."""
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 7115002714:
        return await edit_or_reply(mention, f"**✎┊‌ لكك دي هذا المطور**")
    if user.id == 815010872:
        return await edit_or_reply(mention, f"**✎┊‌ لكك دي هذا المطور **")
    JoKeRUB = user.first_name.replace("\u2060", "") if user.first_name else user.username
    me = await mention.client.get_me()
    my_first = me.first_name
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    await edit_or_reply(mention, f"**✎┊‌ الحلو** [{JoKeRUB}](tg://user?id={user.id}) \n**✎┊‌  تـم رفعـه بزون 🐱 بواسطة :** {my_mention} \n**✎┊‌ كول ميااااو 🎀🐱 **")

@l313l.on(admin_cmd(pattern="رفع طلي(?:\s|$)([\s\S]*)"))
async def permalink(mention):
    """Generates a link to the user's PM with a custom text."""
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 7115002714:
        return await edit_or_reply(mention, f"**✎┊‌ لكك دي هذا المطور**")
    if user.id == 815010872:
        return await edit_or_reply(mention, f"**✎┊‌ لكك دي هذا المطور **")
    JoKeRUB = user.first_name.replace("\u2060", "") if user.first_name else user.username
    me = await mention.client.get_me()
    my_first = me.first_name
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    await edit_or_reply(mention, f"**✎┊‌ المستخدم** [{JoKeRUB}](tg://user?id={user.id}) \n**✎┊‌  تـم رفعه طلي 🐏 بواسطة :** {my_mention} \n**✎┊‌ كوول ميعععع خل اخذلك صورة 😹🐏   **")

@l313l.on(admin_cmd(pattern="رفع جانتي(?:\s|$)([\s\S]*)"))
async def permalink(mention):
    """Generates a link to the user's PM with a custom text."""
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 7115002714:
        return await edit_or_reply(mention, f"**✎┊‌ لكك دي هذا المطور**")
    if user.id == 815010872:
        return await edit_or_reply(mention, f"**✎┊‌ لكك دي هذا المطور **")
    JoKeRUB = user.first_name.replace("\u2060", "") if user.first_name else user.username
    me = await mention.client.get_me()
    my_first = me.first_name
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    await edit_or_reply(mention, f"**✎┊‌ المستخدم** [{JoKeRUB}](tg://user?id={user.id}) \n**✎┊‌  تـم رفعه جانتي بواسطة :** {my_mention} \n**✎┊‌ لك انتة تبقة ثور مع احترامي الك 😂 **")

@l313l.on(admin_cmd(pattern="رفع مميز(?:\s|$)([\s\S]*)"))
async def permalink(mention):
    """Generates a link to the user's PM with a custom text."""
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 7115002714:
        return await edit_or_reply(mention, f"**✎┊‌ لكك دي هذا المطور**")
    if user.id == 815010872:
        return await edit_or_reply(mention, f"**✎┊‌ لكك دي هذا المطور **")
    JoKeRUB = user.first_name.replace("\u2060", "") if user.first_name else user.username
    me = await mention.client.get_me()
    my_first = me.first_name
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    await edit_or_reply(mention, f"**✎┊‌ الحلو** 「[{JoKeRUB}](tg://user?id={user.id})」 \n**✎┊‌  تـم رفعه مميز بواسطة :** {my_mention}")

@l313l.on(admin_cmd(pattern="رفع ادمن(?:\s|$)([\s\S]*)"))
async def permalink(mention):
    """Generates a link to the user's PM with a custom text."""
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 7115002714:
        return await edit_or_reply(mention, f"**✎┊‌ لكك دي هذا المطور**")
    if user.id == 815010872:
        return await edit_or_reply(mention, f"**✎┊‌ لكك دي هذا المطور **")
    JoKeRUB = user.first_name.replace("\u2060", "") if user.first_name else user.username
    me = await mention.client.get_me()
    my_first = me.first_name
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    await edit_or_reply(mention, f"**✎┊‌ الحلو** 「[{JoKeRUB}](tg://user?id={user.id})」 \n**✎┊‌  تـم رفعه ادمن بواسطة :** {my_mention}")

@l313l.on(admin_cmd(pattern="رفع منشئ(?:\s|$)([\s\S]*)"))
async def permalink(mention):
    """Generates a link to the user's PM with a custom text."""
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 7115002714:
        return await edit_or_reply(mention, f"**✎┊‌ لكك دي هذا المطور**")
    if user.id == 815010872:
        return await edit_or_reply(mention, f"**✎┊‌ لكك دي هذا المطور **")
    JoKeRUB = user.first_name.replace("\u2060", "") if user.first_name else user.username
    me = await mention.client.get_me()
    my_first = me.first_name
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    await edit_or_reply(mention, f"**✎┊‌ الحلو** 「[{JoKeRUB}](tg://user?id={user.id})」 \n**✎┊‌  تـم رفعه منشئ بواسطة :** {my_mention}")

@l313l.on(admin_cmd(pattern="رفع مالك(?:\s|$)([\s\S]*)"))
async def permalink(mention):
    """Generates a link to the user's PM with a custom text."""
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 7115002714:
        return await edit_or_reply(mention, f"**✎┊‌ لكك دي هذا المطور**")
    if user.id == 815010872:
        return await edit_or_reply(mention, f"**✎┊‌ لكك دي هذا المطور **")
    JoKeRUB = user.first_name.replace("\u2060", "") if user.first_name else user.username
    me = await mention.client.get_me()
    my_first = me.first_name
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    await edit_or_reply(mention, f"**✎┊‌ الحلو** 「[{JoKeRUB}](tg://user?id={user.id})」 \n**✎┊‌  تـم رفعه مالك الكروب بواسطة :** {my_mention}")

@l313l.on(admin_cmd(pattern="رفع مجنب(?:\s|$)([\s\S]*)"))
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 7115002714:
        return await edit_or_reply(mention, f"**✎┊‌ لكك دي هذا المطور**")
    if user.id == 815010872:
        return await edit_or_reply(mention, f"**✎┊‌ لكك دي هذا المطور **")
    JoKeRUB = user.last_name.replace("\u2060", "") if user.last_name else user.username
    me = await mention.client.get_me()
    my_first = me.first_name
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    await edit_or_reply(mention, f" ** ✎┊‌  المستخدم => • ** [{JoKeRUB}](tg://user?id={user.id}) \n ☑️ **✎┊‌  تم رفعه مجنب بواسطه  :**{my_mention} .\n**✎┊‌  كوم يلمجنب اسبح مو عيب تضرب جلغ 😹** ")

@l313l.on(admin_cmd(pattern="رفع وصخ(?:\s|$)([\s\S]*)"))
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 7115002714:
        return await edit_or_reply(mention, f"**✎┊‌ لكك دي هذا المطور**")
    if user.id == 815010872:
        return await edit_or_reply(mention, f"**✎┊‌ لكك دي هذا المطور **")
    JoKeRUB = user.last_name.replace("\u2060", "") if user.last_name else user.username
    me = await mention.client.get_me()
    my_first = me.first_name
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    await edit_or_reply(mention, f"** ✎┊‌  المستخدم ** [{JoKeRUB}](tg://user?id={user.id}) \n ☑️ **✎┊‌  تم رفعه وصخ الكروب 🤢 بواسطه  :**{my_mention} .\n**✎┊‌  لك دكوم يلوصخ اسبح مو ريحتك كتلتنا 🤮 ** ")

@l313l.on(admin_cmd(pattern="زواج(?:\s|$)([\s\S]*)"))
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 7115002714:
        return await edit_or_reply(mention, f"**✎┊‌ لكك دي هذا المطور**")
    if user.id == 815010872:
        return await edit_or_reply(mention, f"**✎┊‌ لكك دي هذا المطور **")
    JoKeRUB = user.last_name.replace("\u2060", "") if user.last_name else user.username
    me = await mention.client.get_me()
    my_first = me.first_name
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    await edit_or_reply(mention, f"✎┊‌ ** لقد تم زواجك/ج من : **[{JoKeRUB}](tg://user?id={user.id}) 💍\n**✎┊‌  الف الف مبروك الان يمكنك اخذ راحتك ** ")

@l313l.on(admin_cmd(pattern="طلاك(?:\s|$)([\s\S]*)"))
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 7115002714:
        return await edit_or_reply(mention, f"**✎┊‌ لكك دي هذا المطور**")
    if user.id == 815010872:
        return await edit_or_reply(mention, f"**✎┊‌ لكك دي هذا المطور **")
    JoKeRUB = user.last_name.replace("\u2060", "") if user.last_name else user.username
    me = await mention.client.get_me()
    my_first = me.first_name
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    await edit_or_reply(mention, f"**✎┊‌  انتِ طالق طالق طالق 🙎🏻‍♂️ من  :**{my_mention} .\n**✎┊‌  لقد تم طلاقها بلثلاث وفسخ زواجكما الان الكل حر طليق ** ")
lMl10l = [7115002714, 815010872]
@l313l.on(events.NewMessage(incoming=True))
async def Hussein(event):
    if event.reply_to and event.sender_id in lMl10l:
       reply_msg = await event.get_reply_message()
       owner_id = reply_msg.from_id.user_id
       if owner_id == l313l.uid:
           if event.message.message == "منصب؟":
               await event.reply("**اي حبيبي منصب ✅**")
           elif event.message.message == "منو فخر العرب؟":
               await event.reply("**الأمام علي عليه الصلاة والسلام ❤️**")
           elif event.message.message == "تاج راسك منو؟":
               await event.reply("**محمد و علوش**")
           elif event.message.message == "علوش":
               await event.reply("**لك هاذ تاج راسيييي😔@I_e_e_l**") 
           elif event.message.message == "اقوة سورس منو؟":
               await event.reply("سورس العقرب واحد عراق")
           elif event.message.message == "محمد":
               await event.reply("**لك هاذ تاج راسيييي😔@Zo_r0**")
@l313l.on(admin_cmd(pattern="همسه(?:\s|$)([\s\S]*)"))
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    JoKeRUB = user.last_name.replace("\u2060", "") if user.last_name else user.username
    me = await mention.client.get_me()
    my_first = me.first_name
    lMl10l = random.choice(rehu)
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    await edit_or_reply(mention, f"**✎┊‌الهمسة من المستخدم [{JoKeRUB}](tg://user?id={user.id}) تم كشفها بنجاح ✓**\n**✎┊‌  الهمسة هي : {lMl10l} ** ")
