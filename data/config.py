from environs import Env
import os
from dotenv import load_dotenv

env = Env()
env.read_env()
load_dotenv()

BOT_TOKEN = env.str("BOT_TOKEN")
ADMINS = env.list("ADMINS")
IP = env.str("ip")
BASE_URL = env.str("BASE_URL")