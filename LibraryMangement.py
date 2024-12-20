from Book import Book
from Student import Student

students = []
books = []

while True:
    print("\nLibrary Management System")
    print("1. Add Student")
    print("2. Add Book")
    print("3. Get Student Info")
    print("4. Get Book Info")
    print("5. Delete Student")
    print("6. Delete Book")
    print("7. View Library Summary")
    print("8. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
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

    elif choice == "2":
        bookId = int(input("Enter Book ID: "))
        title = input("Enter Book Title: ")
        author = input("Enter Author Name: ")
        publishedYear = int(input("Enter Published Year: "))
        genre = input("Enter Genre: ")
        totalCopies = int(input("Enter Total Copies: "))

        if any(book.BookId == bookId for book in books):
            print(f"Book ID {bookId} already exists.")
        else:
            books.append(Book(bookId, title, author, publishedYear, genre, totalCopies))
            print(f"Book '{title}' by {author} added successfully.")

    elif choice == "3":
        for student in students:
            print(student)


    elif choice == "4":
        for book in books:
            print(book)

    elif choice == "5":
        studentId = int(input("Enter Student ID to delete: "))
        for student in students:
            if student.StudentId == studentId:
                print(students.remove(student),f"Student Id {studentId} has been removed")
            else:
                print(f"Student ID {studentId} not found")

    elif choice == "6":
        bookId = int(input("Enter Book ID to delete: "))
        for book in books:
            if book.BookId == bookId:
                print(books.remove(book),f"Book with ID {bookId} has been removed")
            else:
                print(f"Book ID {bookId} not found")



    elif choice == "7":
        if students:
            print("\nStudents in Library:")
            for student in students:
                print(f"Student ID: {student.StudentId}, Name: {student.FirstName} {student.LastName}")
        else:
            print("\nNo students registered.")

        if books:
            print("\nBooks in Library:")
            for book in books:
                print(f"Book ID: {book.BookId}, Title: {book.Title}")
        else:
            print("\nNo books registered.")

    elif choice == "8":
        print("Exiting the system. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")
