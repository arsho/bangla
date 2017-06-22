# -*- coding: utf-8 -*-
import unittest
import datetime
import time
import os
import sys
BASEDIR = os.path.abspath(os.path.join(
                          os.path.dirname(os.path.abspath(__file__)),
                          ".."))
sys.path.insert(0, BASEDIR)
import bangla
import locale

class TestBangla(unittest.TestCase):
    def test_is_leap_year(self):
        is_leap_year_flag = bangla.is_leap_year(2000)
        self.assertEqual(is_leap_year_flag, 1)

    def test_get_bangla_year(self):
        res = bangla.get_bangla_year(22,6,2017)
        self.assertEqual(res, 1424)

    def test_get_bangla_weekday(self):
        res = bangla.get_bangla_weekday(22,6,2017)
        self.assertEqual(res, "বৃহস্পতিবার")

    def test_convert_english_digit_to_bangla_digit(self):
        res = bangla.convert_english_digit_to_bangla_digit("123456")
        self.assertEqual(res, "১২৩৪৫৬")

    def test_get_date(self):
        res = bangla.get_date(22,6,2017)
        self.assertEqual(res, {'date': '৮', 'month': 'আষাঢ়', 'year': '১৪২৪', 'season': 'বর্ষা', 'weekday': 'বৃহস্পতিবার'})
        
if __name__ == "__main__":
    unittest.main()
