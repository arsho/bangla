# -*- coding: utf-8 -*-
"""Bangla - Bengali calendar date conversion and numeral translation.

This package provides functions for:
- Converting Gregorian dates to the Bengali calendar (Bangabda)
- Translating English numeral strings to Bangla numeral strings
- Translating Bangla numeral strings to English numeral strings
- Generating Bengali ordinal representations for date numbers

The Bengali calendar follows the revised standard officially adopted in
Bangladesh in 1987. For Bengali communities in India, the calendar may
differ slightly.

Example usage::

    import bangla

    # Get today's Bengali date
    bangla_date = bangla.get_date()
    print(bangla_date)

    # Convert a specific Gregorian date
    bangla_date = bangla.get_date(20, 6, 2017)

    # Include the Bengali ordinal
    bangla_date = bangla.get_date(20, 6, 2017, ordinal=True)

    # Convert English numerals to Bangla
    bangla_num = bangla.convert_english_digit_to_bangla_digit("123456")
    # Result: "১২৩৪৫৬"

    # Convert Bangla numerals to English
    english_num = bangla.convert_bangla_digit_to_english_digit("১২৩৪৫৬")
    # Result: "123456"
"""
from __future__ import annotations

import datetime

# Bengali digit characters ০-৯
bangla_number = ["০", "১", "২", "৩", "৪", "৫", "৬", "৭", "৮", "৯"]

# English digit characters 0-9
english_number = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

# Pre-built dict mappings for O(1) digit lookup (replaces list.index O(n))
_english_to_bangla_map = dict(zip(english_number, bangla_number))
_bangla_to_english_map = dict(zip(bangla_number, english_number))

# Pre-built translation tables for str.translate() (C-level character mapping)
_english_to_bangla_table = str.maketrans(_english_to_bangla_map)
_bangla_to_english_table = str.maketrans(_bangla_to_english_map)

# Bengali month names indexed by Gregorian month (0-indexed, January=0)
# Each month corresponds to the Bengali month that overlaps with that Gregorian month
greg_equivalent_bangla_months = [
    "পৌষ",      # January  → Poush
    "মাঘ",      # February → Magh
    "ফাল্গুন",   # March    → Falgun
    "চৈত্র",     # April    → Chaitra
    "বৈশাখ",    # May      → Boishakh
    "জ্যৈষ্ঠ",   # June     → Joishtha
    "আষাঢ়",     # July     → Asharh
    "শ্রাবণ",    # August   → Shravan
    "ভাদ্র",     # September → Bhadra
    "আশ্বিন",    # October  → Ashwin
    "কার্তিক",   # November → Kartik
    "অগ্রহায়ণ", # December → Agrahayan
]

# Bengali weekday names indexed by Python weekday() (0=Monday)
python_bangla_weekdays = [
    "সোমবার",       # Monday
    "মঙ্গলবার",     # Tuesday
    "বুধবার",       # Wednesday
    "বৃহস্পতিবার",  # Thursday
    "শুক্রবার",     # Friday
    "শনিবার",       # Saturday
    "রবিবার",       # Sunday
]

# Bengali season names (6 seasons, each spanning 2 Bengali months)
greg_equivalent_bangla_seasons = [
    "শীত",    # Winter (Poush-Magh)
    "বসন্ত",   # Spring (Falgun-Chaitra)
    "গ্রীষ্ম",  # Summer (Boishakh-Joishtha)
    "বর্ষা",   # Monsoon (Asharh-Shravan)
    "শরৎ",    # Autumn (Bhadra-Ashwin)
    "হেমন্ত",  # Late Autumn (Kartik-Agrahayan)
]

# Bengali ordinal names for days 1-31
bengali_ordinals = [
    "পহেলা", "দোসরা", "তেসরা", "চৌঠা", "পাঁচই",
    "ছয়ই", "সাতই", "আটই", "নয়ই", "দশই",
    "এগারোই", "বারোই", "তেরোই", "চৌদ্দই", "পনেরোই",
    "ষোলোই", "সতেরোই", "আঠারোই", "ঊনিশে", "বিশে",
    "একুশে", "বাইশে", "তেইশে", "চব্বিশে", "পঁচিশে",
    "ছাব্বিশে", "সাতাশে", "আঠাশে", "ঊনত্রিশে", "ত্রিশে",
    "একত্রিশে",
]

# Pre-built Bangla digit string to ordinal mapping for convert_to_ordinal
# Numbers 1-31 mapped to their Bangla numeral ordinal equivalents
_bangla_digit_to_ordinal = {
    str(i).translate(_english_to_bangla_table): bengali_ordinals[i - 1]
    for i in range(1, len(bengali_ordinals) + 1)
}

