import re
from pprint import pprint
import csv

with open("phonebook_raw.csv", encoding="utf-8") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
    names_pattern = r"([А-я]+) ([А-я]+ ?[А-я]+)?"
    numbers_pattern = r"^(\+7|8) ?\(?(\d\d\d?)\)? ?-?(\d\d\d) ?-?(\d\d)-?(\d\d) ?\(?([а-я][а-я][а-я].)?( \d+)?\)?"
    list_of_surnames = []
    string_counter = 0
    duplicate_indexes = []
    human_counter = 0
    for human in contacts_list:
        counter = 0
        list_of_human_names = []
        for data_element in human:
            if 0 <= counter < 2:
                spaces_in_names = re.findall(" ", data_element)
                if len(spaces_in_names) != 0:
                    grouped_names = re.search(names_pattern, data_element)
                    counter_plus_1 = counter + 1
                    human[counter] = grouped_names.group(1)
                    human[counter_plus_1] = grouped_names.group(2)
                    counter_plus_1 = 0
            elif counter == 5 and data_element != "" and data_element != "phone":
                grouped_numbers = re.search(numbers_pattern, data_element)
                second_group = f"({grouped_numbers.group(2)})"
                data_element = re.sub(r'^(\+7|8) ?\(?(\d\d\d?)\)? ?-?(\d\d\d) ?-?(\d\d)-?(\d\d)( ?)\(?(\(?[а-я][а-я][а-я].)? ?(\d+)?\)?', r'+7 (\2)\3-\4-\5\6\7\8', data_element)
                contacts_list[human_counter][counter] = data_element
            counter += 1
            spaces_in_names = 0
        human_counter += 1

    # pprint(contacts_list)
    for normal_human_string in contacts_list: #для каждой человеческой строчки
        # print(string_counter, normal_human_string)
        if normal_human_string[0] in list_of_surnames: #если эта фамилия имеется в списке фамилий
            first_duplicate = list_of_surnames.index(normal_human_string[0]) #получаем индекс ранее вставленной фамилии
            # print(f"FIRST DUPLICATE - {first_duplicate}")
            duplicate_indexes.append(first_duplicate) #добавляем индекс этой фамилии в список дубликатов
            column_counter=0 # счетчик колонок равен 0
            element_counter=0
            # print(f"===")
            list_of_surnames.append(normal_human_string[0])
            for element in normal_human_string: # в каждой колонке человеческой строчки
                if column_counter > 6: # если это 7-ая колонка - то выход из цикла
                    break
                if element == "": # если в какой-то колонке значение второго дубликата - пустое, то
                    # print(f"Работа в строке - {string_counter}, колонке - {column_counter}")
                    # print(f"Номер пустого элемента - {element_counter}")
                    # print(f"Строка + Пустой элемент второго дубликата ДО ЗАМЕНЫ:")
                    # print(contacts_list[string_counter], contacts_list[string_counter][column_counter])
                    contacts_list[string_counter][column_counter] = contacts_list[first_duplicate][column_counter]
                    # print(f"Строка в базовом списке В КОТОРОЙ меняем - {contacts_list[string_counter]}")
                    # print(f"Элемент в базовом списке КОТОРЫЙ - {contacts_list[string_counter][column_counter]}")
                    # print(f"Строка в базовом спике НА КОТОРУЮ меняем - {contacts_list[first_duplicate]}")
                    # print(f"Элемент в базовом спике НА КОТОРЫЙ меняем - {contacts_list[first_duplicate][column_counter]}")
                    # #назначь второму дубликату в колонке с пустотой значение из первого дубликата
                    # print(f"Строка + Пустой элемент второго дубликата ПОСЛЕ ЗАМЕНЫ:")
                    # print(contacts_list[first_duplicate], contacts_list[first_duplicate][column_counter])
                column_counter+=1
        else:
            list_of_surnames.append(normal_human_string[0])
        string_counter +=1

    # pprint(contacts_list)

    for duplicate_in_index in duplicate_indexes:
        # print(contacts_list[duplicate_in_index])
        contacts_list.pop(duplicate_in_index)

    pprint(contacts_list)

with open("phonebook.csv", "w", newline='') as f:
  datawriter = csv.writer(f, delimiter=',')
  datawriter.writerows(contacts_list)
