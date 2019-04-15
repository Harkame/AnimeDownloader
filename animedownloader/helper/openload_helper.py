import os,sys
import requests
import time
from selenium import webdriver
from tqdm import tqdm
from docopt import docopt

def extract_video_source(browser, url):
    browser.get(url)
    browser.execute_script("$('#videooverlay')[0].click();")
    time.sleep(1)
    browser.execute_script("$('.vjs-big-play-button')[0].click();")
    time.sleep(1)

    video_tag = browser.find_element_by_id('olvideo_html5_api')

    video_source = video.get_attribute('src')

    return video_source
