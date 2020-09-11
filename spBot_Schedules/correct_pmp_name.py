import time
from spBot_Core.BotLogin import set_site, login, browser


def find_schedule(schedule, location_based=0):
    browser.implicitly_wait(10)
    if location_based == 0:
        browser.get('https://sysco.sprocketcmms.com/Default.aspx?screen=PM%20Projects&SSF=-108')
        print('---> Loading Equipment Based View')
    elif location_based == 1:
        browser.get('https://sysco.sprocketcmms.com/Default.aspx?screen=PM%20Projects&SSF=244')
        print('---> Loading Location Based View')
    else:
        print('--->!! Value outside of defined parameters\nlocation_based=0\nor\nlocation_based=1')

    project_link = schedule
    time.sleep(1)
    search_link = browser.find_element_by_link_text('Search')
    time.sleep(1)
    search_link.click()
    pm_number_field = browser.find_element_by_id('PMNumber_txt3')
    pm_number_field.clear()
    pm_number_field.send_keys(schedule)
    search_button = browser.find_element_by_id('SearchScreenBtnSearch')
    search_button.click()
    time.sleep(1)
    browser.find_element_by_partial_link_text(project_link).click()


def correct_pmp_name(new_sch_name, archive_flag=0):
    browser.implicitly_wait(10)
    details_name = browser.find_element_by_id('Name_txt')
    details_name.clear()
    details_name.send_keys(new_sch_name)
    if archive_flag == 0:
        archive_flag_box = browser.find_element_by_id('Archived_chk')
        archive_flag_box.click()
    save_details = browser.find_element_by_link_text('Save')
    save_details.click()
    time.sleep(3)


def remove_asset():
    browser.implicitly_wait(10)
    assets_tab = browser.find_element_by_id('liAssets')
    assets_tab.click()
    time.sleep(1)
    remove_asset_link = browser.find_element_by_link_text('Remove')
    remove_asset_link.click()
    time.sleep(1)
    browser.switch_to.alert.accept()


def remove_schedule():
    browser.implicitly_wait(10)
    sch_tab = browser.find_element_by_id('liSchedules')
    sch_tab.click()
    time.sleep(1)
    remove_sch_link = browser.find_element_by_link_text('Remove')
    remove_sch_link.click()
    time.sleep(1)
    browser.switch_to.alert.accept()


