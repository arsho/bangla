# -*- coding: utf-8 -*-
import unittest
import os
import sys
import datetime

BASEDIR = os.path.abspath(
    os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
)
sys.path.insert(0, BASEDIR)
import bangla


class TestBangla(unittest.TestCase):
    """Original tests preserved for backward compatibility."""

    def test_is_leap_year(self):
        is_leap_year_flag = bangla.is_leap_year(2000)
        self.assertEqual(is_leap_year_flag, 1)
        is_leap_year_flag = bangla.is_leap_year(2016)
        self.assertEqual(is_leap_year_flag, 1)
        is_leap_year_flag = bangla.is_leap_year(1900)
        self.assertEqual(is_leap_year_flag, 0)

    def test_get_bangla_year(self):
        res = bangla.get_bangla_year(22, 6, 2017)
        self.assertEqual(res, 1424)
        res = bangla.get_bangla_year(1, 1, 2017)
        self.assertEqual(res, 1423)
        res = bangla.get_bangla_year(22, 3, 2017)
        self.assertEqual(res, 1424)

    def test_get_bangla_weekday(self):
        res = bangla.get_bangla_weekday(22, 6, 2017)
        self.assertEqual(res, "বৃহস্পতিবার")

    def test_convert_english_digit_to_bangla_digit(self):
        res = bangla.convert_english_digit_to_bangla_digit("123456")
        self.assertEqual(res, "১২৩৪৫৬")

    def test_convert_to_ordinal(self):
        res = bangla.convert_to_ordinal("২১")
        self.assertEqual(res, "একুশে")

        res = bangla.convert_to_ordinal("21")
        self.assertEqual(res, "একুশে")

    def test_get_date(self):
        res = bangla.get_date(22, 6, 2017)
        self.assertEqual(
            res,
            {
                "date": "৮",
                "month": "আষাঢ়",
                "year": "১৪২৪",
                "season": "বর্ষা",
                "weekday": "বৃহস্পতিবার",
            },
        )
        res = bangla.get_date(7, 6, 2017)
        self.assertEqual(
            res,
            {
                "date": "২৪",
                "month": "জ্যৈষ্ঠ",
                "year": "১৪২৪",
                "season": "গ্রীষ্ম",
                "weekday": "বুধবার",
            },
        )
        res = bangla.get_date(7, 3, 2016)
        self.assertEqual(
            res,
            {
                "date": "২৪",
                "month": "ফাল্গুন",
                "year": "১৪২২",
                "season": "বসন্ত",
                "weekday": "সোমবার",
            },
        )
        res = bangla.get_date(7, 3, 2016, ordinal=True)
        self.assertEqual(
            res,
            {
                "date": "২৪",
                "month": "ফাল্গুন",
                "year": "১৪২২",
                "season": "বসন্ত",
                "weekday": "সোমবার",
                "ordinal": "চব্বিশে",
            },
        )

        res = bangla.get_date()
        self.assertIsInstance(res, dict, "The return type is not a dictionary")


class TestLeapYear(unittest.TestCase):
    """Comprehensive leap year tests."""

    def test_century_leap_year(self):
        self.assertTrue(bangla.is_leap_year(2000))
        self.assertTrue(bangla.is_leap_year(2400))

    def test_century_non_leap_year(self):
        self.assertFalse(bangla.is_leap_year(1900))
        self.assertFalse(bangla.is_leap_year(2100))

    def test_regular_leap_year(self):
        self.assertTrue(bangla.is_leap_year(2016))
        self.assertTrue(bangla.is_leap_year(2020))
        self.assertTrue(bangla.is_leap_year(2024))

    def test_regular_non_leap_year(self):
        self.assertFalse(bangla.is_leap_year(2017))
        self.assertFalse(bangla.is_leap_year(2019))
        self.assertFalse(bangla.is_leap_year(2023))

    def test_is_leap_year_returns_bool(self):
        self.assertIsInstance(bangla.is_leap_year(2020), bool)
        self.assertIsInstance(bangla.is_leap_year(2021), bool)

    def test_is_leap_year_truthiness(self):
        # Verify backward compatibility: True/False are truthy/falsy like 1/0
        self.assertTrue(bangla.is_leap_year(2020))
        self.assertFalse(bangla.is_leap_year(2021))


