import time
from selenium.webdriver.support.select import Select
from spBot_Core.BotLogin import set_site, login, browser
from spBot_Core.secrets import bot1, bot2, bot3, bot4, bot5, bot6, password
import pandas


def find_schedule(schedule, location_based=0):
    if location_based == 0:
        browser.get('https://sysco.sprocketcmms.com/Default.aspx?screen=PM%20Projects&SSF=-108')
        print('---> Loading Equipment Based View')
    elif location_based == 1:
        browser.get('https://sysco.sprocketcmms.com/Default.aspx?screen=PM%20Projects&SSF=244')
        print('---> Loading Location Based View')
    else:
        print('--->!! Value outside of defined parameters\nlocation_based=0\nor\nlocation_based=1')

    #project_link = schedule
    project_anchor = '{}: {}'.format(schedule, schedule)
    time.sleep(3)
    search_link = browser.find_element_by_link_text('Search')
    time.sleep(3)
    search_link.click()
    time.sleep(1)
    pm_number_field = browser.find_element_by_id('PMNumber_txt3')
    pm_number_field.clear()
    pm_number_field.send_keys(schedule)
    search_button = browser.find_element_by_id('SearchScreenBtnSearch')
    search_button.click()
    time.sleep(5)
    browser.find_element_by_partial_link_text(project_anchor).click()


def correct_pmp_name(new_sch_name, archive_flag=0):
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
    assets_tab = browser.find_element_by_id('liAssets')
    assets_tab.click()
    time.sleep(1)
    remove_asset_link = browser.find_element_by_link_text('Remove')
    remove_asset_link.click()
    time.sleep(1)
    browser.switch_to.alert.accept()


def remove_schedule():
    sch_tab = browser.find_element_by_id('liSchedules')
    sch_tab.click()
    time.sleep(1)
    remove_sch_link = browser.find_element_by_link_text('Remove')
    remove_sch_link.click()
    time.sleep(1)
    browser.switch_to.alert.accept()


def empty_sch():
    # Create Empty Sch
    empty_sch_tab = browser.find_element_by_id('liSchedules')
    empty_sch_tab.click()
    time.sleep(1)
    browser.find_element_by_id('AddNewProjectPlanLink').click()
    browser.find_element_by_id('schedule_txtName').clear()
    browser.find_element_by_id('schedule_txtName').send_keys('Test Update')
    browser.find_element_by_id('schedule_txtStartDate').send_keys('01012099')
    daily3 = Select(browser.find_element_by_id('ddlRecurrenceType'))
    daily3.select_by_visible_text('Does not repeat')
    lead_days = browser.find_element_by_id('schedule_txtLeadDays')
    lead_days.clear()
    lead_days.send_keys('0')
    empty_save_sch = save_sch3 = browser.find_element_by_xpath(
        '/html/body/form/div[3]/div[3]/div[5]/div[1]/table/tbody/tr[5]/td[2]/input')
    empty_save_sch.click()
    time.sleep(1)
    # Use Empty Request
    empty_req_tab = browser.find_element_by_id('liRequests')
    empty_req_tab.click()
    time.sleep(1)
    browser.find_element_by_id('txtRequestName').send_keys('testing')
    empty_add = browser.find_element_by_id('lnkAddRequest')
    empty_add.click()
    time.sleep(1)
    save_details = browser.find_element_by_link_text('Save')
    save_details.click()
    return_to_details = browser.find_element_by_id('liInformation')
    return_to_details.click()
    time.sleep(1)


# Read CSV of Target Schedules
target_file = 'targets_to_archive.csv'
col_names = ['target_schedule',  'target_site']
data = pandas.read_csv(target_file, names=col_names)

# Store entries in list for variables
target_schedule = data.target_schedule.tolist()
target_site = data.target_site.tolist()

# While Loop
x = 0
counter = len(target_schedule)
login(bot2, password)
browser.implicitly_wait(30)
set_site(target_site[1])
time.sleep(3)

while x <= counter:
    try:
        x += 1
        #set_site(target_site[x])
        new_schedule = 'Archive-{}'.format(target_schedule[x])
        print('Starting {}'.format(target_schedule[x]))
        find_schedule(target_schedule[x])
        correct_pmp_name(new_schedule)
        remove_asset()
        remove_schedule()
        print('{} archived to {}'.format(target_schedule[x], new_schedule))
    except IndexError:
        print('Script Complete')
        break
    except Exception as b:
        print('Error {}\nSprocket is being slow as .... again\n'.format(target_schedule[x], b))
        """
        try:
            print('Starting {}......Again..'.format(target_schedule[x]))
            browser.switch_to.alert.accept()
            #browser.get('https://sysco.sprocketcmms.com/Default.aspx?screen=PM%20Projects&SSF=-108')
            #find_schedule(target_schedule[x])
            empty_sch()
            new_schedule = 'Archive-{}'.format(target_schedule[x])
            correct_pmp_name(new_schedule)
            remove_asset()
            remove_schedule()
        except Exception as y:
            print('Could not correct....Check your code dummy....lol')
            continue
        """
    continue

browser.quit()
