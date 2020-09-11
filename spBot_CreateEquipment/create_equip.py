import sys

from selenium.webdriver import ActionChains
from spBot_Core.BotLogin import browser, login, bot1, password, set_site
import time
from selenium.webdriver.support.select import Select
import pandas

login(bot1, password)
browser.implicitly_wait(15)

# Parse .csv
file = 'target_equip.csv'
colNames = ['target_number', 'inv_number', 'equip_type', 'equip_sys', 'department', 'gb_fuel_type', 'make',
            'model', 'unit_descrip', 'vin_serial', 'start_date', 'status', 'location', 'site_code', 'const_year']
data = pandas.read_csv(file, names=colNames)

# Store entries in list for variables
target_number = data.target_number.tolist()
inv_number = data.inv_number.tolist()
equip_type = data.equip_type.tolist()
equip_sys = data.equip_sys.tolist()
department = data.department.tolist()
gb_fuel_type = data.gb_fuel_type.tolist()
make = data.make.tolist()
model = data.model.tolist()
unit_descrip = data.unit_descrip.tolist()
vin_serial = data.vin_serial.tolist()
start_date = data.start_date.tolist()
status = data.status.tolist()
location = data.location.tolist()
site_code = data.site_code.tolist()
const_year = data.const_year.tolist()

browser.get('https://sysco.sprocketcmms.com/Default.aspx?screen=Equipment')
set_site(site_code[1])

counter = len(target_number)
x = 0

while x <= counter:
    try:
        x = x + 1
        browser.get('https://sysco.sprocketcmms.com/Default.aspx?screen=Equipment')
        time.sleep(1)
        new_equip_button = browser.find_element_by_id('btnNewLink')
        new_equip_button.click()

        # Populate Form
        field_id = browser.find_element_by_id('StdSf_70_EquipmentIdentifier_txt')
        #field_id.clear()
        field_id.send_keys(target_number[x])
        desc_field = browser.find_element_by_id('StdSf_70_Description_txt')
        #desc_field.clear()
        desc_field.send_keys(unit_descrip[x])
        loc_field = browser.find_element_by_id('StdSf_70_LocationID_txt')
        #loc_field.clear()
        loc_field.send_keys(location[x])
        type_field = browser.find_element_by_id('StdSf_70_EquipmentTypeID_txt')
        #type_field.clear()
        type_field.send_keys(equip_type[x])
        dept_field = browser.find_element_by_xpath('//*[@id="StdSf_70_Div1"]/p[8]/div/input')
        dept_field.send_keys(department[x])
        man_field = browser.find_element_by_id('StdSf_70_Manufacturer_txt')
        #man_field.clear()
        man_field.send_keys(make[x])
        model_field = browser.find_element_by_id('StdSf_70_ModelNumber_txt')
        #model_field.clear()
        model_field.send_keys(model[x])
        vin_field = browser.find_element_by_id('StdSf_70_SerialNumber_txt')
        #vin_field.clear()
        vin_field.send_keys(vin_serial[x])
        inv_field = browser.find_element_by_id('StdSf_70_InventoryNumber_txt')
        #inv_field.clear()
        inv_field.send_keys(inv_number[x])
        const_year_field = browser.find_element_by_id('StdSf_70_ConstructionYear_txt')
        #const_year_field.clear()
        const_year_field.send_keys(const_year[x])
        start_date_field = browser.find_element_by_id('StdSf_70_DateInService_txt')
        start_date_field.send_keys(start_date[x])
        #status_field =browser.find_element_by_id('StdSf_70_EquipmentStatusID_txt')
        #status_field.clear()
        #status_field.send_keys(status[x])
        #gb_type_field = Select(browser.find_element_by_xpath('//*[@id="StdSf_70_Div3"]/p[12]/div/input'))
        #gb_type_field.select_by_visible_text(gb_fuel_type[x])
        gb_type_field = browser.find_element_by_xpath('//*[@id="StdSf_70_Div3"]/p[12]/div/input')
        gb_type_field.send_keys(gb_fuel_type[x])
        equip_sys_field = browser.find_element_by_id('StdSf_70_EquipmentSystemID_txt')
        #equip_sys_field.clear()
        equip_sys_field.send_keys(equip_sys[x])
        browser.find_element_by_link_text('Save').click()
        time.sleep(3)

    except IndexError:
        print('Complete!')
        break

    except Exception as b:
        tb = sys.exc_info()[2]
        print(tb.tb_lineno)
        print('____ERROR_____\nScript was at Equip ID {} at {} of {}\n____Reason____\n{}'.format(target_number[x], x,
                                                                                                 counter, b))
        try:
           """ browser.switch_to.alert.accept()
            #alert.dismiss()
            print('Accepting Alert and returning to Equipment Page')
            time.sleep(1)
            browser.get('https://sysco.sprocketcmms.com/Default.aspx?screen=Equipment')
            continue"""

        except Exception as a:
            print(a)
            break

browser.quit()
