import random
from telethon import events
import random, re
from JoKeRUB.utils import admin_cmd
import asyncio
from JoKeRUB import l313l
from ..core.managers import edit_or_reply
plugin_category = "extra"

# فريق العقرب 
# علوش @ZS_SQ
# محمد @Zo_r0

@l313l.ar_cmd(
    pattern="اوامر الحظر$",
    command=("اوامر الحظر ", plugin_category),
           )
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit(
        "**شـرح عـن اوامـر الحـظر ✍🏻\n \n ✎┊‌ اختر احدى هذه الاوامر \n\n{ `.حظر` } \n-  تقوم بالرد على شخص او وضع معرفه مع الامر وسيحظره من المجموعة\n\n{ `.الغاء حظر` }\n - بالرد على الشخص او كتابة معرفه مع الامر لالغاء حظره\n \n[العقرب | 𝐒𝐜𝐨𝐫𝐩𝐢𝐨𝐧 ](t.me/Scorpion_scorp)☑️** "
           )
      
@l313l.ar_cmd(
    pattern="اوامر الكتم والتقييد$",
    command=("اوامر الكتم والتقييد ", plugin_category),
           )
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit(
        "**شـرح عـن اوامـر الكـتم والتقييد ✍🏻\n \n ✎┊‌ اختر احدى هذه الاوامر \n\n{ `.كتم` } \n-  قُم بالرد على شخص او وضع معرفه مع الامر وسيكتمه من المجموعة\n\n{ `.الغاء كتم` }\n - قُم بالرد على الشخص او كتابة معرفه مع الامر لالغاء كتمه \n\n{ `.تقييد` } \n-  قُم بالرد على شخص او وضع معرفه مع الامر وسيتم تقييده في المجموعة\n\n{ `.الغاء التقييد` }\n - قُم بالرد على الشخص او كتابة معرفه مع الامر لالغاء تقييدهُ \n\n \n[العقرب | 𝐒𝐜𝐨𝐫𝐩𝐢𝐨𝐧 ](t.me/Scorpion_scorp)☑️** "
           )

@l313l.ar_cmd(
    pattern="اوامر التثبيت$",
    command=("اوامر التثبيت ", plugin_category),
           )
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit(
        "**شـرح عـن اوامـر التثبيت ✍🏻\n \n ✎┊‌ اختر احدى هذه الاوامر \n\n{ `.تثبيت` } \n-  تقوم بالرد على الرسالة مع الامر وستثبت في المجموعة\n\n{ `.الغاء التثبيت` }\n - بالرد على الرسالة مع الامر لإلغاء تثبيتها\n \n[العقرب | 𝐒𝐜𝐨𝐫𝐩𝐢𝐨𝐧 ](t.me/Scorpion_scorp)☑️** "
           )

@l313l.ar_cmd(
    pattern="اوامر الاشراف$",
    command=("اوامر الاشراف", plugin_category),
           )
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit(
        "**شـرح عـن اوامـر الاشراف ✍🏻\n \n ✎┊‌ اختر احدى هذه الاوامر \n\n{ `.رفع مشرف` } \n-  تقوم بالرد على الشخص مع الامر و سيرفع مشرفا في المجموعة\n\n{ `.طرد` } \n- لطرد المستخدم \n\n{ `.تنزيل مشرف` } \n-لتنزيل الشخص من رتبة الاشراف في جميع المجموعات\n  \n[العقرب | 𝐒𝐜𝐨𝐫𝐩𝐢𝐨𝐧 ](t.me/Scorpion_scorp)☑️** "
           )

# اوامر المجموعة ل سورس الجوكر
@l313l.ar_cmd(
    pattern="اوامر التفليش$",
    command=("اوامر التفليش", plugin_category),
           )
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit(
       "**شـرح عـن اوامـر التفليـش ✍🏻\n \n ✎┊‌ اختر احدى هذه الاوامر \n\n- { `.تفليش بالطرد` } \n ارسل  الامـر لطرد جميع الاعضاء من المجموعه \n\n- { `.تفليش` } \n كتابة الامـر فقط في المجموعه لحظر جميع الاعضاء\n- { `.الغاء التفليش` } \nيكتب لالغاء التفليش \n\n- { `.حظر الكل` } \n كتابة  الامـر فقط في المجموعه لحظر جميع الاعضاء بدون صلاحيات عن طريق بوت الحماية \n\n- { `.طرد الكل` } \n كتابة  الامـر فقط في المجموعه ليقوم بطرد جميع الاعضا بدون صلاحيات عن طريق بوت الحماية \n\n- { `.كتم الكل` } \n كتابة الامـر فقط في المجموعه ليقوم بكتم جميع الاعضاء بدون صلاحيات اشراف عن طريق بوت الحماية\n\n \n [العقرب | 𝐒𝐜𝐨𝐫𝐩𝐢𝐨𝐧 ](t.me/Scorpion_scorp)☑️**"
           )

@l313l.ar_cmd(
    pattern="اوامر المحذوفين$",
    command=("اوامر المحذوفين", plugin_category),
           )
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit(
        "**شـرح عـن اوامـر المـحذوفين ✍🏻\n \n ✎┊‌ اختر احدى هذه الاوامر \n\n- { `.حذف المحظورين` } \n كتابة  الامـر في الكروب لالغاء حظر جميع الاعضاء \n\n- { `.اطردني` } \n فقـط ارسل الامر في المجموعة لمغادرة المجموعه التي تم ارسال الامر فيها\n\n- { `.المحذوفين` } \n لعرض الحسابات المحذوفة في مجمـوعة معيـنة ولحذفهم ارسل .المحذوفين اطردهم\n\n \n✎┊‌ [العقرب | 𝐒𝐜𝐨𝐫𝐩𝐢𝐨𝐧 ](t.me/Scorpion_scorp)☑️**"
           )
