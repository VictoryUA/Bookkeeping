from collections import defaultdict

class Book:
    def __init__(self, author, title, category):
        self.author = author
        self.title = title
        self.category = category
    
    def __repr__(self):
        return f"Book(author='{self.author}', title='{self.title}', category='{self.category}')"

class Shelf:
    def __init__(self):
        self.books = []
    
    def add_book(self, book):
        self.books.append(book)
    
    def sort_books_by_title(self):
        self.books.sort(key=lambda x: x.title)

class Library:
    def __init__(self):
        self.shelves = defaultdict(Shelf)
    
    def add_book(self, book):
        self.shelves[book.category].add_book(book)
    
    def organize_books(self, books):
        for book in books:
            self.add_book(book)
    
    def sort_books_on_shelves(self):
        for shelf in self.shelves.values():
            shelf.sort_books_by_title()
    
    def print_library(self):
        for category, shelf in self.shelves.items():
            print(f"Shelf for {category}: {shelf.books}")

# Example usage
if __name__ == "__main__":
    # Creating some sample books
    book1 = Book("Joe Dispenza", "You Are the Placebo: Making Your Mind Matter", "Ezoterik")
    book2 = Book("George Orwell", "1984", "Dystopian")
    book3 = Book("Sergey Plokhiy", "Lost kindom", "History")
    
    # Organizing the books
    library = Library()
    all_books = [book1, book2, book3]
    library.organize_books(all_books)
    
    # Sorting the books on shelves
    library.sort_books_on_shelves()
    
    # Printing the organized shelves
    library.print_library()
