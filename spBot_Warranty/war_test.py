from spBot_Warranty.create_new import war_dates, mack_warranty_length, equipment_page, create_new, log_result, \
    mack_warranty, log_result
from spBot_Core.BotLogin import set_site, login, browser
from spBot_Core.secrets import bot1, bot2, bot3, bot4, bot5, bot6, password
import pandas


# Parse .csv
colnames = ['site', 'unit', 'year']
data = pandas.read_csv('war_main.csv', names=colnames)

# Store entries in list for variables
site = data.site.tolist()
unit = data.unit.tolist()
year = data.year.tolist()

login(bot2, password)

counter = len(unit)
x = 0
while x <= counter:
    try:
        x += 1
        set_site(site[x])
        equipment_page(unit[x])
        war_counter = len(mack_warranty)
        y = 0
        while y <= war_counter:
            try:
                y += 1
                year_var = year[x]
                target_war = '{} {}'.format(year_var, mack_warranty[y])
                length = mack_warranty_length[y]
                default_start = war_dates(mack_warranty_length[y], year=int(year_var))
                create_new(target_war, default_start[0], default_start[1])
                log_result(unit[x], mack_warranty[y], log_type=0)

            except IndexError:
                print('{} complete'.format(unit[x]))
                break
            except Exception as b:
                try:
                    print('Error---->Checking for Alert)')
                    log_result(unit[x], mack_warranty[y], log_type=1)
                    browser.switch_to.alert.accept()
                    continue
                except Exception as g:
                    print('!Failed!')
                    continue

        print('Unit Complete\n------> Moving to Next')
    except IndexError:
        print('Script Complete')
        break
    except Exception as b:
        print('!!Unit level Error!!!\n----> Attempting Move to next')
        print(b)
        continue

browser.quit()