# Last Gregorian day that falls in the current Bengali month for each Gregorian month
# For example, in January, the last day that is still in Poush is January 13
greg_equivalent_last_day_of_bangla_months = [
    13,  # January  - Poush ends on Jan 13
    12,  # February - Magh ends on Feb 12
    14,  # March    - Falgun ends on Mar 14 (non-leap year)
    13,  # April    - Chaitra ends on Apr 13
    14,  # May      - Boishakh ends on May 14
    14,  # June     - Joishtha ends on Jun 14
    15,  # July     - Asharh ends on Jul 15
    15,  # August   - Shravan ends on Aug 15
    15,  # September - Bhadra ends on Sep 15
    15,  # October  - Ashwin ends on Oct 15
    14,  # November - Kartik ends on Nov 14
    14,  # December - Agrahayan ends on Dec 14
]

# Total days in each Bengali month
total_days_in_bangla_months = [30, 30, 30, 30, 31, 31, 31, 31, 31, 30, 30, 30]

# Index of the Bengali month affected by leap year adjustment (Falgun = index 2)
greg_equivalent_leap_year_index_in_bangla_months = 2


def is_leap_year(passed_year: int) -> bool:
    """Check if a given year is a leap year in the Gregorian calendar.

    A year is a leap year if it is divisible by 4, except for century years
    which must be divisible by 400.

    Args:
        passed_year: The Gregorian year to check.

    Returns:
        True if the year is a leap year, False otherwise.

    Example::

        >>> is_leap_year(2020)
        True
        >>> is_leap_year(1900)
        False
        >>> is_leap_year(2000)
        True
    """
    if passed_year % 400 == 0:
        return True
    elif passed_year % 4 == 0 and passed_year % 100 != 0:
        return True
    else:
        return False


def get_bangla_year(passed_date: int, passed_month: int, passed_year: int) -> int:
    """Get the Bengali year for a given Gregorian date.

    The Bengali calendar year starts on April 14 (Pohela Boishakh).
    Dates before April 14 belong to the previous Bengali year.

    Note:
        When called from get_date(), passed_month is 0-indexed (0=January).
        When called directly, be aware that month=3 corresponds to April
        in the 0-indexed system used internally.

    Args:
        passed_date: The day of the month (1-31).
        passed_month: The month (0-indexed when called from get_date).
        passed_year: The Gregorian year.

    Returns:
        The Bengali year.

    Example::

        >>> get_bangla_year(22, 5, 2017)  # June (0-indexed: 5)
        1424
    """
    if passed_month > 3:
        bangla_year = passed_year - 593
    elif passed_month == 3 and passed_date > 13:
        bangla_year = passed_year - 593
    else:
        bangla_year = passed_year - 594
    return bangla_year


