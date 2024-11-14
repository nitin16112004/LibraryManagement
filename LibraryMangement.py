class LibraryManagement:
    def __init__(self):
        self.books = {}
        self.students = {}
        self.issued_books = {}

    def option(self):
        while True:
            print("\nWelcome to the Library Management System")
            print("1. Manage Books")
            print("2. Manage Students")
            print("3. Issue Books")
            print("4. Return Books")
            print("5. Exit")
            choice = input("Select an option: ")

            if choice == '1':
                self.book_option()
            elif choice == '2':
                self.student_option()
            elif choice == '3':
                self.issuebook_option()
            elif choice == '4':
                self.returnbook_option()
            elif choice == '5':
                print("Thank you for using the Library Management System. Goodbye!")
                break
            else:
                print("Invalid option. Please try again.")

    def book_option(self):
        while True:
            print("\nBooks Menu")
            print("1. Add a New Book")
            print("2. View All Books")
            print("3. Update Book")
            print("4. Delete Book")
            print("5. Back to Main Menu")
            choice = input("Choose an option: ")

            if choice == '1':
                book_id = input("Enter Book ID: ")
                if book_id in self.books:
                    print("Book ID already exists. Try again.")
                else:
                    title = input("Enter Book Title: ")
                    author = input("Enter Author Name: ")
                    quantity = int(input("Enter Quantity of Books: "))
                    self.books[book_id] = {'title': title, 'author': author, 'quantity': quantity}
                    print("Book has been added.")
            elif choice == '2':
                print("\nBooks Available:")
                for book_id, info in self.books.items():
                    status = "Available" if book_id not in self.issued_books else "Issued"
                    print(f"ID: {book_id}, Title: {info['title']}, Author: {info['author']}, Quantity: {info['quantity']}, Status: {status}")
            elif choice == '3':
                self.update_book()
            elif choice == '4':
                book_id = input("Enter Book ID to Delete: ")
                if book_id in self.books:
                    del self.books[book_id]
                    if book_id in self.issued_books:
                        del self.issued_books[book_id]
                    print("Book has been deleted.")
                else:
                    print("Book ID not found.")
            elif choice == '5':
                break
            else:
                print("Invalid choice. Try again.")

    def update_book(self):
        book_id = input("Enter Book ID to Update: ")
        if book_id in self.books:
            while True:
                print("\nWhat would you like to update?")
                print("1. Book Title")
                print("2. Book Author")
                print("3. Quantity")
                print("4. Back to Books Menu")
                choice = input("Choose an option: ")

                if choice == '1':
                    new_title = input("Enter new title: ")
                    self.books[book_id]['title'] = new_title
                    print("Book title has been updated.")
                elif choice == '2':
                    new_author = input("Enter new author: ")
                    self.books[book_id]['author'] = new_author
                    print("Book author has been updated.")
                elif choice == '3':
                    new_quantity = int(input("Enter new quantity: "))
                    self.books[book_id]['quantity'] = new_quantity
                    print("Book quantity has been updated.")
                elif choice == '4':
                    break
                else:
                    print("Invalid choice. Try again.")
        else:
            print("Book ID not found.")

    def student_option(self):
        while True:
            print("\nStudents Menu")
            print("1. Register a Student")
            print("2. View Registered Students")
            print("3. Delete a Student")
            print("4. Back to Main Menu")
            choice = input("Choose an option: ")

            if choice == '1':
                student_id = input("Enter Student ID: ")
                if student_id in self.students:
                    print("Student ID already exists. Try again.")
                else:
                    name = input("Enter Student Name: ")
                    self.students[student_id] = name
                    print("Student has been registered.")
            elif choice == '2':
                print("\nRegistered Students:")
                for student_id, name in self.students.items():
                    print(f"ID: {student_id}, Name: {name}")
            elif choice == '3':
                student_id = input("Enter Student ID to Delete: ")
                if student_id in self.students:
                    del self.students[student_id]
                    print("Student has been deleted.")
                else:
                    print("Student ID not found.")
            elif choice == '4':
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

                    if self.books[book_id]['quantity'] > 0:

                        self.books[book_id]['quantity'] -= 1

                        if book_id in self.issued_books:
                            self.issued_books[book_id].append(student_id)
                        else:
                            self.issued_books[book_id] = [student_id]
                        print("Book has been issued successfully.")
                    else:
                        print("No copies of this book are available.")
                else:
                    print("Invalid Book ID or Student ID.")
            elif choice == '2':
                print("\nIssued Books List:")
                for book_id, students in self.issued_books.items():
                    book_title = self.books[book_id]['title']
                    print(f"Book ID: {book_id}, Title: {book_title}, Issued to Students: {', '.join(students)}")
            elif choice == '3':
                break
            else:
                print("Invalid choice. Try again.")

    def returnbook_option(self):
        print("\nReturn Book Menu")
        book_id = input("Enter Book ID to Return: ")
        student_id = input("Enter Student ID: ")


        if book_id in self.issued_books and student_id in self.issued_books[book_id]:

            self.books[book_id]['quantity'] += 1

            self.issued_books[book_id].remove(student_id)


            if not self.issued_books[book_id]:
                del self.issued_books[book_id]

            print("Book has been returned successfully.")
        else:
            print("Invalid Book ID or this book was not issued to this student.")



library = LibraryManagement()
library.option()
