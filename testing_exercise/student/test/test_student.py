import unittest

from project.student import Student


class StudentTests(unittest.TestCase):
    def setUp(self) -> None:
        self.student = Student('Angel', {"course_name": ["notes"]})

    def test_initialization_student(self):
        self.assertEqual(self.student.name, 'Angel')
        self.assertEqual({}, self.student.courses)

    def test_if_course_is_none_course_is_equal_to_empty_dictionary(self):
        self.assertEqual(self.student.courses, {})

    def test_enroll_expect_add_all_notes_to_the_course(self):
        self.student.courses = {'course_name': ['notes']}
        self.student.enroll('course_name', ['a', 'b', 'c'], add_course_notes="abc")
        self.assertEqual(self.student.courses, {'course_name': ['notes', 'a', 'b', 'c']})

    def test_enroll_expect_return_correct_result_if_course_already_exist(self):
        self.student.courses = {'course_name': ['notes']}
        self.assertEqual("Course already added. Notes have been updated.",
                         self.student.enroll('course_name', ['a', 'b', 'c'], add_course_notes="abc"))

    def test_enroll_expect_add_course_notes_if_course_name_is_y_or_empty_string(self):
        self.student.courses = {'course_name': ['notes']}
        self.student.enroll('c', ['a', 'b', 'c'], add_course_notes="")
        self.assertEqual(self.student.courses, {'c': ['a', 'b', 'c'], 'course_name': ['notes']})

        self.student.courses = {'course_name': ['notes']}
        self.student.enroll('co', ['a', 'b', 'c'], add_course_notes="Y")
        self.assertEqual(self.student.courses, {'co': ['a', 'b', 'c'], 'course_name': ['notes']})

    def test_enroll_expect_create_new_course_and_notes_if_course_is_not_in_the_courses(self):
        self.student.courses = {'course': ['notes']}
        self.student.enroll('course_name', ['a', 'b', 'c'], add_course_notes="N")
        self.assertEqual(self.student.courses, {'course': ['notes'], 'course_name': ['a', 'b', 'c']})

    def test_enroll_expect_return_correct_result_if_course_not_exist(self):
        self.student.courses = {'course': ['notes']}
        self.assertEqual('Course and course notes have been added.',
                         self.student.enroll('course_name', ['a', 'b', 'c'], add_course_notes="N"))

    def test_enroll_expect_add_new_course_if_course_is_not_exist_in_courses_and_no_notes(self):
        self.student.courses = {'course': ['notes']}
        self.student.enroll('name', ['a', 'b'], add_course_notes="N")
        self.assertEqual(self.student.courses, {'course': ['notes'], 'name': []})

    def test_enroll_expect_return_correct_result_if_course_is_not_exist_in_courses_and_no_notes(self):
        self.student.courses = {'course': ['notes']}
        self.assertEqual("Course has been added.", self.student.enroll('names', [], add_course_notes="N"))

    def test_student_enroll_if_course_name_not_in_courses_and_add_notes_not_valid(self):
        self.student.enroll("new", ['abc'], "N")
        self.assertEqual({"course_name": ["notes"], "new": []}, self.student.courses)

    def test_add_notes_expect_raise_error_if_course_not_in_courses(self):
        self.student.courses = {'course': ['notes']}
        with self.assertRaises(Exception) as ex:
            self.student.add_notes('new_course', [])
        self.assertEqual("Cannot add notes. Course not found.", str(ex.exception))

    def test_add_notes_expect_add_notes_if_the_course_is_in_the_courses(self):
        self.student.courses = {'course': ['notes']}
        self.student.add_notes('course', 'new')
        self.assertEqual(self.student.courses, {'course': ['notes', 'new']})

    def test_add_notes_expect_return_correct_result(self):
        self.student.courses = {'course': ['notes']}
        self.assertEqual("Notes have been updated", self.student.add_notes('course', 'new'))

    def test_leave_course_expect_remove_course_if_exist_in_the_courses(self):
        self.student.courses = {'course': ['notes']}
        self.student.leave_course('course')
        self.assertEqual(self.student.courses, {})

    def test_leave_course_expect_return_correct_result_if_course_in_courses(self):
        self.student.courses = {'course': ['notes']}
        self.assertEqual("Course has been removed", self.student.leave_course('course'))

    def test_leave_course_expect_raise_error_if_course_not_exist_in_the_courses(self):
        self.student.courses = {'course': ['notes']}
        with self.assertRaises(Exception) as ex:
            self.student.leave_course('new')
        self.assertEqual("Cannot remove course. Course not found.", str(ex.exception))


if __name__ == '__main__':
    unittest.main()
