import pickle
from hm7task1 import AddressBook, Record

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Enter a valid command."
        except ValueError as e:
            return str(e) 
        except IndexError:
            return "Enter username and phone number separated by space."

    return inner

def parse_input(user_input):
    parts = user_input.split()  
    command = parts[0].strip().lower()  
    args = parts[1:]  
    return command, args  

def hello():
    return "How can I help you?"

def check_existing_contact(func):
    def wrapper(args, book):
        username = args[0]
        if book.find_record(username):
            return "Contact with this name already exists."
        else:
            return func(args, book)
    return wrapper

@input_error
def add_contact(args, book: AddressBook):
    if len(args) != 2:
        raise ValueError("Give me format command name and phone please.")
    
    name, phone = args

    if len(name) < 3:
        raise ValueError("Name should be at least two characters long.")

    if len(phone) != 10:
        raise ValueError("Phone number should be 10 digits long.")

    if not phone.isdigit():
        raise ValueError("Phone number should contain only digits.")

    record = book.find_record(name)
    message = "Contact updated."
    if record is None:
        record = Record(name)
        book.add_record(record)
        message = "Contact added."
    if phone:
        record.add_phone(phone)
    return message



@input_error
def change_contact(args, book):
    
    if len(args) != 2:
        raise ValueError("Give me format command name and phone please.")
    
    username, phone = args

    if len(username) < 3:
        raise ValueError("Name should be at least two characters long.")

    if len(phone) != 10:
        raise ValueError("Phone number should be 10 digits long.")

    if not phone.isdigit():
        raise ValueError("Phone number should contain only digits.")
    
  
    record = book.find_record(username)
    if record:
        record.phones = []
        record.add_phone(phone)
        return "Contact phone number updated."
    else:
        raise ValueError("Name not found in adr book.")

@input_error
def get_phone(args, book):
    if len(args) != 1:
        raise IndexError
    username = args[0]
    record = book.find_record(username)
    if record:
        return record.phones[0]
    else:
        raise ValueError("Name not found in adr book.")

@input_error
def show_all(book):
    contacts = book.contacts
    if not contacts:
        return "No contacts found."
    result = ""
    for record in contacts.values():
        result += f"{record.name}: {record.phones[0]}\n"
    return result.strip()

@input_error
def add_birthday(args, book):
    if len(args) != 2:
        raise ValueError("Give me command name and birthday please.")
    username, birthday = args
    record = book.find_record(username)
    if record:
        if record.birthday:
            record.add_birthday(birthday)
            return "Birthday already set for this contact. Birthday was updated!"
        record.add_birthday(birthday)
        return "Birthday added to contact."
    else:
        raise ValueError("Name not found in address book. can't add Birthday")

@input_error
def show_birthday(args, book):
    if len(args) != 1:
        raise IndexError("Enter username.")
    username = args[0]
    record = book.find_record(username)
    if record and record.birthday:
        return f"{record.name}'s birthday: {record.birthday}"
    else:
        raise ValueError("User not found in adr book")

@input_error
def birthdays(book):
    upcoming_birthdays = book.get_upcoming_birthdays()
    if not upcoming_birthdays:
        return "Список привітань на цьому тижні: []"
    result = [f"{name}'s birthday: {birthday}" for name, birthday in upcoming_birthdays]
    return "Список привітань на цьому тижні: [" + ', '.join(result) + "]"

def help():
    commands = [
        {"hello": 'responds with "How can I help you?"'},#+
        {"add username phone": "Adds a new contact. User inputs username and phone number separated by space."},#+
        {"change username phone": "Updates the phone number for an existing contact."},#+
        {"phone username": "Displays the phone number for the specified contact."},#+
        {"add-birthday username birthday": "Adds birthday to a contact."},
        {"show-birthday username": "Displays the birthday for the specified contact."},
        {"all": "Displays all saved contacts with their phone numbers."},#+
        {"birthdays": "Displays upcoming birthdays."},
        {"close or exit": 'terminates the program with "Good bye!" message'} #+
    ]
    help_text = ""
   
    for command_info in commands:
        for command, description in command_info.items():
            help_text += f"\n{command}: {description}\n"
    return help_text

# Function to save data
def save_data(book, filename="addressbook.pkl"):
    with open(filename, "wb") as file:
        pickle.dump(book, file)

# Function to load data
def load_data(filename="addressbook.pkl"):
    try:
        with open(filename, "rb") as file:
            data = pickle.load(file)
            return data if isinstance(data, AddressBook) else AddressBook()
    except (FileNotFoundError, EOFError):
        return AddressBook() 


def main():
    book = load_data()

    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            save_data(book)
            break
        elif command == "hello":
            print(hello()) 
        elif command == "add":
            print(add_contact(args, book))  
        elif command == "change":
            print(change_contact(args, book)) 
        elif command == "phone":
            print(get_phone(args, book)) 
        elif command == "all":
            print(show_all(book))  
        elif command == "add-birthday":
            print(add_birthday(args, book)) 
        elif command == "show-birthday":
            print(show_birthday(args, book))
        elif command == "birthdays":
            print(birthdays(book)) 
        elif command == "help":
            print(help())  
        else:
            print("Invalid command.") 

if __name__ == "__main__":
    main()