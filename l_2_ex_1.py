# Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента.
# Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

my_list = []
my_list.append(9)
my_list.append(12.5)
my_list.append("слово")
my_list.append(True)
my_list.append([3, 4, 5])
my_list.append({'a': 4})
my_list.append(('о', 'б', 'ъ', 'e', 'к', 'т'))
print(my_list)
for i in my_list:
    print(type(i))



#print(type(my_list[1] my_list[2]))
#print(my_list)