class Student:
    def __init__(self, studentId, firstName, lastName, email, phoneNo):
        self.studentId = studentId
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.phoneNo = phoneNo

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


def update_student_record(studentId, student_records, firstName=None, lastName=None, email=None, phoneNo=None):
    if studentId in student_records:
        student = student_records[studentId]
        student.update_details(firstName, lastName, email, phoneNo)
        student_records[studentId] = student.get_student_info()
        return f"Student {studentId} details updated successfully."
    else:
        return f"Student ID {studentId} not found."


def get_student_details(studentId, student_records):
    if studentId in student_records:
        return student_records[studentId]
    return f"Student ID {studentId} not found."

