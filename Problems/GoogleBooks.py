

b=int(input("No.of Books"))
l=int(input("No.of Libraries"))
d=int(input("No.of Days"))
bookScores=[]
for i in range(b):
    bookScores.append(int(input("Enter the book score")))
for i in range(l):
    bl=int(input("No. of books in the library"))
    t=int(input("Days to finish signup of library"))
    m=int(input("no. of books that can be shipped from the library"))
    for j in range(bl):
        bid.append(int(input("Enter the ids of the book available in the library")))