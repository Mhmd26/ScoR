# فريق العقرب 
# علوش @ZS_SQ
# محمد @Zo_r0

from telethon import events
import random, re
from ..Config import Config

from JoKeRUB.utils import admin_cmd

import asyncio
from JoKeRUB import l313l
from random import choice

from ..core.managers import edit_or_reply
from ..sql_helper.globals import gvarstatus

plugin_category = "extra"

rehu = [ " 𝗔𝗹𝘄𝗮𝘆𝘀 𝗦𝗰𝗼𝗿𝗽𝗶𝗼𝗻 𝟯𝗺𝗸 💪🏻😉   ========================== ",]
@l313l.ar_cmd(pattern="الاوامر(?:\s|$)([\s\S]*)")
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        Zo_r0 = random.choice(rehu)
        await event.edit(
        f"** \n===========================           [قائمة اوامر العقرب |𝗦𝗰𝗼𝗿𝗽𝗶𝗼𝗻 𝗼𝗿𝗱𝗲𝗿𝘀](t.me/Scorpion_scorp) ✍🏻\n( `.م1`  )  ⦙ أوآمِر الآدمِنْ\n( `.م2`  )  ⦙ أوآمِر المَجمُوعَة\n( `.م3`  )  ⦙ حِمآيَة ٱلخَاصُ وٱلتِلِگراف\n( `.م4`  )  ⦙ المِنشنُ وٱلأنتِحال\n( `.م5`  )  ⦙ النُطْقُ وَ ٱلتَحمِيل \n( `.م6`  )  ⦙ أوآمِرُ ٱلمَنعُ وَ ٱلقُفل \n( `.م7`  )  ⦙ أوآمِر التَنظِيفُ وَ ٱلتِكرَآر\n( `.م8`  )  ⦙ أوآمِر الكِتآبَة وَ النَشرْ\n( `.م9`  )  ⦙ ألوَقتِي وَٱلتَشغِيل\n( `.م10` ) ⦙ ألكَشفُ وَٱلرَوابِط\n( `.م11` ) ⦙ الإرسَالُ وٱلأذكَار\n( `.م12` ) ⦙ أوآمِر المُلصَقآت وَ الإستِخرَاج\n( `.م13` ) ⦙ أوآمِر التَسلِية وَ المِيمْز \n( `.م14` ) ⦙ أوَآمر التَحوِيل وَٱلإضآفة\n( `.م15` ) ⦙ حِسَاباتٌ وَهمِية وَإستِنسآخ\n( `.م16` ) ⦙ أوآمِر تَجمِيع ٱلنُقاط\n( `.م17` ) ⦙ أوآمِر الثِيمآت وَالصُور\n( `.م18` ) ⦙ أفَتآراتْ وَأوآمِر مُنَوَعة \n( `.م19` ) ⦙ ألقُرْآن ألكَرِيمْ وَٱلأحَآدِيثْ \n( `.م20` ) ⦙ قِسْمُ ٱلذَكآء الإصطِناَعِي     {Zo_r0} **"
)

@l313l.ar_cmd(
    pattern="م1$",
    command=("م1", plugin_category),
)
async def _(event):
	if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
		await event.edit(
		"** قائمة اوامر الادمن | 𝗔𝗱𝗺𝗶𝗻 𝗼𝗿𝗱𝗲𝗿𝘀 ✍🏻  **:\n \n** إختر احداها **:\n\n**- { `.اوامر الحظر` }**\n**- { `.اوامر الكتم والتقييد` }**\n**- { `.اوامر التثبيت` }**\n**- { `.اوامر الاشراف` }**\n\n **[العقرب | 𝐒𝐜𝐨𝐫𝐩𝐢𝐨𝐧 ](t.me/Scorpion_scorp)☑️**"
)
		
@l313l.ar_cmd(
    pattern="م2$",
    command=("م2", plugin_category),
)
async def _(event):
	if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
		await event.edit(
		"**أوامر المجـموعة | 𝗚𝗿𝗼𝘂𝗽 𝗢𝗿𝗱𝗲𝗿𝘀 ✍🏻**:\n \n** إختر إحداها: **\n\n** - { `.اوامر التفليش` } **\n** - { `.اوامر المحذوفين` } **\n** - { `.اوامر الكروب` } **\n\n** [العقرب | 𝐒𝐜𝐨𝐫𝐩𝐢𝐨𝐧 ](t.me/Scorpion_scorp)☑️**"
)


