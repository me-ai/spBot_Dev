import time
from spBot_Core.BotLogin import set_site, login, browser
from spBot_Core.secrets import bot1, bot2, bot3, bot4, bot5, bot6, password
from selenium.webdriver.support.select import Select
from selenium.webdriver import ActionChains
import pyautogui
import pandas

actionChains = ActionChains(browser)


def find_main(main_target):
    browser.get('https://sysco.sprocketcmms.com/Default.aspx?screen=Inspection%20Manager')
    search_box = browser.find_element_by_id('liSearch')
    search_box.click()
    search_by_name = browser.find_element_by_id('Inspection_Name_txt1')
    search_by_name.clear()
    search_by_name.send_keys(main_target)
    submit_search = browser.find_element_by_id('SearchScreenBtnSearch')
    submit_search.click()
    time.sleep(2)


def clone_main():
    time.sleep(1)
    clone_it = browser.find_element_by_xpath('//*[@id="ctl00_MainPage_Search2_resultsGrid_ctl00__0"]/td[11]/a')
    clone_it.click()
    print('Inspection cloned')
    time.sleep(1)


def find_clone(clone_target):
    time.sleep(1)
    find_main(clone_target)
    time.sleep(1)


def flip_clone(new_name):
    edit_clone = browser.find_element_by_xpath('//*[@id="ctl00_MainPage_Search2_resultsGrid_ctl00__0"]/td[7]/a')
    edit_clone.click()

    pyautogui.moveTo(537, 250, duration=1)
    pyautogui.rightClick()
    pyautogui.moveTo(538, 251, duration=1)
    pyautogui.leftClick()
    time.sleep(1)

    clone_name = browser.find_element_by_xpath('/html/body/form/div[7]/div[2]/div/table/tbody/tr[2]/td[2]/input')
    clone_name.clear()
    clone_name.send_keys(new_name)
    clone_description = browser.find_element_by_xpath('/html/body/form/div[7]/div[2]/div/table/tbody/tr[3]/td[2]/input')
    clone_description.clear()
    clone_description.send_keys(new_name)
    save_clone_update = browser.find_element_by_xpath('/html/body/form/div[7]/div[2]/div/table/tbody/tr[5]/td[2]/input')
    save_clone_update.click()


target_item_list = 'target_clone.csv'
col_names = ['clone_name']
data = pandas.read_csv(target_item_list, names=col_names)
clone_name = data.clone_name.tolist()

browser.implicitly_wait(60)
login(bot1, password)
set_site('Global Site Code')

counter = len(clone_name)
x = 0

while x <= counter:
    main_to_target = 'TEST_CABL_FSI_Monthly Cooler v2 by Aisle MAIN'
    clone_to_target = 'TEST_CABL_FSI_Monthly Cooler v2 by Aisle MAIN Clone'
    try:
        x += 1
        print('{} of {}'.format(x, counter))
        time.sleep(1)
        find_main(main_to_target)
        time.sleep(1)
        clone_main()
        time.sleep(1)
        find_clone(clone_to_target)
        time.sleep(1)
        flip_clone(clone_name[x])
        time.sleep(1)
    except IndexError:
        print('Script Complete')
        break
    except Exception as b:
        print('Error {}\n{}'.format(clone_name[x], b))
        try:
            browser.switch_to.alert.accept()
        except Exception as c:
            print('Sprocket to slow.....2nd Catch error\n{}'.format(c))
            continue
        continue


