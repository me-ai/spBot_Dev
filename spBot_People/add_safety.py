import time
from spBot_Core.BotLogin import set_site, login, browser
from spBot_Core.secrets import bot1, bot2, bot3, bot4, bot5, bot6, password
from selenium.webdriver.support.select import Select
import pandas


def add_safety(target_user, a):
    browser.implicitly_wait(10)
    browser.get('https://sysco.sprocketcmms.com/Default.aspx?screen=People&SSF=-134')
    search_box = browser.find_element_by_link_text('Search')
    search_box.click()
    user_name_field = browser.find_element_by_id('UserName_txt0')
    user_name_field.clear()
    user_name_field.send_keys(target_user)
    start_search = browser.find_element_by_id('SearchScreenBtnSearch')
    start_search.click()
    browser.find_element_by_link_text(target_user).click()
    time.sleep(3)

    if int(a) == 1:
        print('Flagging OverrideWorkDay')
        ignore_wdt = browser.find_element_by_id('StdSf_62_OverrideWorkDay_chk')
        ignore_wdt.click()

    groups_tab = browser.find_element_by_id('liGroups')
    time.sleep(3)
    groups_tab.click()
    add_group = browser.find_element_by_id('txt_Group')
    add_group.send_keys('Data-FSY')
    submit_group = browser.find_element_by_xpath('//*[@id="divGroups"]/table/tbody/tr[1]/td[2]/input[2]')
    submit_group.click()
    time.sleep(1)
    save_exit = browser.find_element_by_link_text('Save')
    save_exit.click()
    time.sleep(3)
    browser.switch_to.alert.accept()


def page_final(unit):
    # Log Success
    file = open('log.txt', 'a')
    file.write('{} Success\n'.format(unit))
    file.close()


def page_error(unit):
    file = open('ErrorLog.txt', 'a')
    file.write('{} error\n'.format(unit))
    file.close()


target_file = 'add_user_group.csv'
col_names = ['target_user', 'target_site', 'override_workday']
data = pandas.read_csv(target_file, names=col_names)
target_user = data.target_user.tolist()
target_site = data.target_site.tolist()
override_workday = data.override_workday.tolist()

counter = len(target_user)
x = 0
browser.implicitly_wait(15)
login(bot2, password)
set_site('Global Site Code')

while x <= counter:
    try:
        x = x + 1
        print('Starting {} of {}'.format(x, (counter - 1)))
        add_safety(target_user[x], override_workday[x])
        page_final(target_user[x])
        print('---> User {} updated.'.format(target_user[x]))

    except IndexError:
        print('Script complete!!')
        break

    except Exception as b:
        try:
            browser.switch_to.alert.accept()
            print('Extra Popup resolved')
            continue
        except Exception as c:
            print('----->Popup cannot be resolved\n{}'.format(c))
            print(b)
            page_error(target_user[x])
            continue


browser.quit()
