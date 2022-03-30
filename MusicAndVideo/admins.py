from pyrogram import Client, filters
from pyrogram.types import Message

from config import HNDLR, call_py
from MusicAndVideo.helpers.decorators import authorized_users_only
from MusicAndVideo.helpers.handlers import skip_current_song, skip_item
from MusicAndVideo.helpers.queues import QUEUE, clear_queue


@Client.on_message(filters.command(["س"], prefixes=f"{HNDLR}"))
@authorized_users_only
async def skip(client, m: Message):
    await m.delete()
    chat_id = m.chat.id
    if len(m.command) < 2:
        op = await skip_current_song(chat_id)
        if op == 0:
            await m.reply("**❤️‍🔥 يَاެعينِي مَاެكۅ شيَ مَشتغݪ ؟**")
        elif op == 1:
            await m.reply("❤️‍🔥قِاެئمَةَ اެنِتَظِاެࢪ فَاެࢪغِةَ ، مَغِاެدَࢪةَ اެݪدَࢪدَشِةَ اެݪصَۅٛتَيَةَ**")
        else:
            await m.reply(
                f"**⏭ اެبشࢪ عَينِي تَم اެݪتخِطي** \n**❤️‍🔥 يَتمَ اެݪتشغِيݪ اެلانِ** - [{op[0]}]({op[1]}) | `{op[2]}`",
                disable_web_page_preview=True,
            )
    else:
        skip = m.text.split(None, 1)[1]
        OP = "**🗑️ تمت إزالة الأغاني التالية من قائمة الانتظار: -**"
        if chat_id in QUEUE:
            items = [int(x) for x in skip.split(" ") if x.isdigit()]
            items.sort(reverse=True)
            for x in items:
                if x == 0:
                    pass
                else:
                    hm = await skip_item(chat_id, x)
                    if hm == 0:
                        pass
                    else:
                        OP = OP + "\n" + f"**#⃣{x}** - {hm}"
            await m.reply(OP)


@Client.on_message(filters.command(["ك", "اوكف"], prefixes=f"{HNDLR}"))
@authorized_users_only
async def stop(client, m: Message):
    await m.delete()
    chat_id = m.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.leave_group_call(chat_id)
            clear_queue(chat_id)
            await m.reply("**❤️‍🔥 تَم اެݪانِهاء اެبشࢪ**")
        except Exception as e:
            await m.reply(f"**ERROR** \n`{e}`")
    else:
        await m.reply("**❤️‍🔥 يَاެعينِي مَاެكۅ شيَ مَشتغݪ ؟**")


@Client.on_message(filters.command(["توقف"], prefixes=f"{HNDLR}"))
@authorized_users_only
async def pause(client, m: Message):
    await m.delete()
    chat_id = m.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.pause_stream(chat_id)
            await m.reply(
                f"**⏸ توقف التشغيل مؤقتًا.**\n\n• لاستمرار التشغيل  » {HNDLR}استمر"
            )
        except Exception as e:
            await m.reply(f"**ERROR** \n`{e}`")
    else:
        await m.reply("** ❤️‍🔥 يَاެعينِي مَاެكۅ شيَ مَشتغݪ ؟**")


@Client.on_message(filters.command(["استمر"], prefixes=f"{HNDLR}"))
@authorized_users_only
async def resume(client, m: Message):
    await m.delete()
    chat_id = m.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.resume_stream(chat_id)
            await m.reply(
                f"**▶ استئناف التشغيل المتوقف مؤقتًا**\n\n• لإيقاف التشغيل مؤقتًا ، استخدم الأمر » {HNDLR}توقف**"
            )
        except Exception as e:
            await m.reply(f"**ERROR** \n`{e}`")
    else:
        await m.reply("**❤️‍🔥 يَاެعينِي مَاެكۅ شيَ مَشتغݪ ؟**")
