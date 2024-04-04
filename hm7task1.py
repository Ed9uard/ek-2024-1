from collections import UserDict
from datetime import datetime, timedelta

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    def __init__(self, value):
        if not value:
            raise ValueError("Ім'я не може бути порожнім.")
        super().__init__(value)


class Phone(Field):
    def __init__(self, value):
        if not value.isdigit() or len(value) != 10:
            raise ValueError("Недійсний формат номера телефону. Номер повинен містити рівно 10 цифр.")
        super().__init__(value)


class Birthday(Field):
    def __init__(self, value):
        try:
            datetime.strptime(value, '%d.%m.%Y')
        except ValueError:
            raise ValueError("Недійсний формат дати. Використовуйте формат DD.MM.YYYY.")
        super().__init__(value)


class Record:
    def __init__(self, name, birthday=None):
        self.name = Name(name)
        self.phones = []
        self.birthday = Birthday(birthday) if birthday else None

    def add_phone(self, phone_number):
        phone = Phone(phone_number)
        self.phones.append(phone)

    def remove_phone(self, phone_number):
        self.phones = [phone for phone in self.phones if phone.value != phone_number]

    def edit_phone(self, old_phone_number, new_phone_number):
        # Если старый номер не существует в списке phones, добавляем новый номер
        if old_phone_number not in [phone.value for phone in self.phones]:
            self.add_phone(new_phone_number)
        else:
            # Удаляем старый номер и добавляем новый
            self.remove_phone(old_phone_number)
            self.add_phone(new_phone_number)

    def find_phone(self, phone_number):
        for phone in self.phones:
            if phone.value == phone_number:
                return phone
        return None

    def add_birthday(self, birthday):
        self.birthday = Birthday(birthday)

    def __str__(self):
        phones_str = '; '.join(p.value for p in sorted(self.phones, key=lambda x: x.value))
        birthday_str = self.birthday.value if self.birthday else "N/A"
        return f"Ім'я контакту: {self.name.value}, номери телефонів: {phones_str}, дата народження: {birthday_str}"


class AddressBook(UserDict):
    def __init__(self):
        self.contacts = {}

    def add_record(self, record):
        self.contacts[record.name.value] = record

    def find_record(self, name):
        return self.contacts.get(name, None)

    def delete_record(self, name):
        if name in self.contacts:
            del self.contacts[name]

    def get_upcoming_birthdays(self):
        today = datetime.today().date()
        upcoming_birthdays = []

        for name, record in self.contacts.items():
            if record.birthday:
                birthday_date = datetime.strptime(record.birthday.value, '%d.%m.%Y').date()
                birthday_date = birthday_date.replace(year=today.year)                
                # Перевірка, чи день народження потрапляє в наступний тиждень
                if today <= birthday_date <= today + timedelta(weeks=1):
                    upcoming_birthdays.append((record.name.value, record.birthday.value))
                    
        return upcoming_birthdays