@l313l.ar_cmd(
    pattern="م3$",
    command=("م3", plugin_category),
)
async def _(event):
	if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
		await event.edit(
		"** الحماية والتلكراف | 𝗣𝗿𝗼𝘁𝗲𝗰𝘁𝗶𝗼𝗻 𝗼𝗿𝗱𝗲𝗿𝘀 ✍🏻**:\n \n ** إختر إحداها : **\n\n**- { `.اوامر الحماية` }**\n**- { `.اوامر التلكراف` }** \n \n **[العقرب | 𝐒𝐜𝐨𝐫𝐩𝐢𝐨𝐧 ](t.me/Scorpion_scorp)☑️**"
)
@l313l.ar_cmd(
    pattern="م4$",
    command=("م4", plugin_category),
)
async def _(event):
	if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
		await event.edit(
		"** المنشن والانتحال |  𝗠𝗲𝗻𝘁𝗶𝗼𝗻, 𝗽𝗹𝗮𝗴𝗶𝗮𝗿𝗶𝘀𝗺 ✍🏻 **:\n \n ** اختر احداها : **\n\n**- { `.اوامر الانتحال` }**\n**- { `.اوامر التقليد` }**\n**- { `.اوامر المنشن` }** \n\n **[العقرب | 𝐒𝐜𝐨𝐫𝐩𝐢𝐨𝐧 ](t.me/Scorpion_scorp)☑️**"
)

@l313l.ar_cmd(
    pattern="م5$",
    command=("م5", plugin_category),
)
async def _(event):
	if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
		await event.edit(
		"** النطق والتحميل | 𝗗𝗼𝘄𝗻𝗹𝗼𝗮𝗱 , 𝗦𝗽𝗲𝗮𝗸𝗶𝗻𝗴 ✍🏻 **:\n \n **اختر احداها :** \n\n**- { `.اوامر النطق` } **\n**- { `.اوامر التحميل` }** \n**- { `.امر التجربة` }** \n\n**[العقرب | 𝐒𝐜𝐨𝐫𝐩𝐢𝐨𝐧 ](t.me/Scorpion_scorp)☑️**"
)

@l313l.ar_cmd(
    pattern="م6$",
    command=("م6", plugin_category),
)
async def _(event):
	if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
		await event.edit(
		"** قفل ومنع | 𝗟𝗼𝗰𝗸 𝗮𝗻𝗱 𝗯𝗹𝗼𝗰𝗸 ✍🏻 :\n\n أختر احداها : \n\n- { `.اوامر القفل` }\n- { `.اوامر الفتح` }\n- { `.اوامر المنع` } \n\n [العقرب | 𝐒𝐜𝐨𝐫𝐩𝐢𝐨𝐧 ](t.me/Scorpion_scorp)☑️**"
)
async def _(event):
	if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
		await event.edit(
		"** **:\n\n ****\n\n****\n**\n**** \n\n ****"
		)

@l313l.ar_cmd(
    pattern="م7$",
    command=("م7", plugin_category),
)
async def _(event):
	if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
		await event.edit(
		"**التنظيف والتكرار | 𝗖𝗹𝗲𝗮𝗻 𝗮𝗻𝗱 𝗿𝗲𝗽𝗲𝗮𝘁 ✍🏻 **:\n\n ** اختر احداها: **\n\n**- { `.اوامر التكرار` }**\n**- { `.اوامر السبام` }**\n**- { `.اوامر التنظيف` }** \n**- { `.اوامر المسح` }** \n\n**[العقرب | 𝐒𝐜𝐨𝐫𝐩𝐢𝐨𝐧 ](t.me/Scorpion_scorp)☑️**"
)

@l313l.ar_cmd(
    pattern="م8$",
    command=("م8", plugin_category),
)
async def _(event):
	if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
		await event.edit(
		"** والنشر والكتابة | Writing , Publish ✍🏻**:\n\n** اختر احداها: **\n\n**- { `.أوامر الكتابة` }**\n\n**- { `.اوامر النشر` }**\n\n**[العقرب | 𝐒𝐜𝐨𝐫𝐩𝐢𝐨𝐧 ](t.me/Scorpion_scorp)☑️**"
		)