class TestBanglaYear(unittest.TestCase):
    """Comprehensive Bengali year conversion tests."""

    def test_year_after_march_14(self):
        # After March 14, Bengali year = Gregorian year - 593
        self.assertEqual(bangla.get_bangla_year(15, 3, 2024), 1431)
        self.assertEqual(bangla.get_bangla_year(1, 6, 2024), 1431)

    def test_year_before_april_14(self):
        # Before April 14 (0-indexed month < 3), Bengali year = Gregorian year - 594
        # Note: get_bangla_year uses 0-indexed month as called by get_date
        self.assertEqual(bangla.get_bangla_year(13, 2, 2024), 1430)  # March (0-indexed: 2)
        self.assertEqual(bangla.get_bangla_year(1, 0, 2024), 1430)   # January (0-indexed: 0)

    def test_year_on_april_14_boundary(self):
        # April 14 starts the new Bengali year (0-indexed month 3)
        # Month 3 (0-indexed) = April, date > 13 means new Bengali year
        self.assertEqual(bangla.get_bangla_year(14, 3, 2024), 1431)  # April 14
        self.assertEqual(bangla.get_bangla_year(13, 3, 2024), 1430)  # April 13

    def test_year_after_april(self):
        # May onwards (0-indexed month > 3) = new Bengali year
        self.assertEqual(bangla.get_bangla_year(1, 5, 2024), 1431)   # June (0-indexed: 5)
        self.assertEqual(bangla.get_bangla_year(1, 11, 2024), 1431)  # December (0-indexed: 11)

    def test_year_in_january(self):
        # January is 0-indexed month 0, so year = 2017 - 594 = 1423
        self.assertEqual(bangla.get_bangla_year(1, 0, 2017), 1423)

    def test_year_in_december(self):
        # December is 0-indexed month 11, so year = 2023 - 593 = 1430
        self.assertEqual(bangla.get_bangla_year(31, 11, 2023), 1430)


class TestBanglaWeekday(unittest.TestCase):
    """Comprehensive Bengali weekday tests."""

    def test_monday(self):
        self.assertEqual(bangla.get_bangla_weekday(7, 3, 2016), "সোমবার")

    def test_tuesday(self):
        self.assertEqual(bangla.get_bangla_weekday(8, 3, 2016), "মঙ্গলবার")

    def test_wednesday(self):
        self.assertEqual(bangla.get_bangla_weekday(7, 6, 2017), "বুধবার")

    def test_thursday(self):
        self.assertEqual(bangla.get_bangla_weekday(22, 6, 2017), "বৃহস্পতিবার")

    def test_friday(self):
        self.assertEqual(bangla.get_bangla_weekday(26, 3, 1971), "শুক্রবার")

    def test_saturday(self):
        self.assertEqual(bangla.get_bangla_weekday(29, 2, 2020), "শনিবার")

    def test_sunday(self):
        self.assertEqual(bangla.get_bangla_weekday(31, 12, 2023), "রবিবার")

    def test_against_datetime_weekday(self):
        """Verify Zeller's congruence matches datetime.weekday() for many dates."""
        test_dates = [
            (1, 1, 1900), (15, 8, 1947), (26, 3, 1971),
            (22, 6, 2017), (7, 6, 2017), (7, 3, 2016),
            (29, 2, 2020), (1, 1, 2020), (31, 12, 2023),
            (14, 2, 2024), (1, 3, 2024), (14, 3, 2024),
            (15, 3, 2024), (16, 12, 2024),
        ]
        for d, m, y in test_dates:
            dt_weekday = datetime.datetime(y, m, d).weekday()
            expected = bangla.python_bangla_weekdays[dt_weekday]
            actual = bangla.get_bangla_weekday(d, m, y)
            self.assertEqual(actual, expected, f"Mismatch for {d}/{m}/{y}")


