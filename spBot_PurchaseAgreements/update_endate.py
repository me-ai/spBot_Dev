import time
import pandas
from spBot_Core.BotLogin import set_site, login, browser
from spBot_Core.secrets import bot1, bot2, bot3, bot4, bot5, bot6, password


def find_vpa(target):
    browser.get('https://sysco.sprocketcmms.com/Default.aspx?screen=Vendor%20Purchase%20Agreements')
    target_vpa = browser.find_element_by_link_text(target)
    target_vpa.click()


def update_vendor(vendor_id):
    vendor_field = browser.find_element_by_id('StdSf580_VendorID_txt')
    vendor_field.clear()
    vendor_field.send_keys(vendor_id)


def update_vpa_start_date(target_date):
    end_date_field = browser.find_element_by_id('StdSf580_StartDate_txt')
    end_date_field.clear()
    end_date_field.send_keys(target_date)


def save_vpa():
    browser.find_element_by_link_text('Save').click()
    time.sleep(1)
    browser.find_element_by_link_text('Exit').click()


target_file = 'update_vpa.csv'
col_names = ['target_site', 'target_suvc']
data = pandas.read_csv(target_file, names=col_names)
target_site = data.target_site.tolist()
target_suvc = data.target_suvc.tolist()

target_vpa = [
    'NAAN', 'Interstate Battery MPA'
]


target_date = '08/21/2020'

counter = len(target_site)
x = 0
login(bot1, password)
while x <= counter:
    try:
        x += 1
        set_site(target_site[x])
        find_vpa(target_vpa[1])
        update_vendor(target_suvc[x])
        update_vpa_start_date(target_date)
        save_vpa()
        print('{} {} update to {}'.format(target_site[x], target_vpa[1], target_suvc[x]))
    except IndexError:
        print('Script Complete')
    except Exception as c:
        continue
browser.quit()
