import time
from datetime import datetime, timedelta
import pandas
from spBot_Core.BotLogin import set_site, login, browser
from spBot_Core.secrets import bot1, bot2, bot3, bot4, bot5, bot6, password

mack_warranty = (
    "Mack - Trunnion Bracket Warranty",
    "Mack - Transmission, Driveline, Rear Axle, Front Non-Drive Steer Axle Warranty",
    "Mack - T300 / mDrive Transmission Warranty",
    "Mack - T300 / mDrive Transmission / Engine Towing  Warranty",
    "Mack - mDrive clutch Warranty",
    "Mack - Major Mack Engine Components Warranty",
    "Mack - Mack Engine Components Base Warranty",
    "Mack - Internal Cab Corrosion Warranty",
    "Mack - Frame Rail/ Cross members Corrosion Warranty",
    "Mack - Engine Towing Warranty",
    "Mack - Chassis Towing Warranty",
    "Mack - Chassis Basic Coverage Warranty",
    "Mack - Carrier and Axle Housing Warranty",
    "Mack - Cab Structure Warranty",
    "Mack - Air Conditioning Warranty"
)
mack_warranty_length = (
    1095,
    1095,
    1825,
    730,
    1095,
    1825,
    730,
    1825,
    2190,
    730,
    90,
    365,
    1825,
    1825,
    365
)
international_warranty_core = (
    "International - Battery Warranty (Standard Batteries)",
    "International - Chassis/Frame Warranty (Drivetrain)",
    "International - Emissions System Warranty (All Models)",
    "International - Towing Warranty (All Models)",
    "International - Chassis/Frame Warranty (Frame Rails)"
)
international_warranty_core_length = (
    365,
    730,
    1825,
    90,
    2555
)
international_warranty_model = (
    "International - Vehicle Base Warranty (International Tractors RH and LT)",
    "International - Vehicle Base Warranty (Durastar 4300/4400 Straight Trucks)"
)
international_warranty_model_length =(
    730,
    730
)
international_warranty_engine = (
    "International - Engine Warranty (International A26)",
    "International - Engine Warranty (Cummins X15)",
    "International - Engine Warranty (Cummins ISB on Single Axle)",
    "International - Engine Warranty (Cummins ISL on Tandem Axle)"
)
international_warranty_engine_length = (
    730,
    730,
    1095,
    730
)
international_warranty_transmission = (
    "International - Transmission Warranty (Allison 2500HS)",
    "International - Transmission Warranty (Allison 3000HS)",
    "International - Transmission Warranty (Eaton Ultrashift)",
    "International - Transmission Warranty (Eaton Clutch)"
)
international_warranty_transmission_length = (
    1460,
    1460,
    1825,
    1825
)
international_warranty_axle = (
    "International - Axles Warranty (Front and Rear on Medium Duty-M2)",
    "International - Axles Warranty (Front and Rear on LT/RH Tractors)"
)
international_warranty_axle_length = (
    1095,
    1825
)
international_warranty_alternator = (
    "International - Remy Starter/Alternator Warranty (38SI Alternator (RH/LT) through Remy after 2 years)",
    "International - Remy Starter/Alternator Warranty (36SI Alternator (Durastar) through Remy after 2 years)",
    "International - Mitsubishi Alternator Warranty (Electric All Models)"
)
international_warranty_alternator_length =(
    1095,
    1095,
    1095
)


