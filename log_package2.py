#-*- coding: utf-8 -*-
import logging
from colorlog import ColoredFormatter



def log_setting(log):
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)

    fh = logging.FileHandler(filename="test05_2.log")
    fh.setLevel(logging.DEBUG)

    formatter = ColoredFormatter(
        "%(log_color)s[%(asctime)s] %(message)s",
        datefmt=None,
        reset=True,
        log_colors={
            'DEBUG':    'cyan',
            'INFO':     'white,bold',
            'INFOV':    'cyan,bold',
            'WARNING':  'yellow',
            'ERROR':    'red,bold',
            'CRITICAL': 'red,bg_white',
        },
        secondary_log_colors={},
        style='%'
    )
    ch.setFormatter(formatter)

    logger = log.getLogger('attcap')
    logger.setLevel(logging.DEBUG)
    logger.handlers = []       # No duplicated handlers
    logger.propagate = False   # workaround for duplicated logs in ipython


    logger.addHandler(ch)
    logger.addHandler(fh)
    return logger

