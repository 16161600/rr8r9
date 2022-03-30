import os
import sys
from datetime import datetime
from time import time

from pyrogram import Client, filters
from pyrogram.types import Message

from config import HNDLR, SUDO_USERS

# System Uptime
START_TIME = datetime.utcnow()
TIME_DURATION_UNITS = (
    ("Minggu", 60 * 60 * 24 * 7),
    ("Hari", 60 * 60 * 24),
    ("Jam", 60 * 60),
    ("Menit", 60),
    ("Detik", 1),
)


async def _human_time_duration(seconds):
    if seconds == 0:
        return "inf"
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append("{} {}{}".format(amount, unit, "" if amount == 1 else ""))
    return ", ".join(parts)


@Client.on_message(filters.command(["بنك"], prefixes=f"{HNDLR}"))
async def ping(client, m: Message):
    await m.delete()
    start = time()
    current_time = datetime.utcnow()
    m_reply = await m.reply_text("⚡")
    delta_ping = time() - start
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await m_reply.edit(
        f"<b>🏓 بنك</b> `{delta_ping * 1000:.3f} ms` \n<b>⏳ AKTIF</b> - `{uptime}`"
    )


@Client.on_message(
    filters.user(SUDO_USERS) & filters.command(["اعادة تشغيل"], prefixes=f"{HNDLR}")
)
async def restart(client, m: Message):
    await m.delete()
    loli = await m.reply("1")
    await loli.edit("2")
    await loli.edit("3")
    await loli.edit("4")
    await loli.edit("5")
    await loli.edit("6")
    await loli.edit("7")
    await loli.edit("8")
    await loli.edit("9")
    await loli.edit("**✅ تم اعادة تشغيل البوت**")
    os.execl(sys.executable, sys.executable, *sys.argv)
    quit()


@Client.on_message(filters.command(["الاوامر"], prefixes=f"{HNDLR}"))
async def help(client, m: Message):
    await m.delete()
    HELP = f"""
<b>❤️‍🔥 مرحبا عزيز {m.from_user.mention}!
❤️‍🔥 قائمة الاوامر هاذي
❤️‍🔥 يمكنك استخدامها في المجموعة
• {HNDLR}ش › بالرد على ملف صوتي او اعطاء شي للبحث
• {HNDLR}ف › بالرد على مقطع فيديو او اعطاء اسم فيديو
• {HNDLR}بنك › لمعرفة بنك البوت
• {HNDLR}الاوامر › لرؤية اوامر المشرفين
• {HNDLR}استمر › لاستمرار الاغنية المتوقفة
• {HNDLR}توقف › لايقاف الاغنية مؤقتا
• {HNDLR}ص › لتحويل الرسالة الى بصمة صوتية
• {HNDLR}س › لتخطي اغنية 
• {HNDLR}فيديو › لتحميل فيديو من اليوتيوب 
• {HNDLR}الانتضار › لرؤية قائمة الانتضار  
• {HNDLR}اغاني  -› [اضغط هنا لمعرفة هذة الامر ♪](t.me/xl444/140) 
• {HNDLR}ك › لايقاف الاغنية</b>
"""
    await m.reply(HELP)
