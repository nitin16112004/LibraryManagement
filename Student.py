class Student:
    """
    Represents a student with basic details such as ID, name, email, and phone number.

    Attributes:
        StudentId (int): The unique identifier for the student.
        FirstName (str): The first name of the student.
        LastName (str): The last name of the student.
        Email (str): The email address of the student.
        PhoneNo (str): The phone number of the student.
    """

    def __init__(self, studentId, firstName, lastName, email, phoneNo):
        """
        Initializes a new instance of the Student class with the provided details.

        Args:
            studentId (int): The unique identifier for the student.
            firstName (str): The first name of the student.
            lastName (str): The last name of the student.
            email (str): The email address of the student.
            phoneNo (str): The phone number of the student.
        """
        self.StudentId = studentId
        self.FirstName = firstName
        self.LastName = lastName
        self.Email = email
        self.PhoneNo = phoneNo

    def GetStudentInfo(self):
        """
        Retrieves the student's details in a formatted string.

        Returns:
            str: A string containing the student's ID, first name,
                    last name, email, and phone number.
        """
        return (
            f"Student ID: {self.StudentId}, First Name: {self.FirstName},"
            f" Last Name: {self.LastName}, Email: {self.Email}, Phone No: {self.PhoneNo}"
        )

    def UpdateDetails(self, firstName=None, lastName=None, email=None, phoneNo=None):
        """
        Updates the student's details with the provided information.

        Args:
            firstName (str, optional): The new first name of the student. Defaults to None.
            lastName (str, optional): The new last name of the student. Defaults to None.
            email (str, optional): The new email address of the student. Defaults to None.
            phoneNo (str, optional): The new phone number of the student. Defaults to None.

        Returns:
            str: A message indicating the update status.
        """
        if firstName:
            self.FirstName = firstName
        if lastName:
            self.LastName = lastName
        if email:
            self.Email = email
        if phoneNo:
            self.PhoneNo = phoneNo
        return f"Student ID {self.StudentId} details updated successfully."

    def __str__(self):
        """
        Returns a string representation of the student's details.

        Returns:
            str: A string containing the student's ID, first name,
                    last name, email, and phone number.
        """
        return (
            f"Student ID: {self.StudentId}, First Name: {self.FirstName},"
            f" Last Name: {self.LastName}, Email: {self.Email}, Phone No: {self.PhoneNo}"
        )
