import time
import pandas
from spBot_Core.BotLogin import set_site, login, browser
from spBot_Core.secrets import bot1, bot2, bot3, bot4, bot5, bot6, password
from selenium.webdriver.support.select import Select
# target_site = ['X9X', 'X9X']
target_item_list = 'target_item_price_update_list.csv'
col_names = ['inventory_id', 'price',  'vpa_target']
data = pandas.read_csv(target_item_list, names=col_names)
inventory_id = data.inventory_id.tolist()
price = data.price.tolist()
vpa_target = data.vpa_target.tolist()

target_sites_list = 'target_sites_list.csv'
col_names_sites = ['target_site']
data1 = pandas.read_csv(target_sites_list, names=col_names_sites)
target_site = data1.target_site.tolist()


def update_item_price(target_agreement, item_id, item_price,):
    browser.get('https://sysco.sprocketcmms.com/Default.aspx?screen=Vendor%20Purchase%20Agreements')
    parent_vpa = browser.find_element_by_link_text(target_agreement)
    parent_vpa.click()
    items_tab = browser .find_element_by_id('liItems')
    items_tab.click()
    search_id = browser.find_element_by_id('ajaxReport_itemsReport_promptsdivContainer_0_input')
    search_id.clear()
    search_id.send_keys(item_id)
    id_search_button = browser.find_element_by_xpath('/html/body/form/div[3]/div[3]/div[2]/div/div[2]/div/div[1]/input')
    id_search_button.click()
    time.sleep(1)
    get_edit = browser.find_element_by_link_text('Edit')
    get_edit.click()
    price_field = browser.find_element_by_id('StdSf581_Price_txt')
    price_field.clear()
    price_field.send_keys(item_price)
    save_button = browser.find_element_by_xpath('/html/body/form/div[3]/div[3]/div[3]/div[3]/input[1]')
    save_button.click()
    time.sleep(1)
    print('VPA {} item {} price updated to {}'.format(target_agreement, item_id, item_price))


login(bot1, password)
x = 0
counter = len(target_site)
while x <= counter:
    try:
        x += 1
        set_site(target_site[x])
        print('------> Starting Site {}'.format(target_site[x]))
        y = 0
        y_counter = len(inventory_id)
        while y <= y_counter:
            try:
                y += 1
                update_item_price(
                    vpa_target[y],
                    inventory_id[y],
                    price[y]
                )
            except IndexError:
                print('------> All items added at {}'.format(target_site[x]))
                break
            except Exception as b:
                print('{} error!'.format(inventory_id[y]))
                continue
    except IndexError:
        print('Script Complete!')
        break
    except Exception as c:
        print('Site Code Error {}'.format(target_site[x]))
        continue

browser.quit()
