
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Added book: {book.title} by {book.author}")

    def list_books(self):
        if not self.books:
            print("Library is empty.")
        else:
            print("Books in Library:")
            for i, b in enumerate(self.books, start=1):
                print(f"{i}. {b}")

    def search(self, query, by="title"):
        query = query.lower()
        if by == "title":
            result = [b for b in self.books if query in b.title.lower()]
        elif by == "author":
            result = [b for b in self.books if query in b.author.lower()]
        else:
            print("Invalid search type. Use 'title' or 'author'.")
            return

        if result:
            print(f"Search results for '{query}' by {by}:")
            for i, b in enumerate(result, start=1):
                print(f"{i}. {b}")
        else:
            print(f"No matches found for '{query}' by {by}.")


# ---- Example Usage ----
if __name__ == "__main__":
    lib = Library()
    lib.add_book(Book("Clean Code", "Robert Martin"))
    lib.add_book(Book("The Pragmatic Programmer", "Andrew Hunt"))
    lib.add_book(Book("Introduction to Algorithms", "Cormen"))

    lib.list_books()
    lib.search("code", by="title")
    lib.search("martin", by="author")
    lib.search("unknown", by="author")