@l313l.ar_cmd(
    pattern="اوامر الكروب$",
    command=("اوامر الكروب", plugin_category),
           )
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit(
        "**شـرح عـن اوامـر الكروب ✍🏻\n \n ✎┊‌ اختر احدى هذه الاوامر \n\n- { `.الاحداث` } \n كتابة  الامـر في الكروب لعرض احداث الكروب\n\n- { `.الاعضاء` } \n فقـط ارسل الامر في المجموعة لعرض اعضاء المجموعة\n\n- { `.المشرفين` } \n ارسل الامر في المجموعه لعرض حسابات المشرفين\n\n- { `.البوتات` }\n ارسل الامر في المجموعه لعرض البوتات\n\n- { `.البوتات` }\nيستعمل هذا الامر لرؤية صلاحيات المجموعة \n\n- { `.احصائيات الكروب` }\nيستخدم لاضهار احصائيات المجموعة واعضائها \n\n [العقرب | 𝐒𝐜𝐨𝐫𝐩𝐢𝐨𝐧 ](t.me/Scorpion_scorp)☑️**"
           )


@l313l.ar_cmd(
    pattern="اوامر الحماية$",
    command=("اوامر الحماية", plugin_category),
           )
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit(
        "**شـرح عـن اوامـر الـخاص ✍🏻\n \n اختر احدى هذه الاوامر \n\n- { `.الحماية تشغيل/تعطيل` } \n لتشغيل امر الحمايه او تعطيله في الـخاص \n\n- { `.سماح` } \n بالرد على الشخص للسماح له بالتكلم في الخاص\n\n- { `.رفض` } \n بالرد على الشخص لرفضه من الخاص \n\n- { `.المسموح لهم` }\n فقط ارسل الامر لاظهار الاشخاص المسموح لهم والمرفوضين\n\n- { `.الخاص قفل` }\nيستخدم هذا الامر لقفل الخاص بحث لا يمكن لاحد ارسال الرسائل\n\n- { `.الخاص فتح` }\nيستخدم لفتح الخاص\n\n \n✎┊‌ [العقرب | 𝐒𝐜𝐨𝐫𝐩𝐢𝐨𝐧 ](t.me/Scorpion_scorp)☑️**"
           )
@l313l.ar_cmd(
    pattern="اوامر الحساب$",
    command=("اوامر الحساب", plugin_category),
           )
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit(
        "**شـرح عـن اوامـر الحساب ✍🏻\n \n اختر احدى هذه الاوامر \n\n- { `.معلوماتي` } \n لعرض جميع معلومات الحساب من كروبات وقنوات ودردشات وغيرها \n\n- { `.قائمة قنواتي` } \nيقوم بعرض جميع القنوات التي تكون فيها مشرف\n\n- { `.قائمة كروباتي` } \n يقوم بعرض جميع الكروبات التي تكون فيها مشرف \n\n- { `.قائمة القنوات` }\nيقوم بعرض جميع القنوات المشترك بيها بحسابك على شكل ملف او قائمة\n\n- { `.قائمة الكروبات` }\nيقوم بعرض جميع الكروبات الي منضم بيها على شكل قائمة او ملف \n\n- { `.عرض الحساب` }\nيقوم بالكشف عن الحساب والذهاب له عن طريق ID\n\n \n✎┊‌ [العقرب | 𝐒𝐜𝐨𝐫𝐩𝐢𝐨𝐧 ](t.me/Scorpion_scorp)☑️**"
	)
@l313l.ar_cmd(
    pattern="تصفية الحساب$",
    command=("تصفية الحساب", plugin_category),
           )
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit(
        "**شـرح عـن اوامـر التنظيف ✍🏻\n \n اختر احدى هذه الاوامر \n\n- { `.مغادرة الكروبات` } \nيقوم بحذف ومغادرة جميع الكروبات في حسابك \n\n- { `.مغادرة القنوات` } \nيقوم بحذف ومغادرة جميع القنوات في حسابك\n\n- { `.تصفية الخاص` } \nيقوم بحذف جميع المحادثات في الخاص\n\n- { `.تصفية البوتات` }\nيقوم بحذف جميع البوتات في حسابك\n\n✎┊‌ [العقرب | 𝐒𝐜𝐨𝐫𝐩𝐢𝐨𝐧 ](t.me/Scorpion_scorp)☑️**"
	)
@l313l.ar_cmd(
    pattern="اوامر التلكراف$",
    command=("اوامر التلكراف", plugin_category),
           )
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit(
        "**شـرح عـن اوامـر التلكراف ✍🏻\n \n  اختر احدى هذه الاوامر \n\n- { `.تلكراف ميديا` } \n\n لاستخراج رابط من الصورة على شكل رابط تلكراف  \n\n- { `.تلكراف نص` } \n بالرد على النص او المقالة لصنع رابط تلكراف للنص\n\n \n✎┊‌ [العقرب | 𝐒𝐜𝐨𝐫𝐩𝐢𝐨𝐧 ](t.me/Scorpion_scorp)☑️**"
           )

@l313l.ar_cmd(
    pattern="اوامر الانتحال$",
    command=("اوامر الانتحال", plugin_category),
           )
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit(
        "**شـرح عـن اوامـر الانتحال ✍🏻\n \n ✎┊‌اختر احدى هذه الاوامر \n\n- { `.انتحال` } \n\n بالرد على الشخص لنسخ حسابه بالكامل من صورة واسم وبايو  \n\n- { `.اعادة` } \n لارجاع الحساب الى وضعه الطبيعي لما كان سابقا\n\n [العقرب | 𝐒𝐜𝐨𝐫𝐩𝐢𝐨𝐧 ](t.me/Scorpion_scorp)☑️**"
           )

@l313l.ar_cmd(
    pattern="اوامر التقليد$",
    command=("اوامر التقليد", plugin_category),
           )
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit(
        "**شـرح عـن اوامـر الـتقليـد ✍🏻\n \n ✎┊‌ اختر احدى هذه الاوامر \n\n- { `.تقليد` } \n بالرد على الشخص لتقليد جميع رسائله في الدردشه \n\n- { `.الغاء التقليد` } \n بالرد على الشخص لايقاف التقليد\n\n- { `.المقلدهم` } \nلاظهـار قائمه الاشخاص الذي فعـلت عليهم امر التقليد ولمسحهم ارسل  (`.مسح المقلدهم`) \n\n \n[العقرب | 𝐒𝐜𝐨𝐫𝐩𝐢𝐨𝐧 ](t.me/Scorpion_scorp)☑️**"
           )

