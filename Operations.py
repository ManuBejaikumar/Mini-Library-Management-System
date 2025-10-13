# operations.py

genres = ("Fiction", "Non-Fiction", "History","Horror")  # Tuples

books = {}
members = []
def is_valid_genre(genre):
    return genre in genres

def get_available_copies(ISBN):
    if ISBN not in books:
        return 0
    total = books[ISBN]["total_copies"]
    borrowed_count = 0
    for member in members:
        borrowed_count += member["borrowed_books"].count(ISBN)
    return total - borrowed_count

def add_book(ISBN, title, author, genre, total_copies):
    if ISBN in books:
        print("Error: ISBN already exists.")
        return False
    if not is_valid_genre(genre):
        print("Error: Invalid genre.")
        return False
    books[ISBN] = {
        "title": title,
        "author": author,
        "genre": genre,
        "total_copies": total_copies
    }
    print("Book added successfully.")
    return True

def add_member(member_id, name, email):
    for member in members:
        if member["id"] == member_id:
            print("Error: Member ID already exists.")
            return False
    members.append({
        "id": member_id,
        "name": name,
        "email": email,
        "borrowed_books": []
    })
    print("Member added successfully.")
    return True

def search_books(query):
    results = []
    for ISBN, book in books.items():
        if query.lower() in book["title"].lower() or query.lower() in book["author"].lower():
            results.append((ISBN, book))
    return results

def update_book(ISBN, title=None, author=None, genre=None, total_copies=None):
    if ISBN not in books:
        print("Error: Book not found.")
        return False
    if title is not None:
        books[ISBN]["title"] = title
    if author is not None:
        books[ISBN]["author"] = author
    if genre is not None:
        if not is_valid_genre(genre):
            print("Error: Invalid genre.")
            return False
        books[ISBN]["genre"] = genre
    if total_copies is not None:
        books[ISBN]["total_copies"] = total_copies
    print("Book updated successfully.")
    return True

def update_member(member_id, name=None, email=None):
    for member in members:
        if member["id"] == member_id:
            if name is not None:
                member["name"] = name
            if email is not None:
                member["email"] = email
            print("Member updated successfully.")
            return True
    print("Error: Member not found.")
    return False

def delete_book(ISBN):
    if ISBN not in books:
        print("Error: Book not found.")
        return False
    if get_available_copies(ISBN) != books[ISBN]["total_copies"]:
        print("Error: Cannot delete book with borrowed copies.")
        return False
    del books[ISBN]
    print("Book deleted successfully.")
    return True

def delete_member(member_id):
    for i, member in enumerate(members):
        if member["id"] == member_id:
            if member["borrowed_books"]:
                print("Error: Cannot delete member with borrowed books.")
                return False
            del members[i]
            print("Member deleted successfully.")
            return True
    print("Error: Member not found.")
    return False

def borrow_book(member_id, ISBN):
    # Find member
    member = next((m for m in members if m["id"] == member_id), None)
    if not member:
        print("Error: Member not found.")
        return False
    if len(member["borrowed_books"]) >= 3:
        print("Error: Member has reached borrowing limit (3 books).")
        return False
    if ISBN not in books:
        print("Error: Book not found.")
        return False
    if get_available_copies(ISBN) <= 0:
        print("Error: No available copies.")
        return False
    member["borrowed_books"].append(ISBN)
    print("Book borrowed successfully.")
    return True

def return_book(member_id, ISBN):
    """Return borrowed book."""
    # Find member
    member = next((m for m in members if m["id"] == member_id), None)
    if not member:
        print("Error: Member not found.")
        return False
    if ISBN not in member["borrowed_books"]:
        print("Error: Member does not have this book borrowed.")
        return False
    member["borrowed_books"].remove(ISBN)
    print("Book returned successfully.")
    return True