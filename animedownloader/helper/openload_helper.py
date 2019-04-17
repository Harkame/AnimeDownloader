import os,sys
import requests
import time
from selenium import webdriver
from tqdm import tqdm
from docopt import docopt
from bs4 import BeautifulSoup

def extract_video_source(browser, url):
    browser.get(url)
    browser.execute_script("$('#videooverlay')[0].click();")
    time.sleep(1)
    browser.execute_script("$('.vjs-big-play-button')[0].click();")
    time.sleep(1)

    anime_page = BeautifulSoup(browser.page_source, features='lxml')
    
    video_tag = browser.find('div', {'id' :'olvideo_html5_api'})

    video_source = video_tag['src']

    return video_source
