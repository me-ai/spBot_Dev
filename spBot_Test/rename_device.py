from spBot_Core.BotLogin import login, set_site, password, bot1, bot2, browser
import pandas
import time


target_file = 'device_to_change.csv'
col_names = ['old', 'target_site', 'new']
data = pandas.read_csv(target_file, names=col_names)

# Store entries in list for variables

old = data.old.tolist()
target_site = data.target_site.tolist()
new = data.new.tolist()


def device_search(old_value):
    browser.get('https://sysco.sprocketcmms.com/Default.aspx?screen=Devices')
    search_button = browser.find_element_by_id('liSearch')
    search_button.click()
    device_id_search_field = browser.find_element_by_id('Device_Identifier_txt0')
    device_id_search_field.clear()
    device_id_search_field.send_keys(old_value)
    start_search = browser.find_element_by_id('SearchScreenBtnSearch')
    start_search.click()
    time.sleep(1)
    record_link = browser.find_element_by_link_text(old_value)
    record_link.click()
    time.sleep(1)


def correct_device_id(new_value, old_value):
    device_id_field = browser.find_element_by_id('StdSf45_DeviceIdentifier_txt')
    device_id_field.clear()
    device_id_field.send_keys(new_value)
    save_record = browser.find_element_by_id('liSave')
    save_record.click()
    time.sleep(1)
    print('{} updated to {}'.format(old_value, new_value))


counter = len(old)
x = 0
login(bot2, password)
set_site(target_site[1])
while x <= counter:
    try:
        x += 1
        device_search(old[x])
        correct_device_id(new[x], old[x])
    except IndexError:
        print('Device IDs corrected\nScript Complete')
        break
    except Exception as b:
        print('Error\n----> Moving to Next')
        continue

browser.quit()