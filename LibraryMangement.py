from Book import Book
from Student import Student

students = []
books = []

while True:
    print("\nLibrary Management System")
    print("1. Student Operation")
    print("2. Book Operation")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("/nStudent Operation")
        print("1. Add Student")
        print("2. Get Student Info")
        print("3. Delete Student")
        print("4. Update Student Details")
        print("5. Exit")
        Choice = input("Enter your choice")
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
                print(f"Student {firstName} {lastName} added successfully.")

        elif Choice == "2":
            for student in students:
                print(student)

        elif Choice == "3":
            studentId = int(input("Enter Student ID to delete: "))
            for student in students:
                if student.StudentId == studentId:
                    students.remove(student)
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
                    break
            else:
                print(f"Student ID {studentId} not found.")

        elif Choice == "5":
            print("Exiting the Student System. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

    elif choice == "2":
        print("/nBook Operation")
        print("1. Add Book")
        print("2. Get Book Info")
        print("3. Delete Book")
        print("4. Update Book Details")
        print("5. Exit")
        Choice = input("Enter your choice")

        if Choice == "1":
            bookId = int(input("Enter Book ID: "))
            title = input("Enter Book Title: ")
            author = input("Enter Author Name: ")
            publishedYear = input("Enter Published Year: ")
            genre = input("Enter Genre: ")
            totalCopies = input("Enter Total Copies: ")

            if any(book.BookId == bookId for book in books):
                print(f"Book ID {bookId} already exists.")
            else:
                books.append(
                    Book(bookId, title, author, publishedYear, genre, totalCopies)
                )
                print(f"Book '{title}' by {author} added successfully.")

        elif Choice == "2":
            for book in books:
                print(book)

        elif Choice == "3":
            bookId = int(input("Enter Book ID to delete: "))
            for book in books:
                if book.BookId == bookId:
                    books.remove(book)
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
                    publishedYear = (
                        input("Enter New Published Year:") or book.PublishedYear
                    )
                    genre = input("Enter New Genre:") or book.Genre
                    totalCopies = input("Enter New Total Copies:") or book.TotalCopies
                    print(
                        book.UpdateDetails(
                            title, author, publishedYear, genre, totalCopies
                        )
                    )
                    break
            else:
                print(f"Book ID {bookId} not found")

        elif Choice == "5":
            print("Exiting the Book Operation. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

    elif choice == "3":
        print("Exiting the system. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")
