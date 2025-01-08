class Contact:
    def __init__(self, first_name="", last_name="", address="", city="", state="", zip="", phone_num="", email=""):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.phone = phone_num
        self.email = email

    def create_contact(self):
        self.first_name = input("Enter First Name: ")
        self.last_name = input("Enter Last Name: ")
        self.address = input("Enter your Address: ")
        self.city = input("Enter your City: ")
        self.state = input("Enter your State: ")
        self.zip = input("Enter your Pin code: ")
        self.phone = input("Enter Phone number: ")
        self.email = input("Enter your Email address: ")

    def get_key(self):
        return f"{self.first_name} {self.last_name} {self.phone}"

    def __str__(self):
        return (f"Name: {self.first_name} {self.last_name}\n"
                f"Address: {self.address}, {self.city}, {self.state} - {self.zip}\n"
                f"Phone: {self.phone}, Email: {self.email}")

class AddressBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, contact):
        contact_key = contact.get_key()
        if contact_key in self.contacts:
            print(f"Contact with the name {contact.first_name} {contact.last_name} and phone number {contact.phone} already exists.")
        else:
            self.contacts[contact_key] = contact
            print(f"Added contact for {contact.first_name} {contact.last_name} with phone: {contact.phone}.")

    def display_contacts(self):
        if not self.contacts:
            print("No contacts in the address book.")
        else:
           
            print("Address Book:")
            for contact in self.contacts.values():
                print(f"\n{contact}")

class AddressBookMain:
    def __init__(self):
        self.address_book = AddressBook()

    def display(self):
        print("Welcome to the Address Book program")

    def add_new_contact(self):
        contact = Contact()
        contact.create_contact()
        self.address_book.add_contact(contact)

    def show_all_contacts(self):
        self.address_book.display_contacts()

if __name__ == "__main__":
    address_book_main = AddressBookMain()
    address_book_main.display()

    while True:
        print("\n1. Add a new contact")
        print("2. Display all contacts")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            address_book_main.add_new_contact()
        elif choice == '2':
            address_book_main.show_all_contacts()
        elif choice == '3':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")