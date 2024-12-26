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
        self.last_name = input("Enter Last name: ")
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

    def edit_contact(self):
        print("Edit Contact Details. Press Enter to skip an attribute.")
        first_name = input(f"Edit First Name ({self.first_name}): ") or self.first_name
        last_name = input(f"Edit Last Name ({self.last_name}): ") or self.last_name
        address = input(f"Edit Address ({self.address}): ") or self.address
        city = input(f"Edit City ({self.city}): ") or self.city
        state = input(f"Edit State ({self.state}): ") or self.state
        zip_code = input(f"Edit Zip Code ({self.zip}): ") or self.zip
        phone = input(f"Edit Phone Number ({self.phone}): ") or self.phone
        email = input(f"Edit Email ({self.email}): ") or self.email
        
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip_code
        self.phone = phone
        self.email = email

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

    def edit_contact(self, first_name, last_name, phone):
        contact_key = f"{first_name} {last_name} {phone}"
    
        if contact_key in self.contacts:
            contact = self.contacts[contact_key]
            print(f"Found contact: \n{contact}")
            contact.edit_contact()
            print(f"Contact updated: \n{contact}")
        else:
            print(f"No contact found with the name {first_name} {last_name} and phone number {phone}.")

    def delete_contact(self, first_name, last_name, phone):
        contact_key = f"{first_name} {last_name} {phone}"
        
        if contact_key in self.contacts:
            del self.contacts[contact_key]
            print(f"Deleted contact: {first_name} {last_name} with phone number {phone}.")
        else:
            print(f"No contact found with the name {first_name} {last_name} and phone number {phone}.")

class AddressBookMain:
    def __init__(self):
        self.address_book = AddressBook()

    def display(self):
        print("Welcome to the Address Book program")

    def add_new_contact(self):
        while True:
            contact = Contact()
            contact.create_contact()
            self.address_book.add_contact(contact)
            
            add_another = input("Do you want to add another contact? (y/n): ")
            if add_another.lower() != 'y':
                break

    def show_all_contacts(self):
        self.address_book.display_contacts()

    def edit_existing_contact(self):
        first_name = input("Enter the first name of the contact to edit: ")
        last_name = input("Enter the last name of the contact to edit: ")
        phone = input("Enter the phone number of the contact to edit: ")
        self.address_book.edit_contact(first_name, last_name, phone)

    def delete_contact(self):
        first_name = input("Enter the first name of the contact to delete: ")
        last_name = input("Enter the last name of the contact to delete: ")
        phone = input("Enter the phone number of the contact to delete: ")
        self.address_book.delete_contact(first_name, last_name, phone)

if __name__ == "__main__":
    address_book_main = AddressBookMain()
    address_book_main.display()

    while True:
        print("\n1. Add a new contact")
        print("2. Display all contacts")
        print("3. Edit an existing contact")
        print("4. Delete a contact")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            address_book_main.add_new_contact()
        elif choice == '2':
            address_book_main.show_all_contacts()
        elif choice == '3':
            address_book_main.edit_existing_contact()
        elif choice == '4':
            address_book_main.delete_contact()
        elif choice == '5':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")
