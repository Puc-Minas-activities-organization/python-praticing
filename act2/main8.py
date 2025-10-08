class Book:

    def __init__(self, title, author):
        self.title = title
        self.author = author
    
    #str serve para definir o comportamento do objeto em uma string, sem definir vai aparecer o objeto por default
    def __str__(self):
        return f"{self.title} by {self.author}"
    
    #define a comparação, você pode comparar com os atributos que escolher
    def __eq__(self, other):
        return self.title ==  other.title and self.author == other.author
    
    #também tem o lt (less than) e o gt(greather than) para usar como o eq, você pode definir

    def __add__(self, other):
        return self.author + other.author
    
    def __contains__(self, keyword):
        return keyword in self.title or keyword in self.author

    def __getitem__(self, key):
        if key == "title":
            return self.title
        elif key == "author":
            return self.author
        else: 
            return False

book1 = Book("Hobbit", "J R R Tolkien")
book2 = Book("Alice no país das maravilhas", "Unknown")

print(book1)
print(book2)
print(book1 == book2)
print(book1 + book2)
print("Unknown" in book2)
print(book1['title'])