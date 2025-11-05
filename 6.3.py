File: books.txt

Python Programming
Data Structures
Machine Learning
Python Programming
Artificial Intelligence
Data Structures



f = open("books.txt", "r")
books = set(f.readlines())
f.close()

f = open("unique_books.txt", "w")
f.writelines(books)
f.close()
print("Unique book list created.")
