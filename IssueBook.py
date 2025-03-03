from Book import Book
from Student import Student

class BookIssue:
    """
    Represents a book issue record, including student details, issue date, and due date.

    Attributes:
        Book (Book): The book object associated with the issue.
        Student (Student): The student object who issued the book.
        IssueDate (str): The date when the book was issued.
        DueDate (str): The due date for returning the book.
    """

    def __init__(self, book, student, issueDate, dueDate):
        """
        Initializes a new instance of the BookIssue class with the provided details.

        Args:
            book (Book): The book object associated with the issue.
            student (Student): The student object who issued the book.
            issueDate (str): The date when the book was issued.
            dueDate (str): The due date for returning the book.
        """
        self.Book = book
        self.Student = student
        self.IssueDate = issueDate
        self.DueDate = dueDate

    def GetBookIssueInfo(self):
        """
        Retrieves the book issue details in a formatted string.

        Returns:
            str: A string containing the book issue details.
        """
        return (
            f"Book ID: {self.Book.BookId}, Title: {self.Book.Title}, Student ID: {self.Student.StudentId}, Student Name: {self.Student.FirstName} {self.Student.LastName}, Issue Date: {self.IssueDate}, "
            f"Due Date: {self.DueDate}"
        )

    def UpdateDetails(self, issueDate=None, dueDate=None):
        """
        Updates the book issue details with the provided information.

        Args:
            issueDate (str, optional): The new issue date. Defaults to None.
            dueDate (str, optional): The new due date. Defaults to None.

        Returns:
            str: A message indicating the update status.
        """
        if issueDate:
            self.IssueDate = issueDate
        if dueDate:
            self.DueDate = dueDate
        return f"Book ID {self.Book.BookId} details updated successfully."

    def __str__(self):
        """
        Returns a string representation of the book issue details.

        Returns:
            str: A string containing the book issue details.
        """
        return (
            f"Book ID: {self.Book.BookId}, Title: {self.Book.Title}, Student ID: {self.Student.StudentId}, Student Name: {self.Student.FirstName} {self.Student.LastName}, Issue Date: {self.IssueDate}, "
            f"Due Date: {self.DueDate}"
        )