@l313l.ar_cmd(
    pattern="اوامر المنشن$",
    command=("اوامر المنشن", plugin_category),
           )
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit(
        "**شـرح عـن اوامـر الـمنشن ✍🏻\n \n ✎┊‌ اختر احدى هذه الاوامر \n\n- (`.منشن + المسج`)\nقم بكتابة الامر في المجموعة لعمل تاك مفرد للاعظاء الموجودين\n- (`.الغاء منشن`)\nلألغاء التاك \n\n \n✎┊‌ [العقرب | 𝐒𝐜𝐨𝐫𝐩𝐢𝐨𝐧 ](t.me/Scorpion_scorp)☑️**"
           )

@l313l.ar_cmd(
    pattern="اوامر التحميل$",
    command=("اوامر التحميل", plugin_category),
           )
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit(
        "**شـرح عـن امـر التحمـيل ✍🏻\n \n ✎┊‌ اختر احدى هذه الاوامر\n\n- (`.تيك + رابط المقطع`)\nبكتابة تيك توك مع رابط المقطع سيتم تحميلة مباشرة\n - مثـال : `.تيك https://vt.tiktok.com/example` \n\n- (`.بحث + اسم الفيديو او الاغنية`)\nكتابة الامر مع اسم الفيديو او الاغنية ليعطيك نتائج البحث وروابط من يوتيوب تستخدم مع اوامر التحميل\n - مثال `.بحث سورة الفاتحة `\n\n- (`.انستا + الرابط `)\nيستخدم هذا الامر لتحميل من الانستا فقط اكتب الامر مع رابط الفيديو ليحمله\n- مثـال : `.انستا https://instagram.com/example...`\n\n[العقرب | 𝐒𝐜𝐨𝐫𝐩𝐢𝐨𝐧 ](t.me/Scorpion_scorp)☑️**"
           )

@l313l.ar_cmd(
    pattern="اوامر الترجمة$",
    command=("اوامر الترجمة", plugin_category),
           )
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit(
        "**شـرح عـن اوامـر الترجمة ✍🏻\n \n ✎┊‌ اختر احدى هذه الاوامر \n\n- { `.ترجمة ar` } \n\n بالرد على النص لترجمته للغه  ية\n\n- { `.ترجمة en` } \n بالرد على النص لترجمته للغه الانكليزية\n\n \n✎┊‌ [العقرب | 𝐒𝐜𝐨𝐫𝐩𝐢𝐨𝐧 ](t.me/Scorpion_scorp)☑️**"
           )

@l313l.ar_cmd(
    pattern="اوامر النطق$",
    command=("اوامر النطق", plugin_category),
           )
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit(
        "**شـرح عـن اوامـر الـنطق ✍🏻\n \n ✎┊‌ اختر احدى هذه الاوامر \n\n- { `.تكلم ar` } \n بالرد على النص لتحويله الى مقطع صوتي للغة  العربية \n\n- { `.تكلم en` } \n بالرد على النص لتحوليه الى مقطع صوتي للغه الانكليزية\n\n- { `.احجي ar` } \n بالرد على مقطع صوتي او بصمة لتحوليه الى نص للغه  العربية\n\n- { `.احجي en` } \n بالرد على مقطع صوتي او بصمة لتحوليه الى نص للغه الانكليزية\n\n[العقرب | 𝐒𝐜𝐨𝐫𝐩𝐢𝐨𝐧 ](t.me/Scorpion_scorp)☑️**"
           )

@l313l.ar_cmd(
    pattern="اوامر القفل$",
    command=("اوامر القفل", plugin_category),
           )
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit(
        "**شـرح عـن اوامـر القـفـل ✍🏻\n \n ✎┊‌ اختر احدى هذه الاوامر \n\n- { `.قفل + الاضافة` } \n تكتب الامر مع الاضافة لقفل شي معين في المجموعة \n\nالاضافات  : \n - الدردشه  : لقفل ارسال الرسائل \n- الوسائط   : لقفل ارسال الوسائط\n - الملصقات  : لقفل ارسال الملصقات\n- الروابط  : لقفل ارسال الروابط\n- المتحركه  : لقفل ارسال المتحركه\n- الالعاب  : لقفل ارسال الالعاب الانلاين\n- الانلاين  : لقفل ارسال البوتات الانلاين\n- التصويت  : لقفل ارسال التوصيتات \n- الكل :  لقفل ارسال كل شي\n\n \n[العقرب | 𝐒𝐜𝐨𝐫𝐩𝐢𝐨𝐧 ](t.me/Scorpion_scorp)☑️**"
           )

@l313l.ar_cmd(
    pattern="اوامر الفتح$",
    command=("اوامر الفتح", plugin_category),
           )
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit(
        "**شـرح عـن اوامـر الفـتـح ✍🏻\n \n ✎┊‌ اختر احدى هذه الاوامر \n\n- { `.فتح + الاضافة` } \n تكتب الامر مع الاضافة لفتـح شي معين في المجموعة \n\nالاضافات  : \n - الدردشه  : لفتح ارسال الرسائل \n- الوسائط   : لفتح ارسال الوسائط\n - الملصقات  : لفتح ارسال الملصقات\n- الروابط  : لفتح ارسال الروابط\n- المتحركه  : لفتح ارسال المتحركه\n- الالعاب  : لفتح ارسال الالعاب الانلاين\n- الانلاين  : لفتح ارسال البوتات الانلاين\n- التصويت  : لفتح ارسال التوصيتات \n- الكل :  لفتح ارسال كل شي\n\n [العقرب | 𝐒𝐜𝐨𝐫𝐩𝐢𝐨𝐧 ](t.me/Scorpion_scorp)☑️**"
           )

