from selenium import webdriver
from pyquery import PyQuery as pq
import re 
import time
from selenium.webdriver.chrome.options import Options
 


def words(search_key):

    def search(search_key):
        # options = Options()
        # options.add_argument('--headless')
        # options.add_argument('--no-sandbox')
        # bs = webdriver.Chrome(executable_path="/usr/bin/chromedriver",chrome_options=options)
        opt = webdriver.ChromeOptions()
        opt.set_headless()
        bs = webdriver.Chrome(options =opt)
        bs.get('http://fanyi.youdao.com/')
        input_info = bs.find_element_by_id('inputOriginal')
        input_info.send_keys(search_key)
        time.sleep(2)
        button = bs.find_element_by_id('transMachine')
        button.click()
        return bs



    def send_results(bs):
        doc = pq(bs.page_source)
        context = doc('.no-link').items()
        result = []
        for i in context:
            result.append(i.text())
        return result


    bs = search(search_key)
    result = send_results(bs)
    bs.close()
    return result




def sentences(search_key):

    def search(search_key):
         # options = Options()
        # options.add_argument('--headless')
        # options.add_argument('--no-sandbox')
        # bs = webdriver.Chrome(executable_path="/usr/bin/chromedriver",chrome_options=options)
        opt = webdriver.ChromeOptions()
        opt.set_headless()
        bs = webdriver.Chrome(options =opt)
        bs.get('http://fanyi.youdao.com/')
        input_info = bs.find_element_by_id('inputOriginal')
        input_info.send_keys(search_key)
        time.sleep(2)
        button = bs.find_element_by_id('transMachine')
        button.click()
        time.sleep(0.1)
        know = bs.find_element_by_class_name('i-know')
        know.click()
        return bs



    def send_results(bs):
        doc = pq(bs.page_source)
        context = doc('#transTarget').items()
        result = []
        for i in context:
            result.append(i.text())
        return result


    bs = search(search_key)
    result = send_results(bs)
    bs.close()
    return result
