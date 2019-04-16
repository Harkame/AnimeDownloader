from helper.config_helper import get_config
from helper.argument_helper import get_arguments
from helper.download_helper import download_anime

import settings.settings as settings

import cfscrape
import logging
import sys
import os

def main(arguments):
    settings.init(arguments)

    browser = settings.browser

    for anime in settings.animes:
        download_anime(browser, anime)

if __name__ == '__main__':
    main(sys.argv[1:])