@l313l.ar_cmd(
    pattern="اوامر المنع$",
    command=("اوامر المنع", plugin_category),
           )
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit(
        "**شـرح عـن اوامـر الـمنـع ✍🏻\n \n ✎┊‌ اختر احدى هذه الاوامر \n\n- { `.منع + الكلمة` } \n لمـنع الـكلمة في الـدردشة وسيتم حذفها عند ارسالها من اي شخص \n\n- { `.الغاء منع + الكلمة` } \n لالغاء منع الكلمة والسماح للجميع بأرسالها في الدردشة\n\n- { `.قائمة المنع` } \nلاظهـار قائمه الكـلمات الـتي منعـتها في الـدردشـه \n\n \n [العقرب | 𝐒𝐜𝐨𝐫𝐩𝐢𝐨𝐧 ](t.me/Scorpion_scorp)☑️**"
           )


@l313l.ar_cmd(
    pattern="اوامر التسلية$",
    command=("اوامر التسلية", plugin_category),
           )
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit(
        "**قائمة اوامر التسـلية ✍🏻\n  \n ✎┊‌ اختر احدى هذه القوائم\n\n- { `.افكر` }\n- { `.متت` }\n- { `.ضايج` }\n- { `.ساعه` }\n- { `.مح` }\n- { `.قلب` }\n- { `.جيم` }\n- { `.الارض` }\n- { `.قمر` }\n- { `.اقمار` }\n- { `.قمور` }\n\nتحذيـر : لا تكثر من استخدام هذه الاوامر لانها قد تسبب ضغط على حسابك او تعليقه من ارسال الرسائل لفترة وجيزة.\n\n[العقرب | 𝐒𝐜𝐨𝐫𝐩𝐢𝐨𝐧 ](t.me/Scorpion_scorp)☑️**"
           )


@l313l.ar_cmd(
    pattern="اوامر الملصقات$",
    command=("اوامر الملصقات", plugin_category),
           )
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit(
        "**شـرح عـن اوامـر الملصقـات ✍🏻\n \n ✎┊‌ اختر احدى هذه الاوامر\n\n- { `.ملصق` }\nبالرد على الملصق لأخذه و عمل حزمه خاصة بك و اضافته بها\n\n- { `.حزمة` }\n بكتابة الامر + اسم للحزمة وسيتم اخذها \n- مثال (`.حزمة Scorpion `) \n\n- (`.معلومات الملصق` }\nبالرد على الملصق لعرض معلومات الحزمة\n\n- { `.تحويل ملصق` }\n بالرد على الصورة لتحويلها الى الملصق\n- { `.تحويل صورة` }\n بالرد على الملصق لتحويله الى صورة\n\n [العقرب | 𝐒𝐜𝐨𝐫𝐩𝐢𝐨𝐧 ](t.me/Scorpion_scorp)☑️**"
            )

@l313l.ar_cmd(
    pattern="اوامر التكرار$",
    command=("اوامر التكرار", plugin_category),
            )
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit(
        "**شـرح عـن اوامـر التـكرار ✍🏻\n\n \n✎┊‌ اختر احدى هذه الاوامر\n\n- { `.كرر  +عدد التكرار  +بالرد على الرسالة` }\n يقوم بتكرار النصوص والوسائط بالرد على الرسالة او الصورة \nمثال  :  ( بالرد على صورة  `.كرر 10` }\n\n- { `.تكرار الملصق + بالرد على ملصق` }\n بالرد على الملصق ليقوم باستخراج جميع ملصقات الحزمه وارسالها\n\n- (`.مكرر  + وقت بالدقائق  + عدد  + بالرد` }\n بالرد على نص او صورة او اي شي يقوم بالتكرار  مع وقت معين .\nمثال  : بالـرد على نص { `.مكرر 10 2` }  عندها سترسل 10 رسائل نصية ( النص الي رديت عليه ) بفاصل ثانيتين بين كل رسالة\n\n- { `.ضع تكرار` + العدد )\nلمنع التكرار بالمجموعة الخاصة بك بالعدد الذي وضعته للعودة للوضع الطبيعي ضع 999999.\n مثال : { `.ضع تكرار 10 `}\n\n- { `.ايقاف التكرار` } \nلأيقاف جميع التكرار ومن بينهم النشر التلقائي\n\n \n[العقرب | 𝐒𝐜𝐨𝐫𝐩𝐢𝐨𝐧 ](t.me/Scorpion_scorp)☑️**"
            )

@l313l.ar_cmd(
    pattern="اوامر السبام$",
    command=("اوامر السبام", plugin_category),
            )
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit(
        "**شـرح عـن اوامـر السبـام ✍🏻\n \n✎┊‌ اختر احدى هذه الاوامر\n\n- { `.سبام + كلمـة` }\nيقوم بتفصيخ احرف الكلمه وارسالها جربه بنفسك\n\n- { `.وسبام + كلـمة` }\nكتابة الامر مع نص معين يقوم بتفصيخ الجمله كلمه كلمه وارسالها\n\n[العقرب | 𝐒𝐜𝐨𝐫𝐩𝐢𝐨𝐧 ](t.me/Scorpion_scorp)☑️**"
             )

@l313l.ar_cmd(
    pattern="اوامر التنظيف$",
    command=("اوامر التنظيف", plugin_category),
            )
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit(
        "**شـرح عـن اوامـر التنظيـف ✍🏻\n \n ✎┊‌ اختر احدى هذه الاوامر\n\n- { `.تنظيف + عدد الرسائل` }\nيقوم بحذف الرسائل اكتب الامر وعدد معين من الرسائل سيقوم بحذفها \n\n- ( .تنظيف  + الاضافة )\n يـجب وضع الشـارحه مع الاضافة (-)\nمثـال  :  { `.تنظيف -ح` }  <سيقوم بحذف المتحركات في الدردشة>\nالاضافات : \n (`-ب`) : لحـذف الرسائل الـصوتية\n (`-م`): لحـذف الملفات\n (`-ح`): لحـذف المتحـركه\n (`-ص`): لحـذف الـصور\n (`-غ`): لحـذف الاغاني\n (`-ق`): لحـذف الـملصقات\n (`-ر`): لحـذف الـروابط \n(`-ف`): لحـذف الفـيديوهـات\n\n \n[العقرب | 𝐒𝐜𝐨𝐫𝐩𝐢𝐨𝐧 ](t.me/Scorpion_scorp)☑️**"
          )               

