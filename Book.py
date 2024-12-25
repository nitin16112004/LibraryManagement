class Book:
    """
    A class that represents a book and its associated details.

    Attributes:
        BookId (int): Unique identifier for the book.
        Title (str): The title of the book.
        Author (str): The author's name.
        PublishedYear (int): The year the book was published.
        Genre (str): The book's genre or category.
        TotalCopies (int): Total number of copies available.

    """

    def __init__(self, bookId, title, author, publishedYear, genre, totalCopies):
        """
        Initializes a new book instance with the provided details.

        Args:
            bookId (int): Unique ID for the book.
            title (str): The book's title.
            author (str): Name of the author.
            publishedYear (int): Year of publication.
            genre (str): Genre or category of the book.
            totalCopies (int): Number of copies in stock.

        """

        self.BookId = bookId
        self.Title = title
        self.Author = author
        self.PublishedYear = publishedYear
        self.Genre = genre
        self.TotalCopies = totalCopies

    def GetBookInfo(self):
        """
        Returns a string summarizing the book's details.

        Returns:
             str: A string with the book's key attributes.
        """
        return (
            f"Book ID: {self.BookId}, Title: {self.Title}, Author: {self.Author}, "
            f"Published Year: {self.PublishedYear}, Genre: {self.Genre},"
            f" Total Copies: {self.TotalCopies}"
        )

    def UpdateDetails(
        self, title=None, author=None, publishedYear=None, genre=None, totalCopies=None
    ):
        """
        Updates specific attributes of the book. Only provided arguments are updated.

         Args:
            title (str, optional): Updated title.
            author (str, optional): Updated author name.
            publishedYear (int, optional): Updated publication year.
            genre (str, optional): Updated genre.
            totalCopies (int, optional): Updated number of available copies.

            Returns:
                str: Confirmation message about the updates.
        """
        if title:
            self.Title = title
        if author:
            self.Author = author
        if publishedYear:
            self.PublishedYear = publishedYear
        if genre:
            self.Genre = genre
        if totalCopies is not None:
            self.TotalCopies = totalCopies
        return f"Book {self.BookId} details updated successfully."

    def __str__(self):
        """
        Returns a readable string representation of the book.

        Returns:
            str: A formatted string with the book's information.
        """
        return (
            f"Book ID: {self.BookId}, Title: {self.Title}, Author: {self.Author}, "
            f"Published Year: {self.PublishedYear}, Genre: {self.Genre},"
            f" Total Copies: {self.TotalCopies}"
        )
