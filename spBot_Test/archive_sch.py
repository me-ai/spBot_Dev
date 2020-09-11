from spBot_Core.BotLogin import login, set_site, password, bot1, browser
import pandas
import time

target_file = 'targets_to_archive.csv'
col_names = ['unit', 'target_site']
data = pandas.read_csv(target_file, names=col_names)

# Store entries in list for variables

unit = data.unit.tolist()
target_site = data.target_site.tolist()

login(bot1, password)
counter = len(unit)
browser.implicitly_wait(30)
x = 0
set_site(target_site[x+1])
sch_type = 1 ## 0 = Equipment Based

while x <= counter:
    try:
        x += 1
        if sch_type == 0:
            browser.get('https://sysco.sprocketcmms.com/Default.aspx?screen=PM%20Projects&SSF=-108')
        else:
            browser.get('https://sysco.sprocketcmms.com/Default.aspx?screen=PM%20Projects&SSF=244')
        search_trigger = browser.find_element_by_id('liSearch').click()
        search_box = browser.find_element_by_id('PMNumber_txt3')
        search_box.clear()
        search_box.send_keys(unit[x])
        search_button = browser.find_element_by_id('SearchScreenBtnSearch')
        search_button.click()
        time.sleep(5)
        archive_link = browser.find_element_by_xpath('//*[@id="ctl00_MainPage_Search2_resultsGrid_ctl00__0"]/td[11]/a')
        archive_link.click()


    except IndexError:
        print('Script Complete!')
        break
    except Exception as b:
        print('Error----->\n{}'.format(b))
        continue

browser.quit()
