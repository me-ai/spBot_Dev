from spBot_Core.BotLogin import browser, login, bot1, password, set_site
import time
from selenium.webdriver.support.select import Select
import pandas


"""
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
"""


def gen_number(
        unit_description,
        location,
        equipment_type,
        department,
        manufacturer,
        inventory_number,
        start_date,
        gb_fuel_type,
        equipment_system):

    browser.get('https://sysco.sprocketcmms.com/Default.aspx?screen=Equipment&SSF=-102')
    time.sleep(1)
    new_equip_button = browser.find_element_by_id('btnNewLink')
    new_equip_button.click()

    field_id = browser.find_element_by_id('StdSf_70_EquipmentIdentifier_txt')
    field_id.send_keys('AUTONUMBER')

    desc_field = browser.find_element_by_id('StdSf_70_Description_txt')
    desc_field.send_keys(unit_description)

    location_field = browser.find_element_by_id('StdSf_70_LocationID_txt')
    location_field.send_keys(location)

    type_field = browser.find_element_by_id('StdSf_70_EquipmentTypeID_txt')
    type_field.send_keys(equipment_type)

    dept_field = browser.find_element_by_xpath('//*[@id="StdSf_70_Div1"]/p[8]/div/input')
    dept_field.send_keys(department)

    man_field = browser.find_element_by_id('StdSf_70_Manufacturer_txt')
    man_field.send_keys(manufacturer)

    inv_field = browser.find_element_by_id('StdSf_70_InventoryNumber_txt')
    inv_field.send_keys(inventory_number)

    start_date_field = browser.find_element_by_id('StdSf_70_DateInService_txt')
    start_date_field.send_keys(start_date)

    gb_type_field = browser.find_element_by_xpath('//*[@id="StdSf_70_Div3"]/p[12]/div/input')
    gb_type_field.send_keys(gb_fuel_type)

    equip_sys_field = browser.find_element_by_id('StdSf_70_EquipmentSystemID_txt')
    equip_sys_field.send_keys(equipment_system)

    browser.find_element_by_link_text('Save').click()
    time.sleep(3)


browser.quit()
