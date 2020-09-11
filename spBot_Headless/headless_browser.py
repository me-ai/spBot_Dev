import os
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import time
from spBot_Core.secrets import bot1, bot2, bot3, bot4, bot5, bot6, password, binaries

set_options = Options()
set_options.add_argument("--headless")
set_options.add_argument("--window-size=1920x1080")
#browser = webdriver.Chrome(binaries)
browser = webdriver.Chrome(binaries, options=set_options)
browser.implicitly_wait(30)

class BotLogin:
    def __init__(self, uname, pword):
        self.uname = uname
        self.pword = pword


def login(uname, pword, www='https://sysco.sprocketcmms.com/Default.aspx'):
    browser.get(www)
    alt_log = browser.find_element_by_id('btnSprocketLogin')
    alt_log.click()
    username = browser.find_element_by_id('ctl00_ContentPlaceHolder1_txtUserName')
    username.send_keys(uname)
    enter_password = browser.find_element_by_id('ctl00_ContentPlaceHolder1_txtPassword')
    enter_password.send_keys(pword)
    main_log = browser.find_element_by_id('ctl00_ContentPlaceHolder1_btnLogin')
    main_log.click()


def set_site(site):
    change_site = browser.find_element_by_xpath('//*[@id="menuDiv"]/div[3]/div[2]/div/input')
    change_site.send_keys(u'\ue009' + 'a')
    change_site.send_keys(u'\ue017')
    time.sleep(1)
    change_site.send_keys(site)
    time.sleep(1)
    change_site.send_keys(u'\ue00f')
    change_site.send_keys(u'\ue007')
    time.sleep(5)


# Example Usage
#login(bot2, password)
#set_site(site='000')
#browser.get_screenshot_as_file("capture.png")
#time.sleep(10)
#browser.quit()