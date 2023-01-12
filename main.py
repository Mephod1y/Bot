from help import all_commands
import book_commands
import sys
import os
dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, dir_path)

COMMANDS =  {
    'hello': book_commands.hello_func,
    'exit': book_commands.exit_func,
    'close': book_commands.exit_func,
    'good bye': book_commands.exit_func,
    'add contact': book_commands.add_contact_func,
    'add phone': book_commands.add_phone_func,
    'add address': book_commands.add_address_func,
    'add email': book_commands.add_email_func,
    'add birthday': book_commands.add_birthday_func,
    'change phone': book_commands.change_phone_func,
    'change address': book_commands.change_address_func,
    'change email': book_commands.change_email_func,
    'change birthday': book_commands.change_birthday_func,
    'delete phone': book_commands.delete_phone_func,
    'delete address': book_commands.delete_address_func,
    'delete email': book_commands.delete_email_func,
    'delete birthday': book_commands.delete_birthday_func,
    'delete contact': book_commands.delete_contact_func,
    'help': all_commands,
    'show all contacts': book_commands.show_all_info,
    'phone': book_commands.phone,
    'birthday contact': book_commands.show_birthday,
    'birthday list': book_commands.list_birthday,
    'search': book_commands.find_contacts
}

def main():

    print(f'Hello! I`m your Bot-assistant Ivan. How can I help you?')
    print('Тo see all commands type: help')

    while True:
        command = input("Please enter the command: ").lower().strip()
        try:
            for key in COMMANDS:
                if command.startswith(key):
                    command = key
                    break
            result = COMMANDS[command]()

            print(result)
        except KeyError:
            book_commands.find_same_input(command, COMMANDS)

if __name__ == '__main__':
    main()
