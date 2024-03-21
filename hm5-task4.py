def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Enter a valid command."
        except ValueError:
            return "Give me name and phone please."
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
    def wrapper(args, contacts):
        username = args[0]
        if username in contacts:
            return "Contact with this name already exists."
        else:
            return func(args, contacts)
    return wrapper

@input_error
@check_existing_contact
def add_contact(args, contacts):
    if len(args) != 2:
        raise ValueError("Give me name and phone please.")
    username, phone = args
    contacts[username] = phone
    return "Contact added."

@input_error
def change_contact(args, contacts):
    if len(args) != 2:
        raise IndexError
    username, phone = args
    if username in contacts:
        contacts[username] = phone
        return "Contact phone number updated."
    else:
        raise KeyError

@input_error
def get_phone(args, contacts):
    if len(args) != 1:
        raise IndexError
    username = args[0]
    if username in contacts:
        return contacts[username]
    else:
        raise KeyError

@input_error
def show_all(contacts):
    if not contacts:
        return "No contacts found."
    result = ""
    for username, phone in contacts.items():
        result += f"{username}: {phone}\n"
    return result.strip()

def help():
    commands = [
        {"hello": 'responds with "How can I help you?"'},
        {"add username phone": "Adds a new contact. User inputs username and phone number separated by space."},
        {"change username phone": "Updates the phone number for an existing contact."},
        {"phone username": "Displays the phone number for the specified contact."},
        {"all": "Displays all saved contacts with their phone numbers."},
        {"close or exit": 'terminates the program with "Good bye!" message'}
    ]
    help_text = ""
   
    for command_info in commands:
        for command, description in command_info.items():
            help_text += f"\n{command}: {description}\n"
    return help_text

def main():
    contacts = {} 
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print(hello()) 
        elif command == "add":
            print(add_contact(args, contacts))  
        elif command == "change":
            print(change_contact(args, contacts)) 
        elif command == "phone":
            print(get_phone(args, contacts)) 
        elif command == "all":
            print(show_all(contacts))  
        elif command == "help":
            print(help())  
        else:
            print("Invalid command.") 

if __name__ == "__main__":
    main()