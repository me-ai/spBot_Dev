import time
from spBot_Core.BotLogin import set_site, login, browser
from spBot_Core.secrets import bot1, bot2, bot3, bot4, bot5, bot6, password
from selenium.webdriver.support.select import Select


def fsi_page_one(sch_name, start, sch_on_comp_flag=1):
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
def fsi_page_two(unit, set=1):
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
def fsi_page_three(sch_name, start, frequency, day_dropdown='Daily', set=0, week_day=0):
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
    daily3.select_by_visible_text(day_dropdown)
    # week_day 1=Daily 2=Weekly 3=Monthly
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
    elif week_day == 2:
        browser.find_element_by_id('weekR_txtEvery').send_keys(frequency)
        browser.find_element_by_id('weekR_sunday').click()
        save_sch3 = browser.find_element_by_xpath('//*[@id="tblPMProjectPlanSchedule"]/table/tbody/tr[2]/td[2]/input')
        time.sleep(1)
        save_sch3.click()
        time.sleep(1)
        next3 = browser.find_element_by_id('btn_Step3_Next')
        time.sleep(1)
        next3.click()
        time.sleep(1)
    elif week_day == 3:
        browser.find_element_by_id('monthR_XOfEveryMonths').click()
        browser.find_element_by_id('monthR_XInstanceMonth').send_keys(frequency)
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


def fsi_page_four(target_request):
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


# FSI
def create_fsi_daily(fsi_site, fsi_start):
    site_code = fsi_site
    fsi_daily_start = fsi_start
    fsi_target_sch = 'FSI-Daily Consolidated'
    fsi_daily_name = '{} {}'.format(site_code, fsi_target_sch)
    fsi_location = '{}-BLDA'.format(site_code)
    daily_frequency = 1
    fsi_page_one(fsi_daily_name, fsi_daily_start, sch_on_comp_flag=0)
    fsi_page_two(fsi_location, set=1)
    fsi_page_three(fsi_daily_name, fsi_daily_start,daily_frequency, day_dropdown='Daily', set=0, week_day=1)
    fsi_page_four(fsi_target_sch)
    print('{} Created'.format)


def create_fsi_weekly(weekly_fsi_site, weekly_fsi_start):
    weekly_site_code = weekly_fsi_site
    fsi_weekly_start = weekly_fsi_start
    fsi_target_sch = 'FSI-Weekly Consolidated'
    fsi_daily_name = '{} {}'.format(weekly_site_code, fsi_target_sch)
    fsi_location = '{}-BLDA'.format(weekly_site_code)
    daily_frequency = 1
    fsi_page_one(fsi_daily_name, fsi_weekly_start, sch_on_comp_flag=0)
    fsi_page_two(fsi_location, set=1)
    fsi_page_three(fsi_daily_name, fsi_weekly_start, daily_frequency, day_dropdown='Weekly', set=0, week_day=2)
    fsi_page_four(fsi_target_sch)
    print('{} Created'.format)


def create_fsi_monthly(monthly_fsi_site, monthly_fsi_start, monthly_frequency=1):
    fsi_target_sch = 'FSI-Monthly Consolidated'
    if monthly_frequency == 3:
        fsi_target_sch = 'FSI-Quarterly Consolidated'
    monthly_site_code = monthly_fsi_site
    fsi_monthly_start = monthly_fsi_start
    fsi_monthly_name = '{} {}'.format(monthly_site_code, fsi_target_sch)
    fsi_location = '{}-BLDA'.format(monthly_site_code)
    daily_frequency = monthly_frequency
    fsi_page_one(fsi_monthly_name, fsi_monthly_start, sch_on_comp_flag=0)
    fsi_page_two(fsi_location, set=1)
    fsi_page_three(fsi_monthly_name, fsi_monthly_start, daily_frequency, day_dropdown='Monthly', set=0, week_day=3)
    fsi_page_four(fsi_target_sch)
    print('{} Created'.format)


mw_sites = []

browser.implicitly_wait(30)
login(bot1, password)

target_site_code = mw_sites[10]
target_start_daily = '09072020'
target_start_weekly = '09062020'
target_start_monthly = '09072020'
set_site(target_site_code)

browser.get('https://sysco.sprocketcmms.com/Default.aspx?screen=PM%20Projects&SSF=244')
create_fsi_daily(target_site_code, target_start_daily)
create_fsi_weekly(target_site_code, target_start_weekly)
create_fsi_monthly(target_site_code, target_start_monthly, monthly_frequency=1)
# Quarterly variant of Monthly
create_fsi_monthly(target_site_code, target_start_monthly, monthly_frequency=3)
