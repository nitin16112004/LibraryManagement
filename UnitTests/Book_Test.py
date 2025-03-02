import unittest
from Book import Book


class TestStudent(unittest.TestCase):
    def setUp(self):
        """
        This method runs before every test. Use it to create a common setup for tests.
        """
        self.book = Book(1, "Mockingbird", "Hamper", 2005, "Nature Lover", 26)

    def test_initialization(self):
        """Test if the book object is initialized with correct attributes."""
        self.assertEqual(self.book.BookId, 1)
        self.assertEqual(self.book.Title, "Mockingbird")
        self.assertEqual(self.book.Author, "Hamper")
        self.assertEqual(self.book.PublishedYear, 2005)
        self.assertEqual(self.book.Genre, "Nature Lover")
        self.assertEqual(self.book.TotalCopies, 26)

    def test_get_book_info(self):
        """Test the GetBookInfo method."""
        expected_info = ("Book ID: 1, Title: Mockingbird, Author: Hamper, "
                         "Published Year: 2005, Genre: Nature Lover, Total Copies: 26")
        self.assertEqual(self.book.GetBookInfo(), expected_info)

    def test_update_details(self):
        """Test the UpdateDetails method."""
        update_message = self.book.UpdateDetails(
            publishedYear=2006, totalCopies=30
        )
        self.assertEqual(update_message, "Book 1 details updated successfully.")
        self.assertEqual(self.book.PublishedYear, 2006)
        self.assertEqual(self.book.TotalCopies, 30)
        self.assertEqual(self.book.Author, "Hamper")  # Ensure other details are unchanged

    def test_string_representation(self):
        """Test the __str__ method."""
        expected_str = ("Book ID: 1, Title: Mockingbird, Author: Hamper, "
                        "Published Year: 2005, Genre: Nature Lover, Total Copies: 26")
        self.assertEqual(str(self.book), expected_str)

    def test_partial_update(self):
        """Test partial updates using UpdateDetails."""
        self.book.UpdateDetails(author="Hamper Lee")
        self.assertEqual(self.book.Author, "Hamper Lee")
        self.assertEqual(
            self.book.Title, "Mockingbird"
        )  # Ensure other details are unchanged


if __name__ == "__main__":
    unittest.main()
