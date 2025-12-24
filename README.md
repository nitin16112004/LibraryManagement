# LibraryManagement

## Overview
The **LibraryManagement** project is a versatile and easy-to-use system designed for managing libraries, including their books, patrons, and administrative workflows. Written entirely in Python, this project enables seamless interaction between the library staff, book inventory, and students. Advanced Python principles and industry-standard practices, like continuous integration and quality checks, ensure the project remains robust and maintainable.

---

## 🚀 Key Features

### Book Management
- **Add and Update Books**: Include new books or modify details such as title, author, genre, year, and inventory.
- **Retrieve Book Details**: Fetch complete information of a book, including ID, title, author, and availability.
- **Efficient Inventory Management**: Track the total copies available for lending.

### Student Management
- **Register Students**: Add new student profiles with details like name, email, and contact number.
- **Update Profiles**: Modify student information (e.g., email, phone) while keeping other details intact.
- **Fetch Student Details**: Retrieve a comprehensive student profile for administrative purposes.

### Robust Architecture
- Modular design for easy scalability and maintainability.
- Clearly defined classes and methods encapsulating various operations.

### Testing Suite
- Complete test coverage using the Python `unittest` library.
- Tests ensure all functionalities (e.g., Book and Student management) behave as expected.

### Continuous Integration and Linting
- Automated pipelines ensure the codebase meets quality and functionality standards.
- CI pipeline validates all changes on pull requests or commits.
- Thorough linting using Flake8, Black, and Pylint.

---

## 📂 Project Structure
```
📦LibraryManagement
 ┣ 📂UnitTests
 ┃ ┣ 📜Book_Test.py               # Unit tests for Book-related operations
 ┃ ┗ 📜Student_Test.py            # Unit tests for Student-related operations
 ┣ 📂.github/workflows
 ┃ ┣ 📜lint.yml                   # Linting workflow
 ┃ ┗ 📜test-pipeline.yml          # Testing workflow
 ┣ 📜requirements.txt             # Dependency list
 ┗ 📜README.md                    # Project documentation
```

---

## 🛠️ Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/nitin16112004/LibraryManagement.git
   cd LibraryManagement
   ```

2. **Install Dependencies:**
   Ensure you have Python 3.10 or later installed. Install required libraries using:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run Tests:**
   Verify the system by running all unit tests:
   ```bash
   python -m unittest discover UnitTests
   ```

---

## 🔎 Examples and Usage

### Example: Add a New Book
```python
from Book import Book

# Initialize a Book object
new_book = Book(101, "The Great Gatsby", "F. Scott Fitzgerald", 1925, "Classic", 10)
print(new_book.GetBookInfo())
```

### Example: Update Book Details
```python
new_book.UpdateDetails(totalCopies=15)
print(new_book.GetBookInfo())  # Updated copies
```

### Example: Register a Student
```python
from Student import Student

# Create a new student profile
student = Student(201, "Alice", "Johnson", "alice@example.com", "9876543210")
print(student.GetStudentInfo())
```

### Example: Modify Student Information
```python
student.UpdateDetails(email="alice.johnson@example.com")
print(student.GetStudentInfo())  # Updated email
```

---

## 🔄 Continuous Integration (CI/CD)
### 1. **Linting Workflow:**
   - Runs automatically on pull requests to validate code formatting and quality.
   - Tools: Flake8, Pylint, and Black.

### 2. **Testing Workflow:**
   - Executes all unit tests automatically for every push or pull request.
   - HTML test reports generated for detailed analysis.

### Trigger Points:
   - Changes pushed to `main` or any `feature/*` branch.
   - Pull requests targeting the `main` branch.

---

## 📋 Contribution Guidelines
Contributions are highly encouraged! Here's how you can get involved:
1. Fork the repository.
2. Create a new feature branch:
   ```bash
   git checkout -b feature/new-feature
   ```
3. Commit your changes and push the branch:
   ```bash
   git add .
   git commit -m "Add a new feature"
   git push origin feature/new-feature
   ```
4. Open a pull request.

---

## 📬 Contact
- **Author**: [nitin16112004](https://github.com/nitin16112004)
- **Feedback & Suggestions**: Use the [issues](https://github.com/nitin16112004/LibraryManagement/issues) tab.

### 🌟 Don't forget to star this repository if you find it helpful!
