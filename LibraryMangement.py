class LibraryManagment:
    def __init__(self):
        self.books = {}  # Store book details with a dictionary
        self.students = {}  # Store student details
        self.issued_books = {}  # Track issued books with a dictionary

    def option(self):
        while True:
            print("\nWelcome to the Library Management System")
            print("1. Manage Books")
            print("2. Manage Students")
            print("3. Issue Books")
            print("4. Exit")
            choice = input("Select an option: ")

            if choice == '1':
                self.book_option()
            elif choice == '2':
                self.student_option()
            elif choice == '3':
                self.issuebook_option()
            elif choice == '4':
                print("Thank you for using the Library Management System. Goodbye!")
                break
            else:
                print("Invalid option. Please try again.")

    def book_option(self):
        while True:
            print("\nBooks Menu")
            print("1. Add a New Book")
            print("2. View All Books")
            print("3. Back to Main Menu")
            choice = input("Choose an option: ")

            if choice == '1':
                book_id = input("Enter Book ID: ")
                title = input("Enter Book Title: ")
                author = input("Enter Author Name: ")
                self.books[book_id] = {'title': title, 'author': author}
                print("Book has been added.")
            elif choice == '2':
                print("\nBooks Available:")
                for book_id, info in self.books.items():
                    print(f"ID: {book_id}, Title: {info['title']}, Author: {info['author']}")
            elif choice == '3':
                break
            else:
                print("Invalid choice. Try again.")

    def student_option(self):
        while True:
            print("\nStudents Menu")
            print("1. Register a Student")
            print("2. View Registered Students")
            print("3. Back to Main Menu")
            choice = input("Choose an option: ")

            if choice == '1':
                student_id = input("Enter Student ID: ")
                name = input("Enter Student Name: ")
                self.students[student_id] = name
                print("Student has been registered.")
            elif choice == '2':
                print("\nRegistered Students:")
                for student_id, name in self.students.items():
                    print(f"ID: {student_id}, Name: {name}")
            elif choice == '3':
                break
            else:
                print("Invalid choice. Try again.")

    def issuebook_option(self):
        while True:
            print("\nBook Issue Menu")
            print("1. Issue a Book")
            print("2. View Issued Books")
            print("3. Back to Main Menu")
            choice = input("Choose an option: ")

            if choice == '1':
                book_id = input("Enter Book ID to Issue: ")
                student_id = input("Enter Student ID: ")

                if book_id in self.books and student_id in self.students:
                    self.issued_books[book_id] = student_id
                    print("Book has been issued successfully.")
                else:
                    print("Invalid Book ID or Student ID.")
            elif choice == '2':
                print("\nIssued Books List:")
                for book_id, student_id in self.issued_books.items():
                    book_title = self.books[book_id]['title']
                    student_name = self.students[student_id]
                    print(f"Book ID: {book_id}, Title: {book_title}, Issued to: {student_name}")
            elif choice == '3':
                break
            else:
                print("Invalid choice. Try again.")


# Initialize and run the library system
library = LibraryManagment()
library.option()
