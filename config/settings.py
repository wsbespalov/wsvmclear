import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

class CacheBase:
    def __init__(self):
        self.host = os.environ.get('REDIS_HOST', 'localhost')
        self.port = os.environ.get('REDIS_PORT', 6379)
        self.charset = 'utf-8'
        self.decode_responses = True

class Queue(CacheBase):
    def __init__(self):
        self.db = os.environ.get('REDIS_QUEUE_DB', 0)
        super(Queue, self).__init__()
    
class Stats(CacheBase):
    def __init__(self):
        self.db = os.environ.get('REDIS_STATS_DB', 1)
        super(Stats, self).__init__()

class Cache(CacheBase):
    def __init__(self):
        self.db = os.environ.get('REDIS_CACHE_DB', 3)
        super(Cache, self).__init__()

class Collections:
    ping_counter = 'ping_counter_collection'
    run_plugins = 'run_plugins_collection'
    helpers = 'helpers_collection'

class Postgres:
    def __init__(self):
        self.pg_database = os.environ.get('PG_DATABASE', 'updater_db')
        self.pg_user = os.environ.get('PG_USER', 'admin')
        self.pg_password = os.environ.get('PG_PASS', 'admin')
        self.pg_host = os.environ.get('PG_HOST', 'loaclhost')
        self.pg_port = os.environ.get('PG_PORT', 5432)
        self.reconnect_count = os.environ.get('PG_RECONNECT_COUNT', 1000)
        self.updater_offset = os.environ.get('PG_UPDATER_OFFSET', 1000)

class Settings:
    cache = Cache()
    queue = Queue()
    stats = Stats()
    postgres = Postgres()