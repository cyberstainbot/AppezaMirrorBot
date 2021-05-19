import os
import shutil, psutil
import signal
import pickle
from pyrogram import idle
from pmb import app
from os import execl, kill, path, remove
from sys import executable
from datetime import datetime
import pytz
import time
from telegram import ParseMode, BotCommand, InlineKeyboardMarkup, InlineKeyboardButton
from telegram import Update
from telegram.ext import CallbackContext, CommandHandler
from pmb import bot, dispatcher, updater, botStartTime, IMAGE_URL
from pmb.helper.ext_utils import fs_utils
from pmb.helper.telegram_helper.bot_commands import BotCommands
from pmb.helper.telegram_helper.message_utils import *
from .helper.ext_utils.bot_utils import get_readable_file_size, get_readable_time
from .helper.telegram_helper.filters import CustomFilters
from .helper.config import editor
from .helper.config.subproc import killAll
from .helper.config import sync
from .helper.config.dynamic import configList, DYNAMIC_CONFIG
from .modules import authorize, list, cancel_mirror, mirror_status, mirror, clone, watch, shell, eval, anime, stickers, search, delete, speedtest, usage, mediainfo 

from pyrogram import idle
from pmb import app

now=datetime.now(pytz.timezone('Asia/Dhaka'))

def stats(update: Update, context: CallbackContext):
    currentTime = get_readable_time(time.time() - botStartTime)
    current = now.strftime('%Y/%m/%d %I:%M:%S')
    total, used, free = shutil.disk_usage('.')
    total = get_readable_file_size(total)
    used = get_readable_file_size(used)
    free = get_readable_file_size(free)
    sent = get_readable_file_size(psutil.net_io_counters().bytes_sent)
    recv = get_readable_file_size(psutil.net_io_counters().bytes_recv)
    cpuUsage = psutil.cpu_percent(interval=0.5)
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent
    stats = f'<b>╭──「  ⭕️ BOT STATISTICS ⭕️ 」 </b>\n' \
            f'<b>│</b>\n' \
            f'<b>├  ⏰ Bot Uptime : {currentTime}</b>\n' \
            f'<b>├  🔊 Start Time :</b> {current}\n' \
            f'<b>├  🗄 Total Disk Space : {total}</b>\n' \
            f'<b>├  🗂 Total Used Space : {used}</b>\n' \
            f'<b>├  📂 Total Free Space : {free}</b>\n' \
            f'<b>├  📑 Data Usage 📑:</b>\n' \
            f'<b>├  📤 Total Upload : {sent}</b>\n' \
            f'<b>├  📥 Total Download : {recv}</b>\n' \
            f'<b>├  🖥️ CPU : {cpuUsage}%</b>\n' \
            f'<b>├  🚀 RAM : {memory}%</b>\n' \
            f'<b>├  🗄 DISK : {disk}%</b>\n' \
            f'<b>│</b>\n' \
            f'<b>╰──「 🚸 @PriiiiyoBOTs 🚸 」</b>'
    update.effective_message.reply_photo(IMAGE_URL, stats, parse_mode=ParseMode.HTML)


def start(update: Update, context: CallbackContext):
    start_string = f'''
This is a bot which can mirror all your links to Google drive!

👲 Modded By: @priiiiyo

Type /{BotCommands.HelpCommand} to get a list of available commands
'''
    update.effective_message.reply_photo(IMAGE_URL, start_string, parse_mode=ParseMode.MARKDOWN)

    
def owner(update: Update, context: CallbackContext):
    button = [
    [InlineKeyboardButton("👤 Owner 👤", url=f"https://t.me/priiiiyo")],
    [InlineKeyboardButton("🔰 Mirror Group 🔰", url=f"https://t.me/PriiiiyoMirror")]]
    reply_markup = InlineKeyboardMarkup(button)
    update.effective_message.reply_photo(IMAGE_URL, reply_markup=reply_markup)


def repo(update: Update, context: CallbackContext):
    button = [
    [InlineKeyboardButton("⚠️ Repo ⚠️", url=f"https://github.com/priiiiyo/priiiiyo-mirror-bot")],
    [InlineKeyboardButton("🔰 Support Group 🔰", url=f"https://t.me/PriiiiyoBOTs_Support")]]
    reply_markup = InlineKeyboardMarkup(button)
    update.effective_message.reply_photo(IMAGE_URL, reply_markup=reply_markup)


