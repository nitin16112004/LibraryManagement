import pandas as pd
from Student import Student
from Book import Book


class DataExcel:
    FILE_NAME = "library_data.xlsx"  # Single file for both students and books
    STUDENT_SHEET = "Students"
    BOOK_SHEET = "Books"

#Student Data Handling

    @staticmethod
    def save_students(students):
        """
        Saves a list of students to the 'Students' sheet in an Excel file.
        If book data already exists, it remains unchanged.
        """
        data = [{
            "Student ID": student.StudentId,
            "First Name": student.FirstName,
            "Last Name": student.LastName,
            "Email": student.Email,
            "Phone Number": student.PhoneNo
        } for student in students]

        df_students = pd.DataFrame(data)

        try:
            existing_data = pd.read_excel(DataExcel.FILE_NAME, sheet_name=None)
            df_books = existing_data.get(DataExcel.BOOK_SHEET, pd.DataFrame())
        except FileNotFoundError:
            df_books = pd.DataFrame()

        with pd.ExcelWriter(DataExcel.FILE_NAME, engine="xlsxwriter") as writer:
            df_students.to_excel(writer, sheet_name=DataExcel.STUDENT_SHEET, index=False)
            df_books.to_excel(writer, sheet_name=DataExcel.BOOK_SHEET, index=False)

        print(f"Student data saved in {DataExcel.FILE_NAME} (Sheet: {DataExcel.STUDENT_SHEET})")

    @staticmethod
    def load_students():
        """
        Loads student data from the 'Students' sheet.

        Returns:
            list: A list of Student objects.
        """
        try:
            df = pd.read_excel(DataExcel.FILE_NAME, sheet_name=DataExcel.STUDENT_SHEET)
            students = [
                Student(row["Student ID"], row["First Name"], row["Last Name"], row["Email"], row["Phone Number"]) for
                _, row in df.iterrows()]
            return students
        except (FileNotFoundError, ValueError):
            print("No previous student data found.")
            return []

#  Book Data Handling

    @staticmethod
    def save_books(books):
        """
        Saves a list of books to the 'Books' sheet in the Excel file.
        If student data already exists, it remains unchanged.
        """
        data = [{
            "Book ID": book.BookId,
            "Title": book.Title,
            "Author": book.Author,
            "Genre": book.Genre,
            "Published Year":book.PublishedYear,
            "Total Copies": book.TotalCopies
        } for book in books]

        df_books = pd.DataFrame(data)

        try:
            existing_data = pd.read_excel(DataExcel.FILE_NAME, sheet_name=None)
            df_students = existing_data.get(DataExcel.STUDENT_SHEET, pd.DataFrame())
        except FileNotFoundError:
            df_students = pd.DataFrame()

        with pd.ExcelWriter(DataExcel.FILE_NAME, engine="xlsxwriter") as writer:
            df_students.to_excel(writer, sheet_name=DataExcel.STUDENT_SHEET, index=False)
            df_books.to_excel(writer, sheet_name=DataExcel.BOOK_SHEET, index=False)

        print(f"Book data saved in {DataExcel.FILE_NAME} (Sheet: {DataExcel.BOOK_SHEET})")

    @staticmethod
    def load_books():
        """
        Loads book data from the 'Books' sheet.

        Returns:
            list: A list of Book objects.
        """
        try:
            df = pd.read_excel(DataExcel.FILE_NAME, sheet_name=DataExcel.BOOK_SHEET)
            books = [Book(row["Book ID"], row["Title"], row["Author"], row["Genre"], row["Published Year"],row["Total Copies"]) for _, row in
                     df.iterrows()]
            return books
        except (FileNotFoundError, ValueError):
            print("No previous book data found.")
            return []


