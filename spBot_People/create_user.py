import time
from spBot_Core.BotLogin import set_site, login, browser
from spBot_Core.secrets import bot1, bot2, bot3, bot4, bot5, bot6, password

import pandas


def user_details(target_id, first_name, last_name, a=1):
    browser.get('https://sysco.sprocketcmms.com/Default.aspx?screen=People&SSF=-134')
    create_new_person_button = browser.find_element_by_xpath('//*[@id="btnNewLink"]')
    create_new_person_button.click()
    time.sleep(3)
    id_field = browser.find_element_by_id('StdSf_62_UserName_txt')
    id_field.clear()
    id_field.send_keys(target_id)
    fname_field = browser.find_element_by_id('StdSf_62_FirstName_txt')
    fname_field.clear()
    fname_field.send_keys(first_name)
    lname_field = browser.find_element_by_id('StdSf_62_LastName_txt')
    lname_field.clear()
    lname_field.send_keys(last_name)
    ignore_wdt = browser.find_element_by_id('StdSf_62_OverrideWorkDay_chk')
    ignore_wdt.click()
    ignore_wd_termination = browser.find_element_by_id('StdSf_62_IgnoreWorkDayTermination_chk')
    ignore_wd_termination.click()
    access_flag = int(a)

    if access_flag == 1:
        access_food_safety = browser.find_element_by_id('StdSf_62_Food_Safety_chk')
        access_food_safety.click()

    save_initial = browser.find_element_by_id('liSave')
    save_initial.click()
    time.sleep(5)
    browser.switch_to.alert.accept()
    time.sleep(1)


def update_employee_tab():
    browser.implicitly_wait(10)
    employee_tab = browser.find_element_by_id('liEmployee')
    employee_tab.click()
    time.sleep(1)
    remove_web_requester = browser.find_element_by_id('StdSf_102_License_ddl')
    remove_web_requester.send_keys('User')
    save_update_employee = browser.find_element_by_id('liSave')
    save_update_employee.click()
    time.sleep(5)
    browser.switch_to.alert.accept()
    time.sleep(1)


def add_user_group(group):
    groups_tab = browser.find_element_by_id('liGroups')
    groups_tab.click()
    time.sleep(3)
    add_group = browser.find_element_by_id('txt_Group')
    add_group.send_keys(group)
    submit_group = browser.find_element_by_xpath('//*[@id="divGroups"]/table/tbody/tr[1]/td[2]/input[2]')
    submit_group.click()
    time.sleep(3)


def remove_web_group():
    browser.implicitly_wait(10)
    group_tab = browser.find_element_by_id('liGroups')
    group_tab.click()
    time.sleep(3)
    web_group = browser.find_element_by_xpath('//*[@id="groups_AssignedGroups"]/option[2]')
    web_group.click()
    remove_button = browser.find_element_by_xpath('//*[@id="divGroups"]/table/tbody/tr[2]/td[2]/input')
    remove_button.click()
    time.sleep(3)
    save_groups = browser.find_element_by_link_text('Save')
    save_groups.click()
    time.sleep(5)
    browser.switch_to.alert.accept()
    time.sleep(1)


def set_default_password():
    additional_tab = browser.find_element_by_id('liAdditional')
    additional_tab.click()
    time.sleep(3)
    pw_field = browser.find_element_by_id('txtNewPass')
    pw_field.clear()
    pw_field.send_keys('sprocket')
    confirm_pw_field = browser.find_element_by_id('txtConfirmNewPass')
    confirm_pw_field.clear()
    confirm_pw_field.send_keys('sprocket')


def save_record_final():
    save_exit = browser.find_element_by_link_text('Save')
    save_exit.click()
    time.sleep(5)
    browser.switch_to.alert.accept()
    time.sleep(1)


target_file = 'create_user.csv'
col_names = ['target_user', 'name_first', 'name_last', 'target_site']
data = pandas.read_csv(target_file, names=col_names)
target_user = data.target_user.tolist()
name_first = data.name_first.tolist()
name_last = data.name_last.tolist()
target_site = data.target_site.tolist()


counter = len(target_user)
x = 0
browser.implicitly_wait(15)
login(bot2, password)

while x <= counter:
    try:
        x += 1
        set_site(target_site[x])
        time.sleep(5)
        user_details(target_user[x], name_first[x], name_last[x])
        update_employee_tab()
        remove_web_group()
        add_user_group('Access-Technician')
        time.sleep(1)
        add_user_group('Data-FSY')
        set_default_password()
        save_record_final()

    except IndexError:
        print('Script complete!!')
        break

    except Exception as b:
        try:
            browser.switch_to.alert.accept()
            print('Extra Popup resolved')
            continue
        except Exception as c:
            print('----->Popup cannot be resolved\n{}'.format(c))
            print(b)
            continue

browser.quit()
