from spBot_Core.BotLogin import login, set_site, password, bot1, bot2, browser
import pandas
import time

target_file = 'targets_to_prep.csv'
col_names = ['target_wo', 'sp_id', 'target_site']
data = pandas.read_csv(target_file, names=col_names)

# Store entries in list for variables

target_wo = data.target_wo.tolist()
sp_id = data.sp_id.tolist()
target_site = data.target_site.tolist()

login(bot2, password)
counter = len(target_wo)
browser.implicitly_wait(10)
x = 0



def nav_wo_record(target_id):
    record_link = \
        'https://sysco.sprocketcmms.com/Default.aspx?screen=Work%20Order%20Details&InstanceName={}'.format(target_id)
    browser.get(record_link)
    time.sleep(3)
    inspection_tab = browser.find_element_by_id('liInspection')
    inspection_tab.click()


def remove_inspection():
    remove_link = browser.find_element_by_link_text('Remove')
    remove_link.click()
    time.sleep(1)
    browser.switch_to.alert.accept()
    time.sleep(1)


while x <= counter:
    try:
        x += 1
        set_site(target_site[x])
        nav_wo_record(sp_id[x])
        y = 0
        while y <= 5:
            try:
                y += 1
                print('{} of 5'.format(y))
                remove_inspection()

            except IndexError:
                y = 0
                break
            except Exception as c:
                if y >= 4:
                    break
                continue

        print('{} complete'.format(target_wo[x]))
        time.sleep(1)
    except IndexError:
        print('Prep Complete')
        break
    except Exception as b:
        print('!Error! {}'.format(target_wo[x]))
        continue

browser.quit()
