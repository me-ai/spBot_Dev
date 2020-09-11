from spBot_Core.BotLogin import login, set_site, password, bot1, bot2, browser
import pandas
import time

target_file = 'targets_to_clear_oos.csv'
col_names = ['unit', 'target_site']
data = pandas.read_csv(target_file, names=col_names)

# Store entries in list for variables
unit = data.unit.tolist()
target_site = data.target_site.tolist()


def search_equip(unit):
    browser.get('https://sysco.sprocketcmms.com/Default.aspx?screen=Equipment&SSF=-102')
    equip_search = browser.find_element_by_id('liSearch')
    equip_search.click()
    equip_field = browser.find_element_by_id('Equipment_txt4')
    equip_field.clear()
    equip_field.send_keys(unit)
    submit_button = browser.find_element_by_id('SearchScreenBtnSearch')
    submit_button.click()
    time.sleep(1)


def clear_oos_field(unit):
    unit_link = browser.find_element_by_link_text(unit)
    unit_link.click()
    time.sleep(1)
    date_oos_field = browser.find_element_by_id('StdSf_70_DateOutOfService_txt')
    date_oos_field.clear()
    save_change = browser.find_element_by_link_text('Save')
    save_change.click()
    time.sleep(3)
    exit_record = browser.find_element_by_link_text('Exit')
    exit_record.click()
    time.sleep(3)


browser.implicitly_wait(15)
login(bot1, password)
counter = len(unit)
x = 0
while x <= counter:
    try:
        x += 1
        set_site(target_site[x])
        print('{} of {}\nUnit-{}\nSiteCode-{}'.format(x, counter, unit[x], target_site[x]))
        set_site(target_site[x])
        search_equip(unit[x])
        clear_oos_field(unit[x])
        print('Success!----->\n         Moving to Next----->')

    except IndexError:
        print('Script Complete!')
        break
    except Exception as b:
        print('!!!Error!!!\nEquipment {} @ Site {}\n{}'.format(unit[x], target_site[x], b))
        try:
            browser.switch_to.alert.accept()
            browser.get('https://sysco.sprocketcmms.com/Default.aspx?screen=Equipment&SSF=-102')
            continue
        except Exception as c:
            print('Bad Equipment Data Import -------> GasBoy Type Or Date In Service Missing')
            continue

browser.quit()
