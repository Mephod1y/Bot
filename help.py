from tabulate import tabulate
from abc import ABC, abstractmethod

class Output(ABC):
    @abstractmethod
    def out_info(self):
        pass
class OutInfo(Output):
    def __init__(self, data, header_table):
        self.data = data
        self.headers = header_table
    def out_info(self):
        print(tabulate(self.data, headers=self.headers, tablefmt= 'pipe', showindex='always'))

def all_commands():

    help_list = [

        ('Add a birthday to an existing contact', 'add birthday'),
        ('Add a new phone number to an existing contact', 'add phone'),
        ('Add an address to an existing contact', 'add address'),
        ('Add an email address to an existing contact', 'add email'),
        ('Change the address of an existing contact', 'change address'),
        ('Change the birthday of an existing contact', 'change birthday'),
        ('Change the phone number of an existing contact', 'change phone'),
        ('Change the mailbox of an existing contact', 'change email'),
        ('Close program and save data', 'close'),
        ('Close program and save data', 'good bye'),
        ('Command list', 'help'),
        ('Create a new contact with the following fields', 'add contact'),
        ('Delete an address from an existing contact', 'delete address'),
        ('Delete an existing contact', 'delete contact'),
        ("Delete an existing contact's mailbox", 'delete email'),
        ('Delete the birthday of an existing contact', 'delete birthday'),
        ('Delete the phone number of an existing contact', 'delete phone'),
        ('Exit the program and save the data', 'exit'),
        ('Greeting', 'hello'),
        ('List users whose birthday is in N days', 'birthday list'),
        ('Look up a phone number based on the name of an existing contact', 'phone'),
        ('Search contact', 'search'),
        ('Shows how many days are left until the birthday', 'birthday contact'),
        ('View all contacts', 'show all contacts'),

        ]

    OutInfo(help_list,['DESCRIPTION', 'COMMAND']).out_info()
    return f''
