import time
import pandas
from spBot_Core.BotLogin import set_site, login, browser
from spBot_Core.secrets import bot1, bot2, bot3, bot4, bot5, bot6, password
from selenium.webdriver.support.select import Select

target_item_list = 'target_item_list.csv'
col_names = ['inventory_id', 'price', 'purchase_status', 'vendor_part_number', 'vpa_target']
data = pandas.read_csv(target_item_list, names=col_names)
inventory_id = data.inventory_id.tolist()
price = data.price.tolist()
purchase_status = data.purchase_status.tolist()
vendor_part_number = data.vendor_part_number.tolist()
vpa_target = data.vpa_target.tolist()

target_sites_list = 'target_sites_list.csv'
col_names_sites = ['target_site']
data1 = pandas.read_csv(target_sites_list, names=col_names_sites)
target_site = data1.target_site.tolist()


def add_item(
        target_agreement,
        item_id,
        item_price,
        status,
        vendor_id
):
    browser.get('https://sysco.sprocketcmms.com/Default.aspx?screen=Perform%20Inspection&ID=43579&InstanceName=43579')
    target_vpa = browser.find_element_by_id('question_4881136')
    target_vpa.send_keys(target_agreement)
    product_id = browser.find_element_by_id('question_4881132')
    product_id.send_keys(item_id)
    price_field = browser.find_element_by_id('question_4881133')
    price_field.send_keys(item_price)
    purchase_status_field = browser.find_element_by_id('question_4881134')
    purchase_status_field.send_keys(status)
    vendor_id_field = browser.find_element_by_id('question_4881135')
    vendor_id_field.send_keys(vendor_id)
    is_true_field = browser.find_element_by_id('question_4881137')
    is_true_field.send_keys('TRUE')
    submit_btn = browser.find_element_by_id('ctl00_MainPage_PerformInspection_43579_submit')
    submit_btn.click()
    time.sleep(1)
    print('-----> {} added'.format(item_id))


login(bot1, password)
x = 0
counter = len(target_site)
while x <= counter:
    try:
        x += 1
        set_site(target_site[x])
        y = 0
        y_counter = len(inventory_id)
        while y <= y_counter:
            try:
                y += 1
                add_item(
                    vpa_target[y],
                    inventory_id[y],
                    price[y],
                    purchase_status[y],
                    vendor_part_number[y]
                )
            except IndexError:
                print('All items added at {}'.format(target_site[x]))
                break
            except Exception as b:
                print('{} error!')
                continue
    except IndexError:
        print('Script Complete!')
        break
    except Exception as c:
        print('Site Code Error {}'.format(target_site[x]))
        continue

browser.quit()
