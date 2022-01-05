class Subscriber:
    def __init__(self):
        self.index = 0
        self.people = []

    def string_error(self, string):
        if type(string) is not str:
            raise TypeError('Given value is not a string')

    def index_error(self, index):
        if type(index) is not int:
            raise TypeError("Index must be an integer")

    def add_person(self, person):
        self.string_error(person)
        if " " not in person:
            raise ValueError("Person must have a name and a surname")
        dic = {self.index: person, "messages": []}
        self.people.append(dic)
        self.index += 1
        return "person added"

    def delete_person(self, index):
        self.index_error(index)
        is_index = False
        for item in self.people:
            if index in item.keys():
                self.people.remove(item)
                is_index = True
                return "person deleted"
        if not is_index:
            raise ValueError("Person with given index has not been found")

    def message(self, index, message):
        self.string_error(message)
        self.index_error(index)
        is_index = False
        for item in self.people:
            if index in item.keys():
                item["messages"].append(message)
                is_index = True
                return "message sent"
        if not is_index:
            raise ValueError("Person with given index has not been found")


import unittest
from unittest import TestCase, main
from unittest.mock import *
from assertpy import *



class Tests(unittest.TestCase):
    def setUp(self):
        self.temp = Subscriber()

    def test_add_person(self):
        self.temp.add_person = Mock()
        self.temp.add_person.return_value = "person added"
        self.assertEqual(self.temp.add_person("me mike"), "person added")

    def test_add_person_not_full_name(self):
        self.temp.add_person = Mock()
        self.temp.add_person.side_effect = ValueError("Person must have a name and a surname")
        assert_that(self.temp.add_person).raises(ValueError).when_called_with("Mike")

    def test_add_person_not_string(self):
        self.temp.add_person = Mock()
        self.temp.add_person.side_effect = TypeError('Given value is not a string')
        assert_that(self.temp.add_person).raises(TypeError).when_called_with(5)

    def test_add_person_not_string_1(self):
        self.temp.add_person = Mock()
        self.temp.add_person.side_effect = TypeError('Given value is not a string')
        assert_that(self.temp.add_person).raises(TypeError).when_called_with(["mike wazowski"])

    def test_add_person_not_string_2(self):
        self.temp.add_person = Mock()
        self.temp.add_person.side_effect = TypeError('Given value is not a string')
        assert_that(self.temp.add_person).raises(TypeError).when_called_with(None)

    def test_add_person_not_string_3(self):
        self.temp.add_person = Mock()
        self.temp.add_person.side_effect = TypeError('Given value is not a string')
        assert_that(self.temp.add_person).raises(TypeError).when_called_with(False)

    def test_delete_person(self):
        self.temp.delete_person = Mock()
        self.temp.delete_person.return_value = "person deleted"
        self.assertEqual(self.temp.delete_person(0), "person deleted")

    def test_delete_person_not_int(self):
        self.temp.delete_person = Mock()
        self.temp.delete_person.side_effect = TypeError("Index must be an integer")
        assert_that(self.temp.delete_person).raises(TypeError).when_called_with("5")

    def test_delete_person_not_int1(self):
        self.temp.delete_person = Mock()
        self.temp.delete_person.side_effect = TypeError("Index must be an integer")
        assert_that(self.temp.delete_person).raises(TypeError).when_called_with([5])

    def test_delete_person_not_int2(self):
        self.temp.delete_person = Mock()
        self.temp.delete_person.side_effect = TypeError("Index must be an integer")
        assert_that(self.temp.delete_person).raises(TypeError).when_called_with(True)

    def test_delete_person_not_int3(self):
        self.temp.delete_person = Mock()
        self.temp.delete_person.side_effect = TypeError("Index must be an integer")
        assert_that(self.temp.delete_person).raises(TypeError).when_called_with(None)


    def test_message(self):
        self.temp.message = Mock()
        self.temp.message.return_value = "message sent"
        self.assertEqual(self.temp.message(0, "good luck"), "message sent")

    def test_message_person_not_int(self):
        self.temp.message = Mock()
        self.temp.message.side_effect = TypeError("Index must be an integer")
        assert_that(self.temp.message).raises(TypeError).when_called_with("5", "okk")


    def test_message_person_not_int1(self):
        self.temp.message = Mock()
        self.temp.message.side_effect = TypeError("Index must be an integer")
        assert_that(self.temp.message).raises(TypeError).when_called_with([5], "okk")


    def test_message_person_not_int2(self):
        self.temp.message = Mock()
        self.temp.message.side_effect = TypeError("Index must be an integer")
        assert_that(self.temp.message).raises(TypeError).when_called_with(None, "okk")

    def test_message_person_not_int3(self):
        self.temp.message = Mock()
        self.temp.message.side_effect = TypeError("Index must be an integer")
        assert_that(self.temp.message).raises(TypeError).when_called_with(True, "okk")

    def test_message_person_not_str(self):
        self.temp.message = Mock()
        self.temp.message.side_effect = TypeError('Given value is not a string')
        assert_that(self.temp.message).raises(TypeError).when_called_with(0, "okk")

    def test_message_person_not_str1(self):
        self.temp.message = Mock()
        self.temp.message.side_effect = TypeError('Given value is not a string')
        assert_that(self.temp.message).raises(TypeError).when_called_with(0, ["okk"])

    def test_message_person_not_str2(self):
        self.temp.message = Mock()
        self.temp.message.side_effect = TypeError('Given value is not a string')
        assert_that(self.temp.message).raises(TypeError).when_called_with(0, False)

    def test_message_person_not_str3(self):
        self.temp.message = Mock()
        self.temp.message.side_effect = TypeError('Given value is not a string')
        assert_that(self.temp.message).raises(TypeError).when_called_with(0, None)




if __name__ == '__main__':
    main()