BANGLA
======

|Version| |Python| |Size|

Bangla is a Python package for converting Gregorian dates to the Bengali calendar, translating English numerals to Bangla numerals, and generating Bangla ordinals for dates.
It computes the full Bengali calendar date, including year, month, day, weekday, season, and ordinal based on the revised Bengali calendar (https://en.wikipedia.org/wiki/Bengali_calendars) officially adopted in Bangladesh in 1987.
(For Bengali communities in India, the calendar may differ slightly.)

The package also allows converting English numeric strings (e.g., "123") into Bangla numerals (e.g., "১২৩").
It is compatible with Linux, macOS, and Windows systems.

Features
~~~~~~~~

-  Convert Gregorian dates to Bengali calendar , including::
   - Bangla Date (১-৩১)

   - Bangla Month ("বৈশাখ", "জ্যৈষ্ঠ", "আষাঢ়", "শ্রাবণ", "ভাদ্র", "আশ্বিন", "কার্তিক", "অগ্রহায়ণ", "পৌষ", "মাঘ", "ফাল্গুন", "চৈত্র")

   - Bangla Year (১৯৮৭ - )

   - Bangla Season ("গ্রীষ্ম", "বর্ষা", "শরৎ", "হেমন্ত", "শীত", "বসন্ত")

   - Bangla Weekday ("শনিবার", "রবিবার", "সোমবার", "মঙ্গলবার", "বুধবার", "বৃহস্পতিবার", "শুক্রবার")

   - Bangla Weekday ("শনিবার", "রবিবার", "সোমবার", "মঙ্গলবার", "বুধবার", "বৃহস্পতিবার", "শুক্রবার")

   - Bangla Ordinal for dates ("পহেলা", "দোসরা", "তেসরা", ... , "একত্রিশে")

-  Convert English numeric string to Bangla numeric string (123456 -> ১২৩৪৫৬).

Installation
~~~~~~~~~~~~

We recommend install ``bangla`` through pip install.

.. code:: bash

    $ pip install bangla

Example
~~~~~~~

To get today's date in Bangla calendar:

.. code:: python

    import bangla
    bangla_date = bangla.get_date()
    print(bangla_date)
    # Output: {'date': '৮', 'month': 'আষাঢ়', 'year': '১৪২৪', 'season': 'বর্ষা', 'weekday': 'বৃহস্পতিবার'}
    # Use bangla.get_date(ordinal = True) to include the Bangla ordinal
	
To convert any Gregorian date to Bangla date :

.. code:: python

    import bangla
    bangla_date = bangla.get_date(20, 6, 2017) # date, month, year
    print(bangla_date)
    # Output: {'date': '৬', 'month': 'আষাঢ়', 'year': '১৪২৪', 'season': 'বর্ষা', 'weekday': 'মঙ্গলবার'}
	
To convert any English numeric string to Bangla numeric string :

.. code:: python

    import bangla
    bangla_numeric_string = bangla.convert_english_digit_to_bangla_digit("123456")
    print(bangla_numeric_string)
    # Output: ১২৩৪৫৬
	
Contributors
~~~~~~~~~~~~

|Contributors|

Want to contribute?

Submit a Github Pull Request (must add/update unittests) https://github.com/arsho/bangla/pulls

For suggestions or feedback, please contact https://arshovon.com/

Thanks
~~~~~~

Influenced by বঙ্গাব্দ - jQuery Plugin 
https://github.com/nuhil/bangla-calendar

.. |Version| image:: https://img.shields.io/pypi/v/bangla.svg?
   :target: http://badge.fury.io/py/bangla
   
.. |Python| image:: https://img.shields.io/pypi/pyversions/bangla.svg?
   :target: https://pypi.python.org/pypi/bangla/0.0.4
      
.. |Size| image:: https://img.shields.io/github/size/arsho/bangla/bangla/__init__.py.svg?
   :target: https://github.com/arsho/bangla/   

.. |Contributors| image:: https://contrib.rocks/image?repo=arsho/bangla
   :target: https://github.com/arsho/bangla/graphs/contributors
