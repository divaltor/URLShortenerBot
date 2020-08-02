from envparse import env

env.read_envfile()

SERVICE_TOKEN = env.str('SERVICE_TOKEN')
API_VERSION = env.float('API_VERSION', default=5.103)

BIT_TOKEN = env.str('BIT_TOKEN')

BOT_TOKEN = env.str('BOT_TOKEN')

REDIS_HOST = env.str('REDIS_HOST', default='localhost')
REDIS_PORT = env.int('REDIS_PORT', default=6379)
REDIS_PASS = env.str('REDIS_PASS', default=None)