def restart(update: Update, context: CallbackContext):
    restart_msg = sendMessage('Restarting, Please Wait...', context.bot, update)
    LOGGER.info(f'Restarting the Bot...')
    fs_utils.clean_all()
    killAll()
    if DYNAMIC_CONFIG:
        time.sleep(3)
        restart_msg.edit_text(f'Syncing to Google Drive...')
        sync.handler(configList)
        restart_msg.edit_text(f'Sync Completed!\n{configList}')
    if not DYNAMIC_CONFIG:
        time.sleep(5)
    # Save restart message info in order to reply to it after restarting
    restart_msg_dat = f"{restart_msg.chat_id} {restart_msg.message_id}"
    open('restart_msg.txt', 'wt').write(restart_msg_dat)
    execl(executable, executable, "-m", "pmb")


def ping(update: Update, context: CallbackContext):
    start_time = int(round(time.time() * 1000))
    reply = sendMessage("Starting Ping...", context.bot, update)
    end_time = int(round(time.time() * 1000))
    editMessage(f'{end_time - start_time} ms', reply)


def log(update: Update, context: CallbackContext):
    sendLogFile(context.bot, update)


def bot_help(update: Update, context: CallbackContext):
    help_string_adm = f'''
/{BotCommands.HelpCommand}: To get this message

/{BotCommands.MirrorCommand} [download_url][magnet_link]: Start mirroring the link to Google Drive.

/{BotCommands.UnzipMirrorCommand} [download_url][magnet_link]: Starts mirroring and if downloaded file is any archive, extracts it to Google Drive

/{BotCommands.TarMirrorCommand} [download_url][magnet_link]: Start mirroring and upload the archived (.tar) version of the download

/{BotCommands.CloneCommand}: Copy file/folder to Google Drive

/{BotCommands.DeleteCommand} [link]: Delete file from Google Drive (Only Owner & Sudo)

/{BotCommands.WatchCommand} [youtube-dl supported link]: Mirror through youtube-dl. Click /{BotCommands.WatchCommand} for more help.

/{BotCommands.TarWatchCommand} [youtube-dl supported link]: Mirror through youtube-dl and tar before uploading

/{BotCommands.CancelMirror}: Reply to the message by which the download was initiated and that download will be cancelled

/{BotCommands.StatusCommand}: Shows a status of all the downloads

/{BotCommands.ListCommand} [search term]: Searches the search term in the Google Drive, if found replies with the link

/{BotCommands.StatsCommand}: Show Stats of the machine the bot is hosted on

/{BotCommands.AuthorizeCommand}: Authorize a chat or a user to use the bot (Can only be invoked by Owner & Sudo of the bot)

/{BotCommands.UnAuthorizeCommand}: Unauthorize a chat or a user to use the bot (Can only be invoked by Owner & Sudo of the bot)

/{BotCommands.AuthorizedUsersCommand}: Show authorized users (Only Owner & Sudo)

/{BotCommands.AddSudoCommand}: Add sudo user (Only Owner)

/{BotCommands.RmSudoCommand}: Remove sudo users (Only Owner)

/{BotCommands.LogCommand}: Get a log file of the bot. Handy for getting crash reports

/{BotCommands.UsageCommand}: To see Heroku Dyno Stats (Owner & Sudo only).

/{BotCommands.SpeedCommand}: Check Internet Speed of the Host

/{BotCommands.RepoCommand}: Get the bot repo.

/shell: Run commands in Shell (Terminal).

/mediainfo: Get detailed info about replied media.

/tshelp: Get help for Torrent search module.

/weebhelp: Get help for Anime, Manga, and Character module.

/stickerhelp: Get help for Stickers module.
'''

    help_string = f'''
/{BotCommands.HelpCommand}: To get this message

/{BotCommands.MirrorCommand} [download_url][magnet_link]: Start mirroring the link to Google Drive.

/{BotCommands.UnzipMirrorCommand} [download_url][magnet_link]: Starts mirroring and if downloaded file is any archive, extracts it to Google Drive

/{BotCommands.TarMirrorCommand} [download_url][magnet_link]: Start mirroring and upload the archived (.tar) version of the download

/{BotCommands.CloneCommand}: Copy file/folder to Google Drive

/{BotCommands.WatchCommand} [youtube-dl supported link]: Mirror through youtube-dl. Click /{BotCommands.WatchCommand} for more help.

/{BotCommands.TarWatchCommand} [youtube-dl supported link]: Mirror through youtube-dl and tar before uploading

/{BotCommands.CancelMirror}: Reply to the message by which the download was initiated and that download will be cancelled

/{BotCommands.StatusCommand}: Shows a status of all the downloads

/{BotCommands.ListCommand} [search term]: Searches the search term in the Google Drive, if found replies with the link

/{BotCommands.StatsCommand}: Show Stats of the machine the bot is hosted on

/{BotCommands.SpeedCommand}: Check Internet Speed of the Host

/{BotCommands.RepoCommand}: Get the bot repo.

/mediainfo: Get detailed info about replied media.

/tshelp: Get help for Torrent search module.

/weebhelp: Get help for Anime, Manga, and Character module.

/stickerhelp: Get help for Stickers module.
'''

    if CustomFilters.sudo_user(update) or CustomFilters.owner_filter(update):
        sendMessage(help_string_adm, context.bot, update)
    else:
        sendMessage(help_string, context.bot, update)


