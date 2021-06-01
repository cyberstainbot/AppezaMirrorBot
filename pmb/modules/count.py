from telegram.ext import CommandHandler
from pmb.helper.mirror_utils.upload_utils.gdriveTools import GoogleDriveHelper
from pmb.helper.telegram_helper.message_utils import deleteMessage, sendMessage
from pmb.helper.telegram_helper.filters import CustomFilters
from pmb.helper.telegram_helper.bot_commands import BotCommands
from pmb import dispatcher


def countNode(update,context):
    args = update.message.text.split(" ",maxsplit=1)
    if len(args) > 1:
        link = args[1]
        msg = sendMessage(f"📚 Counting: <code>{link}</code>",context.bot,update)
        gd = GoogleDriveHelper()
        result = gd.count(link)
        deleteMessage(context.bot,msg)
        sendMessage(result,context.bot,update)
    else:
        sendMessage("Provide G-Drive Shareable Link to Count.",context.bot,update)

count_handler = CommandHandler(BotCommands.CountCommand,countNode,filters=CustomFilters.authorized_chat | CustomFilters.authorized_user, run_async=True)
dispatcher.add_handler(count_handler)
