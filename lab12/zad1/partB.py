import unittest
import requests
from unittest.mock import *



class Test_randomuser(unittest.TestCase):
    @patch("requests.get", return_value={"info": {}})
    def test_if_info_field_is_in_response(self, value):
        responseData = requests.get("https://randomuser.me/api/")
        self.assertIn("info", responseData)


    @patch("requests.get", return_value={"results": {}, "info": {}})
    def test_json_is_dict(self, value):
        res = requests.get("https://randomuser.me/api/")
        self.assertIsInstance(res, dict)


    @patch("requests.get", return_value={"results": {}})
    def test_results_key_exists(self, value):
        res = requests.get("https://randomuser.me/api/")
        self.assertIn("results", res.keys())


    @patch("requests.get", return_value={"results": [{"gender": "female"}]})
    def test_results_non_empty(self, value):
        res = requests.get("https://randomuser.me/api/")
        self.assertTrue(bool(res["results"]))

    @patch("requests.get", return_value={"results": [{"gender": "female"}]})
    def test_results_is_list(self, value):
        res = requests.get("https://randomuser.me/api/")
        self.assertIsInstance(res["results"], list)


    @patch("requests.get", return_value={'results': [{'gender': 'male', 'name': {'title': 'Mr', 'first': 'Hans-Karl', 'last': 'Gold'}, 'location': {'street': {'number': 7547, 'name': 'Dorfstraße'}, 'city': 'Lambrecht (Pfalz)', 'state': 'Berlin', 'country': 'Germany', 'postcode': 94060, 'coordinates': {'latitude': '-40.7523', 'longitude': '-148.5938'}, 'timezone': {'offset': '-2:00', 'description': 'Mid-Atlantic'}}, 'email': 'hans-karl.gold@example.com', 'login': {'uuid': '636c372e-17b6-49fe-805a-b73811570481', 'username': 'greenmouse764', 'password': '1959', 'salt': 'hBQAK86t', 'md5': 'f202e4ce9b94e03448eb43c719282ada', 'sha1': '59ac70678c84fc76e63b411d58e1077f03b42354', 'sha256': '3b3461b255f524e20261a8b15d19eef35bd81a02de4881b0e56152d1925707ce'}, 'dob': {'date': '1970-01-03T23:52:30.949Z', 'age': 52}, 'registered': {'date': '2006-06-25T19:44:50.003Z', 'age': 16}, 'phone': '0013-4025142', 'cell': '0170-2491890', 'id': {'name': '', 'value': None}, 'picture': {'large': 'https://randomuser.me/api/portraits/men/51.jpg', 'medium': 'https://randomuser.me/api/portraits/med/men/51.jpg', 'thumbnail': 'https://randomuser.me/api/portraits/thumb/men/51.jpg'}, 'nat': 'DE'}]})
    def test_dicts_in_results_list(self, value):
        res = requests.get("https://randomuser.me/api/")
        for data_type in res["results"]:
            self.assertIsInstance(data_type, dict)

    @patch("requests.get", return_value={"info": {}})
    def test_info_key_exists(self, value):
        res = requests.get("https://randomuser.me/api/")
        self.assertIn("info", res.keys())

    @patch("requests.get", return_value={'info': {'seed': '25bf592a9c830376', 'results': 1}})
    def test_info_non_empty(self, value):
        res = requests.get("https://randomuser.me/api/")
        self.assertTrue(bool(res["info"]))

    @patch("requests.get", return_value={"info": {}})
    def test_info_is_dict(self, value):
        res = requests.get("https://randomuser.me/api/")
        self.assertIsInstance(res["info"], dict)


    @patch("requests.get", return_value={"results": [{"gender": "female"}]})
    def test_gender_is_male_or_female(self, value):
        res = requests.get("https://randomuser.me/api/")
        self.assertTrue(res["results"][0]["gender"] == "male" or res["results"][0]["gender"] == "female")

    @patch("requests.get", return_value={'results': [{'name': {'title': 'Mrs', 'first': 'Emeline', 'last': 'Rodriguez'}}]})
    def test_full_name(self, value):
        res = requests.get("https://randomuser.me/api/")
        self.assertTrue(bool(res["results"][0]["name"]["first"]) and bool(res["results"][0]["name"]["last"]))


    @patch("requests.get", return_value={'results': [{"location": {"street": {"number" : 129}}}]})
    def test_location_address_is_number(self, value):
        res = requests.get("https://randomuser.me/api/")
        self.assertIsInstance(res["results"][0]["location"]["street"]["number"], int)

    @patch("requests.get", return_value={'results': [{"location": {"coordinates": {"latitude" : "129.29"}}}]})
    def test_latitude_is_float(self, value):
        res = requests.get("https://randomuser.me/api/")
        self.assertIn(".", res["results"][0]["location"]["coordinates"]["latitude"])

    @patch("requests.get", return_value={'results': [{"location": {"coordinates": {"longitude" : "129.29"}}}]})
    def test_longtitude_float(self, value):
        res = requests.get("https://randomuser.me/api/")
        self.assertIn(".", res["results"][0]["location"]["coordinates"]["longitude"])

    @patch("requests.get", return_value={'info': {'seed': '4f4720f2b85503fe', 'results': 1, 'page': 1, 'version': '1.3'}})
    def test_info_correct_keys(self, value):
        res = requests.get("https://randomuser.me/api/")
        for value in ["seed", "results", "page", "version"]:
            self.assertTrue(value in res["info"].keys())