import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from config.settings import Settings
from base.cache import Cache

cache = Cache(settings=Settings.cache)

print(cache.ping())
print(cache.set('test', 'test'))
print(cache.get('test'))
print(cache.push('test2', [1,2,3]))
print(cache.pop('test2'))