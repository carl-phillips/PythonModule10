import unittest
from unittest.mock import patch
from class_definitions import student as s


class MyTestSet(unittest.TestCase):
    def setUp(self):
        self.student = s.Student('Phillips', 'Carl', 'CIS', 3.78)

    def tearDown(self):
        del self.student

    def test_object_created_required_attributes(self):
        self.assertEqual(self.student.last_name, 'Phillips')
        self.assertEqual(self.student.first_name, 'Carl')


if __name__ == '__main__':
    unittest.main()
