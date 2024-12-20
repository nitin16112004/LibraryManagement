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
    print("7. Update Student Details")
    print("8. Update Book Details")
    print("9. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        studentId = int(input("Enter Student ID: "))
        firstName = input("Enter First Name: ")
        lastName = input("Enter Last Name: ")
        email = input("Enter Email: ")
        phoneNo = int(input("Enter Phone Number: "))

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
                students.remove(student)
                print(f"Student with ID {studentId} has been removed")
            else:
                print(f"Student ID not found")

    elif choice == "6":
        bookId = int(input("Enter Book ID to delete: "))
        for book in books:
            if book.BookId == bookId:
                b=books.remove(book)
                print(f"Book with ID {bookId} has been removed")
            else:
                print(f"Book ID not found")

    elif choice == "7":
        studentId = int(input("Enter Student ID to update:"))
        for student in students:
            if student.StudentId==studentId:
                firstName = input("Enter New First Name:") or student.FirstName
                lastName = input("Enter New Last Name:") or student.LastName
                email = input("Enter New Email:") or student.Email
                phoneNo = int(input("Enter New Phone No.:")) or student.PhoneNo
                print(student.UpdateDetails(firstName,lastName,email,phoneNo))
            else:
                print(f"Student ID {studentId} not found.")

    elif choice == "8":
        bookId = int(input("Enter Book ID to update:"))
        for book in books:
            if book.BookId==bookId:
                title = input("Enter New Title:") or book.Title
                author = input("Enter New Author:") or book.Author
                publishedYear = int(input("Enter New Published Year:")) or book.PublishedYear
                genre = input("Enter New Genre:") or book.Genre
                totalCopies = int(input("Enter New Total Copies:")) or book.TotalCopies
                print(book.UpdateDetails(title,author,publishedYear,genre,totalCopies))
            else:
                print(f"Book ID {bookId} not found")

    elif choice == "9":
        print("Exiting the system. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")
