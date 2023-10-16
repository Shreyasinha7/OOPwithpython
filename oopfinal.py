from datetime import datetime, timedelta
#DOMAIN ENTITIES:
class Book:
    def __init__(self, title, author, ISBN, description, available_copies):
        self.title = title
        self.author = author
        self.ISBN = ISBN
        self.description = description
        self.available_copies = available_copies

    def display_info(self):
        return f"Title: {self.title}\nAuthor: {self.author}\nISBN: {self.ISBN}\nDescription: {self.description}\nAvailable Copies: {self.available_copies}"

class Borrower:
    def __init__(self, title, editor, ISSN, description, available_copies):
        self.title = title
        self.editor = editor
        self.ISSN = ISSN
        self.description = description
        self.available_copies = available_copies
    def display_info(self):
        return f"Title: {self.title}\nEditor: {self.editor}\nISSN: {self.ISSN}\nDescription: {self.description}\nAvailable Copies: {self.available_copies}"

class User:
    def __init__(self, title, editor, ISSN, description, available_copies):
        self.title = title
        self.editor = editor
        self.ISSN = ISSN
        self.description = description
        self.available_copies = available_copies

    def display_info(self):
        return f"Title: {self.title}\nEditor: {self.editor}\nISSN: {self.ISSN}\nDescription: {self.description}\nAvailable Copies: {self.available_copies}"



class Journal:
    def __init__(self, title, editor, ISSN, description, available_copies):
        self.title = title
        self.editor = editor
        self.ISSN = ISSN
        self.description = description
        self.available_copies = available_copies

    def display_info(self):
        return f"Title: {self.title}\nEditor: {self.editor}\nISSN: {self.ISSN}\nDescription: {self.description}\nAvailable Copies: {self.available_copies}"




class Magazine:
    def __init__(self, title, editor, ISSN, description, available_copies):
        self.title = title
        self.editor = editor
        self.ISSN = ISSN
        self.description = description
        self.available_copies = available_copies

    def display_info(self):
        return f"Title: {self.title}\nEditor: {self.editor}\nISSN: {self.ISSN}\nDescription: {self.description}\nAvailable Copies: {self.available_copies}"



class Vendor:
    def __init__(self, name, address, contact_info):
        self.name = name
        self.address = address
        self.contact_info = contact_info

    def display_info(self):
        return f"Vendor Name: {self.name}\nAddress: {self.address}\nContact Info: {self.contact_info}"

class Publisher:
    def __init__(self, name, address, contact_info):
        self.name = name
        self.address = address
        self.contact_info = contact_info

    def display_info(self):
        return f"Publisher Name: {self.name}\nAddress: {self.address}\nContact Info: {self.contact_info}"
    


######## END OF DOMAIN ENTITIES   #########



#CONTROL ENTITIES
from datetime import datetime, timedelta

class Book:
    def __init__(self, title, author, available_copies):
        self.title = title
        self.author = author
        self.available_copies = available_copies

    def display_info(self):
        return f"Title: {self.title}\nAuthor: {self.author}\nAvailable Copies: {self.available_copies}"

class Patron:
    def __init__(self, name, id, borrow_date, return_date, contact):
        self.name = name
        self.id = id
        self.borrow_date = borrow_date
        self.return_date = return_date
        self.contact = contact

    def display_info(self):
        return f"Name: {self.name}\nID: {self.id}\nBorrow Date: {self.borrow_date}\nReturn Date: {self.return_date}\nContact: {self.contact}"

class LibraryManagementSystem:
    def __init__(self):
        self.books = []
        self.patrons = []

    def add_book(self, book):
        self.books.append(book)

    def add_patron(self, patron):
        self.patrons.append(patron)

    def list_books(self):
        for book in self.books:
            print(book.display_info())
            print("\n")

    def list_patrons(self):
        for patron in self.patrons:
            print(patron.display_info())
            print("\n")

