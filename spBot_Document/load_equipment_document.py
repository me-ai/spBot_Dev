import time
import pandas
from spBot_Core.BotLogin import set_site, login, browser
from spBot_Core.secrets import bot1, bot2, bot3, bot4, bot5, bot6, password
from selenium.webdriver.support.select import Select

login(bot1, password)
browser.implicitly_wait(30)
target_file = 'docs_to_load.csv'
col_names = ['unit', 'target_site', "target_url"]
data = pandas.read_csv(target_file, names=col_names)

unit = data.unit.tolist()
target_site = data.target_site.tolist()
target_url = data.target_url.tolist()

counter = len(unit)
x = 0

while x <= counter:
    try:
        x += 1
        set_site(target_site[x])
        target_inspection = \
            'https://sysco.sprocketcmms.com/Default.aspx?screen=Perform%20Inspection&ID=43575&InstanceName=43575'
        browser.get(target_inspection)
        question_equipment_id = browser.find_element_by_id('question_4880706')
        question_equipment_id.send_keys(unit[x])
    except:
        break


