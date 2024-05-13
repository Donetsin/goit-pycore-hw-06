'''this module provides OOP model of the note helper'''
import re
from collections import UserDict

class Field:
    '''documentation for the class Field'''
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    '''documentation for the class Name'''
    pass

class Phone(Field):
    '''documentation for the class Phone'''
    def __init__(self, value):
        super().__init__(value)
        if not re.fullmatch(r"\d{10}", value):
            raise ValueError("Error. Phone number must be 10 digits")

class Record:
    '''documentation for the class Record'''
    def __init__(self, person_name):
        self.name = Name(person_name)
        self.phones = []

    def __str__(self):
        return f"Contact name: {self.name.value}, phone(s): {', '.join(number for number in self.phones)}"

    def add_phone(self, phone):
        '''add phone number to record line'''
        self.phones.append(phone)

    def del_phone(self, phone):
        '''delete phone number from record line'''
        self.phones = [number for number in self.phones if number.value != phone]

    def edit_phone(self, old_phone, new_phone):
        '''edit phone number in record line'''
        for number in self.phones:
            if number == old_phone:
                number = new_phone

    def find_phone(self, phone):
        '''return phone number from record line'''
        for number in self.phones:
            if number == phone:
                return number
        raise IndexError("Phone number is not found.")

class AddressBook(UserDict):
    '''documentation for the class AddressBook'''
    def add_record(self, record):
        '''add record to address book'''
        self.data[record.name.value] = record

    def find(self, name):
        '''return record from address book'''
        return self.data.get(name)

    def delete(self, name):
        '''delete record from address book'''
        if name in self.data:
            del self.data[name]