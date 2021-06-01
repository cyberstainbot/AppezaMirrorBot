[![Priiiyo](https://telegra.ph/file/b5d9a2910d65ce0596f59.jpg)](http://t.me/PriiiyoMirror)

# Priiiiyo Mirror Bot 
![GitHub Repo stars](https://img.shields.io/github/stars/priiiiyo/priiiiyo-mirror-bot?color=blue&style=flat)
![GitHub forks](https://img.shields.io/github/forks/priiiiyo/priiiiyo-mirror-bot?color=green&style=flat)
![GitHub issues](https://img.shields.io/github/issues/priiiiyo/priiiiyo-mirror-bot)
![GitHub closed issues](https://img.shields.io/github/issues-closed/priiiiyo/priiiiyo-mirror-bot)
![GitHub pull requests](https://img.shields.io/github/issues-pr/priiiiyo/priiiiyo-mirror-bot)
![GitHub closed pull requests](https://img.shields.io/github/issues-pr-closed/priiiiyo/priiiiyo-mirror-bot)
![GitHub contributors](https://img.shields.io/github/contributors/priiiiyo/priiiiyo-mirror-bot?style=flat)
![GitHub repo size](https://img.shields.io/github/repo-size/priiiiyo/priiiiyo-mirror-bot?color=red)
![GitHub commit activity](https://img.shields.io/github/commit-activity/m/priiiiyo/priiiiyo-mirror-bot)
[![Priiiiyo Mirror Support](https://img.shields.io/badge/priiiiyo%20mirror%20group-blue)](https://t.me/PriiiiyoMirror)


 **Priiiiyo Mirror Bot** A Telegram bot which can mirror all your links to Google drive! This is the Modified version.

# Features supported:

## From Source Repos
- Mirroring direct download links, Torrent, and Telegram files to Google Drive
- Copy files from someone's drive to your drive (Using Autorclone)
- Mirroring Mega.nz links to Google Drive (In development stage)
- Download/upload progress, speeds and ETAs
- Mirror all youtube-dl supported links
- Uploading To Team Drives
- Service Account Support
- Delete files from Drive
- Stable Mega.nz support
- Index Link support
- Shortener support
- Docker support
- Custom Filename (Only for url, telegram files and ytdl. Not for mega links and magnet/torrents)
- Extracting password protected files, using custom filename and download from password protected index links see these examples:
<p><a href="https://telegra.ph/Magneto-Python-Aria---Custom-Filename-Examples-01-20"> <img src="https://img.shields.io/badge/see%20on%20telegraph-grey?style=for-the-badge" width="190""/></a></p>

- Extract these filetypes and uploads to google drive
```
ZIP, RAR, TAR, 7z, ISO, WIM, CAB, GZIP, BZIP2, 
APM, ARJ, CHM, CPIO, CramFS, DEB, DMG, FAT, 
HFS, LZH, LZMA, LZMA2, MBR, MSI, MSLZ, NSIS, 
NTFS, RPM, SquashFS, UDF, VHD, XAR, Z.
```


## Additional Features

- Mirroring Uptobox.com links to Google Drive (Uptobox account must be premium)
- Get detailed info about replied media
- Nyaa.si and Sukebei Torrent search
- Speedtest with picture results
- Limiting torrent size support
- Sudo with database support
- Multiple Trackers support
- Check Heroku dynos stats
- Pixeldrain.com support
- Counting file/folders
- Custom image support
- Racaty.net support
- Shell and Executor
- Stickers module


## Special Features

- Dynamic Config Support, to facilitate easier and streamlined experience for editing config files.
- Sync Config Files at every /restart command.
- Edit values of environment variables in 'config.env' from within the bot using InlineKeyboardButtons.
- 'aria2c' daemon starts as a subprocess from within the 'bot' python module, facilitating better handling of processes. This also results in both 'aria2c' daemon and the 'bot' python module restarting with every '/restart' command.
- Support for using custom tracker list formatted as a text file, as required by 'aria2c' daemon.


# Development Status:

## To-Dos

- Add option to select files for torrent/magnet downloads.

**NOTE:** All the above to-dos are aimed at achieving zero human-intervention after initial deploy to Heroku.

## Info of Branches

- **master** : most stable environment for production deploys.
- **beta** : testing new features, fixes or better implementations of already existing ones.
- **dev** : major feature updates that are under development.


# How to deploy?
Deploying is pretty much straight forward and is divided into several steps as follows:


## Installing requirements

- Clone this repo:
```
git clone https://github.com/priiiiyo/priiiiyo-mirror-bot priiiiyo-mirror-bot/
cd priiiiyo-mirror-bot
```
- Install requirements
For Debian based distros
```
sudo apt install python3
```
Install Docker by following the [official Docker docs](https://docs.docker.com/engine/install/debian/)
```
sudo snap install docker 
```
- For Arch and it's derivatives:
```
sudo pacman -S docker python
```


## Setting up config file
<details>
    <summary><b>Click here for more details</b></summary>

```
cp config_sample.env config.env
```
- Remove the first line saying:
```
_____REMOVE_THIS_LINE_____=True
```
Fill up rest of the fields. Meaning of each fields are discussed below:
### Required Config
- **BOT_TOKEN**: The telegram bot token that you get from [@BotFather](https://t.me/BotFather)
- **GDRIVE_FOLDER_ID**: This is the folder ID of the Google Drive Folder to which you want to upload all the mirrors.
- **DOWNLOAD_DIR**: The path to the local folder where the downloads should be downloaded to
- **DOWNLOAD_STATUS_UPDATE_INTERVAL**: A short interval of time in seconds after which the Mirror progress message is updated. (I recommend to keep it 5 seconds at least)  
- **OWNER_ID**: The Telegram user ID (not username) of the owner of the bot.
- **API_KEY**: This is to authenticate to your telegram account for downloading Telegram files. You can get this from https://my.telegram.org DO NOT put this in quotes.
- **API_HASH**: This is to authenticate to your telegram account for downloading Telegram files. You can get this from https://my.telegram.org
- **DATABASE_URL**: Your Database URL. See Generate Database to generate database. (NOTE: If you deploying on Heroku, no need to generate database manually, because it will automatic generate database).
- **AUTO_DELETE_MESSAGE_DURATION**: Interval of time (in seconds), after which the bot deletes it's message (and command message) which is expected to be viewed instantly. Note: Set to -1 to never automatically delete messages
### Optional Field
- **AUTHORIZED_CHATS**: Fill user_id and chat_id of you want to authorize.
- **GROUP_ID**: Add Group id to get 'Bot Restarted' msg after bot restarts.
- **IS_TEAM_DRIVE**: (Optional config) Set to `True` if GDRIVE_FOLDER_ID is from a Team Drive else False or Leave it empty.
- **USE_SERVICE_ACCOUNTS**: (Optional field) (Leave empty if unsure) Whether to use service accounts or not. For this to work see "Using service accounts" section below.
- **INDEX_URL**: (Optional field) Refer to https://github.com/maple3142/GDIndex/ The URL. See [Generate Database](https://github.com/priiiiyo/priiiiyo-mirror-bot/tree/master#generate-database) should not have any trailing '/'
- **MEGA_KEY**: Mega.nz api key to mirror mega.nz links. Get it from [Mega SDK Page](https://mega.nz/sdk)
- **MEGA_USERNAME**: Your mega email id (You can leave it empty, it will start megasdkrest server in anonymous mode)
- **MEGA_PASSWORD**: Your password for your mega.nz account. (**NOTE**: You must deactivate 2FA to use the account with the bot otherwise bot will not be able to sign in)
- **STOP_DUPLICATE_MIRROR**: (Optional field) (Leave empty if unsure) if this field is set to `True` , bot will check file in drive, if it is present in drive, downloading will ne stopped. (Note - File will be checked using filename, not using filehash, so this feature is not perfect yet)
- **ENABLE_FILESIZE_LIMIT**: Set it to `True` if you want to use `MAX_TORRENT_SIZE`.
- **MAX_TORRENT_SIZE**: To limit the torrent mirror size, Fill The amount you want to limit, examples: if you fill `15` it will limit `15gb`.
- **HEROKU_API_KEY**: (Only if you deploying on Heroku) Your Heroku API key, get it from https://dashboard.heroku.com/account.
- **HEROKU_APP_NAME**: (Only if you deploying on Heroku) Your Heroku app name.
- **BLOCK_MEGA_FOLDER**: (Optional field) If you want to remove mega.nz folder support, set it to `True`.
- **BLOCK_MEGA_LINKS**: (Optional field) If you want to remove mega.nz mirror support (bcoz it's too much buggy and unstable), set it to `True`.
- **IMAGE_URL**: (Optional field) Show Image/Logo in /start message. Fill value of image your link image, use telegra.ph or any direct link image.
- **UPTOBOX_TOKEN**: Uptobox token to mirror uptobox links. Get it from [Uptobox Premium Account](https://uptobox.com/my_account).
- **SHORTENER_API**: Fill your shortener api key if you are using shortener.
- **SHORTENER**: (Optional field) if you want to use shortener in Gdrive and index link, fill shotener url here. Examples:
```
exe.io
gplinks.in
shrinkme.io
urlshortx.com
shortzon.com
```

Above are the supported url shorteners. Except these only some url shorteners are supported. If you want to use any other url shortener then first ask me that shortener is supported or not.

**Note**: You can limit maximum concurrent downloads by changing the value of **MAX_CONCURRENT_DOWNLOADS** in aria.sh. By default, it's set to `7`.
### Add more buttons (Optional)
Two buttons are already added of File Link and Index Link, you can add extra buttons too, these are optional, if you don't know what are below entries, simply leave them, don't fill anything in them.
- **BUTTON_THREE_NAME**:
- **BUTTON_THREE_URL**:
- **BUTTON_FOUR_NAME**:
- **BUTTON_FOUR_URL**:
- **BUTTON_FIVE_NAME**:
- **BUTTON_FIVE_URL**:

</details>

## Getting Google OAuth API credential file
- Visit the [Google Cloud Console](https://console.developers.google.com/apis/credentials)
- Go to the OAuth Consent tab, fill it, and save.
- Go to the Credentials tab and click Create Credentials -> OAuth Client ID
- Choose Desktop and Create.
- Use the download button to download your credentials.
- Move that file to the root of mirrorbot, and rename it to credentials.json
- Visit [Google API page](https://console.developers.google.com/apis/library)
- Search for Drive and enable it if it is disabled
- Finally, run the script to generate **token.pickle** file for Google Drive:
```
pip install google-api-python-client google-auth-httplib2 google-auth-oauthlib
python3 generate_drive_token.py
```

## Deploying

- Install Requirements:
```
pip3 install -r requirements-cli.txt
```
- Start docker daemon (skip if already running):
```
sudo dockerd
```
- Build Docker image:
```
sudo docker build . -t priiiiyo-mirror-bot
```
- Run the image:
```
sudo docker run priiiiyo-mirror-bot
```

## Generate Database
<details>
    <summary><b>Click here for more details</b></summary>

**1. Using ElephantSQL**
- Go to https://elephantsql.com/ and create account (skip this if you already have ElephantDB accounti)
- Hit **Create New Instance**
- Follow the further instructions in the screen
- Hit **Select Region**
- Hit **Review**
- Hit **Create instance**
- Select your database name
- Copy your database url, and fill to **DATABASE_URL** in config

**2. Using Heroku PostgreSQL**
<p><a href="https://dev.to/prisma/how-to-setup-a-free-postgresql-database-on-heroku-1dc1"> <img src="https://img.shields.io/badge/see%20on%20dev.to-black?style=for-the-badge&logo=dev-dot-to" width="190""/></a></p>

**NOTE**: If you deploying on Heroku, no need to generate database manually, because it will automatic generate database when first deploying

</details>

## Deploying on Heroku

Fork this repo then upload **token.pickle** to your forks

**NOTE**: If you didn't upload **token.pickle**, uploading will not work.
<p><a href="https://heroku.com/deploy"> <img src="https://img.shields.io/badge/Deploy%20To%20Heroku-blueviolet?style=for-the-badge&logo=heroku" width="200""/></a></p>

## Deploying on Heroku using heroku-cli
<details>
    <summary><b>Click here for more details</b></summary>

- Install [Heroku cli](https://devcenter.heroku.com/articles/heroku-cli)

## Creating a Heroku App

- Create a [free Heroku Account](https://id.heroku.com/signup/login).

- Install Heroku CLI:
```
sudo snap install --classic heroku
```
- Login into your heroku account with command:
```
heroku login
```
- Create a new heroku app:
```
heroku create appname
```
- Select This App in your Heroku-cli: 
```
heroku git:remote -a appname
```
- Change Dyno Stack to a Docker Container:
```
heroku stack:set container -a appname
```
- Add Private Credentials and Config Stuff:
```
git add -f credentials.json token.pickle config.env heroku.yml
```
- Commit new changes:
```
git commit -m "Added Creds."
```
- Push Code to Heroku:
```
git push heroku master --force
```
- Restart Worker by these commands,You can Do it manually too in heroku.

# Using CLI

- For Turning off the Bot:
```
heroku ps:scale worker=0 -a appname
```
- For Turning on the Bot:
```
heroku ps:scale worker=1 -a appname		
```
- To Check Status:
```
heroku ps --app your-mirror-bot
```
- To Tail App Logs:
```
heroku logs --tail --app your-mirror-bot
```

</details>


## Deploying on Heroku with heroku-cli and Goorm IDE
<p><a href="https://telegra.ph/How-to-Deploy-a-Mirror-Bot-to-Heroku-with-CLI-05-06"> <img src="https://img.shields.io/badge/see%20on%20telegraph-grey?style=for-the-badge" width="190""/></a></p>

## Bot commands to be set in [@BotFather](https://t.me/BotFather)

```
start - Start the bot
mirror - Start Mirroring
tarmirror - Upload tar (zipped) file
unzipmirror - Extract files
clone - copy file/folder to drive
watch - mirror YT-DL support link
tarwatch - mirror youtube playlist link as tar
authorize - Authorize a group chat or a specific user
unauthorize - Unauthorize a group chat or a specific user
cancel - Cancel a task
cancelall - Cancel all tasks
del - Delete file from Drive
list - [query] searches files in G-Drive
status - Get Mirror Status message
stats - Bot Usage Stats
ping - Ping the bot
restart - Restart the bot
help - Get Detailed Help
speedtest - Check Speed of the host
log - Bot Log [owner only]
repo - Get the bot repo
```

## Using Service Accounts for uploading to avoid user rate limit.
For Service Account to work, you must set **USE_SERVICE_ACCOUNTS="True"** in config file or environment variables
Many thanks to [AutoRClone](https://github.com/xyou365/AutoRclone) for the scripts
**NOTE**: Using Service Accounts is only recommended while uploading to a Team Drive.

## Generate Service Accounts. [What is Service Account](https://cloud.google.com/iam/docs/service-accounts)

Let us create only the Service Accounts that we need. 
**Warning**: abuse of this feature is not the aim of this project and we do **NOT** recommend that you make a lot of projects, just one project and 100 sa allow you plenty of use, its also possible that over abuse might get your projects banned by google. 

```
Note: 1 service account can copy around 750gb a day, 1 project can make 100 service accounts so that's 75tb a day, for most users this should easily suffice. 
```

`python3 gen_sa_accounts.py --quick-setup 1 --new-only`

A folder named accounts will be created which will contain keys for the Service Accounts.

**NOTE**: If you have created SAs in past from this script, you can also just re download the keys by running:
```
python3 gen_sa_accounts.py --download-keys project_id
```

## Add all the Service Accounts to the Team Drive
- Run:
```
python3 add_to_team_drive.py -d SharedTeamDriveSrcID
```

## Youtube-dl authentication using netrc file
For using your premium accounts in youtube-dl, edit the [.netrc](https://github.com/priiiiyo/priiiiyo-mirror-bot/blob/master/netrc) file according to following format:
```
machine host login username password my_youtube_password
```
where host is the name of extractor (eg. youtube, twitch). Multiple accounts of different hosts can be added each separated by a new line

# Support Group
<p><a href="https://t.me/PriiiiyoMirror"> <img src="https://img.shields.io/badge/Priiiiyo%20Mirror%20-black?style=for-the-badge&logo=telegram" width="230""/></a></p>

# Credits

Thanks to:
- [priiiiyo(me)](https://github.com/priiiiyo) for Custom Mod 🙆‍♂️
- [out386](https://github.com/out386) heavily inspired from telegram bot which is written in JS
- [Izzy12](https://github.com/lzzy12) for original repo
- [magneto261290](https://github.com/magneto261290) for some features
- [ksssomesh12](https://github.com/ksssomesh12) for some special features
- [SVR666](https://github.com/SVR666) for some features & fixes
- [Breakdowns](https://github.com/breakdowns) for some cool modules

and many more people who aren't mentioned here, but may be found in [Contributors](https://github.com/priiiyo/priiiyo-mirror-bot/graphs/contributors).
