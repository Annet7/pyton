# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на позиции с нечетным индексом.
# Пример:
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# import random
# my_list = []
# for i in range(10):
#     my_list.append(random.randint(1, 11))

# sum =0
# i=1
# while i<11:
#     sum += my_list[i]
#     i +=2
# print(f'{my_list} -> сумма чисел на нечетных позициях равна {sum}')

data = [x for x in range (10)]
res = list(filter(lambda x: not x % 2, data))
print(res)
print(sum(res))
