from spBot_Headless.headless_browser import login, set_site, password, bot1, browser
import pandas
import time

# Test script for creating FSI schedules

target_file = 'targets_to_flag.csv'
col_names = ['target_site', 'prod_id']
data = pandas.read_csv(target_file, names=col_names)

# Store entries in list for variables

target_site = data.target_site.tolist()
prod_id = data.prod_id.tolist()

counter = len(prod_id)
browser.implicitly_wait(30)

login(bot1, password)
set_site(target_site[1])

x = 0
while x <= counter:
    try:
        x = x + 1
        browser.get('https://sysco.sprocketcmms.com/Default.aspx?screen=Inventory%20Items&SSF=144')
        search_main = browser.find_element_by_id('liSearch')
        search_main.click()
        id_field = browser.find_element_by_id('Product_Identifier_txt0')
        id_field.clear()
        id_field.send_keys(prod_id[x])
        search_button = browser.find_element_by_id('SearchScreenBtnSearch')
        search_button.click()
        time.sleep(1)
        select_prod_id = browser.find_element_by_partial_link_text(prod_id[x])
        select_prod_id.click()
        time.sleep(1)
        change_tab = browser.find_element_by_xpath('//*[@id="liStorerooms"]')
        change_tab.click()
        critical_flag = browser.find_element_by_id('StdSf13_Critical_Item_chk')
        critical_flag.click()
        time.sleep(1)
        browser.find_element_by_link_text('Save').click()
        time.sleep(1)
        browser.find_element_by_link_text('Exit').click()
        time.sleep(1)
        print('{} flagged!'.format(prod_id[x]))


    except IndexError:
        print('Script Complete!')
        break
    except Exception as b:
        print('----> {} Error!'.format(prod_id[x]))
        continue

browser.quit()
