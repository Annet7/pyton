# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# # Пример:
# # 6782 -> 23
# # 0,56 -> 11


my_float = str(input('Введите число: '))

new_float = my_float.replace(',', '')

new_float = int(new_float)
sum = 0

while new_float != 0:
    sum = sum + new_float % 10
    new_float = new_float // 10

print(f'{my_float} -> {sum}')


# # Задайте список из n чисел последовательности (1 + 1/n)**n, выведеите его на экран, а так же сумму элементов списка.
# # Пример:
# # Для n=4 -> [2, 2.25, 2.37, 2.44]
# # Сумма 9.06


n = int(input('Введиче длину списка: '))

list_mask = []
i=1
while i <= n:
    list_mask.append(round((1 + 1 / i)**i, 2))
    i +=1

print(f'Для n = {n} -> {list_mask}')

sum=0
i =0
while i<n:
    sum = sum + list_mask[i]
    i +=1
print(f'Сумма {sum}')

# Реализуйте алгоритм перемешивания списка. 
# НЕ ИСПОЛЬЗОВАТЬ ВСТРОЕННЫЕ БИБЛИОТЕКИ SHUFFLE, максимум использование библиотеки Random для получения случайного int

my_list= list(range(0, 10, 1))
print(my_list)

for i in my_list:
    import random
    j= random.randint(0, 9)
    temp =0
    temp = my_list[j]
    my_list[j] = my_list[i]
    my_list[i] = temp


print(my_list)


