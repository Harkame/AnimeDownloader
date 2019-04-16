import settings.settings as settings

from bs4 import BeautifulSoup
import os
from tqdm import tqdm
import sys

import time

from urllib.parse import urlparse

JETANIME_URL = 'https://www.jetanime.co'

import requests

from helper.openload_helper import extract_video_source

def download_anime(browser, anime):
    session = requests.Session()

    response = session.get(anime)

    animes_page = BeautifulSoup(response.content, features='lxml')

    episodes = animes_page.find('div', {'class': 'items'}).find_all('a');

    for episode in episodes:
        reference = JETANIME_URL + episode['href']

        print(reference)

        browser.get(reference)

        time.sleep(1)

        anime_page = BeautifulSoup(browser.page_source, features='lxml')

        player = anime_page.find('iframe')

        src = player['src']

        print(src)

        video_stream = extract_video_source(browser, src)

        print(video_stream)
