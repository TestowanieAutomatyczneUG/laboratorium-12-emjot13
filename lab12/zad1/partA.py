import unittest
import requests


class Tests(unittest.TestCase):
    def setUp(self):
        self.res = requests.get("https://randomuser.me/api/").json()

    def test_json_is_dict(self):
        self.assertIsInstance(self.res, dict)

    def test_results_key_exists(self):
        self.assertIn("results", self.res.keys())
    
    def test_results_non_empty(self):
        self.assertTrue(bool(self.res["results"]))

    def test_results_is_list(self):
        self.assertIsInstance(self.res["results"], list)

    def test_dicts_in_results_list(self):
        for data_type in self.res["results"]:
            self.assertIsInstance(data_type, dict)

    def test_info_key_exists(self):
        self.assertIn("info", self.res.keys())

    def test_info_non_empty(self):
        self.assertTrue(bool(self.res["info"]))

    def test_info_is_dict(self):
        self.assertIsInstance(self.res["info"], dict)
    
    def test_gender_is_male_or_female(self):
        self.assertTrue(self.res["results"][0]["gender"] == "male" or self.res["results"][0]["gender"] == "female")

    def test_full_name(self):
        self.assertTrue(bool(self.res["results"][0]["name"]["first"]) and bool(self.res["results"][0]["name"]["last"]))

    def test_location_address_is_number(self):
        self.assertIsInstance(self.res["results"][0]["location"]["street"]["number"], int)

    def test_latitude_is_float(self):
        self.assertIn(".", self.res["results"][0]["location"]["coordinates"]["latitude"])

    def test_longtitude_float(self):
        self.assertIn(".", self.res["results"][0]["location"]["coordinates"]["longitude"])

    def test_info_correct_keys(self):
        for value in ["seed", "results", "page", "version"]:
            self.assertTrue(value in self.res["info"].keys())

