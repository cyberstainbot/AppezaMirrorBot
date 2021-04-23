from telegram.ext import CommandHandler
from pmb.helper.mirror_utils.upload_utils.gdriveTools import GoogleDriveHelper
from pmb.helper.telegram_helper.message_utils import *
from pmb.helper.telegram_helper.filters import CustomFilters
from pmb.helper.telegram_helper.bot_commands import BotCommands
from pmb.helper.ext_utils.bot_utils import new_thread
from pmb import dispatcher


def cloneNode(update,context):
    args = update.message.text.split(" ",maxsplit=1)
    if update.message.from_user.username:
        uname = f"@{update.message.from_user.username}"
    else:
        uname = f'<a href="tg://user?id={update.message.from_user.id}">{update.message.from_user.first_name}</a>'
    if uname is not None:
            cc = f'\n\n👤 𝗖𝗹𝗼𝗻𝗲𝗱 𝗕𝘆 : {uname}'
    if len(args) > 1:
        link = args[1]
        msg = sendMessage(f"Cloning: <code>{link}</code>",context.bot,update)
        gd = GoogleDriveHelper()
        result, button = gd.clone(link)
        deleteMessage(context.bot,msg)
        if button == "":
            sendMessage(result,context.bot,update)
        else:
            sendMarkup(result + cc,context.bot,update,button)
    else:
        sendMessage("Provide G-Drive Shareable Link to Clone.",context.bot,update)

clone_handler = CommandHandler(BotCommands.CloneCommand,cloneNode,filters=CustomFilters.authorized_chat | CustomFilters.authorized_user, run_async=True)
dispatcher.add_handler(clone_handler)