def war_dates(length, year=2020):
    if year == 2020:
        today = datetime.today()
        adjust = 300
        default_start = today - timedelta(days=adjust)
        war_length = default_start + timedelta(length)
        m = default_start.month
        if m < 10:
            m = "0{}".format(m)
        d = default_start.day
        yr = default_start.year
        parse_default = ('{}{}{}'.format(m, d, yr))
        mw = war_length.month
        if mw < 10:
            mw = "0{}".format(mw)
        dw = war_length.day
        yrw = war_length.year
        parse_length = ('{}{}{}'.format(mw, dw, yrw))
        return parse_default, parse_length

    elif year == 2019:
        today = datetime.today()
        adjust = 300 + (365 * 1)
        default_start = today - timedelta(days=adjust)
        war_length = default_start + timedelta(length)
        m = default_start.month
        if m < 10:
            m = "0{}".format(m)
        d = default_start.day
        yr = default_start.year
        parse_default = ('{}{}{}'.format(m, d, yr))
        mw = war_length.month
        if mw < 10:
            mw = "0{}".format(mw)
        dw = war_length.day
        yrw = war_length.year
        parse_length = ('{}{}{}'.format(mw, dw, yrw))
        return parse_default, parse_length

    elif year == 2018:
        today = datetime.today()
        adjust = 300 + (365 * 2)
        default_start = today - timedelta(days=adjust)
        war_length = default_start + timedelta(length)
        m = default_start.month
        if m < 10:
            m = "0{}".format(m)
        d = default_start.day
        yr = default_start.year
        parse_default = ('{}{}{}'.format(m, d, yr))
        mw = war_length.month
        if mw < 10:
            mw = "0{}".format(mw)
        dw = war_length.day
        yrw = war_length.year
        parse_length = ('{}{}{}'.format(mw, dw, yrw))
        return parse_default, parse_length

    elif year == 2017:
        today = datetime.today()
        adjust = 300 + (365 * 3)
        default_start = today - timedelta(days=adjust)
        war_length = default_start + timedelta(length)
        m = default_start.month
        if m < 10:
            m = "0{}".format(m)
        d = default_start.day
        yr = default_start.year
        parse_default = ('{}{}{}'.format(m, d, yr))
        mw = war_length.month
        if mw < 10:
            mw = "0{}".format(mw)
        dw = war_length.day
        yrw = war_length.year
        parse_length = ('{}{}{}'.format(mw, dw, yrw))
        return parse_default, parse_length

    elif year == 2016:
        today = datetime.today()
        adjust = 300 + (365 * 4)
        default_start = today - timedelta(days=adjust)
        war_length = default_start + timedelta(length)
        m = default_start.month
        if m < 10:
            m = "0{}".format(m)
        d = default_start.day
        yr = default_start.year
        parse_default = ('{}{}{}'.format(m, d, yr))
        mw = war_length.month
        if mw < 10:
            mw = "0{}".format(mw)
        dw = war_length.day
        yrw = war_length.year
        parse_length = ('{}{}{}'.format(mw, dw, yrw))
        return parse_default, parse_length

    else:
        print('Year not Supported')


def equipment_page(unit):
    # Find and select Equipment
    browser.implicitly_wait(15)
    browser.get('https://sysco.sprocketcmms.com/Default.aspx?screen=Equipment&SSF=-102')
    search_field = browser.find_element_by_link_text('Search')
    search_field.click()
    equip_search = browser.find_element_by_id('Equipment_txt4')
    equip_search.clear()
    equip_search.send_keys(unit)
    searchButton = browser.find_element_by_id('SearchScreenBtnSearch')
    searchButton.click()
    time.sleep(5)
    unit_link = browser.find_element_by_link_text(unit)
    unit_link.click()


def create_new(option, start, length):
    browser.implicitly_wait(15)
    war_tab = browser.find_element_by_link_text('Warranty')
    time.sleep(1)
    war_tab.click()
    time.sleep(1)
    war_link = browser.find_element_by_id('newWarranty_anchor')
    war_link.click()
    war_name = browser.find_element_by_id('newWarranty_WarrantyID')
    war_name.send_keys(option)
    war_start = browser.find_element_by_id('newWarranty_StartDate')
    war_start.clear()
    war_start.send_keys(start)
    war_end = browser.find_element_by_id('newWarranty_EndDate')
    war_end.clear()
    war_end.send_keys(length)
    war_save = browser.find_element_by_id('newWarranty_save')
    war_save.click()
    time.sleep(3)


def log_result(unit, option, log_type=0):
    if log_type == 0:
        print('!Success--> {} -->Warranty {} attached!'.format(unit, option))
        file = open('LogFile.txt', 'a')
        file.write('{} {} attached'.format(unit, option))
        file.close()
    else:
        print('------->Error<-------\n {} warranty {} error!'.format(unit, option))
        file = open('ErrorFile.txt', 'a')
        file.write('{} warranty {} error'.format(unit, option))
        file.close()
