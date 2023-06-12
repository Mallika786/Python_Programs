# Write a Library class with no_of_books and books as two instance variables. Write a program to create a library from this Library class and show how you can print all books, add a book and get the number of books using different methods. Show that your program doesnt persist the books after the program is stopped


class library:
    def __init__(self):
        self.no_of_book=0
        self.books=[]
    def showBooks(self):
        a=1
        for i in self.books:
            print("Book",a,": ",i,"\n")
            a=a+1
    def addBook(self,bk):
        self.books.append(bk)
        self.no_of_book=self.no_of_book+1
    def getBooks(self):
        if(self.no_of_book==len(self.books)):
            print(self.no_of_book)
            print("Everything is fine!")
        else:
            print("There is something wrong in program,check it out.")

# driver code
obj1=library()
a=1
while(a==1 or a==2 or a==3):
    print("-------------------------------------------------------")
    a=int(input("What action you want to perform?\n1.Add a book\n2.Print all books\n3.Get the no. of books\n>>>"))
    if(a==1):
        bk=input("Enter a book name: ")
        obj1.addBook(bk)
    elif(a==2):
        obj1.showBooks()
    elif(a==3):
        print("The no. of books is: ")
        obj1.getBooks()
    else:
        print("Wrong input!")
