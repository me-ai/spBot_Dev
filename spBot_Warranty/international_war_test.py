from spBot_Warranty.create_new import equipment_page, create_new, war_dates, log_result
from spBot_Warranty.create_new import international_warranty_core, international_warranty_core_length
from spBot_Warranty.create_new import international_warranty_model, international_warranty_model_length
from spBot_Warranty.create_new import international_warranty_engine, international_warranty_engine_length
from spBot_Warranty.create_new import international_warranty_transmission, international_warranty_transmission_length
from spBot_Warranty.create_new import international_warranty_axle, international_warranty_axle_length
from spBot_Warranty.create_new import international_warranty_alternator, international_warranty_alternator_length
from spBot_Core.BotLogin import set_site, login, browser
from spBot_Core.secrets import bot1, bot2, bot3, bot4, bot5, bot6, password
import pandas


# Parse .csv
colnames = ['site', 'unit', 'year', 'model_flag', 'engine_flag', 'transmission_flag', 'axle_flag', 'alternator_flag']
data = pandas.read_csv('international_war_main.csv', names=colnames)

# Store entries in list for variables
site = data.site.tolist()
unit = data.unit.tolist()
year = data.year.tolist()
model_flag = data.model_flag.tolist()
engine_flag = data.engine_flag.tolist()
transmission_flag = data.transmission_flag.tolist()
axle_flag = data.axle_flag.tolist()
alternator_flag = data.alternator_flag.tolist()

login(bot1, password)
counter = len(unit)
x = 0
while x <= counter:
    try:
        # Main Loop Control
        x += 1
        set_site(site[x])
        equipment_page(unit[x])

        # Dynamic Warranties
        try:
            year_var = year[x]
            target_war1 = '{} {}'.format(year_var, international_warranty_model[int(model_flag[x])])
            target_war2 = '{} {}'.format(year_var, international_warranty_engine[int(engine_flag[x])])
            target_war3 = '{} {}'.format(year_var, international_warranty_transmission[int(transmission_flag[x])])
            target_war4 = '{} {}'.format(year_var, international_warranty_axle[int(axle_flag[x])])
            target_war5 = '{} {}'.format(year_var, international_warranty_alternator[int(alternator_flag[x])])

            length1 = int(international_warranty_model_length[int(model_flag[x])])
            length2 = int(international_warranty_engine_length[int(engine_flag[x])])
            length3 = int(international_warranty_transmission_length[int(transmission_flag[x])])
            length4 = int(international_warranty_axle_length[int(axle_flag[x])])
            length5 = int(international_warranty_alternator_length[int(alternator_flag[x])])

            default_start1 = war_dates(length1, year=int(year_var))
            print(default_start1)
            default_start2 = war_dates(length2, year=int(year_var))
            default_start3 = war_dates(length3, year=int(year_var))
            default_start4 = war_dates(length4, year=int(year_var))
            default_start5 = war_dates(length5, year=int(year_var))

            create_new(target_war1, default_start1[0], default_start1[1])
            print('->{} model model warranty attached'.format(unit[x]))
            create_new(target_war2, default_start2[0], default_start2[1])
            print('-->{} engine warranty attached'.format(unit[x]))
            create_new(target_war3, default_start3[0], default_start3[1])
            print('--->{} transmission warranty attached'.format(unit[x]))
            create_new(target_war4, default_start4[0], default_start4[1])
            print('---->{} axle warranty attached'.format(unit[x]))
            create_new(target_war5, default_start5[0], default_start5[1])
            print('----->{} alternator warranty attached'.format(unit[x]))
            print('--->{} dynamic warranties attached<---\n<------------------Moving to Core!'.format(unit[x]))
            equipment_page(unit[x])

            # Core Warranties
            war_counter = len(international_warranty_core)
            y = 0
            while y <= war_counter:
                # Core
                try:
                    core_year = year[x]
                    y += 1
                    target_war = '{} {}'.format(core_year, international_warranty_core[y])
                    length = int(international_warranty_core_length[y])
                    default_start = war_dates(length, year=int(core_year))
                    create_new(target_war, default_start[0], default_start[1])
                    # log_result(unit[x], international_warranty_core[y], log_type=0)
                    print('----->Core Warranty {} attached<-----'.format(y))
                except IndexError:
                    print('{} complete'.format(unit[x]))
                    break
                except Exception as b:
                    try:
                        print('Error---->Checking for Alert)')
                        log_result(unit[x], international_warranty_core[y], log_type=1)
                        browser.switch_to.alert.accept()
                        print(b)
                        continue
                    except Exception as g:
                        print('!Failed!')
                        print(g)
                        continue
        except IndexError:
            print('{} complete'.format(unit[x]))
            break
        except Exception as b:
            try:
                print('Error---->Checking for Alert)')
                log_result(unit[x], international_warranty_model[model_flag[x]], log_type=1)
                browser.switch_to.alert.accept()
                continue
            except Exception as g:
                print('!Failed!')
                print(g)
                continue

        print('Unit Complete\n------> Moving to Next')
    except IndexError:
        print('Script Complete')
        break
    except Exception as b:
        print('!!Unit level Error!!!\n----> Attempting Move to next')
        continue

browser.quit()
