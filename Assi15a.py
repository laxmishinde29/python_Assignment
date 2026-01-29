class BookStore:

    NoOfBooks = 0

    def __init__(self,BookName,BookAuthor):
        self.Name = BookName
        self.Author = BookAuthor
        BookStore.NoOfBooks = BookStore.NoOfBooks + 1

    def Display(self):
        print(self.Name,"by",self.Author,"No of books:",BookStore.NoOfBooks)

obj1 = BookStore("Linux system programming","Robert Love.")
obj1.Display()

obj2 = BookStore("C programming","Dennis Ritchie.")
obj2.Display()

obj3 = BookStore("Python Programming","gudo van russum.")
obj3.Display()