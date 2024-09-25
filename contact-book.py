# Simple Contact Book in Python

# Contact Book dictionary
contact_book = {}

# Function to add a contact
def add_contact():
    name = input("Enter the contact's name: ").capitalize()
    phone = input("Enter the contact's phone number: ")
    if name in contact_book:
        print(f"{name} is already in the contact book.")
    else:
        contact_book[name] = phone
        print(f"Contact {name} added successfully!")

# Function to view all contacts
def view_contacts():
    if contact_book:
        print("\nContact List:")
        for name, phone in contact_book.items():
            print(f"Name: {name}, Phone: {phone}")
    else:
        print("No contacts available.")

# Function to update a contact
def update_contact():
    name = input("Enter the name of the contact to update: ").capitalize()
    if name in contact_book:
        new_phone = input(f"Enter the new phone number for {name}: ")
        contact_book[name] = new_phone
        print(f"Contact {name} updated successfully!")
    else:
        print(f"{name} is not in the contact book.")

# Function to delete a contact
def delete_contact():
    name = input("Enter the name of the contact to delete: ").capitalize()
    if name in contact_book:
        del contact_book[name]
        print(f"Contact {name} deleted successfully!")
    else:
        print(f"{name} is not in the contact book.")

# Main loop for the contact book
def contact_book_menu():
    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            update_contact()
        elif choice == '4':
            delete_contact()
        elif choice == '5':
            print("Exiting Contact Book.")
            break
        else:
            print("Invalid option. Please try again.")

# Run the contact book menu
if __name__ == "__main__":
    contact_book_menu()