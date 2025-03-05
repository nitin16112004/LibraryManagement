from Book import Book
from Student import Student
from DataExcel import DataExcel

students = DataExcel.load_students()
books = DataExcel.load_books()
book_issues = []  # List to track issued books

while True:
    print("\nLibrary Management System")
    print("1. Student Operation")
    print("2. Book Operation")
    print("3. Book Issue Operation")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("\nStudent Operation")
        print("1. Add Student")
        print("2. Get Student Info")
        print("3. Delete Student")
        print("4. Update Student Details")
        print("5. Exit")
        Choice = input("Enter your choice: ")
        if Choice == "1":
            studentId = int(input("Enter Student ID: "))
            firstName = input("Enter First Name: ")
            lastName = input("Enter Last Name: ")
            email = input("Enter Email: ")
            phoneNo = input("Enter Phone Number: ")

            if any(student.StudentId == studentId for student in students):
                print(f"Student ID {studentId} already exists.")
            else:
                students.append(Student(studentId, firstName, lastName, email, phoneNo))
                DataExcel.save_students(students)
                print(f"Student {firstName} {lastName} added successfully.")

        elif Choice == "2":
            for student in students:
                print(student)

        elif Choice == "3":
            studentId = int(input("Enter Student ID to delete: "))
            for index, student in enumerate(students):
                if student.StudentId == studentId:
                    del students[index]
                    DataExcel.save_students(students)
                    print(f"Student with ID {studentId} has been removed")
                    break
            else:
                print(f"Student ID {studentId} not found")

        elif Choice == "4":
            studentId = int(input("Enter Student ID to update:"))
            for student in students:
                if student.StudentId == studentId:
                    firstName = input("Enter New First Name:") or student.FirstName
                    lastName = input("Enter New Last Name:") or student.LastName
                    email = input("Enter New Email:") or student.Email
                    phoneNo = input("Enter New Phone No.:") or student.PhoneNo
                    print(student.UpdateDetails(firstName, lastName, email, phoneNo))
                    DataExcel.save_students(students)
                    break
            else:
                print(f"Student ID {studentId} not found.")

        elif Choice == "5":
            print("Exiting the Student System. Goodbye!")

        else:
            print("Invalid choice. Please try again.")

    elif choice == "2":
        print("\nBook Operation")
        print("1. Add Book")
        print("2. Get Book Info")
        print("3. Delete Book")
        print("4. Update Book Details")
        print("5. Exit")
        Choice = input("Enter your choice: ")

        if Choice == "1":
            bookId = int(input("Enter Book ID: "))
            title = input("Enter Book Title: ")
            author = input("Enter Author Name: ")
            publishedYear = input("Enter Published Year: ")
            genre = input("Enter Genre: ")
            totalCopies = int(input("Enter Total Copies: "))

            if any(book.BookId == bookId for book in books):
                print(f"Book ID {bookId} already exists.")
            else:
                books.append(Book(bookId, title, author, publishedYear, genre, totalCopies))
                DataExcel.save_books(books)
                print(f"Book '{title}' by {author} added successfully.")

        elif Choice == "2":
            for book in books:
                print(book)

        elif Choice == "3":
            bookId = int(input("Enter Book ID to delete: "))
            for index, book in enumerate(books):
                if book.BookId == bookId:
                    del books[index]
                    DataExcel.save_books(books)
                    print(f"Book with ID {bookId} has been removed")
                    break
            else:
                print(f"Book ID {bookId} not found")

        elif Choice == "4":
            bookId = int(input("Enter Book ID to update:"))
            for book in books:
                if book.BookId == bookId:
                    title = input("Enter New Title:") or book.Title
                    author = input("Enter New Author:") or book.Author
                    publishedYear = input("Enter New Published Year:") or book.PublishedYear
                    genre = input("Enter New Genre:") or book.Genre
                    totalCopies = int(input("Enter New Total Copies:") or book.TotalCopies)
                    print(book.UpdateDetails(title, author, publishedYear, genre, totalCopies))
                    DataExcel.save_books(books)
                    break
            else:
                print(f"Book ID {bookId} not found")

        elif Choice == "5":
            print("Exiting the Book Operation. Goodbye!")

        else:
            print("Invalid choice. Please try again.")

    elif choice == "3":
        print("\nBook Issue Operation")
        print("1. Issue Book")
        print("2. View Issued Books")
        print("3. Exit")
        Choice = input("Enter your choice: ")

        if Choice == "1":
            studentId = int(input("Enter Student ID: "))
            bookId = int(input("Enter Book ID: "))
            issueDate = input("Enter Issue Date (YYYY-MM-DD): ")
            dueDate = input("Enter Due Date (YYYY-MM-DD): ")

            student = next((s for s in students if s.StudentId == studentId), None)
            book = next((b for b in books if b.BookId == bookId), None)

            if student and book:
                if book.TotalCopies > 0:
                    book.TotalCopies -= 1
                    book_issues.append((bookId, studentId, issueDate, dueDate))
                    DataExcel.save_books(books)
                    print(f"Book ID {bookId} issued to Student ID {studentId} successfully.")
                else:
                    print("No copies of this book are available.")
            else:
                print("Invalid Student ID or Book ID.")

        elif Choice == "2":
            if book_issues:
                print("\nIssued Books:")
                for issue in book_issues:
                    print(f"Book ID: {issue[0]}, Student ID: {issue[1]}, Issue Date: {issue[2]}, Due Date: {issue[3]}")
            else:
                print("No books have been issued.")

        elif Choice == "3":
            print("Exiting Book Issue Operation. Goodbye!")

        else:
            print("Invalid choice. Please try again.")

    elif choice == "4":
        print("Exiting the system. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")
