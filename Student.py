class Student:
    def __init__(self, studentId, firstName, lastName, email, phoneNo):
        self.studentId = StudentId
        self.firstName = FirstName
        self.lastName = LastName
        self.email = Email
        self.phoneNo = PhoneNo

    def get_student_info(self):
        return f"Student ID: {self.studentId}, First Name: {self.firstName}, Last Name: {self.lastName}, Email: {self.email}, Phone No: {self.phoneNo}"

    def update_details(self, firstName=None, lastName=None, email=None, phoneNo=None):
        if firstName:
            self.firstName = firstName
        if lastName:
            self.lastName = lastName
        if email:
            self.email = email
        if phoneNo:
            self.phoneNo = phoneNo
        return f"Student {studentId} details updated successfully."


