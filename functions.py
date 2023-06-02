def show_data() -> None:
    """Выводит информацию из справочника"""
    with open('book.txt', 'r', encoding='utf-8') as file:
        print(file.read())


def add_data() -> None:
    """Добавляет информацию в справочник."""
    fio = input('Введите ФИО: ')
    phone = input('Введите номер телефона: ')
    with open('book.txt', 'a', encoding='utf-8') as file:
        file.write(f'\n{fio} | {phone}')


def find_data() -> None:
    """Печатает результат поиска по справочнику."""
    with open('book.txt', 'r', encoding='utf-8') as file:
      data = file.read()
    data_to_find = input('Введите данные для поиска: ')
    print(data)
    print(search(data, data_to_find))


def search(book: str, info: str) -> str:
    """Находит в списке записи по определенному критерию поиска"""
    book = book.split('\n')
    found_contacts = []
    for contact in book:
        if info in contact:
            found_contacts.append(contact)
    if not found_contacts:
        return 'Совпадений не найдено'
    elif len(found_contacts) == 1:
        return found_contacts[0]
    else:
        result = 'Найдено несколько совпадений:\n\n'
        for i, contact in enumerate(found_contacts):
            result += f'{i+1}. {contact}\n'
        result += f'\nВведите номер нужного контакта (от 1 до {len(found_contacts)}): '
        return result
