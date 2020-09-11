import time
import pandas
from spBot_Core.BotLogin import set_site, login, browser
from spBot_Core.secrets import bot1, bot2, bot3, bot4, bot5, bot6, password

# Set Driver
browser.implicitly_wait(15)

# Bot Login
login(bot2, password)

# Read csv and set variables

# Parse .csv
colnames = ['site', 'unit', 'start']
data = pandas.read_csv('AttachWarranty.csv', names=colnames)

# Store entries in list for variables
site = data.site.tolist()
unit = data.unit.tolist()
start = data.start.tolist()

# Parse .csv
colnames = ['option', 'length']
data = pandas.read_csv('WarrantyOption.csv', names=colnames)

# Store entries in list for variables
option = data.option.tolist()
length = data.length.tolist()

# Set csv counters by list length
counter = len(unit)
counter2 = len(option)
x = 0

while x <= counter:

    x = x + 1
    y = 0

    # Switch Sites
    set_site(site[x])
    # Find and select Equipment
    browser.get('https://sysco.sprocketcmms.com/Default.aspx?screen=Equipment&SSF=-102')
    searchField = browser.find_element_by_link_text('Search')
    searchField.click()
    equipSearch = browser.find_element_by_id('Equipment_txt4')
    equipSearch.clear()
    equipSearch.send_keys(unit[x])
    searchButton = browser.find_element_by_id('SearchScreenBtnSearch')
    searchButton.click()
    time.sleep(5)
    unitLink = browser.find_element_by_link_text((unit[x]))
    unitLink.click()

    # Create Warranties
    # Warranty Option Loop
    while y <= counter2:
        try:
            y = y + 1
            warTab = browser.find_element_by_link_text('Warranty')
            warTab.click()
            warLink = browser.find_element_by_id('newWarranty_anchor')
            warLink.click()
            warName = browser.find_element_by_id('newWarranty_WarrantyID')
            warName.send_keys(option[y])
            warStart = browser.find_element_by_id('newWarranty_StartDate')
            warStart.clear()
            warStart.send_keys(start[x])
            # time.sleep(1)
            warEnd = browser.find_element_by_id('newWarranty_EndDate')
            warEnd.clear()
            warEnd.send_keys(length[y])
            # time.sleep(1)
            warSave = browser.find_element_by_id('newWarranty_save')
            warSave.click()
            time.sleep(3)
            # warCancel = browser.find_element_by_id('newWarranty_cancel')
            # warCancel.click()
        except IndexError:
            break
        except Exception as b:
            print('______Error_______\n{}'.format(b))
            continue


    # Log Success
    file = open('LogFile_bot1.txt', 'a')
    file.write(unit[x] + ' Bot 1 warranty attached\n')
    file.close()

browser.quit()
