import os
import time
from bot import data, download_dir
from pyrogram.types import Message
from .ffmpeg import encode, get_thumbnail, get_duration, get_width_height, get_codec
from pyrogram.errors import FloodWait, MessageNotModified
from bot.progress import progress_for_pyrogram


def on_task_complete():
    del data[0]
    if len(data) > 0:
        add_task(data[0])


def add_task(message: Message):
    try:
        c_time = time.time()
        msg = message.reply_text("`🟡 Video İşleme Alındı... 🟡\n\n⚙️ Motor: Pyrogram\n\n#indirme`", quote=True)
        filepath = message.download(
            file_name=download_dir,
            progress=progress_for_pyrogram,
            progress_args=(
                "`İndiriliyor...`",
                msg,
                c_time
            ))
        try:
            msg.edit("`🟣 Video Kodlanıyor... 🟣\n\n⚙️ Motor: FFMPEG\n\n#kodlama`")
        except MessageNotModified:
            pass
        new_file = encode(filepath)
        if new_file:
            msg.edit("`🟢 Video Kodlandı, Veriler Alınıyor... 🟢`")
            duration = get_duration(new_file)
            thumb = get_thumbnail(new_file, download_dir, duration / 4)
            width, height = get_width_height(new_file)
            audio_codec = get_codec(new_file, channel='a:0')
            base_file_name = os.path.basename(new_file)
            caption_str = ""
            caption_str += "<code>"
            caption_str += base_file_name
            caption_str += "</code>"
            try:
                video = message.reply_video(
                    new_file,
                    caption=caption_str,
                    quote=True,
                    supports_streaming=True,
                    thumb=thumb,
                    duration=duration,
                    width=width,
                    height=height,
                    progress=progress_for_pyrogram,
                    progress_args=(
                        f"`{os.path.basename(new_file)} Yükleniyor...`",
                        msg,
                        c_time
                    ))
                if audio_codec == []:
                    video.reply_text("`⚪️ Bu videonun sesi yoktu ama yine de kodladım.\n\n#bilgilendirme`", quote=True)
            except FloodWait as e:
                print(f"Sleep of {e.x} required by FloodWait ...")
                time.sleep(e.x)
            except MessageNotModified:
                pass

            os.remove(new_file)
            os.remove(thumb)

            try:
                msg.edit("`İşlem Bitti. ✔️`")
            except MessageNotModified:
                pass
        else:
            msg.edit("`🔴 Dosyanızı kodlarken bir şeyler ters gitti.`")
            os.remove(filepath)
    except Exception as e:
        msg.edit(f"**🔴 HATA 🔴**:\n\n`{e}`\n\n#hata")
    on_task_complete()
