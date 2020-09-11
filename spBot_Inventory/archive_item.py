from spBot_Core.BotLogin import login, set_site, password, bot1, bot2, browser
import pandas
import time


def archive_item(inventoryItemId):
    browser.implicitly_wait(60)
    base_url = 'https://sysco.sprocketcmms.com/Default.aspx?screen=Inventory%20Item&InstanceName='
    target_item_url = '{}{}'.format(base_url, inventoryItemId)
    browser.get(target_item_url)
    time.sleep(5)
    archive_chk_box = browser.find_element_by_id('StdSf12_Archived_chk')
    archive_chk_box.click()
    save_archive = browser.find_element_by_id('liSave')
    save_archive.click()
    time.sleep(5)
    browser.find_element_by_id('liExit').click()
    time.sleep(5)


target_file = 'records_to_archive.csv'
col_names = ['target_inventory_id']
data = pandas.read_csv(target_file, names=col_names)

target_inventory_item = data.target_inventory_id.tolist()

counter = len(target_inventory_item)
x = 0
login(bot1, password)
set_site('Global Site Code')
while x <= counter:
    try:
        x += 1
        print('Starting {} of {}'.format(x, counter))
        archive_item(target_inventory_item[x])
        print('{} archived'.format(target_inventory_item[x]))

    except IndexError:
        print('Script Complete')
        break
    except Exception as b:
        print('Error!\n{}\n{}'.format(target_inventory_item[x], b))
        continue


browser.close()
