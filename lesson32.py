# import os, itertools
# all_files = []
# duplicates = []
# p = r'C:\Users\angus\OneDrive\Desktop\root'
# for i in list(os.walk(p)):
#     all_files.append(i[-1])

# chain = []
# for i in all_files:
#     if i == []:  pass
#     else: chain.extend(i)
# print(chain)

# for j in all_files:
#     if (all_files.count(j) > 1) and (j not in duplicates):
#         duplicates.append(j)

# print(f"All files: {all_files}")
# print(f"Files have duplicates: {duplicates}")


# ___________________________JSON_________________________________
# import json 

# person = {
#     'name' : 'Vardges',
#     'surname' : 'Համբարյան',
#     'age': 19.7,
#     'married': False,
# }


# with open('info.json' , 'w' , encoding='UTF-8') as file:
#     json.dump(person , file , indent=2 , ensure_ascii=False)


# with open('info.json' , 'r' , encoding='UTF-8') as file:
#     result = json.load(file)
# print(result)

# def add_info():
#     while True:
#         name = input('Enter name: ')
#         if name == '':
#             break
#         else:
#             surname = input('Enter surname: ')
#             age = int(input('Enter age: '))
#             info = {
#                     'name' : name,
#                     'surname' : surname,
#                     'age' : age,
#                 }
#             with open('users_info.json' , 'r') as file:
#                 result = json.load(file)
#             result.append(info)
#             with open('users_info.json' , 'w') as file:
#                 json.dump(result , file , indent=4)



# def add_names():
#     with open('users_info.json' , 'r') as file:
#         result = json.load(file)
#     print(result)
#     names = []
#     for i in result:
#         names.append(i['name'])

#     with open('names.json' , 'w') as file:
#         json.dump(names , file)
#     print(names)

# if __name__ == '__main__':
    # add_info()
    # add_names()



# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# import sys
# import json
# if __name__ == '__main__':
#     workers = []
#     while True:
#         command = input("Enter command> ").lower()
#         if command == "exit":
#             break
#         elif command == "add":
#             las_name = str(input("Enter last name>  "))
#             name = str(input("Enter first name> "))
#             tel = int(input("Enter phone> +"))
#             date = list(map(int, input("Enter birthdate separated by space> ").split(" ")))
#             temp = {
#                 'las_name': las_name,
#                 'name': name,
#                 'tel': tel,
#                 'date': date
#             }
#             workers.append(temp)
#             # Отсортировать список в случае необходимости.
#             if len(workers) > 1:
#                 workers.sort(key=lambda item: item.get('las_name', ''))
#         elif command == "list":
#             line = "+-{}-+-{}-+-{}-+-{}-+-{}-+".format(
#                 '-' * 4,
#                 '-' * 15,
#                 '-' * 15,
#                 '-' * 20,
#                 '-' * 20
#             )
#             print(line)
#             print(
#                 "| {:^4} | {:^15} | {:^15} | {:^20} | {:^20} |".format(
#                     "№",
#                     "Фамилия",
#                     "Имя",
#                     "Телефон",
#                     "Дата рождения"
#                 )
#             )
#             print(line)
#             for idx, worker in enumerate(workers, 1):
#                 print(
#                     '| {:>4} | {:<15} | {:<15} | {:>20} | {:^20} |'.format(
#                         idx,
#                         worker.get('las_name', ''),
#                         worker.get('name', ''),
#                         worker.get('tel', 0),
#                         ".".join(map(str, worker.get('date')))
#                     )
#                 )
#             print(line)
#         elif command == "task":
#             check = list(map(int, input("Enter birthdate separated by space> ").split(" ")))
#             task_list = []
#             iz = 0
#             for worker in workers:
#                 if ''.join(map(str, worker.get('date'))) == ''.join(map(str, check)):
#                     task_list.append(worker)
#                     iz += 1
#             if iz == 0:
#                 print("Workers not found")
#             else:
#                 line = "+-{}-+-{}-+-{}-+-{}-+-{}-+".format(
#                     '-' * 4,
#                     '-' * 15,
#                     '-' * 15,
#                     '-' * 20,
#                     '-' * 20
#                 )
#                 print(line)
#                 print(
#                     "| {:^4} | {:^15} | {:^15} | {:^20} | {:^20} |".format(
#                         "№",
#                         "Фамилия",
#                         "Имя",
#                         "Телефон",
#                         "Дата рождения"
#                     )
#                 )
#                 print(line)
#                 for idx, worker in enumerate(task_list, 1):
#                     print(
#                         '| {:>4} | {:<15} | {:<15} | {:>20} | {:^20} |'.format(
#                             idx,
#                             worker.get('las_name', ''),
#                             worker.get('name', ''),
#                             worker.get('tel', 0),
#                             ".".join(map(str, worker.get('date')))
#                         )
#                     )
#                 print(line)
#         elif command.startswith('load '):
#             # Разбить команду на части для выделения имени файла.
#             parts = command.split(' ', maxsplit=1)
#             # Прочитать данные из файла JSON.
#             with open(parts[1], 'r') as f:
#                 workers = json.load(f)
#         elif command.startswith('save '):
#             # Разбить команду на части для выделения имени файла.
#             parts = command.split(' ', maxsplit=1)
#             # Сохранить данные в файл JSON.
#             with open(parts[1], 'w') as f:
#                 json.dump(workers, f)
#         elif command == 'help':
#             # Вывести справку о работе с программой.
#             print("Список команд:\n")
#             print("add - добавить работника;")
#             print("list - вывести список работников;")
#             print("task - вывести сотрудников определенной даты рождения")
#             print("load <имя файла> - загрузить данные из файла;")
#             print("save <имя файла> - сохранить данные в файл;")
#             print("exit - выход из программы;")
#         else:
#             print("Неизвестная команда {command}", file=sys.stderr)
# import json

# with open('users_info.json' , 'r') as file:
#     result = json.load(file)


# names = []
# surnames = []

# for i in result:
#     names.append(i['name'])
#     surnames.append(i['surname'])

# search = input('Enter search text: ') 


# print((search in names) or (search in surnames))








































