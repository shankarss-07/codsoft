# Simple Contact Book in Python
contacts = {}
def add_contact(name, phone, email):
    contacts[name] = {"Phone": phone, "Email": email}  # Add contact to dictionary
    print(f"Contact {name} added successfully.")  

 # Function to remove  contact
def remove_contact(name):
    if name in contacts:  
        del contacts[name]  
        print(f"Contact {name} removed successfully.")  # Confirmation message
    else:
        print(f"Contact {name} does not exist.")

  # Function to view details of  contact
def view_contact(name):
    if name in contacts:  
        print(f"Name: {name}")  # Print contact's name
        print(f"Phone: {contacts[name]['Phone']}")  # Print contact's phone number
        print(f"Email: {contacts[name]['Email']}")  # Print contact's email
    else:
        print(f"Contact {name} not found.")  

 # Function to list all contacts
def list_contacts():
    if contacts:  
        print("Contact List:")
        for name, details in contacts.items():  
            print(f"Name: {name}, Phone: {details['Phone']}, Email: {details['Email']}")
    else:
        print("No contacts found.")  

 # Function to update an existing contact
def update_contact(name, phone=None, email=None):
    if name in contacts:  
        if phone: 
            contacts[name]['Phone'] = phone
        if email:  
            contacts[name]['Email'] = email
        print(f"Contact {name} updated successfully.")  
    else:
        print(f"Contact {name} not found.")  

 # Menu  interface
while True:
    print("\nContact Book Menu:")
    print("1. Add Contact")
    print("2. Remove Contact")
    print("3. View Contact")
    print("4. List All Contacts")
    print("5. Update Contact")
    print("6. Exit")
    
    # Get the user's choice
    choice = input("Choose an option (1-6): ")

    if choice == '1':  # Add contact
        name = input("Enter Name: ")
        phone = input("Enter Phone Number: ")
        email = input("Enter Email: ")
        add_contact(name, phone, email)

    elif choice == '2':  # Remove contact
        name = input("Enter Name to Remove: ")
        remove_contact(name)

    elif choice == '3':  # View contact
        name = input("Enter Name to View: ")
        view_contact(name)
        
    elif choice == '4':  # List all contacts
        list_contacts()
        
    elif choice == '5':  # Update contact
        name = input("Enter Name to Update: ")
        phone = input("Enter New Phone Number (leave blank if no change): ")
        email = input("Enter New Email (leave blank if no change): ")
        update_contact(name, phone if phone else None, email if email else None)
        
    elif choice == '6':  # Exit the program
        print("Exiting Contact Book. Goodbye!")
        break  # Break the loop 
    else:
        print("Invalid choice. Please select a valid option.")  # Error message for invalid input
