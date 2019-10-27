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

    def test_object_created_all_attributes(self):
        self.assertEqual(self.student.last_name, 'Phillips')
        self.assertEqual(self.student.first_name, 'Carl')
        self.assertEqual(self.student.major, 'CIS')
        self.assertEqual(self.student.gpa, 3.78)

    def test_student_str(self):
        a = s.Student('Phillips', 'Carl', 'CIS', 3.78)
        self.assertEqual(a.__str__(), "Phillips, Carl has major CIS with gpa: 3.78")

    def test_object_not_create_error_last_name(self):
        with self.assertRaises(ValueError):
            a = s.Student()

    def test_object_not_created_error_first_name(self):
        with self.assertRaises(ValueError):
            a = s.Student()

    def test_object_not_create_error_major(self):
        with self.assertRaises(ValueError):
            a = s.Student()

    def test_object_not_create_error_gpa(self):
        with self.assertRaises(ValueError):
            a = s.Student()

if __name__ == '__main__':
    unittest.main()
