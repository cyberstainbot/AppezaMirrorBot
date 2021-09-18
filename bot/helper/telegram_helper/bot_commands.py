import os
from bot import BOT_NO

def getCommand(name: str, command: str):
    try:
        if len(os.environ[name]) == 0:
            raise KeyError
        return os.environ[name]
    except KeyError:
        return command
class _BotCommands:
    def __init__(self):
        self.StartCommand = getCommand('START_COMMAND', 'start')
        self.MirrorCommand = getCommand('MIRROR_COMMAND', 'mirror')
        self.UnzipMirrorCommand = getCommand('UNZIP_COMMAND', 'unzipmirror')
        self.TarMirrorCommand = getCommand('TAR_COMMAND', 'tarmirror')
        self.ZipMirrorCommand = getCommand('ZIP_COMMAND', 'zipmirror')
        self.CancelMirror = getCommand('CANCEL_COMMAND', 'cancel')
        self.CancelAllCommand = getCommand('CANCELALL_COMMAND', 'cancelall')
        self.ListCommand = getCommand('LIST_COMMAND', 'list')
        self.StatusCommand = getCommand('STATUS_COMMAND', 'status')
        self.AuthorizedUsersCommand = getCommand('USERS_COMMAND', 'users')
        self.AuthorizeCommand = getCommand('AUTH_COMMAND'), 'authorize')
        self.UnAuthorizeCommand = getCommand('UNAUTH_COMMAND', 'unauthorize')
        self.AddSudoCommand = getCommand('ADDSUDO_COMMAND', 'addsudo')
        self.RmSudoCommand = getCommand('RMSUDO_COMMAND', 'rmsudo')
        self.PingCommand = getCommand('PING_COMMAND', 'ping')
        self.RestartCommand = getCommand('RESTART_COMMAND', 'restart')
        self.StatsCommand = getCommand('STATS_COMMAND', 'stats')
        self.HelpCommand = getCommand('HELP_COMMAND', 'help')
        self.LogCommand = getCommand('LOG_COMMAND', 'log')
        self.SpeedCommand = getCommand('SPEED_COMMAND', 'speedtest')
        self.CloneCommand = getCommand('CLONE_COMMAND', 'clone')
        self.CountCommand = getCommand('COUNT_COMMAND', 'count')
        self.WatchCommand = getCommand('WATCH_COMMAND', 'watch')
        self.TarWatchCommand = getCommand('TARWATCH_COMMAND', 'tarwatch')
        self.ZipWatchCommand = getCommand('ZIPWATCH_COMMAND', 'zipwatch')
        self.QbMirrorCommand = getCommand('QBMIRROR_COMMAND', 'qbmirror')
        self.QbUnzipMirrorCommand = getCommand('QBUNZIPMIRROR_COMMAND', 'qbunzipmirror')
        self.QbTarMirrorCommand = getCommand('QBTARMIRROR_COMMAND', 'qbtarmirror')
        self.QbZipMirrorCommand = getCommand('QBZIPMIRROR_COMMAND', 'qzipmirror')
        self.DeleteCommand = getCommand('DELETE_COMMAND', 'del')
        self.ShellCommand = getCommand('SHELL_COMMAND', 'shell')
        self.ExecHelpCommand = getCommand('EXECHELP_COMMAND', 'exechelp')
        self.TsHelpCommand = getCommand('TSHELP_COMMAND', 'tshelp')

BotCommands = _BotCommands()