@l313l.ar_cmd(
    pattern="م9$",
    command=("م9", plugin_category),
)
async def _(event):
	if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
		await event.edit(
		"** الوقتي والتشغيل | 𝗧𝗶𝗺𝗶𝗻𝗴 , 𝗼𝗽𝗲𝗿𝗮𝘁𝗶𝗼𝗻 ✍🏻 **:\n \n ** اختر احداها :**\n\n**- { `.اوامر الاسم` }**\n**- { `.اوامر البايو` }**\n**- { `.اوامر الكروب الوقتي` }**\n**- { `.اوامر التشغيل` } **\n**- { `.اوامر الاطفاء` } **\n\n**[العقرب | 𝐒𝐜𝐨𝐫𝐩𝐢𝐨𝐧 ](t.me/Scorpion_scorp)☑️**"
)	

@l313l.ar_cmd(
    pattern="م10$",
    command=("م10", plugin_category),
)
async def _(event):
	if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
		await event.edit(
		"** الكشف والروابط | 𝗦𝗵𝗼𝘄 𝗮𝗻𝗱 𝗹𝗶𝗻𝗸𝘀 ✍🏻  **:\n \n **اختر احداها: **\n\n**- { `.اوامر الكشف` }**\n**- { `.اوامر الروابط` }** **\n- { `.مراقب الروابط` }\n- { `.بروكسي` } **\n\n **[العقرب | 𝐒𝐜𝐨𝐫𝐩𝐢𝐨𝐧 ](t.me/Scorpions_scorp)☑️**"
)
@l313l.ar_cmd(
    pattern="م11$",
    command=("م11", plugin_category),
)
async def _(event):
	if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
		await event.edit(
		"** اوامر الارسال | 𝗧𝗿𝗮𝗻𝘀𝗺𝗶𝘀𝘀𝗶𝗼𝗻 𝗼𝗿𝗱𝗲𝗿𝘀 ✍🏻 :\n \n   اختر احداها \n\n- { `.امر الصورة الذاتية` }\n- { `.اوامر التحذيرات` }\n- { `.اوامر الملكية` } \n- { `.اوامر السليب` } \n- { `.اوامر الاذكار` }\n- { `.الحاسبة` }\n\n[العقرب | 𝐒𝐜𝐨𝐫𝐩𝐢𝐨𝐧 ](t.me/Scorpion_scorp)☑️**"
)
@l313l.ar_cmd(
    pattern="م12$",
    command=("م12", plugin_category),
)
async def _(event):
	if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
		await event.edit(
		"** ملصقات و استخراح | 𝗦𝘁𝗶𝗰𝗸𝗲𝗿𝘀 , 𝗘𝘅𝘁𝗿𝗮𝗰𝘁 ✍🏻**:\n \n **اختر احداها :** \n\n**- { `.اوامر الملصقات` }**\n**- { `.اوامر الاستخراج` }**\n\n**[العقرب | 𝐒𝐜𝐨𝐫𝐩𝐢𝐨𝐧 ](t.me/Scorpion_scorp)☑️**"
)
async def _(event):
	if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
		await event.edit(
		"** **:\n\n ****\n\n****\n**\n**** \n\n ****"
)

@l313l.ar_cmd(
    pattern="م13$",
    command=("م13", plugin_category),
)
async def _(event):
	if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
		await event.edit(
		"**تسلية وتحشيش | 𝗘𝗻𝗷𝗼𝘆 𝗮𝗻𝗱 𝗙𝘂𝗻𝗻𝘆 ✍🏻 :\n \n اختر احداها :\n\n- { `.اوامر التسلية` }\n- { `.اوامر التحشيش` } \n- { `.اوامر الضحك` } \n- { `.اضافة ميمز` }\n\n [العقرب | 𝐒𝐜𝐨𝐫𝐩𝐢𝐨𝐧 ](t.me/Scorpion_scorp)☑️ **"
)

