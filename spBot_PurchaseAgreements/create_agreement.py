import time
import pandas
from spBot_Core.BotLogin import set_site, login, browser
from spBot_Core.secrets import bot1, bot2, bot3, bot4, bot5, bot6, password
from selenium.webdriver.support.select import Select
import datetime
login(bot1, password)

# target_site = ['X9X', 'X9X']
target_sites_list = 'target_sites_list.csv'
col_names_sites = ['target_site']
data1 = pandas.read_csv(target_sites_list, names=col_names_sites)
target_site = data1.target_site.tolist()

vpa_list = "vpa_list.csv"
col_names_vpa = ['Purchase_Agreement_Name', 'Description', 'VendorID', 'StartDate', 'EndDate']
data2 = pandas.read_csv(vpa_list, names=col_names_vpa)
Purchase_Agreement_Name = data2.Purchase_Agreement_Name.tolist()
Description = data2.Description.tolist()
VendorID = data2.VendorID.tolist()
StartDate = data2.StartDate.tolist()
EndDate = data2.EndDate.tolist()


def create_vpa(y, y_description, y_vendor_id, y_date, y_expire, PreferredVendor=1):
    browser.get('https://sysco.sprocketcmms.com/Default.aspx?screen=Vendor%20Purchase%20Agreements')
    vpa_new_button = browser.find_element_by_xpath('//*[@id="btnNewLink"]')
    time.sleep(1)
    vpa_new_button.click()
    name_field = browser.find_element_by_id('StdSf580_Name_txt')
    name_field.send_keys(y)
    description_field = browser.find_element_by_id('StdSf580_Description_txt')
    description_field.send_keys(y_description)
    vendor_id_field = browser.find_element_by_id('StdSf580_VendorID_txt')
    vendor_id_field.send_keys(y_vendor_id)
    start_date_field = browser.find_element_by_id('StdSf580_StartDate_txt')
    start_date_field.send_keys(y_date)
    end_date_field = browser.find_element_by_id('StdSf580_EndDate_txt')
    end_date_field.send_keys(y_expire)
    preferred_vendor_check = browser.find_element_by_id('StdSf580_PreferredVendor_chk')

    if PreferredVendor == 1:
        preferred_vendor_check.click()
        time.sleep(1)
        browser.find_element_by_link_text('Save').click()
        time.sleep(1)
        browser.find_element_by_link_text('Exit').click()
    else:
        browser.find_element_by_link_text('Save').click()
        time.sleep(1)
        browser.find_element_by_link_text('Exit').click()


x = 0
counter = len(target_site)
while x <= counter:
    try:
        x = x + 1
        set_site(target_site[x])
        vpa_counter = len(Purchase_Agreement_Name)
        y = 0
        while y <= vpa_counter:
            try:
                y = y + 1
                create_vpa(Purchase_Agreement_Name[y],
                           Description[y],
                           VendorID[y],
                           StartDate[y],
                           EndDate[y],
                           PreferredVendor=1
                           )
            except IndexError:
                print('Site {} all VPAs created'.format(target_site[x]))
                y = 0
                break

            except Exception as b:
                print('!!!Error site {}\nVPA\n{}'.format(target_site[x], b))
    except IndexError:
        print('Script Complete')
        break
    except Exception as a:
        print('!!!Error site {}\nVPA\n{}'.format(target_site[x], a))
        continue


browser.quit()
