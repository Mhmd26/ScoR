from JoKeRUB import l313l

from ..core.managers import edit_or_reply 
@l313l.on(admin_cmd(pattern="اوامر الضحك(?: |$)(.*)"))
async def _(event):
    await edit_or_reply(event, "\n **قائمة الضحك العقرب ✍🏻** \n \n ✎┊‌ اختر احداها:          \n- {`.طيط`} \n- {`.طح`} \n- {`.موت`} \n- {`.نعل`} \n- {`.اسبح`} \n- {`.بشر`} \n- {`.الحيوان`} \n- {`.صلي`} \n- {`.صمون`} \n **العقرب | 𝐒𝐜𝐨𝐫𝐩𝐢𝐨𝐧 ☑️**") 

@l313l.on(admin_cmd(pattern="طيط(?: |$)(.*)"))
async def _(event):
    await edit_or_reply(event, "طيطيطيطيطيطيططيطيييطططططططططططططططططططططططططططططططططططططططططططططططططططططططططط")
            
@l313l.on(admin_cmd(pattern="طح(?: |$)(.*)"))
async def _(event):
    await edit_or_reply(event, "طح طح بيو بيو 🔫")
            
@l313l.on(admin_cmd(pattern="موت(?: |$)(.*)"))
async def _(event):
    await edit_or_reply(event,  " مووت لك عاار 😹 ")
@l313l.on(admin_cmd(pattern="نعل(?: |$)(.*)"))
async def _(event):
    await edit_or_reply(event,  " هاك نعال على راسك 🩴")
@l313l.on(admin_cmd(pattern="اسبح(?: |$)(.*)"))
async def _(event):
    await edit_or_reply(event, "اسبح يالـ وصخ صابونة بربع ومي بلااش 😹🩴")
@l313l.on(admin_cmd(pattern="البشر(?: |$)(.*)"))
async def _(event):
    await edit_or_reply(event, "البشر هم الوحوش الحقيقيون 😢😔")
@l313l.on(admin_cmd(pattern="الحيوان(?: |$)(.*)"))
async def _(event):
    await edit_or_reply(event, "الحيوان احسن منك 😂😂")
@l313l.on(admin_cmd(pattern="صلي(?: |$)(.*)"))
async def _(event):
    await edit_or_reply(event, "گوم صلي لك هيية صلاة 3 دقايق خاف ربك")
@l313l.on(admin_cmd(pattern="صمون(?: |$)(.*)"))
async def _(event):
    await edit_or_reply(event, "گوووووم جيب صموووون 😹")
