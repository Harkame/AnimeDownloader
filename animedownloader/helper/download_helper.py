import settings.settings as settings

from bs4 import BeautifulSoup
import os
from tqdm import tqdm
import sys

from urllib.parse import urlparse

JETANIME_URL = 'https://www.jetanime.co'

import requests

def download_anime(browser, anime):
    session = requests.Session()

    response = session.get(anime)

    animes_page = BeautifulSoup(response.content, features='lxml')

    episodes = animes_page.find('div', {'class': 'items'}).find_all('a');

    for episode in episodes:
        reference = JETANIME_URL + episode['href']

        browser.get(reference)

        video_tag = browser.find_elements_by_css_selector('iframe')[0].get_attribute('href')

        print(video_tag)
        print('toto')