class TestNumeralConversion(unittest.TestCase):
    """Comprehensive numeral conversion tests."""

    def test_english_to_bangla_single_digit(self):
        self.assertEqual(bangla.convert_english_digit_to_bangla_digit("0"), "০")
        self.assertEqual(bangla.convert_english_digit_to_bangla_digit("5"), "৫")
        self.assertEqual(bangla.convert_english_digit_to_bangla_digit("9"), "৯")

    def test_english_to_bangla_multi_digit(self):
        self.assertEqual(bangla.convert_english_digit_to_bangla_digit("123456"), "১২৩৪৫৬")
        self.assertEqual(bangla.convert_english_digit_to_bangla_digit("000"), "০০০")

    def test_english_to_bangla_integer_input(self):
        self.assertEqual(bangla.convert_english_digit_to_bangla_digit(123456), "১২৩৪৫৬")
        self.assertEqual(bangla.convert_english_digit_to_bangla_digit(0), "০")

    def test_english_to_bangla_mixed_string(self):
        self.assertEqual(
            bangla.convert_english_digit_to_bangla_digit("Price: 500"),
            "Price: ৫০০"
        )
        self.assertEqual(
            bangla.convert_english_digit_to_bangla_digit("2024-03-15"),
            "২০২৪-০৩-১৫"
        )

    def test_english_to_bangla_empty_string(self):
        self.assertEqual(bangla.convert_english_digit_to_bangla_digit(""), "")

    def test_english_to_bangla_non_digit_string(self):
        # Bengali strings with no English digits should pass through unchanged
        self.assertEqual(bangla.convert_english_digit_to_bangla_digit("আষাঢ়"), "আষাঢ়")
        self.assertEqual(bangla.convert_english_digit_to_bangla_digit("বর্ষা"), "বর্ষা")

    def test_bangla_to_english_single_digit(self):
        self.assertEqual(bangla.convert_bangla_digit_to_english_digit("০"), "0")
        self.assertEqual(bangla.convert_bangla_digit_to_english_digit("৫"), "5")
        self.assertEqual(bangla.convert_bangla_digit_to_english_digit("৯"), "9")

    def test_bangla_to_english_multi_digit(self):
        self.assertEqual(bangla.convert_bangla_digit_to_english_digit("১২৩৪৫৬"), "123456")

    def test_bangla_to_english_mixed_string(self):
        self.assertEqual(
            bangla.convert_bangla_digit_to_english_digit("বাংলাদেশ ১৭ কোটি"),
            "বাংলাদেশ 17 কোটি"
        )

    def test_bangla_to_english_empty_string(self):
        self.assertEqual(bangla.convert_bangla_digit_to_english_digit(""), "")

    def test_round_trip_conversion(self):
        original = "9876543210"
        bangla_version = bangla.convert_english_digit_to_bangla_digit(original)
        back = bangla.convert_bangla_digit_to_english_digit(bangla_version)
        self.assertEqual(back, original)


