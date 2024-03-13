def parse_input(user_input):
    parts = user_input.split()  
    command = parts[0].strip().lower()  
    args = parts[1:]  
    return command, args  # Повертаємо команду та аргументи у вигляді кортежу

def hello():
    return "How can I help you?"

def add_contact(args, contacts):
    if len(args) != 2:
        return "Invalid number of arguments for add command."
    username, phone = args
    contacts[username] = phone
    return "Contact added."

def change_contact(args, contacts):
    if len(args) != 2:
        return "Invalid number of arguments for change command."
    username, phone = args
    if username in contacts:
        contacts[username] = phone
        return "Contact phone number updated."
    else:
        return "Contact does not exist."

def get_phone(args, contacts):
    if len(args) != 1:
        return "Invalid number of arguments for phone command."
    username = args[0]
    if username in contacts:
        return contacts[username]
    else:
        return "Contact not found."

def show_all(contacts):
    if not contacts:
        return "No contacts found."
    result = ""
    for username, phone in contacts.items():
        result += f"{username}: {phone}\n"
    return result.strip()

def help():
    commands = [
        {"hello": 'відповідає у консоль повідомленням "How can I help you?"'},
        {"add username phone": "За цією командою бот зберігає у пам'яті, наприклад у словнику, новий контакт. Користувач вводить ім'я username та номер телефону phone, обов'язково через пробіл"},
        {"change username phone": "За цією командою бот зберігає в пам'яті новий номер телефону phone для контакту username, що вже існує в записнику."},
        {"phone username": "За цією командою бот виводить у консоль номер телефону для зазначеного контакту username."},
        {"all": "За цією командою бот виводить всі збереженні контакти з номерами телефонів у консоль"},
        {"close або exit": 'за будь-якою з цих команд бот завершує свою роботу після того, як виведе у консоль повідомлення "Good bye!" та завершить своє виконання'}
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