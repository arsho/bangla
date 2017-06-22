BANGLA
======

|Build Status| |Version| |Python| |Size| |Codecov|

Bangla is a package for Bangla language users with various functionalities including Bangla date and Bangla numeric conversation.

It can be used to get Bangla date that includes year, month, date, weekday and season of Bangla year.
Bangla has used the rules from Wikipedia https://en.wikipedia.org/wiki/Bengali_calendars to convert 
Gregorian date to Bangla date. It is based on the revised version of the Bengali calendar which was officially adopted in Bangladesh in 1987.
Among the Bengali community in India, the provided date may differ.

Moreover, this package has also a method to convert English numeric string to Bangla numeric string.

This software can be used on Linux/Unix, Mac OS and Windows systems.

Features
~~~~~~~~

-  Get Bangla date that includes:

   - Bangla Date (১-৩১)

   - Bangla Month ("বৈশাখ", "জ্যৈষ্ঠ", "আষাঢ়", "শ্রাবণ", "ভাদ্র", "আশ্বিন", "কার্তিক", "অগ্রহায়ণ", "পৌষ", "মাঘ", "ফাল্গুন", "চৈত্র")

   - Bangla Year (১৯৮৭ - )

   - Bangla Season ("গ্রীষ্ম", "বর্ষা", "শরৎ", "হেমন্ত", "শীত", "বসন্ত")

   - Bangla Weekday ("শনিবার", "রবিবার", "সোমবার", "মঙ্গলবার", "বুধবার", "বৃহস্পতিবার", "শুক্রবার")

-  Convert English numeric string to Bangla numeric string (123456 -> ১২৩৪৫৬).

Installation
~~~~~~~~~~~~

We recommend install ``bangla`` through pip install using Python 3.

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

	
To convert any Gregorian date to Bangla date :

.. code:: python

    import bangla
    bangla_date = bangla.get_date(20,6,2017) # date, month, year
    print(bangla_date) 
    # Output: {'date': '৬', 'month': 'আষাঢ়', 'year': '১৪২৪', 'season': 'বর্ষা', 'weekday': 'মঙ্গলবার'}
	
To convert any English numeric string to Bangla numeric string :

.. code:: python

    import bangla
    bangla_numeric_string = bangla.convert_english_digit_to_bangla_digit("123456")
    print(bangla_numeric_string)
    # Output: ১২৩৪৫৬
	
Contribute
~~~~~~~~~~

Create Github Pull Request https://github.com/arsho/bangla/pulls

If you have suggestion use GitHub issue system or send a message in Facebook https://www.facebook.com/ars.shovon.

Thanks
~~~~~~

Influenced by বঙ্গাব্দ - jQuery Plugin 
https://github.com/nuhil/bangla-calendar

.. |Build Status| image:: https://travis-ci.org/arsho/bangla.svg?branch=master
   :target: https://travis-ci.org/arsho/bangla

.. |Version| image:: https://img.shields.io/pypi/v/bangla.svg?
   :target: http://badge.fury.io/py/bangla
   
.. |Python| image:: https://img.shields.io/pypi/pyversions/bangla.svg?
   :target: https://pypi.python.org/pypi/bangla/0.0.1
      
.. |Size| image:: https://img.shields.io/github/size/arsho/bangla/bangla/__init__.py.svg?
   :target: https://github.com/arsho/bangla/   
   
.. |Codecov| image:: https://codecov.io/github/arsho/bangla/coverage.svg?branch=master
   :target: https://github.com/arsho/bangla/      