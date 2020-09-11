from selenium.webdriver import ActionChains

from spBot_Core.BotLogin import browser, login, bot1, password, set_site
import time
from selenium.webdriver.support.select import Select
import pandas

# Login
login(bot1, password)
browser.implicitly_wait(15)

# Parse .csv
file = 'FY21 Freight.csv'
colNames = ['site', 'model', 'freight', 'vendor']
data = pandas.read_csv(file, names=colNames)


# Store entries in list for variables
site = data.site.tolist()
model = data.model.tolist()
freight = data.freight.tolist()
vendor = data.vendor.tolist()


# Set iteration variables
x = 0
counter = len(site)

# Create Options Loop
while x <= counter:
    x = x + 1
    try:
        # Change Site
        set_site(site[x])
        name = '{} {} Freight'.format(site[x], model[x])

        # Open Page
        browser.get('https://sysco.sprocketcmms.com/Default.aspx?screen=Equipment%20Options')
        time.sleep(5)

        # Create Option
        browser.find_element_by_id('btnNewLink').click()
        browser.find_element_by_id('StdSf524_Name_txt').send_keys(name)
        browser.find_element_by_id('StdSf524_Description_txt').send_keys(name)
        browser.find_element_by_id('StdSf524_VendorID_txt').send_keys(vendor[x])
        time.sleep(1)
        browser.find_element_by_link_text('Save').click()
        time.sleep(3)
        browser.find_element_by_link_text('Exit').click()
        browser.get('https://sysco.sprocketcmms.com/Default.aspx?screen=Equipment%20Models')
        time.sleep(1)

        # Attach option to Model
        browser.find_element_by_id('liSearch').click()
        model_search = browser.find_element_by_id('Name_txt0')
        model_search.clear()
        model_search.send_keys(model[x])
        browser.find_element_by_id('SearchScreenBtnSearch').click()
        time.sleep(1)
        browser.find_element_by_link_text(model[x]).click()
        time.sleep(1)
        browser.find_element_by_link_text('Options').click()

        tree1 = '//*[@id="ctl00_MainPage_EquipmentBuilder_OptionsTree"]/ul/li/div/span[2]'
        # tree1 = '//div[@id='ctl00_MainPage_EquipmentBuilder_OptionsTree']/ul/li/div/div/div/div/input'
        tree2 = '//*[@id="ctl00_MainPage_EquipmentBuilder_OptionsTree"]/ul/li/div/div/div/div/input'
        holdChild = browser.find_element_by_xpath(tree1)
        addChild = browser.find_element_by_xpath(tree2)

        # Mouse over and click hidden element
        holdChild.click()
        action = ActionChains(browser)
        action.move_to_element(holdChild).click().perform()
        browser.execute_script("arguments[0].click();", addChild)

        # Attach Option
        # browser.switch_to.active_element()
        select1 = Select(browser.find_element_by_xpath('//*[@id="ObjectTableName"]'))
        select1.select_by_visible_text('Equipment Option')
        # findOPtion = browser.find_element_by_xpath('//*[@id="ObjectID_magnifier"]').click()
        chooseOption = browser.find_element_by_xpath('//*[@id="ObjectID"]')
        chooseOption.send_keys(name)
        select2 = Select(browser.find_element_by_xpath('//*[@id="OptionType"]'))
        select2.select_by_visible_text('Standard')
        browser.find_element_by_id('Price').click()
        browser.find_element_by_id('Price').send_keys(freight[x])
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="equipmentOptionNodeModal"]/p[5]/input[1]').click()
        time.sleep(2)
        browser.find_element_by_link_text('Save').click()
        browser.get('https://sysco.sprocketcmms.com/Default.aspx?screen=Equipment%20Options')


        # Write to Log File
        file = open('LogFile.txt', 'a')
        file.write('{} {} created\n'.format(site[x], model[x]))
        file.close()
        print('<--- !Success! {} {}'.format(site[x], model[x]))

    except IndexError:
        print('Script complete, {} created'.format(x))
        break

    except Exception as b:
        print('---> !Error! {} {}\n Moving to Next\n* {}'.format(site[x], model[x], b))
        file = open('ErrorFile.txt', 'a')
        file.write('{} {} created\n'.format(site[x], model[x]))
        file.close()
        continue

browser.quit()