class Borrowing:
    def __init__(self, patron, book, due_date):
        self.patron = patron
        self.book = book
        self.due_date = due_date
        self.returned = False

    def return_item(self):
        self.returned = True

    def calculate_penalty(self):
        if not self.returned:
            # Calculate penalty based on due date
            days_overdue = (datetime.now() - self.due_date).days
            if days_overdue > 0:
                return days_overdue * 5  # Assuming $5 per day penalty
        return 0  # No penalty if returned on time

class Issuing:
    def issue_item(self, patron, item, borrowing_period):
        if item.available_copies > 0:
            item.available_copies -= 1
            due_date = datetime.now() + timedelta(days=borrowing_period)
            borrowing_record = Borrowing(patron, item, due_date)
            return borrowing_record
        else:
            return None  # No available copies

class Returning:
    def return_item(self, borrowing_record):
        borrowing_record.return_item()
        penalty = borrowing_record.calculate_penalty()
        return penalty


    
    
############# END OF CONTROL ENTITIES ############


#BOUNDARY ENTITIES

class FacultyMember:
    def __init__(self, library_system):
        self.library_system = library_system

    def search_availability(self, title):
        # Functionality for a faculty member to search for the availability of a book
        available_books = self.library_system.search_item_by_title(title)
        return available_books

    def recommend_book(self, faculty, book_title, author, description):
        # Functionality for a faculty member to recommend a new book to the library
        recommended_book = self.library_system.recommend_book(faculty, book_title, author, description)
        return f"Book '{recommended_book.title}' has been recommended to the library."

    def borrow_book(self, faculty, book_title):
        # Functionality for a faculty member to borrow a book
        books = self.library_system.search_item_by_title(book_title)
        if books:
            book = books[0]
            borrowing_record = faculty.borrow_book(book)
            if borrowing_record:
                return f"Successfully borrowed '{book_title}' with due date {borrowing_record.due_date}."
            else:
                return "No available copies of the book."
        else:
            return "Book not found in the catalog."

    def return_book(self, faculty, book_title):
        # Functionality for a faculty member to return a book
        books = self.library_system.search_item_by_title(book_title)
        if books:
            book = books[0]
            penalty = faculty.return_book(book)
            if penalty > 0:
                return f"Book '{book_title}' returned with a penalty of ${penalty}."
            else:
                return f"Book '{book_title}' returned successfully."
        else:
            return "Book not found in the catalog."

    def report_issue(self, faculty, issue_description):
        # Functionality for a faculty member to report an issue to the admin
        admin_email = "admin@example.com"  # Replace with actual admin contact
        # Send an email or create a support ticket with the issue description
        # Additional logic for notifying the admin
        return f"Issue reported to admin. You will be contacted at {admin_email}."


class LibraryStaff:
    def __init__(self, library_system):
        self.library_system = library_system

    def search_availability(self, title):
        # Functionality for a library staff member to search for the availability of a book
        available_books = self.library_system.search_item_by_title(title)
        return available_books

    def issue_book(self, student_faculty, book_title):
        # Functionality for a library staff member to issue a book to a student or faculty
        books = self.library_system.search_item_by_title(book_title)
        if books:
            book = books[0]
            borrowing_record = student_faculty.borrow_book(book)
            if borrowing_record:
                return f"Successfully issued '{book_title}' to {student_faculty.name} with a due date of {borrowing_record.due_date}."
            else:
                return "No available copies of the book."
        else:
            return "Book not found in the catalog."

    def collect_book(self, student_faculty, book_title):
        # Functionality for a library staff member to collect a book returned by a student or faculty
        books = self.library_system.search_item_by_title(book_title)
        if books:
            book = books[0]
            penalty = student_faculty.return_book(book)
            if penalty > 0:
                return f"Book '{book_title}' collected with a penalty of ${penalty}."
            else:
                return f"Book '{book_title}' collected successfully."
        else:
            return "Book not found in the catalog."

    def receive_recommendations(self):
        # Functionality for a library staff member to receive book recommendations from students/faculty
        recommendations = self.library_system.receive_recommendations()
        return recommendations

    def add_book(self, book):
        # Functionality for a library staff member to add a new book to the LMS
        self.library_system.add_book(book)
        return f"Book '{book.title}' has been added to the library."

    def remove_book(self, book_title):
        # Functionality for a library staff member to remove a book from the LMS
        removed_book = self.library_system.remove_book(book_title)
        if removed_book:
            return f"Book '{book_title}' has been removed from the library."
        else:
            return "Book not found in the catalog."

    def penalize_defaulter(self, student_faculty):
        # Functionality for a library staff member to penalize defaulters
        penalty = student_faculty.calculate_penalty()
        if penalty > 0:
            return f"{student_faculty.name} has been penalized with a fine of ${penalty}."
        else:
            return f"{student_faculty.name} is not a defaulter."

    def report_issue(self, issue_description):
        # Functionality for a library staff member to report an issue to the admin
        admin_email = "admin@example.com"  # Replace with actual admin contact
        # Send an email or create a support ticket with the issue description
        # Additional logic for notifying the admin
        return f"Issue reported to admin. You will be contacted at {admin_email}."