botcmds = [
BotCommand(f'{BotCommands.MirrorCommand}', 'Start Mirroring'),
BotCommand(f'{BotCommands.TarMirrorCommand}','Upload tar (zipped) file'),
BotCommand(f'{BotCommands.UnzipMirrorCommand}','Extract files'),
BotCommand(f'{BotCommands.CloneCommand}','Copy file/folder to Drive'),
BotCommand(f'{BotCommands.WatchCommand}','Mirror YT-DL support link'),
BotCommand(f'{BotCommands.TarWatchCommand}','Mirror Youtube playlist link as tar'),
BotCommand(f'{BotCommands.CancelMirror}','Cancel a task'),
BotCommand(f'{BotCommands.CancelAllCommand}','Cancel all tasks'),
BotCommand(f'{BotCommands.DeleteCommand}','Delete file from Drive'),
BotCommand(f'{BotCommands.ListCommand}',' [query] Searches files in G-Drive'),
BotCommand(f'{BotCommands.AuthorizedUsersCommand}','Show authorized users (Only Owner & Sudo)'),
BotCommand(f'{BotCommands.StatusCommand}','Get Mirror Status message'),
BotCommand(f'{BotCommands.StatsCommand}','Bot Usage Stats'),
BotCommand(f'{BotCommands.HelpCommand}','Get Detailed Help'),
BotCommand(f'{BotCommands.SpeedCommand}','Check Speed of the host'),
BotCommand(f'{BotCommands.LogCommand}','Bot Log [owner only]'),
BotCommand(f'{BotCommands.UsageCommand}','To see Heroku Dyno Stats (Owner only)'),
BotCommand(f'{BotCommands.OwnerCommand}','Check Who is My master'),
BotCommand(f'{BotCommands.RestartCommand}','Restart bot [owner only]'),
BotCommand(f'{BotCommands.RepoCommand}','Get the bot repo')]


def main():
    fs_utils.start_cleanup()
    # Check if the bot is restarting
    if path.exists('restart_msg.txt'):
        restart_msg_dat = open('restart_msg.txt', 'rt').read().split(' ')
        bot.editMessageText(text='Sync Completed!\nRestarted Successfully!',
                            chat_id=restart_msg_dat[0], message_id=restart_msg_dat[1])
        LOGGER.info('Restarted Successfully!')
        remove('restart_msg.txt')
    bot.set_my_commands(botcmds)
        
    start_handler = CommandHandler(BotCommands.StartCommand, start,
                                   filters=CustomFilters.authorized_chat | CustomFilters.authorized_user, run_async=True)
    ping_handler = CommandHandler(BotCommands.PingCommand, ping,
                                  filters=CustomFilters.authorized_chat | CustomFilters.authorized_user, run_async=True)
    restart_handler = CommandHandler(BotCommands.RestartCommand, restart,
                                     filters=CustomFilters.owner_filter, run_async=True)
    help_handler = CommandHandler(BotCommands.HelpCommand,
                                  bot_help, filters=CustomFilters.authorized_chat | CustomFilters.authorized_user, run_async=True)
    stats_handler = CommandHandler(BotCommands.StatsCommand,
                                   stats, filters=CustomFilters.authorized_chat | CustomFilters.authorized_user, run_async=True)
    log_handler = CommandHandler(BotCommands.LogCommand, log, filters=CustomFilters.owner_filter, run_async=True)
    repo_handler = CommandHandler(BotCommands.RepoCommand, repo,
                                  filters=CustomFilters.authorized_chat | CustomFilters.authorized_user, run_async=True)
    owner_handler = CommandHandler(BotCommands.OwnerCommand, owner,
                                   filters=CustomFilters.authorized_chat | CustomFilters.authorized_user, run_async=True)
    config_handler = editor.handler
    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(ping_handler)
    dispatcher.add_handler(restart_handler)
    dispatcher.add_handler(help_handler)
    dispatcher.add_handler(stats_handler)
    dispatcher.add_handler(log_handler)
    dispatcher.add_handler(repo_handler)
    dispatcher.add_handler(owner_handler)
    dispatcher.add_handler(config_handler)
    updater.start_polling()
    LOGGER.info("Bot Started!")
    signal.signal(signal.SIGINT, fs_utils.exit_clean_up)


app.start()
main()
idle()
