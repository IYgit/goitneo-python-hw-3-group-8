from address_book import AddressBook, Record

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "KeyError: The specified key does not exist."
        except ValueError:
            return "ValueError: Incorrect value specified."
        except IndexError:
            return "IndexError: The specified index is out of range."

    return inner

def print_users(book):
    users = list(map(lambda record: {str(record.name.value), ", ".join(phone.value for phone in record.phones)}, book.values()))
    print(users)

@input_error
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error
def add_contact(args, book: AddressBook):
    name, phone = args
    record = Record(name)
    record.add_phone(phone)
    book.add_record(record)
    return "Contact added."

@input_error
def change_username_phone(args, book: AddressBook):
    name, phone = args
    if name in book: 
        record = book.find(name) 
        for p in map(lambda x: x.value,record.phones):
            record.delete_phone(p)  
        record.add_phone(phone)
        return "Contact updated."
    else:
        return "Contact not found."

@input_error
def show_phone(args, book):
    name = args[0]
    if name in book:
        return f"{list(map(lambda record: ", ".join(phone.value for phone in record.phones), book.values()))}"
    else:
        return "Contact not found."

@input_error
def show_all(book: AddressBook):
    return list(map(lambda record: {str(record.name.value), ", ".join(phone.value for phone in record.phones)}, book.values()))

def add_birthday(args, book: AddressBook):    
    name, birthday = args
    record = book.find(name)
    record.add_birthday(birthday)
    return "Birthday added."

def show_birthday(args, book: AddressBook):
    name = args[0]
    record = book.find(name)
    return record.birthday

def birthdays(book: AddressBook):
    return book.get_birthdays_per_week()

def main():
    contacts = AddressBook()
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_username_phone(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            for contact in show_all(contacts):
                print(contact)
        elif command == "add-birthday":
            print(add_birthday(args, contacts))
        elif command == "show-birthday":
            print(show_birthday(args, contacts))
        elif command == "birthdays":
            print(birthdays(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()