class Administrator:
    def __init__(self, library_system):
        self.library_system = library_system

    def monitor_dashboard(self):
        # Functionality for the administrator to monitor the overall status of the library
        dashboard_data = self.library_system.monitor_dashboard()
        return dashboard_data

    def search_availability(self, title):
        # Functionality for the administrator to search for the availability of a book
        available_books = self.library_system.search_item_by_title(title)
        return available_books

    def add_book(self, book):
        # Functionality for the administrator to add a new book to the LMS
        self.library_system.add_book(book)
        return f"Book '{book.title}' has been added to the library."

    def remove_book(self, book_title):
        # Functionality for the administrator to remove a book from the LMS
        removed_book = self.library_system.remove_book(book_title)
        if removed_book:
            return f"Book '{book_title}' has been removed from the library."
        else:
            return "Book not found in the catalog."

    def receive_issues(self):
        # Functionality for the administrator to receive all the issues reported by students, faculty, and library staff
        issues = self.library_system.receive_issues()
        return issues

    def library_analytics(self):
        # Functionality for the administrator to view various analytics of the library
        analytics_data = self.library_system.library_analytics()
        return analytics_data

class BoundaryLibrary:
    def __init__(self):
        self.books = []
        self.students = []
        self.faculty = []
        self.library_staff = []
        self.issues = []
        self.vendors = []
        self.publishers = []

# # Create Library Management System
# library_system = LibraryManagementSystem()

# # Add Domain Entities
# book1 = Book("Aditi", "001", "03-sep-23")
# book2 = Book("John Doe", "002", "04-sep-23")
# library_system.add_book(book1)
# library_system.add_book(book2)

# borrower1 = Borrower("Priya", "1RVU22BSC097", "03-sept-23", "03-sept-26", "123456789")
# borrower2 = Borrower("Jane Smith", "1RVU22BSC077", "03-sept-23", "03-sept-26", "987654321")
# library_system.add_borrower(borrower1)
# library_system.add_borrower(borrower2)

# user1 = User("Alice", "U001")
# user2 = User("Bob", "U002")
# library_system.add_user(user1)
# library_system.add_user(user2)

# Journal1 = Journal("John Doe", "P001")
# Journal2 = Journal("Jane Smith", "P002")
# library_system.add_journal(Journal1)
# library_system.add_journal(Journal2)      

# Magazine1 = Magazine("John Doe", "P001")
# Magazine2 = Magazine("Jane Smith", "P002")
# library_system.add_magazine(Magazine1)
# library_system.add_magazine(Magazine2)

# Vendor1 = Vendor("John Doe", "P001")
# Vendor2 = Vendor("Jane Smith", "P002")
# library_system.add_vender(Vendor1)
# library_system.add_vendor(Vendor2)

# Publisher1 = Publisher("John Doe", "P001")
# Publisher2 = Publisher("Jane Smith", "P002")
# library_system.add_Publisher(Publisher1)
# library_system.add_Publisher(Publisher2)


