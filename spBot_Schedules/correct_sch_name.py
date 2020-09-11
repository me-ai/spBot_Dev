import time
from spBot_Core.BotLogin import set_site, login, browser
from spBot_Core.secrets import bot1, bot2, bot3, bot4, bot5, bot6, password
import pandas


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


def correct_pmp_name(new_sch_name, archive_flag=1):
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


target_file = 'targets_to_correct.csv'
col_names = ['target_schedule', 'target_schedule_name', 'target_site']
data = pandas.read_csv(target_file, names=col_names)

# Store entries in list for variables
target_schedule = data.target_schedule.tolist()
target_schedule_name = data.target_schedule_name.tolist()
target_site = data.target_site.tolist()

# While Loop
x = 0
counter = len(target_schedule)
login(bot1, password)
set_site(target_site[1])

while x <= counter:
    try:
        x += 1
        new_schedule = '{}-Intercompany'.format(target_schedule_name[x])
        print('Starting {}'.format(target_schedule[x]))
        find_schedule(target_schedule[x])
        correct_pmp_name(new_schedule)
        print('{} updated to {}'.format(target_schedule[x], new_schedule))
    except IndexError:
        print('Script Complete')
        break
    except Exception as b:
        print('Error {}\nSprocket is being slow as .... again\n'.format(target_schedule[x], b))
        continue
