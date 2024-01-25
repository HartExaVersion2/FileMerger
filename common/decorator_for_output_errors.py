import logging
import os
import inspect
from common.errors import *


def decorator_for_output_errors():
    def decorator(base_function):
        def wrapper(*args, **kwargs):
            try:
                return base_function(*args, **kwargs)
            except Exception as e:
                logging.error('Function {}, Error {}, Path {}'.format(base_function.__name__, e, os.path.abspath(inspect.getfile(base_function))))

        return wrapper
    return decorator