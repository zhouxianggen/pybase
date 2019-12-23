# coding: utf8 
import json
import logging
from datetime import date, datetime


class BaseObject(object):
    def __init__(self, log_name='', log_level=logging.DEBUG):
        self.log = logging.getLogger(log_name or self.__class__.__name__)
        self.log.setLevel(log_level)
        self.log.propagate = False
        if not self.log.handlers:
            fmt = ('[%(name)-15s %(thread)-18d '
                    '%(levelname)-8s %(asctime)s] %(message)s')
            handler = logging.StreamHandler()
            handler.setFormatter(logging.Formatter(fmt))
            self.log.addHandler(handler)
        self.initialized = False


class JsonEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, date):
            return obj.strftime('%Y-%m-%d')
        elif isinstance(obj, bytes):
            return obj.decode('utf8')
        else:
            return json.JSONEncoder.default(self, obj)

