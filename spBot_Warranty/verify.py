import requests
import lxml
import re
from bs4 import BeautifulSoup
import time
from spBot_Core.BotLogin import set_site, login, browser
from spBot_Core.secrets import bot1, bot2, bot3, bot4, bot5, bot6, password

login(bot2, password)
set_site('102')
page = browser.get('https://sysco.sprocketcmms.com/Default.aspx?screen=New%20Equipment&InstanceName=203069')
war_tab = browser.find_element_by_id('liWarranty')
war_tab.click()
time.sleep(3)
html = browser.page_source

soup = BeautifulSoup(html, 'lxml')
#war = soup.tbody.td.find_all_next(string=True)
war = soup.find(id='divWarranties')
#war_anchor = soup.find_all('tr', {'class': re.compile('evenRow')})

for i in war:
    children = i.findChildren('a', recursive=True)
    for child in children:
        info = child.text
        print(info)

#print(war)

browser.quit()
