import json
import unittest
from datetime import timedelta


class TestChbMitSummaryParser(unittest.TestCase):
    def test_parse_chb_summary(self):
        from esdap.helpers import parse_chb_summary

        testfiles_path = "./tests/files/"
        summary_file = testfiles_path + "chb23-summary.txt"
        parsed_summary_file = testfiles_path + "parsed_chb23_summary.json"
        with open(parsed_summary_file) as f:
            parsed_json = json.load(f)
        parsed_summary = parse_chb_summary(summary_file)
        self.assertDictEqual(parsed_summary, parsed_json)


class TestParseGt24HoursTime(unittest.TestCase):
    def test_parse_gt_24_hours_time(self):
        from esdap.helpers import parse_gt_24_hours_time

        self.assertEqual(parse_gt_24_hours_time("24:01:01"), timedelta(1, 61))
        self.assertEqual(parse_gt_24_hours_time("23:01:01"), timedelta(0, 82861))