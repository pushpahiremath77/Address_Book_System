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
        self.city = input("Enter your city: ")
        self.state = input("Enter your state: ")
        self.zip = input("Enter your pin code: ")
        self.phone = input("Enter phone number: ")
        self.email = input("Enter your email address: ")

    def __str__(self):
        return f"Contact created for {self.first_name} {self.last_name}"

class AddressBookMain:
    def display(self):
        print("Welcome to the Address Book System!")

if __name__ == "__main__":
    address_book_main = AddressBookMain()
    address_book_main.display()

    contact1 = Contact()
    contact1.create_contact() 
    print(contact1)  