'''
Practice using
 assertTrue
 assertFalse
 assertIsNone
 assertIsNotNone
 assertIn
 assertNotIn
'''

from studentLists import ClassList, StudentError
from unittest import TestCase

class TestStudentLists(TestCase):

    def test_add_student_check_student_in_list(self):
        test_class = ClassList(2)
        test_class.add_student('Test Student')
        self.assertIn('Test Student', test_class.class_list)

        test_class.add_student('Another Test Student')
        self.assertIn('Test Student', test_class.class_list)
        self.assertIn('Another Test Student', test_class.class_list)

    def test_add_student_already_in_list(self):
        test_class = ClassList(2)
        test_class.add_student('Test Student')
        with self.assertRaises(StudentError):
            test_class.add_student('Test Student')

    def test_add_remove_student(self):
        test_class = ClassList(2)
        test_class.add_student('Mike')
        test_class.add_student('Jake')
        test_class.remove_student('Mike')

        self.assertNotIn("Mike", test_class.class_list)

    def test_remove_student_not_in_list(self):
        test_class = ClassList(2)
        test_class.add_student('Mike')
        test_class.add_student('Jake')

        with self.assertRaises(StudentError):
            test_class.remove_student('Tom')

    def test_remove_student_from_empty_list(self):
        test_class = ClassList(1)
        with self.assertRaises(StudentError):
            test_class.remove_student('Mike')

    def test_is_enrolled_when_student_present(self):
        test_class = ClassList(2)
        test_class.add_student('Snoop Dogg')
        test_class.add_student('Martha Stewart')
        self.assertTrue(test_class.is_enrolled('Snoop Dogg'))
        self.assertTrue(test_class.is_enrolled('Martha Stewart'))

    def test_is_enrolled_empty_class_list(self):
        test_class = ClassList(2)
        self.assertFalse(test_class.is_enrolled('Snoop Dogg'))

    def test_is_erolled_returns_false(self):
        test_class = ClassList(2)
        test_class.add_student('Mike')
        test_class.add_student('Jake')
        self.assertFalse(test_class.is_enrolled('Amanda'))

    def test_string_with_students_enrolled(self):
        test_class = ClassList(2)
        test_class.add_student('Taylor Swift')
        test_class.add_student('Kanye West')
        self.assertEqual('Taylor Swift, Kanye West', str(test_class))

    def test_string_empty_class(self):
        test_class = ClassList(2)
        self.assertEqual('', str(test_class))

    def test_index_of_student_student_present(self):
        test_class = ClassList(3)
        test_class.add_student('Harry')
        test_class.add_student('Hermione')
        test_class.add_student('Ron')

        self.assertEqual(1, test_class.index_of_student('Harry'))
        self.assertEqual(2, test_class.index_of_student('Hermione'))
        self.assertEqual(3, test_class.index_of_student('Ron'))

        # This assert passes, but it's redundant - the first assert statement will fail if
        # the method call returns None
        self.assertIsNotNone(test_class.index_of_student('Harry'))

    def test_index_of_student_returns_none_on_empty_list(self):
        test_class = ClassList(3)
        self.assertIsNone(test_class.index_of_student('Mike'))

    def test_list_for_correct_index_of_none(self):
        test_class = ClassList(3)
        test_class.add_student('Larry')
        test_class.add_student('Curly')
        test_class.add_student('Moe')

        self.assertEqual(None, test_class.index_of_student('Harry'))
        self.assertEqual(None, test_class.index_of_student('Hermione'))
        self.assertEqual(None, test_class.index_of_student('Ron'))

        self.assertIsNone(test_class.index_of_student('Mike'))

    def test_is_class_full(self):
        test_class = ClassList(1)
        test_class.add_student('Amanda')

        self.assertTrue(test_class.is_class_full())

    def test_is_class_not_full(self):
        test_class = ClassList(2)
        test_class.add_student('Amanda')

        self.assertFalse(test_class.is_class_full())
