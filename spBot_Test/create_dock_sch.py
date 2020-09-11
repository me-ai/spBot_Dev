from spBot_Schedules.spBot_Schedules import page_one, page_two, page_three, page_four, page_final, page_error
from spBot_Core.BotLogin import login, set_site, password, bot1, bot2, browser
import pandas
import time

# Test script for creating FSI schedules

target_file = 'targets_to_sch.csv'
col_names = ['unit', 'start', 'target_site', 'target_request', 'frequency']
data = pandas.read_csv(target_file, names=col_names)

# Store entries in list for variables
x = 0
unit = data.unit.tolist()
start = data.start.tolist()
target_site = data.target_site.tolist()
target_request = data.target_request.tolist()
frequency = data.frequency.tolist()

counter = len(unit)
browser.implicitly_wait(30)

login(bot2, password)
set_site(target_site[1])
while x <= counter:
    try:
        x = x + 1
        print('Starting {} of {}'.format(x, (counter - 1)))
        sch_name = '{}-{}'.format(unit[x], target_request[x])  # Customize based on needs
        browser.get('https://sysco.sprocketcmms.com/Default.aspx?screen=PM%20Projects')
        page_one(sch_name, start[x], sch_on_comp_flag=1)
        page_two(unit[x], set=1)  # type = ['Equipment', 'Location'] Default is set=1
        page_three(sch_name, start[x], frequency[x], set=0)  # set_lead_days = ['0', '7', '30']
        page_four(target_request[x])
        page_final(unit[x])
        time.sleep(10)
        print('Moving to Next........')


    except IndexError:
        print('------>Script Complete!<-------\n{} of {} completed'.format(x, counter))
        break

    except Exception as b:
        try:
            browser.switch_to.alert.accept()
            print('Extra Popup resolved')
            continue
        except Exception as c:
            print('----->Popup cannot be resolved\n{}'.format(c))
            print(b)
            page_error(unit[x])
            continue

browser.quit()
