from abc import ABC, abstractmethod
from datetime import date

class InvalidItemTypeException(Exception):
    pass

class AlreadyIssuedException(Exception):
    pass

class LibraryItem(ABC):
    def __init__(self, item_id, title):
        self.id = item_id
        self.title = title
        self.issue_date = None
        self.is_issued = False  

    @abstractmethod 
    def calculate_fine(self, return_date):
        pass

class Book(LibraryItem):
    def calculate_fine(self, return_date):
        if (return_date - self.is_issued>14):
            return (return_date-self.is_issued)*2
        else:
            return 0
    
class Journal(LibraryItem):
    def calculate_fine(self, return_date):
        if (return_date - self.is_issued>7):
            return (return_date-self.is_issued)*5
        else:
            return 0

class DigitalMedia(LibraryItem):
    def calculate_fine(self, return_date):
        return 0  

class LibraryUser:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name
        self.borrowed_items = []

    def borrow_item(self, item):
        try:
            if not isinstance(item, LibraryItem):
                raise InvalidItemTypeException("Not a LibraryItem")

            if item.is_issued:
                raise AlreadyIssuedException("Already issued")

            if item in self.borrowed_items:
                print("You already borrowed this!")
                return
            item.issue_date = date.today()
            item.is_issued = True
            self.borrowed_items.append(item)
            print("Successfully borrowed:", item.title)

        except Exception as e: 
            print("Error:", e)


    def return_item(self, item, return_date):
        if item in self.borrowed_items:
            fine = item.calculate_fine(return_date)
            print("Returning ",item.title," Fine Calculated: ₹","fine")
            
            # Resetting item status
            item.is_issued = False
            item.issue_date = None
            self.borrowed_items.remove(item)
        else:
            print("Error: This item was not borrowed by this user.")

b1 = Book(101, "Python Programming")
j1 = Journal(201, "Science Today")
d1 = DigitalMedia(301, "AI Apps")

user1 = LibraryUser("1", "Alice")

user1.borrow_item(b1)
user1.borrow_item(j1)

user2 = LibraryUser("U002", "Bob")
user2.borrow_item(b1)

