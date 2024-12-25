import unittest

from Student import Student


class TestStudent(unittest.TestCase):
    def setUp(self):
        """
        This method runs before every test. Use it to create a common setup for tests.
        """
        self.student = Student(1, "John", "Doe", "john.doe@example.com", "1234567890")

    def test_initialization(self):
        """Test if the student object is initialized with correct attributes."""
        self.assertEqual(self.student.StudentId, 1)
        self.assertEqual(self.student.FirstName, "John")
        self.assertEqual(self.student.LastName, "Doe")
        self.assertEqual(self.student.Email, "john.doe@example.com")
        self.assertEqual(self.student.PhoneNo, "1234567890")

    def test_get_student_info(self):
        """Test the GetStudentInfo method."""
        expected_info = (
            "Student ID: 1, First Name: John, Last Name: Doe,"
            " Email: john.doe@example.com, Phone No: 1234567890"
        )
        self.assertEqual(self.student.GetStudentInfo(), expected_info)

    def test_update_details(self):
        """Test the UpdateDetails method."""
        update_message = self.student.UpdateDetails(
            firstName="Jane", email="jane.doe@example.com"
        )
        self.assertEqual(update_message, "Student ID 1 details updated successfully.")
        self.assertEqual(self.student.FirstName, "Jane")
        self.assertEqual(self.student.Email, "jane.doe@example.com")
        self.assertEqual(
            self.student.LastName, "Doe"
        )  # Ensure other details are unchanged

    def test_string_representation(self):
        """Test the __str__ method."""
        expected_str = (
            "Student ID: 1, First Name: John, Last Name: Doe,"
            " Email: john.doe@example.com, Phone No: 1234567890"
        )
        self.assertEqual(str(self.student), expected_str)

    def test_partial_update(self):
        """Test partial updates using UpdateDetails."""
        self.student.UpdateDetails(phoneNo="9876543210")
        self.assertEqual(self.student.PhoneNo, "9876543210")
        self.assertEqual(
            self.student.FirstName, "John"
        )  # Ensure other details are unchanged


if __name__ == "__main__":
    unittest.main()
