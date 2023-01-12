from collections import UserDict
from datetime import datetime
import pickle
import sys

class Field():
    def __init__(self, value):
        self._value = None
        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
       self._value = new_value

class Name(Field):
    def __init__(self, value):
        self.value = value

    def __getitem__(self):
        return self.value

class Address(Field):
    pass

class Phone(Field):

    @Field.value.setter
    def value(self, new_value):
        self._value = new_value

    def __getitem__(self):
        return self.value

class Birthday(Field):

    @Field.value.setter
    def value(self, value):
        self._value = value

    def __str__(self) -> str:
        return self._value.strftime("%d.%m.%Y")

class Email(Field):

    @Field.value.setter
    def value(self, new_value):
        self._value = new_value

class Record():
    def __init__(self, name, address: object = None, phones: object = None, email: object = None,
                 birthday: object = None):
        self.name = Name(name)
        self.address = address if address else None
        self.phones = phones if phones else []
        self.email = email if email else None
        self.birthday = birthday if birthday else None

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def get_phones(self):
        return [phone.value for phone in self.phones]

    def add_email(self, email):
        self.email = Email(email)

    def add_address(self, address):
        self.address = Address(address)

    def add_birthday(self, birthday):
        self.birthday = Birthday(birthday)

    def change_phone(self, phone, new_phone):
        for item in self.phones:
            if item.value == phone:
                item.value = new_phone

    def change_email(self, new_email):
        self.email = Email(new_email)

    def change_address(self, new_address):
        self.address = Address(new_address)

    def change_birthday(self, new_birthday):
        self.birthday = Birthday(new_birthday)

    def delete_phone(self, phone):
        for item in self.phones:
            if item.value == phone:
                self.phones.remove(item)

    def delete_email(self):
        self.email = Email(None)

    def delete_address(self):
        self.address = Address(None)

    def delete_birthday(self):
        self.birthday = Birthday(None)

    def get_user_details(self):

        show_phone = ''
        show_birthday = ''
        show_address = ''
        show_email = ''

        for phone in self.phones:
            show_phone += f"{phone.value}  "

        if self.birthday:
            show_birthday = self.birthday.value

        if self.address:
            show_address = self.address.value

        if self.email:
            show_email = self.email.value

        return self.name.value, show_phone, show_birthday, show_address, show_email


class AddressBook(UserDict):

    def __init__(self):
        super().__init__()
        self.address_book_load()

    def add_record(self, record):
        self.data[record.name.value] = record

    def delete_contact(self, name):
        del self.data[name]

    def address_book_load(self):
        try:
            with open('dump.pickle', 'rb') as dump_file:
                self.data = pickle.load(dump_file)
        except FileNotFoundError:
            pass

    def address_book_save(self, archive_book):
        with open('dump.pickle', 'wb') as dump_file:
            pickle.dump(archive_book, dump_file)
        sys.exit()

CONTACTS = AddressBook()