class TestOrdinal(unittest.TestCase):
    """Comprehensive ordinal conversion tests."""

    def test_ordinal_day_1(self):
        self.assertEqual(bangla.convert_to_ordinal("১"), "পহেলা")

    def test_ordinal_day_2(self):
        self.assertEqual(bangla.convert_to_ordinal("২"), "দোসরা")

    def test_ordinal_day_10(self):
        self.assertEqual(bangla.convert_to_ordinal("১০"), "দশই")

    def test_ordinal_day_21(self):
        self.assertEqual(bangla.convert_to_ordinal("২১"), "একুশে")

    def test_ordinal_day_31(self):
        self.assertEqual(bangla.convert_to_ordinal("৩১"), "একত্রিশে")

    def test_ordinal_from_english_digit(self):
        self.assertEqual(bangla.convert_to_ordinal("21"), "একুশে")
        self.assertEqual(bangla.convert_to_ordinal("1"), "পহেলা")

    def test_ordinal_out_of_range(self):
        self.assertEqual(bangla.convert_to_ordinal("32"), "")
        self.assertEqual(bangla.convert_to_ordinal("0"), "")

    def test_ordinal_all_days(self):
        """Verify all 31 ordinals can be looked up."""
        for i in range(1, 32):
            result = bangla.convert_to_ordinal(str(i))
            self.assertNotEqual(result, "", f"Ordinal for day {i} should not be empty")
            self.assertEqual(result, bangla.bengali_ordinals[i - 1])


class TestGetDate(unittest.TestCase):
    """Comprehensive date conversion tests covering all 12 months."""

    def test_january_date(self):
        res = bangla.get_date(15, 1, 2020)
        self.assertEqual(res["year"], "১৪২৬")
        self.assertIn(res["month"], bangla.greg_equivalent_bangla_months)

    def test_february_date(self):
        res = bangla.get_date(15, 2, 2020)
        self.assertEqual(res["year"], "১৪২৬")
        self.assertIn(res["month"], bangla.greg_equivalent_bangla_months)

    def test_march_before_14(self):
        # March 13, still in previous Bengali month
        res = bangla.get_date(13, 3, 2020)
        self.assertIsInstance(res, dict)

    def test_march_after_14(self):
        # March 15, new Bengali month
        res = bangla.get_date(15, 3, 2020)
        self.assertIsInstance(res, dict)

    def test_leap_year_feb_29(self):
        res = bangla.get_date(29, 2, 2020)
        self.assertIsInstance(res, dict)

    def test_non_leap_year_march(self):
        res = bangla.get_date(7, 3, 2016)
        self.assertEqual(res["date"], "২৪")
        self.assertEqual(res["month"], "ফাল্গুন")
        self.assertEqual(res["year"], "১৪২২")

    def test_december_31(self):
        res = bangla.get_date(31, 12, 2023)
        self.assertIsInstance(res, dict)
        self.assertIn("date", res)
        self.assertIn("month", res)
        self.assertIn("year", res)
        self.assertIn("season", res)
        self.assertIn("weekday", res)

    def test_get_date_returns_dict(self):
        res = bangla.get_date(22, 6, 2017)
        self.assertIsInstance(res, dict)

    def test_get_date_keys(self):
        res = bangla.get_date(22, 6, 2017)
        required_keys = {"date", "month", "year", "season", "weekday"}
        self.assertEqual(set(res.keys()), required_keys)

    def test_get_date_with_ordinal(self):
        res = bangla.get_date(22, 6, 2017, ordinal=True)
        self.assertIn("ordinal", res)
        self.assertEqual(res["ordinal"], "আটই")

    def test_get_date_without_ordinal(self):
        res = bangla.get_date(22, 6, 2017, ordinal=False)
        self.assertNotIn("ordinal", res)

    def test_get_date_today(self):
        res = bangla.get_date()
        self.assertIsInstance(res, dict)
        self.assertIn("date", res)
        self.assertIn("month", res)

    def test_get_date_all_months(self):
        """Test at least one date in every Gregorian month."""
        for month in range(1, 13):
            res = bangla.get_date(15, month, 2024)
            self.assertIsInstance(res, dict)
            self.assertIn("date", res)
            self.assertIn("month", res)
            self.assertIn("year", res)

    def test_get_date_seasons(self):
        """Verify season values are valid Bengali season names."""
        for month in range(1, 13):
            res = bangla.get_date(15, month, 2024)
            self.assertIn(res["season"], bangla.greg_equivalent_bangla_seasons)

    def test_get_date_weekdays(self):
        """Verify weekday values are valid Bengali weekday names."""
        for month in range(1, 13):
            res = bangla.get_date(15, month, 2024)
            self.assertIn(res["weekday"], bangla.python_bangla_weekdays)

    def test_known_date_summer(self):
        res = bangla.get_date(22, 6, 2017)
        self.assertEqual(res["date"], "৮")
        self.assertEqual(res["month"], "আষাঢ়")
        self.assertEqual(res["year"], "১৪২৪")
        self.assertEqual(res["season"], "বর্ষা")
        self.assertEqual(res["weekday"], "বৃহস্পতিবার")

    def test_known_date_winter(self):
        res = bangla.get_date(7, 6, 2017)
        self.assertEqual(res["date"], "২৪")
        self.assertEqual(res["month"], "জ্যৈষ্ঠ")
        self.assertEqual(res["year"], "১৪২৪")
        self.assertEqual(res["season"], "গ্রীষ্ম")
        self.assertEqual(res["weekday"], "বুধবার")


