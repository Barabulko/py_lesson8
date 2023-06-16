'''Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных. 
Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал для изменения и удаления данных'''

import os

class PhoneBookUser():
    def __init__(self, last_name, first_name, number, comment) -> None:
        self.last_name = last_name
        self.first_name = first_name
        self.number = number
        self.comment = comment.replace('\n', "")
        return
    
    def __str__(self) -> str:
        # return(f"{self.first_name} - {self.number} ({self.comment})")
        return(f"{self.last_name},{self.first_name},{self.number},{self.comment}\n")


def get_book():
    PhoneBook = {}
    try:
        book_file = open("./phonebook.csv", encoding="utf8")
    except:
        print("file not found")
        return()
    book = book_file.readlines()
    book_file.close()

    headers = ["Фамилия", "Имя", "Номер", "Комментарий"]
    for string in book:
        string = string.split(',')
        for line in string:
            PhoneBook.update({string[0]: PhoneBookUser(string[0], string[1], string[2], string[3])})
    

    return(PhoneBook)

def Show_contacts(book):
    for line in book:
        print(str(book[line]))

def introduction():
    os.system("CLS")
    print('1 - show contacts')
    print('2 - add contacts')
    print('3 - search contacts')
    print('4 - remove contact')
    print('5 - update contact')
    print('6 - exit')

def save_book(book, path = './phonebook.csv'):
    book_file = open(path, "w", encoding='utf8')
    for line in book:
        book_file.write(str(book[line]))
    book_file.close()

def add_contact():
    last_name = input("Введите фамилию: ")
    first_name = input("Введите имя: ")
    number = input("Введите номер: ")
    comment = input("Введите комментарий: ")
    my_book = get_book()
    my_book.update({last_name: PhoneBookUser(last_name, first_name, number, comment)})
    save_book(my_book)

def search_contact():
    search_str = input("Введите строку для поиска: ")
    my_book = get_book()
    for line in my_book:
        if search_str in str(my_book[line]):
            print(f"Найден контакт: {str(my_book[line])}")
            

def remove_contact():
    search_str = input("Введите фамилию контакта для удаления: ")
    my_book = get_book()
    for line in my_book:
        if search_str == str(line):
            print(f"Удален контакт: {str(my_book[line])}")
            my_book.pop(search_str)
            save_book(my_book)
            return()
    print('Подходящие контакты не найдены')

def update_contact():
    print("please choose option 4, then option 2")
    return

def main_cycle():
    introduction()
    while 1:
        choice = int(input("please select an option "))
        if choice==1:
            introduction()
            Show_contacts(get_book())
        if choice==2:
            add_contact()
        if choice==3:
            search_contact()
        if choice==4:
            remove_contact()
        if choice==5:
            update_contact()
        if choice==6:
            return

    return

main_cycle()