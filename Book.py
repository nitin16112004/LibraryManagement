class Book:
    def __init__(self, bookId, title, author, publishedYear, genre, totalCopies):
        self.bookId = BookId
        self.title = Title
        self.author = Author
        self.publishedYear = PublishedYear
        self.genre = Genre
        self.totalCopies = TotalCopies
    def GetBookInfo(self):
        return (f"Book ID: {self.bookId}, Title: {self.title}, Author: {self.author}, "
                f"Published Year: {self.publishedYear}, Genre: {self.genre}, Total Copies: {self.totalCopies}")
    def UpdateDetails(self, title=None, author=None, publishedYear=None, genre=None, totalCopies=None):
        if title:
            self.title = title
        if author:
            self.author = author
        if publishedYear:
            self.publishedYear = publishedYear
        if genre:
            self.genre = genre
        if totalCopies is not None:  # Accepts 0 as a valid update
            self.totalCopies = totalCopies
        return f"Book {self.bookId} details updated successfully."
