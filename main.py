from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    def __init__(self,value):
        if not value:
            raise ValueError('Name cannot be empty')
        super().__init__(value)
    pass
           

class Phone(Field):
    # перевірка номера телефону (повинно бути 10 цифр)
    def __init__(self,value):
        if len(value) != 10:
            raise ValueError('Phone number must contain 10 digits')
        super().__init__(value)

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    # метод додавання номера телефону.
    def add_phone(self,phone):
        self.phones.append(Phone(phone))

    # метод видалення номера телефону.
    def remove_phone(self,phone):
        for item in self.phones:
            if item.value == phone:
                self.phones.remove(item)

    # метод редагування номера телефону.
    def edit_phone(self,old_phone,new_phone):
        if not any(item.value == old_phone for item in self.phones):
            raise ValueError(f'{old_phone} is not found')
        else:
            for item in self.phones:
                if item.value == old_phone:
                    item.value = new_phone

    # метод пошуку об'єктів Phone
    def find_phone(self,phone):
        found_phone = next(filter(lambda item: item.value == phone, self.phones), None)
        return found_phone
         

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"
    
# Реалізовано магічний метод __str__ для красивого виводу об’єкту класу AddressBook .

class AddressBook(UserDict):
    # метод додає запис до self.data.
    def add_record(self, record):
        self.data[record.name.value] = record
    
    # метод знаходить запис за ім'ям.
    def find(self,name):
        return self.data.get(name)
    
    #метод видаляє запис за ім'ям
    def delete(self, name):
        if name in self.data:
            self.data.pop(name)

    def __str__(self):
        lines = [str(record) for record in self.data.values()]
        return "\n".join(lines) if lines else "Address book is empty."


if __name__ == '__main__':
    # Створення нової адресної книги
    book = AddressBook()

    # Створення запису для John
    john_record = Record("John")
    john_record.add_phone("1234567890")
    john_record.add_phone("5555555555")

    # Додавання запису John до адресної книги
    book.add_record(john_record)

    # Створення та додавання нового запису для Jane
    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")
    book.add_record(jane_record)

    # Виведення всіх записів у книзі
     
    print(book)

    # Знаходження та редагування телефону для John
    john = book.find("John")
    john.edit_phone("1234567890", "1112223333")

    print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

    # Пошук конкретного телефону у записі John
    found_phone = john.find_phone("5555555555")
    print(f"{john.name}: {found_phone}")  # Виведення: John: 5555555555

    # Видалення запису Jane
    book.delete("Jane")