@l313l.ar_cmd(
    pattern="اوامر المسح$",
    command=("اوامر المسح", plugin_category),
            )
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit(
        "**شـرح عـن اوامـر المسـح ✍🏻\n \n✎┊‌ اختر احدى هذه الاوامر\n\n- { `.مسح  + بالرد على النص` }\nفقط اكتب الامر بالرد على الرسالة ليقوم بحذفها \n\n- { `.حذف رسائلي` }\nاكتب الامر في اي مكان وسيقوم بحذف جميع رسائلك في الدردشه حتى لو لم يكن لديك صلاحيات \n\n[العقرب | 𝐒𝐜𝐨𝐫𝐩𝐢𝐨𝐧 ](t.me/Scorpion_scorp)☑️**"
         )

@l313l.ar_cmd(
    pattern= "اوامر الوقت$",
    command=("اوامر الوقت", plugin_category),
)
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit(
        "**شرح اوامر الوقت ✍🏻\n  \n✎┊‌ اختر احدى هذه الاوامر\n\n- { `.الوقت` }\nلعرض الوقت على شكل ملصق\n\n- { `.وقت` }\nلعرض الوقت على شكل كتابة\n\n- { `.مؤقت` + الوقت + النص )\nيقوم بإرسال رسالة مؤقتة و حذفها بعد وقت معين\n- مثـال : `.مؤقت 5 العقرب`\n\n[العقرب | 𝐒𝐜𝐨𝐫𝐩𝐢𝐨𝐧 ](t.me/Scorpion_scorp)☑️**"
)


@l313l.ar_cmd(
    pattern="اوامر الروابط$",
    command=("اوامر الروابط", plugin_category),
)
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit(
        "**شرح اوامر الروابط ✍🏻\n\n✎┊‌ اختر احدى هذه الاوامر\n\n- { `.سحب ملف` + الرابط )\nلكشف ملفات موقع معين اكتب الامر مع الرابط\n\n- { `.مصغر` }\nبالرد على الرابط او وضع الرابط مع الامر ليقوم بتصغيره\n\n[العقرب | 𝐒𝐜𝐨𝐫𝐩𝐢𝐨𝐧 ](t.me/Scorpion_scorp)☑️**"
)
@l313l.ar_cmd(
    pattern="اوامر التحذيرات$",
    command=("اوامر التحذيرات", plugin_category),
)
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit(
        "**شرح اوامر التحذيرات ✍🏻\n  \n✎┊‌ اختر احدى هذه الاوامر\n\n- { `.تحذير + السبب` }\nبالرد على الشخص ليقوم بتحذيره يمكنك وضع سبب كذلك\n\n- { `.التحذيرات` }\nبالرد على الشخص ليقوم باظهار تحذيراته.\n\n- { `.ازالة التحذير` }\nبالرد على الشخص لحذف تحذيراته.\n\n [العقرب | 𝐒𝐜𝐨𝐫𝐩𝐢𝐨𝐧 ](t.me/Scorpion_scorp)☑️**"
)

@l313l.ar_cmd(
    pattern="اوامر السليب$",
    command=("اوامر السليب", plugin_category),
)
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit(
        "**شرح اوامر السليب ✍🏻\n  \n✎┊‌ اختر احدى هذه الاوامر\n\n- { `.سليب` + السبب)\nيقوم بادخالك في وضع غير المتصل يقوم بالرد على اي شخص برسالة يقول فيها انك غير متواجد.\n- مثـال : `.سليب نايم`\n- يتوقف وضع السليب في حال قمت بالرد على اي رسالة\n- { `.سليب ميديا` + السبب )\nيقوم بنفس وظيفة الامر العادي غير انه يمكنك ارفاق صورة او متحركة بالرد عليها مع الامر.\n\n[العقرب | 𝐒𝐜𝐨𝐫𝐩𝐢𝐨𝐧 ](t.me/Scorpion_scorp)☑️**"
)

@l313l.ar_cmd(
    pattern="اوامر الاسم$",
    command=("اوامر الاسم", plugin_category),
)
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit(
        "**شرح اوامر الاسم الوقتي ✍🏻\n  \n✎┊‌ اختر احدى هذه الاوامر\n\n- { `.اسم وقتي` }\nبكتابة الامر لاضافة اسم وقتي حسب منطقة التي وضعتها .\n\n- { `.انهاء اسم وقتي` }\nلانهاء الاسم الوقتي و ارجاع الاسم الطبيعي .\n\n- { `.الصورة الوقتية` }\n لوضع صورة تتغير مع الوقت\n\n- { `.انهاء الصورة الوقتية` }\n لأنهاء الصورة واسترجاع الصورة الاصلية\n \n[العقرب | 𝐒𝐜𝐨𝐫𝐩𝐢𝐨𝐧 ](t.me/Scorpion_scorp)☑️**"
)

@l313l.ar_cmd(
    pattern="اوامر البايو$",
    command=("اوامر البايو", plugin_category),
)
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit(
        "**شرح اوامر البايو الوقتي ✍🏻\n  \n✎┊‌ اختر احدى هذه الاوامر\n\n- { `.بايو وقتي` }\nبكتابة الامر لاضافة بايو وقتي حسب منطقة التي وضعتها .\n\n- { `.انهاء بايو وقتي` }\nلانهاء البايو الوقتي و ارجاع البايو الطبيعي .\n\n[العقرب | 𝐒𝐜𝐨𝐫𝐩𝐢𝐨𝐧 ](t.me/Scorpion_scorp)☑️**"
)