@l313l.ar_cmd(
    pattern="م14$",
    command=("م14", plugin_category),
)
async def _(event):
	if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
		await event.edit(
		"**  اوامر تحويل الصيغ و الجهات ✍🏻 **:\n \n **اختر احداها:**\n\n**- { `.اوامر التحويل` }**\n**- { `.اوامر الجهات` }** \n\n**[العقرب | 𝐒𝐜𝐨𝐫𝐩𝐢𝐨𝐧 ](t.me/Scorpion_scorp)☑️**"
)



@l313l.ar_cmd(
    pattern="م15$",
    command=("م15", plugin_category),
)
async def _(event):
	if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
		await event.edit(
		"**ايميل وهمي ونسخ | Fake Mail , Copy ✍🏻**:\n \n  **اختر احداها:**\n\n**- { `.ايميل وهمي` }\n امر يستخدم لجلب ايميل وهمي شغال**\n\n**- { `.احضار الرسالة` }\n امر يستخدم لجلب الرسالة التي تأتي الى الايميل**\n\n**- { `.الايميلات` }\nلعرض الايميلات التي تم انشاؤها**\n\n**- { `.استنساخ ايميل` }\nامر يستخدم لإستنساخ ايميل الى عدة نسخ متفرعة من الايميل نفسه الحد الاقصى للاستنساخ 500 نسخة \n اكتب الايميل ثم الايميل ثم العدد**\n\n**[العقرب | 𝐒𝐜𝐨𝐫𝐩𝐢𝐨𝐧 ](t.me/Scorpion_scorp)☑️**"

)

@l313l.ar_cmd(
    pattern="م16$",
    command=("م16", plugin_category),
)
async def _(event):
    if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit(
            "**نقاط بوتات | 𝗖𝗼𝗹𝗹𝗲𝗰𝘁 𝗽𝗼𝗶𝗻𝘁𝘀 ✍🏻 **:\n \n  **اختر احداها:**\n\n**- { `.اوامر التجميع` } **\n**- { `.اوامر وعد` }** \n\n**[العقرب | 𝐒𝐜𝐨𝐫𝐩𝐢𝐨𝐧 ](t.me/Scorpion_scorp)☑️**"
        )
@l313l.ar_cmd(
    pattern="م17$",
    command=("م17", plugin_category),
)
async def _(event):
	if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
		await event.edit(
		"**الثيمات والصور | 𝗧𝗵𝗲𝗺𝗲𝘀 , 𝗣𝗵𝗼𝘁𝗼𝘀 ✍🏻:\n \n  اختر احداها:\n\n- { `.ثيمات` }\n\n- { `.صور` }\n يستخدم هذا الامر كلآتي  (`.صور` + البحث )\n- مثال : `صور انمي`\n\n- { `.خلفيات` }\nهذا الامر يستخدم نفس استخدام امر الصور \n\n[العقرب | 𝐒𝐜𝐨𝐫𝐩𝐢𝐨𝐧 ](t.me/Scorpion_scorp)☑️**"

	)
@l313l.ar_cmd(
    pattern="م18$",
    command=("م18", plugin_category),
)
async def _(event):
	if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
		await event.edit(
		"**افتارات واوامر منوعة ✍🏻:\n \n  اختر احداها:\n\n- { `.الافتارات` }\n- { `.اوامر اخرى` } \n- { `.اوامر الوهمي` }\n- { `.اوامر الهمسة` } \n\n[العقرب | 𝐒𝐜𝐨𝐫𝐩𝐢𝐨𝐧 ](t.me/Scorpion_scorp)☑️**"

		)
@l313l.ar_cmd(
    pattern="م19$",
    command=("م19", plugin_category),
)
async def _(event):
	if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
		await event.edit(
		"**القرآن والاحاديث | 𝗧𝗵𝗲 𝗤𝘂𝗿’𝗮𝗻 , 𝘀𝗮𝘆𝗶𝗻𝗴𝘀 ✍🏻:\n \n  اختر احداها:\n\n- { `.قسم القرآن ` }\n\n- { `.قسم الاحاديث والاقوال` } \n\n[العقرب | 𝐒𝐜𝐨𝐫𝐩𝐢𝐨𝐧 ](t.me/Scorpion_scorp)☑️**"

	)

	
