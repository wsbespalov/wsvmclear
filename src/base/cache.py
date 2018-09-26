import os
import sys
import abc
import redis
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from config.settings import Settings

from utils.utils import get_module_name


class CachePrototype(metaclass=abc.ABCMeta):
    def __init__(self, settings):
        self.subscribed = False
        self.cache = redis.StrictRedis(
            host=settings.host,
            port=settings.port,
            db=settings.db,
            charset=settings.charset,
            decode_responses=settings.decode_responses
        )

    def ping(self):
        try:
            ping = self.cache.ping()
            if ping:
                return True
            return False
        except Exception as ex:
            return False

    def set(self, collection, data):
        try:
            if self.ping():
                return self.cache.set(collection, data)
            return None
        except Exception as ex:
            return None

    def get(self, collection):
        try:
            if self.ping():
                if self.cache.exists(collection):
                    return self.cache.get(collection)
            return None
        except Exception as ex:
            return None

    def push(self, collection, data):
        try:
            if self.ping():
                return self.cache.rpush(collection, data)
            return None
        except Exception as ex:
            return None

    def pop(self, collection):
        try:
            if self.ping():
                if self.cache.exists(collection):
                    return self.cache.lpop(collection)
            return None
        except Exception as ex:
            return None

    def increment(self, collection, value=1):
        try:
            if self.ping():
                if self.cache.exists(collection):
                    return self.cache.incr(collection, amount=value)
            return None
        except Exception as ex:
            return None

    def decrement(self, collection, value=1):
        try:
            if self.ping():
                if self.cache.exists(collection):
                    return self.cache.decr(collection, amount=value)
            return None
        except Exception as ex:
            return None

    def subscribe(self, channel):
        try:
            if self.ping():
                self.subscriber = self.cache.pubsub()
                self.subscriber.subscribe([channel])
                self.subscribed = True
            return False
        except Exception as ex:
            return False

    def unsubscribe(self, channel):
        try:
            if self.ping():
                return self.subscriber.unsubscribe([channel])
            return None
        except Exception as ex:
            return None

    def publish(self, channel, message):
        try:
            if self.ping():
                return self.cache.publish(channel, message)
            return None
        except Exception as ex:
            return None

    @abc.abstractmethod
    def listen(self, channel):
        pass

class Cache(CachePrototype):
    def __init__(self, settings):
        super(Cache, self).__init__(settings)

    def listen(self, channel):
        pass

class Queue(CachePrototype):
    def __init__(self, settings):
        super(Queue, self).__init__(settings)

    def listen(self, channel):
        pass

class Stats(CachePrototype):
    def __init__(self, settings):
        super(Stats, self).__init__(settings)

    def listen(self, channel):
        pass