# tests.py

from Operations import *

# Reset data for tests
books.clear()
members.clear()

# Test 1: Add a book
assert add_book(123456, "Test Book", "Test Author", "Fiction", 1) == True, "Failed to add book"
assert 123456 in books, "Book not added to dictionary"

# Test 2: Add a member
assert add_member(1, "Test Member", "test@example.com") == True, "Failed to add member"
assert len(members) == 1, "Member not added to list"

# Test 3: Borrow when no copies available (initially 1 copy)
assert borrow_book(1, 123456) == True, "Failed to borrow available book"
assert borrow_book(1, 123456) == False, "Borrowed when no copies available"

# Test 4: Borrow limit
assert borrow_book(1, 123456) == False, "Already borrowed one, but no more copies"
# Add another book
add_book(654321, "Another Book", "Another Author", "Sci-Fi", 1)
borrow_book(1, 654321)
# Borrow third (add one more)
add_book(112233, "Third Book", "Third Author", "Non-Fiction", 1)
borrow_book(1, 112233)
# Try fourth
add_book(445566, "Fourth Book", "Fourth Author", "Fiction", 1)
assert borrow_book(1, 674577) == False, "Borrowed beyond limit of 3"

assert delete_member(1) == False, "Deleted member with borrowed books"
# Return all
return_book(1, 123456)
return_book(1, 654321)
return_book(1, 112233)
assert delete_member(1) == True, "Failed to delete member after returns"

print("All tests passed!")