@l313l.ar_cmd(
    pattern="حماية الكروب$",
    command=("حماية الكروب", plugin_category),
)
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit(
        "**شرح حماية الكروب ✍🏻\n  \n✎┊‌ اختر احدى هذه الاوامر\n\n- { `.التفليش قفل.` | `التفليش فتح` }\nيستخدم هذا الامر لمنع حصول اي عملية تفليش في الكروب\n\n- { `.النشر قفل` | `.النشر فتح` }\nلمنع حصول اي عملية نشر تلقائي في الكروب \n\n- { `.المميز قفل` | `.المميز فتح` }\nلمنع ارسال اي ايموجي مميز حيث يقوم بحذفه \n\n [العقرب | 𝐒𝐜𝐨𝐫𝐩𝐢𝐨𝐧 ](t.me/Scorpion_scorp)☑️**"
)

@l313l.ar_cmd(
    pattern="اوامر التشغيل$",
    command=("اوامر التشغيل", plugin_category),
)
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit(
        "**شرح اوامر التشغيل ✍🏻\n  \n✎┊‌ اختر احدى هذه الاوامر\n\n- { `.تحديث` }\nفقط ارسل الامر للتاكد اذا كان هناك تحديثات من مطورين السورس .\n\n- { `.التحديثات تشغيل` }\nيستخدم هذا الامر لارسال رسالة تجريبية تلقائية لرؤية البوت اذا ما كان شغال بعد اعادة التشغيل او التحديث سيرسل امر `.بنك` ولايقافه ارسل `.التحديثات ايقاف` .\n\n[العقرب | 𝐒𝐜𝐨𝐫𝐩𝐢𝐨𝐧 ](t.me/Scorpion_scorp)☑️**"
)

@l313l.ar_cmd(
    pattern="اوامر الاطفاء$",
    command=("اوامر الاطفاء", plugin_category),
)
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit(
        "**شرح اوامر الاطفاء ✍🏻\n  \n✎┊‌ اختر احدى هذه الاوامر\n\n- { `.اطفاء` }\nلالغاء تشغيل البوت و يجب اعادة تشغيله من المنصه .\n\n  \n[العقرب | 𝐒𝐜𝐨𝐫𝐩𝐢𝐨𝐧 ](t.me/Scorpion_scorp)☑️**"
)

@l313l.ar_cmd(
    pattern="اوامر الكشف$",
    command=("اوامر الكشف", plugin_category),
)
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit(
        "**شرح اوامر الكشف ✍🏻\n  \n✎┊‌ اختر احدى هذه الاوامر\n\n- { `.الايدي` }\nبالرد على الشخص او كتابة معرفه مع الامر لعرض معلوماته.\n\n- { `.ايدي` }\nبالرد على الشخص لعرض معلوماته\n\n- { `.كشف` }\nبالرد على الشخص لعرض معلوماته بشكل مبسط\n\n[العقرب | 𝐒𝐜𝐨𝐫𝐩𝐢𝐨𝐧 ](t.me/Scorpion_scorp)☑️**"
)
@l313l.ar_cmd(
    pattern="اوامر الاستخراج$",
    command=("اوامر الاستخراج", plugin_category),
)
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit(
        "**شرح اوامر الاستخراج ✍🏻\n  \n✎┊‌ اختر احدى هذه الاوامر\n\n- { `.استخرج عربي` } \n لاستخراج النصوص من الصور التي تحتوي على كلمات عربيه\n\n- { `.افتاره` } \nلأخذ صور بروفايل اي شخص بالرد عليه \nمثال : (`.افتاره 1`) حته تاخذ اول صورة\n (`.افتاره كلها`) هنا ياخذ كل الصور\n\n \n[العقرب | 𝐒𝐜𝐨𝐫𝐩𝐢𝐨𝐧 ](t.me/Scorpion_scorp)☑️**"
)

@l313l.ar_cmd(
    pattern="اوامر الاذاعه$",
    command=("اوامر الاذاعه", plugin_category),
)
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit(
        "**شرح اوامر الـتوجيه والأذاعـة ✍🏻\n  \n✎┊‌ اختر احدى هذه الاوامر\n\n- { `.وجه + نص` }\nلعمـل اذاعـة للـنص في المجـموعـات اكتب الامر ونـصـك\n\n- { `.حول + نص` }\nلعمـل اذاعـة للـنص للـ الدردشـات الخـاصة اكتب الامر ونـصـك\n\n[العقرب | 𝐒𝐜𝐨𝐫𝐩𝐢𝐨𝐧 ](t.me/Scorpion_scorp)☑️**"
)


@l313l.ar_cmd(
    pattern="امر الصورة الذاتية$",
    command=(" امر الصورة الذاتية", plugin_category),
)
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit(
        "**شرح امر الصورة الذاتية ✍🏻\n  \n✎┊‌ اختر احدى هذه الاوامر\n\n- { `.ذاتية` }\n بالـرد عـلى الصـورة ذاتيـة الـتدمير ليـقوم بـحفظها وارسالـها لك فـي الرسائل الـمحفوظة بسرية وبـدون عـلم الـطرف الأخر \n{ `.الذاتية تشغيل` }\n قم بكتابة الامر في أي مكان ليقوم بتفعيل الامر وحفظ الصور الذاتية التدمير تلقائياً\n{ `.الذاتية تعطيل` }\n قم بكتابة الامر في مكان لتقوم بتعطيل الامر الصورة الذاتية التدمير\n- { `.بصمة` }\n بالـرد عـلى الصوتية ذاتيـة الـتدمير ليـقوم بـحفظها وارسالـها لك فـي الرسائل الـمحفوظة بسرية وبـدون عـلم الـطرف الأخر\n{ `.الصوتية تشغيل/تعطيل` }\n قم بكتابة الامر في مكان لتقوم بتشغيل وتعطيل امر الصوتيه الذاتية \n- { `.حفظ المحتوى` }\n اكتب الامر مع رابط الصورة او الملف الموجود في القناة ذات المحتوى المقيد ليتم حفظه\n- { `.خزن` }\nيعمل هذا الامر بالرد على اي رسالة ليقوم بحفظها في الرسائل المحفوظة\n\n[العقرب | 𝐒𝐜𝐨𝐫𝐩𝐢𝐨𝐧 ](t.me/Scorpion_scorp)☑️**"
)

