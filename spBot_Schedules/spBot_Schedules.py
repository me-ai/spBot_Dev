import time
from spBot_Core.BotLogin import set_site, login, browser
from spBot_Core.secrets import bot1, bot2, bot3, bot4, bot5, bot6, password
from selenium.webdriver.support.select import Select


"""
The spBot_Schedules module breaks each function down by page, see below for further notes.

Additional imports used in conjunction for custom scripts:
    from spBot_Core.BotLogin import login, set_site, password, bot1, browser
    import pandas

Example:

    Variable example:
        target_file = 'targets_to_sch.csv'
        col_names = ['unit', 'start', 'target_site', 'target_request', 'frequency']
        data = pandas.read_csv(target_file, names=col_names)

        # Store entries in list for variables
            x = 1
            unit = data.unit.tolist()
            start = data.start.tolist()
            target_site = data.target_site.tolist()
            target_request = data.target_request.tolist()
            frequency = data.frequency.tolist()
            sch_name = '{}-{}'.format(unit[x], target_request[x])
        
        Example of function usage w/ variables
            page_one(sch_name, start[x])
            page_two(unit[x])  # type = ['Equipment', 'Location'] Default is set=1
            page_three(sch_name, start[x], frequency[x], set=2)  # set_lead_days = ['0', '7', '30'] Default is set=3
            page_four(target_request[x])
            page_final(unit[x])
"""


def page_one(sch_name, start, sch_on_comp_flag=1):
    new_pm_btn = browser.find_element_by_id('btnNewLink')
    new_pm_btn.click()
    pm_name = browser.find_element_by_id('txtName')
    pm_name.send_keys(sch_name)
    new_des = browser.find_element_by_id('txtDescription')
    new_des.send_keys(sch_name)
    time.sleep(1)
    pm_name.click()
    new_enable_on = browser.find_element_by_id('txtEnableOn')
    new_enable_on.send_keys(start)
    time.sleep(3)
    next1 = browser.find_element_by_id('btn_Step1_Next')
    if sch_on_comp_flag == 1:
        sch_on_completion = browser.find_element_by_id('ScheduleOnCompletion_chk')
        sch_on_completion.click()
        next1.click()
    else:
        time.sleep(1)
        next1.click()
        time.sleep(1)


# Note set will determine type default is Location
def page_two(unit, set=1):
    type = ['Equipment', 'Location']
    in_type = Select(browser.find_element_by_id('ddlAssetType'))
    in_type.select_by_visible_text(type[set])
    add_unit = browser.find_element_by_id('txtAddAsset')
    add_unit.send_keys(unit)
    add_submit = browser.find_element_by_link_text('Add')
    add_submit.click()
    time.sleep(3)
    next2 = browser.find_element_by_id('btn_Step2_Next')
    next2.click()
    time.sleep(3)


# Note set will determine lead days default is 30 days
def page_three(sch_name, start, frequency, set=2, week_day=0):
    set_lead_days = ['0', '7', '30']
    pm_plan_link = browser.find_element_by_link_text('Add a new PM Project Plan Schedule')
    pm_plan_link.click()
    time.sleep(1)
    name_page3 = browser.find_element_by_id('schedule_txtName')
    name_page3.send_keys(sch_name)
    start_page3 = browser.find_element_by_id('schedule_txtStartDate')
    start_page3.send_keys(start)
    lead_days = browser.find_element_by_id('schedule_txtLeadDays')
    lead_days.send_keys(set_lead_days[set])
    daily3 = Select(browser.find_element_by_id('ddlRecurrenceType'))
    daily3.select_by_visible_text('Daily')
    if week_day == 1:
        browser.find_element_by_id('dr_chkEveryWeekday').click()
        save_sch3 = browser.find_element_by_xpath('//*[@id="tblPMProjectPlanSchedule"]/table/tbody/tr[2]/td[2]/input')
        time.sleep(1)
        save_sch3.click()
        time.sleep(1)
        next3 = browser.find_element_by_id('btn_Step3_Next')
        time.sleep(1)
        next3.click()
        time.sleep(1)
    else:
        target_frequency = browser.find_element_by_id('dailyR_txtEvery')
        target_frequency.send_keys(frequency)
        save_sch3 = browser.find_element_by_xpath('//*[@id="tblPMProjectPlanSchedule"]/table/tbody/tr[2]/td[2]/input')
        time.sleep(1)
        save_sch3.click()
        time.sleep(1)
        next3 = browser.find_element_by_id('btn_Step3_Next')
        time.sleep(1)
        next3.click()
        time.sleep(1)


def page_three_alt(sch_name, start, set=0):
    set_lead_days = ['0', '7', '30']
    pm_plan_link = browser.find_element_by_link_text('Add a new PM Project Plan Schedule')
    pm_plan_link.click()
    time.sleep(1)
    name_page3 = browser.find_element_by_id('schedule_txtName')
    name_page3.send_keys(sch_name)
    start_page3 = browser.find_element_by_id('schedule_txtStartDate')
    start_page3.send_keys(start)
    lead_days = browser.find_element_by_id('schedule_txtLeadDays')
    lead_days.clear()
    lead_days.send_keys(set_lead_days[set])
    daily3 = Select(browser.find_element_by_id('ddlRecurrenceType'))
    daily3.select_by_visible_text('Does not repeat')
    save_sch3 = browser.find_element_by_xpath('//*[@id="tblPMProjectPlanSchedule"]/table/tbody/tr[2]/td[2]/input')
    time.sleep(1)
    save_sch3.click()
    time.sleep(1)
    next3 = browser.find_element_by_id('btn_Step3_Next')
    time.sleep(1)
    next3.click()
    time.sleep(1)


def page_four(target_request):
    request = browser.find_element_by_id('txtRequestName')
    request.send_keys(target_request)
    time.sleep(1)
    add4 = browser.find_element_by_id('lnkAddRequest')
    time.sleep(1)
    add4.click()
    time.sleep(2)
    finish4 = browser.find_element_by_id('btn_Step4_Finish')
    finish4.click()
    time.sleep(5)
    browser.switch_to.alert.accept()


def page_final(unit):
    # Log Success
    file = open('log.txt', 'a')
    file.write('{} Success\n'.format(unit))
    file.close()


def page_error(unit):
    file = open('ErrorLog.txt', 'a')
    file.write('{} error\n'.format(unit))
    file.close()
