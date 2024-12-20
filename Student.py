class Student:
    def __init__(self, studentId, firstName, lastName, email, phoneNo):
        self.StudentId = studentId
        self.FirstName = firstName
        self.LastName = lastName
        self.Email = email
        self.PhoneNo = phoneNo

    def GetStudentInfo(self):
        return f"Student ID: {self.StudentId}, First Name: {self.FirstName}, Last Name: {self.LastName}, Email: {self.Email}, Phone No: {self.PhoneNo}"

    def UpdateDetails(self, firstName=None, lastName=None, email=None, phoneNo=None):
        if firstName:
            self.FirstName = firstName
        if lastName:
            self.LastName = lastName
        if email:
            self.Email = email
        if phoneNo:
            self.PhoneNo = phoneNo
        return f"Student {self.StudentId} details updated successfully."

    def DeleteStudent(self):
        return f"Student with ID {self.StudentId} has been deleted.{__str__()}"

    def __str__(self):
        return f"Student ID: {self.StudentId}, First Name: {self.FirstName}, Last Name: {self.LastName}, Email: {self.Email}, Phone No: {self.PhoneNo}"
