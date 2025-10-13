# demo.py

from Operations import *

# Add books
add_book(123456, "The Great Gatsby", "F. Scott Fitzgerald", "Fiction", 5)
add_book(654321, "1984", "George Orwell", "Sci-Fi", 3)
add_book(112233, "To Kill a Mockingbird", "Harper Lee", "Fiction", 4)
add_book(674577, "The Shining", "Stephen king","Horror", 5)
# Add members
add_member(1, "Jack Ripper", "jackRip@example.com")
add_member(2, "Hori Kyoto", "Hori@example.com")

# Search books
results = search_books("gatsby")
print("Search results for 'gatsby':")
for ISBN, book in results:
    print(f"ISBN: {ISBN}, Title: {book['title']}, Author: {book['author']}")

# Borrow books
borrow_book(1, 123456)
borrow_book(1, 654321)
borrow_book(2, 112233)
borrow_book(2,674577)

# Try to borrow when limit reached
borrow_book(1, 112233)  # Should fail (limit 3)

# Update book
update_book(123456, title="The Great Gatsby (Updated)")

# Return book
return_book(1, 123456)

# Delete book (should fail if borrowed, but now returned)
delete_book(123456)  # Should succeed now

# Delete member (should fail if has borrowed)
delete_member(1)  # Should fail (has 654321)
return_book(1, 654321)
delete_member(1)  # Should succeed now