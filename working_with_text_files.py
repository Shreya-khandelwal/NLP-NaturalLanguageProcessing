from datetime import datetime
person = "shreya"
print("my name is {}".format(person))
print(f"my name is {person}")   
d = {'a':123, 'b':456}
print(f"my number is {d['a']}")
mylist = [0,1,2]
print(f"my list number is {mylist[1]}")
library = [('book','author','pages'),('a','aa',1),('b','bb',2),('c','cc',3)]
for books in library:
    print(books)
    print(f"page number count is {books[2]}")

for books,authors,page in library:
    print(f"{books} {authors} {page}")

#formatting : number of spaces
for books,authors,page in library:
    print(f"{books:{5}} {authors:{5}} {page:.>{7}}")

today = datetime(year=1999, month=8, day=4)
print(today)
print(f"{today:%B %d %Y}")