@l313l.ar_cmd(
    pattern="اضافة ميمز$",
    command=("اضافة ميمز", plugin_category),
)
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit(
        "**شرح إضافة ميمز ✍🏻\n\n عزيزي حته تضيف ميمز سواء صوتيه او صورة او نكته لازم تكتب ( `.ميمز `) وتخلي بعدها رابط الرساله ولازم تكون من مجموعه في التلغرام \n - مثال : \n (`.ميمز https://t.me/fasngon/13125 انت اسكتت `)\n\n وحته تعرف وين صار الميمز الي ضفته اكتب (` .قائمة الميمز `) \n\n[العقرب | 𝐒𝐜𝐨𝐫𝐩𝐢𝐨𝐧 ](t.me/Scorpion_scorp)☑️**"
)

@l313l.ar_cmd(
    pattern="اوامر التحشيش$",
    command=("اوامر التحشيش", plugin_category),
)
async def _(event):
	if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
		await event.edit(
		"**قائمة اوامر التحشيش ✍🏻\n  \n\nجميع اوامـر التحشيش تستخـدم بالـرد عـلى الشخص\n [`.حيوان`]  [`.رفع تاج`] \n [`.رفع تيس`]  [`.رفع ططوة`] \n [`.رفع بربوك`]  [`.رفع بكلبي`]\n [`.رفع سني`] [`.رفع جلب`]\n [`.رفع مصري`] [`.رفع كتكوت`] \n [`.رفع سلبوح`] [`.رفع مرتي`]\n [`.رفع شيعي`] [`.نسبة الانوثة`]\n [`.نسبة الحب`] [`.نسبة الغباء`] \n [`.رفع سادس`]  [`.رفع سندرلا`] \n [`.رفع كردي`]  [`.رزله`] \n [`.رفع اخوة`]  [`.رفع حية`] \n [`.رفع بزون`]  [`.رفع وردة`]\n [`.رفع حامل`] [`.رفع طلي`]\n [`.رفع جانتي`] [`.رفع مجنب`]\n [`.رفع مميز`] [`.رفع ادمن`]\n [`.رفع منشئ`] [`.رفع مالك`]\n [`.رفع وصخ`] [`.نسبة الكذب`]\n [`.نسبة التشيع`] [`.نسبة الشذوذ`]\n [`.نسبة الجمال`] [`.نسبة الخيانه`]\n\n[العقرب | 𝐒𝐜𝐨𝐫𝐩𝐢𝐨𝐧 ](t.me/Scorpion_scorp)☑️**" 
)

@l313l.ar_cmd(
    pattern="اوامر التحويل$",
    command=("اوامر التحويل", plugin_category),
)
async def _(event):
	if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
		await event.edit(
		"**شـرح عـن اوامـر تـحويل الصـيغ ✍🏻\n \n ✎┊‌ اختر احدى هذه الاوامر\n\n- { `.تحويل صورة` }\n بالرد على الملصق لتحويله الى صورة\n\n- { `.تحويل ملصق` }\n بالرد على الصورة لتحويلها الى الملصق\n\n \n✎┊‌ [العقرب | 𝐒𝐜𝐨𝐫𝐩𝐢𝐨𝐧 ](t.me/Scorpion_scorp)☑️**"
)



@l313l.ar_cmd(
    pattern="اوامر الترفيه$",
    command=("اوامر الترفيه", plugin_category),
)
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit(
        "** قائمة اوامر الترفيه ✍🏻\n  \n✎┊‌ اختر احدى هذه الاوامر\n\n- { `.بلي` }\n- { `.كت` }\n- { `.خيروك` }\n- { `.غنيلي` }\n- { `.شعر` }\n- { `.قران` }\n- { `.البنك` }\n- { `.فلم` }\n- { `.محيبس` }\n- { `.سباق` }\n- { `.المليون` } \n- { `.سيارات` }\n- { `.اكس او` }\n- { `.اسرع` }\n\n[العقرب | 𝐒𝐜𝐨𝐫𝐩𝐢𝐨𝐧 ](t.me/Scorpion_scorp)☑️**"

)

@l313l.ar_cmd(
    pattern="اوامر الوهمي",
    command=("اوامر الوهمي", plugin_category),
)
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit(
        " **قائمة اوامر الوهمي ✍🏻\n  \n✎┊‌ اختر احدى هذه الاوامر\n\n- { `.كتابة` }\n-مثال : .كتابة + عدد الثواني \n- { `.صوتية` }\n- مثال : .صوتية + عدد الثواني \n- { `.فيد` }\n- مثال : .فيد + عدد الثواني \n- { `.لعبة` }\n- مثال : .لعبة + عدد الثواني\n\n [العقرب | 𝐒𝐜𝐨𝐫𝐩𝐢𝐨𝐧 ](t.me/Scorpion_scorp)☑️**"

)

