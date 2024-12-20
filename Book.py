class Book:
    def __init__(self, bookId, title, author, publishedYear, genre, totalCopies):
        self.BookId = bookId
        self.Title = title
        self.Author = author
        self.PublishedYear = publishedYear
        self.Genre = genre
        self.TotalCopies = totalCopies
    def GetBookInfo(self):
        return (f"Book ID: {self.BookId}, Title: {self.Title}, Author: {self.Author}, "
                f"Published Year: {self.PublishedYear}, Genre: {self.Genre}, Total Copies: {self.TotalCopies}")
    def  UpdateDetails(self, title=None, author=None, publishedYear=None, genre=None, totalCopies=None):
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

    def DeleteBook(self):
        return f"Book with ID {self.BookId} has been deleted."

    def __str__(self):
        return (f"Book ID: {self.BookId}, Title: {self.Title}, Author: {self.Author}, "
                f"Published Year: {self.PublishedYear}, Genre: {self.Genre}, Total Copies: {self.TotalCopies}")