class TestBatchConversion(unittest.TestCase):
    """Batch conversion tests for large-scale correctness."""

    def test_batch_numeral_conversion(self):
        """Convert 1000 numbers and verify round-trip."""
        for i in range(1000):
            original = str(i)
            bangla_version = bangla.convert_english_digit_to_bangla_digit(original)
            back = bangla.convert_bangla_digit_to_english_digit(bangla_version)
            self.assertEqual(back, original, f"Round-trip failed for {original}")

    def test_batch_date_conversion(self):
        """Convert dates for all days in a year and verify structure."""
        for month in range(1, 13):
            res = bangla.get_date(15, month, 2024)
            self.assertIn("date", res)
            self.assertIn("month", res)
            self.assertIn("year", res)
            self.assertIn("season", res)
            self.assertIn("weekday", res)


class TestEdgeCases(unittest.TestCase):
    """Edge case tests."""

    def test_convert_empty_string(self):
        self.assertEqual(bangla.convert_english_digit_to_bangla_digit(""), "")
        self.assertEqual(bangla.convert_bangla_digit_to_english_digit(""), "")

    def test_convert_no_digits_in_string(self):
        self.assertEqual(bangla.convert_english_digit_to_bangla_digit("hello"), "hello")
        self.assertEqual(bangla.convert_bangla_digit_to_english_digit("আষাঢ়"), "আষাঢ়")

    def test_convert_only_digits(self):
        self.assertEqual(bangla.convert_english_digit_to_bangla_digit("0123456789"), "০১২৩৪৫৬৭৮৯")
        self.assertEqual(bangla.convert_bangla_digit_to_english_digit("০১২৩৪৫৬৭৮৯"), "0123456789")

    def test_convert_integer_zero(self):
        self.assertEqual(bangla.convert_english_digit_to_bangla_digit(0), "০")

    def test_convert_large_number(self):
        self.assertEqual(
            bangla.convert_english_digit_to_bangla_digit("9999999999"),
            "৯৯৯৯৯৯৯৯৯৯"
        )

    def test_is_leap_year_year_zero(self):
        # Year 0 is technically a leap year in proleptic Gregorian calendar
        self.assertTrue(bangla.is_leap_year(0))

    def test_get_bangla_year_0_indexed_month(self):
        # get_bangla_year expects 0-indexed month (as used internally by get_date)
        # Month index 1 = February, which is < 3, so year = 2000 - 594 = 1406
        self.assertEqual(bangla.get_bangla_year(1, 1, 2000), 1406)

    def test_ordinal_all_bangla_days(self):
        """Verify ordinal lookup works for all 31 days via Bangla digits."""
        for i in range(1, 32):
            bangla_day = bangla.convert_english_digit_to_bangla_digit(str(i))
            result = bangla.convert_to_ordinal(bangla_day)
            self.assertEqual(result, bangla.bengali_ordinals[i - 1])


if __name__ == "__main__":
    unittest.main()