def get_bangla_weekday(passed_date: int, passed_month: int, passed_year: int) -> str:
    """Get the Bengali weekday name for a given Gregorian date.

    Uses Zeller's congruence for efficient weekday calculation without
    creating a datetime object.

    Args:
        passed_date: The day of the month (1-31).
        passed_month: The month (1-indexed: 1=January, 12=December).
        passed_year: The Gregorian year.

    Returns:
        The Bengali weekday name.

    Example::

        >>> get_bangla_weekday(22, 6, 2017)
        'বৃহস্পতিবার'
    """
    m = passed_month
    y = passed_year
    d = passed_date
    if m < 3:
        m += 12
        y -= 1
    K = y % 100
    J = y // 100
    h = (d + (13 * (m + 1)) // 5 + K + K // 4 + J // 4 + 5 * J) % 7
    python_weekday = (h + 5) % 7
    return python_bangla_weekdays[python_weekday]


def _convert_digits(original, source_digits, target_digits):
    """Convert digit characters in a string from one numeral system to another.

    This is the legacy implementation kept for backward compatibility.
    The optimized convert_english_digit_to_bangla_digit and
    convert_bangla_digit_to_english_digit functions use str.translate()
    for significantly better performance.

    Args:
        original: The input value (string or number).
        source_digits: List of source digit characters.
        target_digits: List of target digit characters.

    Returns:
        String with digit characters converted.
    """
    converted = ""
    for character in str(original):
        if character in source_digits:
            converted += target_digits[source_digits.index(character)]
        else:
            converted += character
    return converted


def convert_english_digit_to_bangla_digit(original) -> str:
    """Convert English numeral characters in a string to Bangla numerals.

    Non-digit characters are left unchanged. This function uses
    str.translate() for C-level performance.

    Args:
        original: The input string or number containing English digits.

    Returns:
        A string with English digits (0-9) replaced by Bangla digits (০-৯).

    Example::

        >>> convert_english_digit_to_bangla_digit("123456")
        '১২৩৪৫৬'
        >>> convert_english_digit_to_bangla_digit("Price: 500")
        'Price: ৫০০'
        >>> convert_english_digit_to_bangla_digit(2024)
        '২০২৪'
    """
    return str(original).translate(_english_to_bangla_table)


def convert_bangla_digit_to_english_digit(original) -> str:
    """Convert Bangla numeral characters in a string to English numerals.

    Non-digit characters are left unchanged. This function uses
    str.translate() for C-level performance.

    Args:
        original: The input string containing Bangla digits.

    Returns:
        A string with Bangla digits (০-৯) replaced by English digits (0-9).

    Example::

        >>> convert_bangla_digit_to_english_digit("১২৩৪৫৬")
        '123456'
        >>> convert_bangla_digit_to_english_digit("বাংলাদেশ ১৭ কোটি")
        'বাংলাদেশ 17 কোটি'
    """
    return str(original).translate(_bangla_to_english_table)


def convert_to_ordinal(day: str) -> str:
    """Convert a day number to its Bengali ordinal representation.

    Accepts day numbers as either Bangla digit strings (e.g., "২১")
    or English digit strings (e.g., "21"). Valid day numbers are 1-31.

    Args:
        day: A string representing a day number (1-31) in either
             Bangla or English digits.

    Returns:
        The Bengali ordinal string, or an empty string if the day
        is out of range (0 or >31).

    Example::

        >>> convert_to_ordinal("২১")
        'একুশে'
        >>> convert_to_ordinal("1")
        'পহেলা'
        >>> convert_to_ordinal("32")
        ''
    """
    if day in _bangla_digit_to_ordinal:
        return _bangla_digit_to_ordinal[day]
    d = int(convert_bangla_digit_to_english_digit(day))
    if 1 <= d <= len(bengali_ordinals):
        return bengali_ordinals[d - 1]
    return ""


def get_date(
    passed_date: int | None = None,
    passed_month: int | None = None,
    passed_year: int | None = None,
    ordinal: bool | None = False,
) -> dict:
    """Convert a Gregorian date to the Bengali calendar date.

    Returns a dictionary containing the Bengali date, month, year,
    season, and weekday. Optionally includes the Bengali ordinal
    representation of the day.

    When called with no arguments, returns today's Bengali date.

    The conversion follows the revised Bengali calendar (Bangabda)
    officially adopted in Bangladesh in 1987.

    Args:
        passed_date: The Gregorian day of the month (1-31).
            If None, uses today's date.
        passed_month: The Gregorian month (1=January, 12=December).
            If None, uses today's month.
        passed_year: The Gregorian year.
            If None, uses today's year.
        ordinal: If True, includes the Bengali ordinal representation
            of the day in the result dictionary.

    Returns:
        A dictionary with the following keys:
        - "date": Bengali date as a Bangla numeral string (e.g., "৮")
        - "month": Bengali month name (e.g., "আষাঢ়")
        - "year": Bengali year as a Bangla numeral string (e.g., "১৪২৪")
        - "season": Bengali season name (e.g., "বর্ষা")
        - "weekday": Bengali weekday name (e.g., "বৃহস্পতিবার")
        - "ordinal": (optional) Bengali ordinal (e.g., "আটই")

    Example::

        >>> get_date(22, 6, 2017)
        {'date': '৮', 'month': 'আষাঢ়', 'year': '১৪২৪',
         'season': 'বর্ষা', 'weekday': 'বৃহস্পতিবার'}

        >>> get_date(22, 6, 2017, ordinal=True)
        {'date': '৮', 'month': 'আষাঢ়', 'year': '১৪২৪',
         'season': 'বর্ষা', 'weekday': 'বৃহস্পতিবার', 'ordinal': 'আটই'}

        >>> get_date()  # Today's Bengali date
        {'date': '...', 'month': '...', 'year': '...',
         'season': '...', 'weekday': '...'}
    """
    if passed_date is None and passed_month is None and passed_year is None:
        current_date_object = datetime.date.today()
        passed_year = current_date_object.year
        passed_month = current_date_object.month
        passed_date = current_date_object.day
    bangla_weekday = get_bangla_weekday(passed_date, passed_month, passed_year)
    passed_month = passed_month - 1
    bangla_year = get_bangla_year(passed_date, passed_month, passed_year)
    if passed_date <= greg_equivalent_last_day_of_bangla_months[passed_month]:
        total_days_in_current_bangla_month = total_days_in_bangla_months[passed_month]
        if (
                passed_month == greg_equivalent_leap_year_index_in_bangla_months
                and is_leap_year(passed_year)
        ):
            total_days_in_current_bangla_month += 1
        bangla_date = (
                total_days_in_current_bangla_month + passed_date
                - greg_equivalent_last_day_of_bangla_months[passed_month]
        )
        bangla_month_index = passed_month
        bangla_month = greg_equivalent_bangla_months[bangla_month_index]
    else:
        bangla_date = (
                passed_date - greg_equivalent_last_day_of_bangla_months[passed_month]
        )
        bangla_month_index = (passed_month + 1) % 12
        bangla_month = greg_equivalent_bangla_months[bangla_month_index]

    bangla_season = greg_equivalent_bangla_seasons[bangla_month_index // 2]

    bangla_date_month_year_season = {
        "date": convert_english_digit_to_bangla_digit(bangla_date),
        "month": bangla_month,
        "year": convert_english_digit_to_bangla_digit(bangla_year),
        "season": bangla_season,
        "weekday": bangla_weekday,
    }

    if ordinal:
        bangla_date_month_year_season["ordinal"] = convert_to_ordinal(bangla_date_month_year_season["date"])

    return bangla_date_month_year_season
