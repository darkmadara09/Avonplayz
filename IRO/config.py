import json
import os


def get_user_list(config, key):
    with open("{}/IRO/{}".format(os.getcwd(), config), "r") as json_file:
        return json.load(json_file)[key]


class Config(object):
    LOGGER = True
    # REQUIRED
    # Login to https://my.telegram.org and fill in these slots with the details given by it
     
    API_ID = 29143195  # integer value, dont use "" this sign get it form my.telegram.org
    API_HASH = "0f81a3974ac1e6b594252b3503174303" # get it form my.telegram.org
    TOKEN = "6964505365:AAGzwpo-uLIRIqu5ixfCNW1pQ7H85OMpb-E"  # get it form @botfather.
    OWNER_ID = 6529892817  # got to @Iro_m_bot and type /id
    OWNER_USERNAME = "Equinixs" # your telegram username
    ALLOW_CHATS = True # leave it as it is
    BOT_USERNAME = "Dazai_ixbot" # your bot username get it form @botfather
    NETWORK_USERNAME = "Alpha_Bots_Updates"
    SUPPORT_CHAT = "Alpha_Bots_Support"  # Your own group for support, do not add the @ if you dont have leave it as it is
    UPDATES_CHANNEL = "Alpha_Bots_Updates"  # Your own chsnnel for support, do not add the @ if you dont have leave it as it is
    JOIN_LOGGER =  (
        -1002117240104
    )  # add @Iro_m_bot in your group and type /id
    EVENT_LOGS = (
        -1002117240104
    )  # add @Iro_m_bot in your group and type /id
    ERROR_LOG = (
        -1002117240104
    )  # add @Iro_m_bot in your group and type /id
    STRICT_GMUTE = True #to allow gmutes
    START_STICKER = "CAACAgUAAx0Ce8yOxwAC2MlmU3_HtB15G_vDwig8i4Be8TDxrgAC1QwAAtjQoVagm6q4xT56cB4E" #sticker id for start animation
    TEMP_DOWNLOAD_DIRECTORY = ". /" # dont change
    OPENWEATHERMAP_ID = None



    # RECOMMENDED
    STRING_SESSION = "1BVtsOHUBu74yhmViJVt_pCtthzeg0X09Pd0Gmxf_s1bpGQ0tXQMoAaHzOd3ogCdIF67A2bAq2roPhh0lC4IS9iliM-bpVU8SKaHkYDChsQBCff6gJMMRpgOS51wGCUqU2Kj3WyljBDZq7kqkOGOoSMcB1Xk7ZOoLeurN_GrJ0LMtes2Ba0B9BoOQrHZ5spxUE9WdVNlyPIR46tkHW6u6TI5ky0ew_RotVzR0VKgMqevstekHqOGEKMSngMP6njtQg3WsGoAzePMZn1oPTk7MPlbe27F7H-6EpvAhM2BB9h5XcX47OO78xgqt9AG0wDAA0oMGavHE8x8pD4ITwcbEJMXJEXymUNg=" #telethon string session of user or bot get it from @Iro_string_bot
    DB_NAME = "Obito"
    MONGO_DB_URI = "mongodb+srv://Obito:Obito@obito.uolt8k3.mongodb.net/?retryWrites=true&w=majority" #get it from mongodb.com get
    ARQ_API_KEY = "GFUXSS-XJINVJ-CMIQKI-NHHBNS" #git it form @ARQRobot
    ARQ_API_URL = "https://arq.hamker.in" # dont change
    SQLALCHEMY_DATABASE_URL = "postgres://ufkji1bcmgibql:pd3a8d235fd8cc99dd58da419133c0f0b83fc43e31fd212b61ddc7628852c6a97@ce0lkuo944ch99.cluster-czrs8kj4isg7.us-east-1.rds.amazonaws.com:5432/d8agip3apc8867"  # needed for any database modules get it from https://www.elephantsql.com/
    LOAD = []
    NO_LOAD = ["rss", "cleaner", "connection", "math"]
    WEBHOOK = False
    INFOPIC = True
    URL = None
    SPAMWATCH_API = "bGPQ5_uXd2gxW2SiMkKNLm360HOtmAZpyf44aJOwI33ofIbE1oNtMeIf23Ru02a9"  # go to support.spamwat.ch to get key
    SPAMWATCH_SUPPORT_CHAT = "@iro_x_support"


    # OPTIONAL
    ##List of id's -  (not usernames) for users which have sudo access to the bot.
    DRAGONS = [6045293810]
    ##List of id's - (not usernames) for developers who will have the same perms as the owner
    DEV_USERS = [6045293810]
    ##List of id's (not usernames) for users which are allowed to gban, but can also be banned.
    DEMONS = [6045293810]
    # List of id's (not usernames) for users which WONT be banned/kicked by the bot.
    TIGERS = [6045293810]
    WOLVES = [6045293810]
    START_IMG = "https://graph.org/file/8f041d46eb3d38cc759cc.jpg" #yor fav img link
    CERT_PATH = None
    PORT = 5000
    DEL_CMDS = True  # Delete commands that users dont have access to, like delete /ban if a non admin uses it.
    STRICT_GBAN = True
    REM_BG_API_KEY = "XHPmZZztSksyF5rqc2CRBvMa"
    WORKERS = (
        8  # Number of subthreads to use. Set as number of threads your processor uses
    )
    BAN_STICKER = None  # banhammer marie sticker id, the bot will send this sticker before banning or kicking a user in chat.
    ALLOW_EXCL = True  # Allow ! commands as well as / (Leave this to true so that blacklist can work)
    CASH_API_KEY = (
        "awoo"  # Get your API key from https://www.alphavantage.co/support/#api-key
    )
    TIME_API_KEY = "awoo"  # Get your API key from https://timezonedb.com/api
    WALL_API = (
        "awoo"  # For wallpapers, get one from https://wall.alphacoders.com/api.php
    )
    BL_CHATS = []  # List of groups that you want blacklisted.
    SPAMMERS = None


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
