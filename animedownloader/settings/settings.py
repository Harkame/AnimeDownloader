from helper.argument_helper import get_arguments
from helper.config_helper import get_config

import logging
import os
import sys

DEFAULT_CONFIG_FILE = os.path.join('.', 'config.yml')
DEFAULT_DESTINATION_PATH = os.path.join('.', 'mangas')
DEFAULT_MANGA_FORMAT = 'jpg'

logger = logging.getLogger()
config_file = None
destination_path = None

browser = None

mangas = []

def init(arguments):
    global logger

    global config_file
    global destination_path

    global mangas

    global browser

    config_file = DEFAULT_CONFIG_FILE

    init_arguments(arguments)

    init_config()

def init_arguments(arguments):
    global logger

    global config_file
    global destination_path

    global mangas

    global browser

    arguments = get_arguments(arguments)

    if arguments.verbose:
        logger.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s :: %(levelname)s :: %(module)s :: %(lineno)s :: %(funcName)s :: %(message)s')
        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(formatter)

        if arguments.verbose == 0:
            logger.setLevel(logging.NOTSET)
        elif arguments.verbose == 1:
            logger.setLevel(logging.DEBUG)
        elif arguments.verbose == 2:
            logger.setLevel(logging.INFO)
        elif arguments.verbose == 3:
            logger.setLevel(logging.WARNING)
        elif arguments.verbose == 4:
            logger.setLevel(logging.ERROR)
        elif arguments.verbose == 5:
            logger.setLevel(logging.CRITICAL)

        logger.addHandler(stream_handler)

    if arguments.config_file:
        config_file = arguments.config_file

    if arguments.destination_path:
        destination_path = arguments.destination_path

    if arguments.chrome:
        chrome_opt=webdriver.ChromeOptions()
        chrome_opt.add_argument('--headless')
        browser=webdriver.Chrome(chrome_options=chrome_opt)
    else:
        fox_opt=webdriver.FirefoxOptions()
        fox_opt.add_argument('--headless')
        browser=webdriver.Firefox(firefox_options=fox_opt)

def init_config():
    global logger

    global destination_path

    global animes

    config = get_config(config_file)

    if config['animes'] is not None:
        mangas.extend(config['animes'])

    if destination_path is None:
        if config['destination_path'] is not None:
            destination_path = config['destination_path']
        else:
            destination_path = DEFAULT_DESTINATION_PATH