@l313l.ar_cmd(
    pattern="اوامر التجميع$",
    command=("اوامر التجميع", plugin_category),
)
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit(
        "** قائمة اوامر التجميع ✍🏻\n  \n✎┊‌ اختر احدى هذه الاوامر\n\n- { `.تجميع المليار` }\n- { `.تجميع الجوكر` }\n- { `.تجميع العقاب` }\n- { `.تجميع المليون` }\n\n[العقرب | 𝐒𝐜𝐨𝐫𝐩𝐢𝐨𝐧 ](t.me/Scorpion_scorp)☑️**"
)
@l313l.ar_cmd(
    pattern="أوامر الكتابة$",
    command=("أوامر الكتابة", plugin_category),
)
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit(
        "** قائمة اوامر الكتابة ✍🏻\n  \n✎┊‌ اختر احدى هذه الاوامر\n\n- { `.غامق` }\n\n- { `.مائل` }\n\n- { `.نسخ` }\n\nملاحظة : كل الاوامر اعلاه تستخدم بالرد على النص \n\n- الخط الغامق: \n - {`.الخط الغامق`} \n - {`.إيقاف الخط الغامق`}\n\n- خط برمجي : \n - {`.خط البرمجة`}\n - {`.ايقاف خط البرمجة`}\n\n- خط العقرب \n - {`.خط العقرب`}\n - {`.ايقاف خط العقرب`}\n\n- خط بايثون \n - {`.خط بايثون`}\n - {`.ايقاف خط بايثون`}\n\n[العقرب | 𝐒𝐜𝐨𝐫𝐩𝐢𝐨𝐧 ](t.me/Scorpion_scorp)☑️**"
)
@l313l.ar_cmd(
    pattern="اوامر النشر$",
    command=("اوامر النشر", plugin_category),
)
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit(
        "** قائمة اوامر النشر التلقائي ✍🏻\n\n✎┊‌ اختر احدى هذه الاوامر\n\n- { `.نشر` }\nيستخدم هذا الامر مع الوقت بالثواني ورابط السوبر بالرد على الرسالة المراد نشرها \nمثال ( `.نشر 60 https://t.me/example` )\n\n- { `.ايقاف النشر` }\nيستخدم لايقاف جميع عمليات النشر\n\n[العقرب | 𝐒𝐜𝐨𝐫𝐩𝐢𝐨𝐧 ](t.me/Scorpion_scorp)☑️**"
)
@l313l.ar_cmd(
    pattern="اوامر التخصيص$",
    command=("اوامر التخصيص", plugin_category),
)
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit(
        "** قائمة اوامر التخصيص ✍🏻\n  \n✎┊‌ اختر احدى هذه الاوامر\n\n- قريباً . .\n\n  \n[العقرب | 𝐒𝐜𝐨𝐫𝐩𝐢𝐨𝐧 ](t.me/Scorpion_scorp)☑️**"
)

@l313l.ar_cmd(
    pattern="اوامر وعد$",
    command=("اوامر وعد", plugin_category),
)
async def _(event):
    if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit(
        "**قائمة اوامر وعد ✍🏻\n  \n✎┊‌ اختر احدى هذه الاوامر\n\n- { `.راتب وعد` } :\nعند كتابة الأمر في المجموعة، يقوم البوت بتجميع الأموال كل ١٠ دقيقة.\n\n- { `.ايقاف راتب وعد` } :\nيستخدم لإيقاف امر تجميع الراتب من بوت وعد .\n\n- { `.سرقة وعد + ايدي الشخص` } :\nيستخدم لسرقة أموال شخص آخر كل ١٠ دقيقة بواسطة إرسال ايدي المستخدم مع الامر .\n\n- { `.ايقاف سرقة وعد` } :\nيستخدم لإيقاف امر سرقة الأموال من الآخرين.\n\n- { `.بخشيش وعد` } :\nيستخدم لإعطاء بخشيش لك كل ١٠ دقيقة في المجموعة.\n\n- { `.ايقاف بخشيش وعد` } :\nيستخدم لإيقاف امر اخذ بخشيش من بوت وعد.\n\n- { `.استثمار وعد` } :\nيستخدم لاستثمار أموالك مع كل ٢٠ دقيقة.\n\n- { `.ايقاف استثمار وعد` } :\nيستخدم لإيقاف عملية الاستثمار بأموالك.\n\n[العقرب | 𝐒𝐜𝐨𝐫𝐩𝐢𝐨𝐧 ](t.me/Scorpion_scorp)☑️**"
)
@l313l.ar_cmd(
    pattern="الافتارات$",
    command=("الافتارات", plugin_category),
)
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit(
        "**قائمة اوامر الافتارات ✍🏻\n \n✎┊‌ اختر احداها\n\n- { `.اولاد رمادي` }\n- { `.بنات رماديه` }\n- { `.ولد انمي ` }\n- { `.بنات انمي` }\n- { `.بيست` }\n- { `.حب` }\n\n[العقرب | 𝐒𝐜𝐨𝐫𝐩𝐢𝐨𝐧 ](t.me/Scorpion_scorp)☑️**"
)
@l313l.ar_cmd(
    pattern="اوامر اخرى$",
    command=("اوامر اخرى", plugin_category),
)
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit(
        "**قائمة اوامر اخرى ✍🏻\n \n✎┊‌ اختر احداها\n\n- { `.ستوري انمي` }\n- { `.حالات` }\n- { `.ادت ` }\n- { `.تويت` }\n- { `.رياكشن` }\n- { `.معلومه` } \n\n- {`تحويل نص`}\nوذالك بالرد على الرسالة ليتم تحويلها الى ملصق \n\n[العقرب | 𝐒𝐜𝐨𝐫𝐩𝐢𝐨𝐧 ](t.me/Scorpion_scorp)☑️**"
)
@l313l.ar_cmd(
    pattern="قسم القرآن$",
    command=("قسم القرآن", plugin_category),
)
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit(
        "**قسم القرآن الكريم ✍🏻\n \n✎┊‌ اختر احداها\n\n- { `.قرآن` }\n\n- { `.آية` }\n\n- { `.سورة` } + اسم السورة \n- مثال : (`.سورة الفاتحة`)\n\n[العقرب | 𝐒𝐜𝐨𝐫𝐩𝐢𝐨𝐧 ](t.me/Scorpion_scorp)☑️**"
)
@l313l.ar_cmd(
    pattern="قسم الاحاديث والاقوال$",
    command=("قسم الاحاديث والاقوال", plugin_category),
)
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit(
        "**قسم الاحاديث والاقوآل ✍🏻\n \n✎┊‌ اختر احداها\n\n- { `.حديث` }\n\n- { `.ادعية` } \n\n[العقرب | 𝐒𝐜𝐨𝐫𝐩𝐢𝐨𝐧 ](t.me/Scorpion_scorp)☑️**"
	)
