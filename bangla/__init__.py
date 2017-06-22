# -*- coding: utf-8 -*-
import datetime

bangla_number = ['০', '১','২', '৩','৪',
                 '৫','৬', '৭', '৮', '৯']

english_number = ['0', '1', '2', '3', '4',
                  '5', '6', '7', '8', '9']

greg_equivalent_bangla_months = ["পৌষ", "মাঘ", "ফাল্গুন", "চৈত্র", "বৈশাখ", "জ্যৈষ্ঠ",
                     "আষাঢ়", "শ্রাবণ", "ভাদ্র", "আশ্বিন", "কার্তিক", "অগ্রহায়ণ"]

python_bangla_weekdays = ["সোমবার", "মঙ্গলবার", "বুধবার",
                       "বৃহস্পতিবার", "শুক্রবার", "শনিবার", "রবিবার"]

greg_equivalent_bangla_seasons = ["শীত", "বসন্ত", "গ্রীষ্ম",
                      "বর্ষা", "শরৎ", "হেমন্ত"]

greg_equivalent_last_day_of_bangla_months =  [13, 12, 14, 13, 14, 14,
                                              15, 15, 15, 15, 14, 14]

total_days_in_bangla_months = [30, 30, 30, 30, 31, 31,
                               31, 31, 31, 30, 30, 30]

greg_equivalent_leap_year_index_in_bangla_months = 2

def is_leap_year(passed_year):
    if passed_year % 400 == 0:
        return 1
    elif passed_year%4 == 0 and passed_year%100 != 0:
        return 1
    else:
        return 0

def get_bangla_year(passed_date, passed_month, passed_year):
    if passed_month > 3:
        bangla_year = passed_year - 593
    elif passed_month == 3 and passed_date > 13:
        bangla_year = passed_year - 593
    else:
        bangla_year = passed_year - 594
    return bangla_year

def get_bangla_weekday(passed_date, passed_month, passed_year):
    current_date_object = datetime.datetime(passed_year, passed_month, passed_date)
    bangla_weekday = python_bangla_weekdays[current_date_object.weekday()]
    return bangla_weekday

def convert_english_digit_to_bangla_digit(original):
    converted = ""
    for character in str(original):
        if character in english_number:
            converted+=bangla_number[english_number.index(character)]
        else:
            converted+=character
    return converted

def get_date(passed_date=None, passed_month=None, passed_year=None):
    if passed_date == None and passed_month == None and passed_year == None:
        current_date_object = datetime.date.today()
        passed_year = current_date_object.year
        passed_month = current_date_object.month
        passed_date = current_date_object.day
    bangla_weekday = get_bangla_weekday(passed_date, passed_month, passed_year)
    passed_month = passed_month - 1
    bangla_year = get_bangla_year(passed_date, passed_month, passed_year)
    if passed_date <= greg_equivalent_last_day_of_bangla_months[passed_month]:
        total_days_in_current_bangla_month = total_days_in_bangla_months[passed_month]
        if passed_month == greg_equivalent_leap_year_index_in_bangla_months and is_leap_year(passed_year) == 1:
            total_days_in_current_bangla_month += 1
        bangla_date = total_days_in_current_bangla_month + passed_date - greg_equivalent_last_day_of_bangla_months[passed_month]
        bangla_month_index = passed_month
        bangla_month = greg_equivalent_bangla_months[bangla_month_index]
    else:
        bangla_date = passed_date - greg_equivalent_last_day_of_bangla_months[passed_month]
        bangla_month_index = (passed_month+1)%12
        bangla_month = greg_equivalent_bangla_months[bangla_month_index]

    bangla_season = greg_equivalent_bangla_seasons[bangla_month_index // 2]

    bangla_date_month_year_season = {
        "date": convert_english_digit_to_bangla_digit(bangla_date),
        "month": convert_english_digit_to_bangla_digit(bangla_month),
        "year": convert_english_digit_to_bangla_digit(bangla_year),
        "season": convert_english_digit_to_bangla_digit(bangla_season),
        "weekday": convert_english_digit_to_bangla_digit(bangla_weekday)
    }

    return bangla_date_month_year_season
