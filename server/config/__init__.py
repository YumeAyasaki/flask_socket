import os
import sys
import config.settings

APP_ENV = os.environ.get('APP_ENV', 'dev')
_current = getattr(sys.modules['config.settings'], '{0}Config'.format(APP_ENV.capitalize()))()

for atr in [f for f in dir(_current) if not '__' in f]:
    val = os.environ.get(atr, getattr(_current, atr))
    setattr(sys.modules[__name__], atr, val)

def as_dict():
    res = {}
    for atr in [f for f in dir(sys.modules[__name__]) if not '__' in f]:
        val = getattr(config, atr)
        res[atr] = val
    return res