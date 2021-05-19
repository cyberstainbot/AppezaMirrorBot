from pmb.helper.telegram_helper.message_utils import sendMessage
from pmb import AUTHORIZED_CHATS, SUDO_USERS, dispatcher
from telegram.ext import CommandHandler
from pmb.helper.telegram_helper.filters import CustomFilters
from telegram.ext import Filters
from telegram import Update
from pmb.helper.telegram_helper.bot_commands import BotCommands
from pmb.helper.ext_utils.db_handler import DbManger


def authorize(update,context):
    reply_message = None
    message_ = None
    reply_message = update.message.reply_to_message
    message_ = update.message.text.split(' ')
    if len(message_) == 2:
        chat_id = int(message_[1])
        if chat_id not in AUTHORIZED_CHATS:
            msg = DbManger().db_auth(chat_id)
        else:
            msg = '✅ User already authorized'
    else:
        if reply_message is None:
            # Trying to authorize a chat
            chat_id = update.effective_chat.id
            if chat_id not in AUTHORIZED_CHATS:
                msg = DbManger().db_auth(chat_id)
            else:
                msg = '✅ Already authorized chat'

        else:
            # Trying to authorize someone in specific
            user_id = reply_message.from_user.id
            if user_id not in AUTHORIZED_CHATS:
                msg = DbManger().db_auth(user_id)
            else:
                msg = '✅ User already authorized'
    sendMessage(msg, context.bot, update)


def unauthorize(update,context):
    reply_message = None
    message_ = None
    reply_message = update.message.reply_to_message
    message_ = update.message.text.split(' ')
    if len(message_) == 2:
        chat_id = int(message_[1])
        if chat_id in AUTHORIZED_CHATS:
            msg = DbManger().db_unauth(chat_id)
        else:
            msg = '❎ User already unauthorized'
    else:
        if reply_message is None:
            # Trying to unauthorize a chat
            chat_id = update.effective_chat.id
            if chat_id in AUTHORIZED_CHATS:
                msg = DbManger().db_unauth(chat_id)
            else:
                msg = '❎ Already unauthorized chat'
        else:
            # Trying to authorize someone in specific
            user_id = reply_message.from_user.id
            if user_id in AUTHORIZED_CHATS:
                msg = DbManger().db_unauth(user_id)
            else:
                msg = '❎ User already unauthorized'
    sendMessage(msg, context.bot, update)


def addSudo(update,context):
    reply_message = None
    message_ = None
    reply_message = update.message.reply_to_message
    message_ = update.message.text.split(' ')
    if len(message_) == 2:
        chat_id = int(message_[1])
        if chat_id not in SUDO_USERS:
            msg = DbManger().db_addsudo(chat_id)
        else:
            msg = '👨‍🦱 Already Sudo User'
    else:
        if reply_message is None:
            msg = "Give ID or Reply To message of whom you want to Promote"
        else:
            # Trying to authorize someone in specific
            user_id = reply_message.from_user.id
            if user_id not in SUDO_USERS:
                msg = DbManger().db_addsudo(user_id)
            else:
                msg = '👨‍🦱 Already Sudo User'
    sendMessage(msg, context.bot, update)


def removeSudo(update,context):
    reply_message = None
    message_ = None
    reply_message = update.message.reply_to_message
    message_ = update.message.text.split(' ') 
    if len(message_) == 2:
        chat_id = int(message_[1])
        if chat_id in SUDO_USERS:
            msg = DbManger().db_rmsudo(chat_id)
        else:
            msg = '🙅‍♂️ Not a Sudo User'
    else:
        if reply_message is None:
            msg = "Give ID or Reply To message of whom you want to remove from Sudo"
        else:
            user_id = reply_message.from_user.id
            if user_id in SUDO_USERS:
                msg = DbManger().db_rmsudo(user_id)
            else:
                msg = '🙅‍♂️ Not a Sudo User'
    sendMessage(msg, context.bot, update)


def sendAuthChats(update,context):
    user = sudo = ''
    user += '\n'.join(str(id) for id in AUTHORIZED_CHATS)
    sudo += '\n'.join(str(id) for id in SUDO_USERS)
    sendMessage(f'<b><u>Authorized Chats</u></b>\n{user}\n<b><u>Sudo Users</u></b>\n{sudo}', context.bot, update)


send_auth_handler = CommandHandler(command=BotCommands.AuthorizedUsersCommand, callback=sendAuthChats,
                                    filters=CustomFilters.owner_filter | CustomFilters.sudo_user, run_async=True)
authorize_handler = CommandHandler(command=BotCommands.AuthorizeCommand, callback=authorize,
                                    filters=CustomFilters.owner_filter | CustomFilters.sudo_user, run_async=True)
unauthorize_handler = CommandHandler(command=BotCommands.UnAuthorizeCommand, callback=unauthorize,
                                    filters=CustomFilters.owner_filter | CustomFilters.sudo_user, run_async=True)
addsudo_handler = CommandHandler(command=BotCommands.AddSudoCommand, callback=addSudo,
                                    filters=CustomFilters.owner_filter, run_async=True)
removesudo_handler = CommandHandler(command=BotCommands.RmSudoCommand, callback=removeSudo,
                                    filters=CustomFilters.owner_filter, run_async=True)

dispatcher.add_handler(send_auth_handler)
dispatcher.add_handler(authorize_handler)
dispatcher.add_handler(unauthorize_handler)
dispatcher.add_handler(addsudo_handler)
dispatcher.add_handler(removesudo_handler)
