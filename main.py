import re
# Читаем адресную книгу в формате CSV в список contacts_list:
import csv

with open("phonebook_raw.csv", encoding='utf-8') as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)


# 1. Выполните пункты 1-3 задания.
def name_format(contacts_list):
    for person in contacts_list:
        if len(person[0].split()) == 3:
            surname_splitted = person[0].split()
            person[0], person[1], person[2] = person[0].split()[0], surname_splitted[1], surname_splitted[2]
        if len(person[1].split()) == 2:
            name_splitted = person[1].split()
            person[1], person[2] = name_splitted[0], name_splitted[1]
        if len(person[0].split()) == 2:
            surname_splitted = person[0].split()
            person[0], person[1] = person[0].split()[0], surname_splitted[1]

    return contacts_list


def get_phone_numbers_format(contacts_list):
    pattern = r"(\+7|8)?\s?\(?(\d{3}?)\)?[-\s]?(\d{3})[-\s]?(\d{2})-?(\d{2})(\s?)\(?([доб.]{4})?\s?(\d{4})?\)?"
    substitution = r"+7(\2)\3-\4-\5\6\7\8"
    for person in contacts_list:
        person[5] = re.sub(pattern, substitution, person[5])

    return contacts_list


def Merge_duplicate_records(contacts_list):
    for contact in contacts_list:
        first_name = contact[0]
        last_name = contact[1]
        for new_contact in contacts_list:
            new_first_name = new_contact[0]
            new_last_name = new_contact[1]
            if first_name == new_first_name and last_name == new_last_name:
                if contact[2] == "": contact[2] = new_contact[2]
                if contact[3] == "": contact[3] = new_contact[3]
                if contact[4] == "": contact[4] = new_contact[4]
                if contact[5] == "": contact[5] = new_contact[5]
                if contact[6] == "": contact[6] = new_contact[6]

    formatted_contacts_list = list()
    for person in contacts_list:
        if person not in formatted_contacts_list:
            formatted_contacts_list.append(person)

    return formatted_contacts_list


if __name__ == "__main__":
    name_format(contacts_list)
    get_phone_numbers_format(contacts_list)
    formatted_contacts_list = Merge_duplicate_records(contacts_list)

    # 2. Сохраните получившиеся данные в другой файл.
    with open("phonebook.csv", "w", encoding='utf-8') as f:
        datawriter = csv.writer(f, delimiter=',')
        datawriter.writerows(formatted_contacts_list)
