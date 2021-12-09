from pyrogram import filters
from bot import app, data, sudo_users
from bot.helper.utils import add_task
from pyrogram.types.bots_and_keyboards import InlineKeyboardButton, InlineKeyboardMarkup
from .translation import Translation

video_mimetype = [
  "video/x-flv",
  "video/mp4",
  "video/avi",
  "video/mkv",
  "application/x-mpegURL",
  "video/mp2t",
  "video/3gpp",
  "video/quicktime",
  "video/x-msvideo",
  "video/x-ms-wmv",
  "video/x-matroska",
  "video/webm",
  "video/x-m4v",
  "video/quicktime",
  "video/mpeg"
  ]

@app.on_message(filters.user(sudo_users) & filters.incoming & filters.command(['start', 'help']))
def help_message(app, message):
        message.reply_text(
            text=Translation.START_TEXT.format(message.from_user.mention()),
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            "Destek", url="https://t.me/botsohbet"
                        )
                    ]
                ]
            ),
            reply_to_message_id=message.message_id
        ) 
    
@app.on_message(filters.user(sudo_users) & filters.incoming & (filters.video | filters.document))
def encode_video(app, message):
    if message.document:
      if not message.document.mime_type in video_mimetype:
        message.reply_text("```Geçersiz Video !\nBu video dosyasına benzemiyor.```", quote=True)
        return
    message.reply_text(f"`✔️ Sıraya Eklendi...\nSıra: {len(data)}\n\nSabırlı olun...\n\n#kuyruk`", quote=True)
    data.append(message)
    if len(data) == 1:
      add_task(message)

app.run()
