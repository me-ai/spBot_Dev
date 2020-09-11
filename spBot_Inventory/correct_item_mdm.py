from spBot_Core.BotLogin import login, set_site, password, bot1, bot2, browser
import pandas
import time
from selenium.webdriver.support.select import Select
"""
target_file = 'records_to_correct.csv'
col_names = [
    'inventory_id',
    'oem_number',
    'sds_value',
    'serialized_value',
    'warranty_value',
    'warranty_days',
    'warranty_hours',
    'base_uom'
]
data = pandas.read_csv(target_file, names=col_names)

# Store entries in list for variables
inventory_id = data.inventory_id.tolist()
oem_number = data.oem_number.tolist()
sds_value = data.sds_value.tolist()
serialized_value = data.serialized_value.tolist()
warranty_value = data.warranty_value.tolist()
warranty_days = data.warranty_days.tolist()
warranty_hours = data.warranty_hours.toList()
base_uom = data.base_uom.tolist()
"""


def search_id(inv_id):
    search_button = browser.find_element_by_id('liSearch')
    search_button.click()
    product_id_field_search = browser.find_element_by_id('Product_Identifier_txt0')
    product_id_field_search.clear()
    product_id_field_search.send_keys(inv_id)
    search_button = browser.find_element_by_id('SearchScreenBtnSearch')
    search_button.click()
    time.sleep(3)


def update_record(inv_id, oem_num, sds_bol):
    browser.find_element_by_link_text(inv_id).click()
    time.sleep(1)
    edit_button = browser.find_element_by_id('btnEditRequest')
    edit_button.click()
    oem_field = browser.find_element_by_id('StdSf12_OEMNumber_txt')
    oem_field.clear()
    oem_field.send_keys(oem_num)
    select1 = Select(browser.find_element_by_id('StdSf12_SDS_txt'))
    select1.select_by_visible_text(sds_bol)

login(bot1, password)
set_site('Global Site Code')
browser.get('https://sysco.sprocketcmms.com/Default.aspx?screen=Inventory%20Items&SSF=72')
search_id('406012')
update_record('406122', '406122', 'True')
