# Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить, к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и dict.

my_month = int(input("Enter month number in range 1 to 12 "))
my_schudle = {
    1: 'winter',
    2: 'winter',
    3: 'winter',
    4: 'spring',
    5: 'spring',
    6: 'spring',
    7: 'summer',
    8: 'summer',
    9: 'summer',
    10: 'autumn',
    11: 'autumn',
    12: 'autumn'
}
if my_month in my_schudle:
    print(my_schudle[my_month])

