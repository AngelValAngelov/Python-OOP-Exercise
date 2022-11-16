import unittest

from project.student_report_card import StudentReportCard


class TestStudentReportCard(unittest.TestCase):
    def setUp(self) -> None:
        self.studentReportCard = StudentReportCard('Angel', 3)
        self.grades_by_subject = {}

    def test_initialization_TestStudentReportCard(self):
        self.assertEqual(self.studentReportCard.student_name, 'Angel')
        self.assertEqual(self.studentReportCard.school_year, 3)
        self.assertEqual(self.studentReportCard.grades_by_subject, {})

    def test_student_name_expect_raise_error_if_value_is_empty_string(self):
        with self.assertRaises(ValueError) as ex:
            self.studentReportCard.student_name = ''
        self.assertEqual(str(ex.exception), "Student Name cannot be an empty string!")

    def test_school_year_set_up_with_valid_number(self):
        for grade in range(1, 13):
            self.studentReportCard.school_year = grade
            self.assertEqual(grade, self.studentReportCard.school_year)

    def test_school_year_expect_raise_error_if_value_is_less_than_one_and_more_than_12(self):
        with self.assertRaises(ValueError) as ex:
            self.studentReportCard.school_year = 15
        self.assertEqual(str(ex.exception), "School Year must be between 1 and 12!")

        with self.assertRaises(ValueError) as ex:
            self.studentReportCard.school_year = 0
        self.assertEqual(str(ex.exception), "School Year must be between 1 and 12!")

    def test_add_grade_expect_add_subject_if_missing_in_the_grades_by_subject(self):
        self.studentReportCard.add_grade('OOP', 6.0)
        self.assertEqual(self.studentReportCard.grades_by_subject, {'OOP': [6.0]})

    def test_add_grade_expect_add_grade_if_subject_in_the_grades_by_subject(self):
        self.studentReportCard.add_grade('OOP', 6.0)
        self.studentReportCard.add_grade('OOP', 5.5)
        self.assertEqual(self.studentReportCard.grades_by_subject, {'OOP': [6.0, 5.5]})

    def test_average_grade_by_subject_expect_return_average_grade_for_the_subject(self):
        self.studentReportCard.add_grade('OOP', 6.0)
        self.studentReportCard.add_grade('OOP', 5.5)
        self.studentReportCard.add_grade('DB', 6.0)
        self.assertEqual(self.studentReportCard.average_grade_by_subject(), 'OOP: 5.75\n''DB: 6.00')

    def test_average_grade_for_all_subjects_expect_return_average_grade_for_all_subjects(self):
        self.studentReportCard.add_grade('OOP', 6.0)
        self.studentReportCard.add_grade('OOP', 5.5)
        self.studentReportCard.add_grade('DB', 6.0)
        self.assertEqual(self.studentReportCard.average_grade_for_all_subjects(), "Average Grade: 5.83")

    def test_studentReportCard_represent_method(self):
        self.studentReportCard.add_grade('OOP', 6.0)
        self.studentReportCard.add_grade('OOP', 5.5)
        self.studentReportCard.add_grade('DB', 6.0)
        self.assertEqual(self.studentReportCard.__repr__(),
                         "Name: Angel\n""Year: 3\n""----------\n""OOP: 5.75\n""DB: 6.00\n""----------\n""Average Grade: 5.83")


if __name__ == "__main__":
    unittest.main()
