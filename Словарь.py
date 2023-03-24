Типы данных справедливы
int, float, boolean, str, list

Ввод и вывод данных
input() - отвечает за ввод данных
print() - отвечает за вывод данных

Ввод переменной пользователем:

a*любая переменная*=int*тип переменной*(input('в ковычках сообщение для пользователя'))
ПРИМЕР a = int(input('Введите числоа: ')) -результат: создание целочисленной переменной а

Арифметические операции

+, -,*, /, %, //,**

Сокращённые операции и операции присваивания
iter = 2
iter += 3 # iter = iter + 3
iter -= 4 # iter = iter - 4
iter *= 5 # iter = iter * 5
iter /= 5 # iter = iter / 5
iter //= 5 # iter = iter // 5
iter %= 5 # iter = iter % 5
iter **= 5 # iter = iter ** 5

Логические операции
>, >=, <, <=, ==, !=
not, and, or – не путать с &, |,^
Кое-что ещё: is, is not, in, not in


Управляющие конструкции: if, if-else
username = input('Введите имя: ')
if(username == 'Маша'):
 print('Ура, это же МАША!');
else:
 print('Привет, ', username);

Управляющие конструкции: elif
username = input('Введите имя: ')
if username == 'Маша':
 print('Ура, это же МАША!')
elif username == 'Марина':
 print('Я так ждала Вас, Марина!')
elif username == 'Ильнар':
 print('Ильнар - топ)')
else:
 print('Привет, ', username)


Управляющие конструкции: while-else
original = 23
inverted = 0
while original != 0:
 inverted = inverted * 10 + (original % 10)
 original //= 10
else:
 print('Пожалуй')
 print('хватит )')
print(inverted)
# Пожалуй
# хватит )
# 32

Управляющие конструкции: for
r = range(100, 0, -20) # range(100, 0, -20)
for i in r:
 print(i)
# 100 80 60 40 20
for i in range(5):
 print(i)
# 0 1 2 3 4

Вывод чисел циклом FOR:

for i in range (1, 10, 1) ранжа создает список с определенным шагом
пробегаем по списку от одного до девяти (десять не включительно) с шагом +1.

for i in range(-переменная, переменная+1):

my_list == [x for x in range(1,20)]
print(my_list)



split - разделить
a = a.split('.')
разделить строку по точке
НАПРИМЕР: 4,58 превращается в ['4', '58']


Для корректной работы с плавающей точкой используй библиотеку:

from decimal import Decimal
a = Decimal ('0,56')


Вывод через запятую в одну строчку:

print(*лист, sep = ', ') в ковычках: запятая пробел

Типы массивов:
list = [] - изменяемый список с четкой индексацией элементов
tuple = () - картеж - НЕизменяемый список с четкой индексацией элементов
set = {} - список БЕЗ индексации элементов, в котором не может быть одинаковых элементов
dict = {УникальныйКлюч: "значение ключа"} - словарь

Создаю рандом из вещественных чисел(дробных)

import random #обращаюсь к библиотеке рандом
my_list = [] #создаю пустой список
for _ in range(10): #говорю создать 10 элементов
    amount = random.randint(0, 3) #прошу включать от нуля до трех знаков после запятой
    my_list.append(round(random.uniform(-10, 10), amount)) #рандомные числа прошу округлять до указанного выше значения (три знака после запятой)
print(my_list) #печатаю мой список


Работа со строками
my_string = 'Питон самый лучший язык' #Создаю строку

new_string = my_string.split('') #создаю новую строку, и записываю в нее список из предыдущей строки разделенной по пробелам
new_string = my_string.replace('и', '$') #заменяю все буквы И в строке на значки бакса
new_string = my_string.strip() # этот метод отчищает все до начала и в конце строки
#\t - отступ вначале строки(табуляция) \nдополнительный переход на новую строку. Пример: '\tПитон самый лучший язык\n'
new_string = my_string.lstrip() #убирает все только слева
new_string = my_string.rstrip() #почистить все только в конце строки
if my_string.startswith('пит')#проверяет начинается ли строка с какого-то значания
    print('да, все верно')
if my_string.endswith('зык')#проверяет заканчивается ли строка каким-то значением
    print('да, все верно')
new_string = my_string.lower()# переводит все символы строки в нижний регистр
new_string = my_string.upper()# переводит все символы строки в верхний регистр

text = 'съешь ещё этих мягких французских булок'
print(len(text)) # 39
print('ещё' in text) # True
print(text.isdigit()) # False
print(text.islower()) # True
print(text.replace('ещё','ЕЩЁ')) #
for c in text:
 print(c)
print(text[0]) # c
print(text[1]) # ъ
print(text[len(text)-1]) # к
print(text[-5]) # б
print(text[:]) # print(text)
print(text[:2]) # съ
print(text[len(text)-2:]) # ок
print(text[2:9]) # ешь ещё
print(text[6:-18]) # ещё этих мягких
print(text[0:len(text):6]) # сеикакл
print(text[::6]) # сеикакл
text = text[2:9] + text[-5] + text[:2] # ...


Списки: введение
numbers = [1, 2, 3, 4, 5]
print(numbers) # [1, 2, 3, 4, 5]
numbers = list(range(1, 6))
print(numbers) # [1, 2, 3, 4, 5]
numbers[0] = 10
print(numbers) # [10, 2, 3, 4, 5]
for i in numbers:
 i *= 2
 print(i) # [20, 4, 6, 8, 10]
print(numbers) # [10, 2, 3, 4, 5]
my_list = ['fvng', 'bhj', 'byl']
add = '-'
print(add.join(my_list)) #из списка строк склеиваит единую строку со зничением переменной add. 
#например из списка строк ['fvng', 'bhj', 'byl'] получаем строку fvng-bhj-byl
colors = ['red', 'green', 'blue']
for e in colors:
 print(e) # red green blue
for e in colors:
 print(e*2) # redred greengreen blueblue
colors.append('gray') # добавить в конец
print(colors == ['red', 'green', 'blue', 'gray']) # True
colors.remove('red') #del colors[0] # удалить элемент


Функции
Это фрагмент программы, используемый многократно
def function_name(x):
    # body line 1
    # . . .
    # body line n
    # optional return

def new_string(symbol, count = 3):
    return symbol * count
print(new_string('!', 5)) # !!!!!
print(new_string('!')) # !!!
print(new_string(4)) # 12

ЧИСЛА ФИБОНАЧИ
def fib(n):
    if n in [1, 2]:
        return 1
    else:
        return fib(n-1) + fib(n-2)
list = []
for e in range(1, 10):
    list.append(fib(e))
print(list) # 1 1 2 3 5 8 13 21 34

работа со словарями
my_dict = {32:37, 'gh':'efuycbye', 1:'one'} #создаю словарь
print(my_dict['gh']) #прошк распечатать значение ключа gh
print(my_dict.get(32, 'нет такого ключа')) #если запрошу существующий ключь - выдаст значение, 
#если зопрошу несуществующий ключ - вместо ошибки напишет "нет такого ключа"
my_dict['new'] = 'bbkj' #добавила в существующий словарь новое значение
#если напишу таким же образом существующий ключ и присвою новое значение, то старое значение сотрется и перезапишется
my_dict[32] = my_dict.get(32) + 1 #увеничиваю значение в существующем ключе на один

my_dict = {} #создаю словарь
num_list = '34567876543234567876543345678' # создаю лист
for dig in num_list: # пробегаюсь по листу
    my_dict[dig] = my_dict.get(dig, 0) + 1 #считаю количество повторений числел в листе
print(my_dict) #распичатываю в терминал что-то такое {'3': 5, '4': 5, '5': 5, '6': 5, '7': 5, '8': 3, '2': 1}



Раюота с файлами

Как работать с файлами: Связать файловую переменную с файлом,определив модификатор работы
a – открытие для добавления данных
r – открытие для чтения данных
w – открытие для записи данных
w+, r+


with open('file.txt', 'w') as data:
    data.write('line 1\n')
    data.write('line 2\n')

colors = ['red', 'green', 'blue']
data = open('file.txt', 'a')
data.writelines(colors) # разделителей не будет
data.close()

path = 'file.txt'
data = open(path, 'r')
for line in data:
    print(line)
data.close()


Ускоренная обработка данных:
lambda, filter, map,  zip, enumerate, List, Comprehension

Анонимные, lambda функции
sum = lambda x: x+10
mult = lambda x: x**2
sum(mult(2))

sum1 = lambda x: x+22
mult2 = lambda x: x**3
sum1(mult2(2))

sum4 = lambda x: x+242
mult4 = lambda x: x**5
sum3(mult2(2))

К чему это всё?
В файле хранятся числа, нужно выбрать четные и составить список пар (число; квадрат числа).
Пример:
1 2 3 5 8 15 23 38
Получить:
[(2, 4), (8, 64), (38, 1444)]

f = open('f.txt', 'r')
data = f.read() + ' '
f.close()
numbers = []
while data != '':
 space_pos = data.index(' ')
 numbers.append(int(data[:space_pos]))
 data = data[space_pos+1:]
out = []
for e in numbers:
 if not e % 2:
 out.append((e,e **2))
print(out)

ИЛИ

def select(f, col):
 return [f(x) for x in col]
def where(f, col):
 return [x for x in col if f(x)]
data = '1 2 3 5 8 15 23 38'.split()
data = select(int, data)
data = where(lambda e: not e % 2, data)
data = list(select(lambda e: (e, e**2), data))

Функция map
Функция map() применяет указанную функцию к каждому элементу итерируемого объекта 
и возвращает итератор с новыми объектами.
f(x) ⇒ x + 10
map(f, [ 1, 2,   3,  4, 5])
         ↓  ↓    ↓   ↓  ↓
      [ 11, 12, 13, 14, 15]
Нельзя пройтись дважды

li = [x for x in range(1,20)]
li = list(map(lambda x:x+10))
print(li)

Функция filter
Функция filter() применяет указанную функцию к каждому элементу итерируемого объекта 
и возвращает итератор с теми объектами, для которых функция вернула True.
f(x) ⇒ x - чётное
filter(f, [ 1, 2, 3, 4,5])
                  ↓
          [    2,    4   ]
Нельзя пройтись дважды
data = [x for x in range (10)]
res = list(filter(lambda x: not x % 2, data))
print(res)

Функция zip
Функция zip() применяется к набору итерируемых объектов и возвращает итератор с кортежами из
элементов входных данных. 
Количество элементов в результате равно минимальному количеству элементов входного набора
zip ([1, 2, 3], [ ‘о‘, ‘д‘, ‘т‘], [‘f’,’s’,’t’])
 ↓
[(1, 'о', 'f'), (2, 'д', 's'), (3, 'т', 't')]
Нельзя пройтись дважды

user = ['anna', 'katay', 'jak']
id = [4,5,6]
data = list(zip(user, id))
print(data)


Функция enumerate
Функция enumerate() применяется к итерируемому объекту и возвращает новый итератор с кортежами
из индекса и элементов входных данных.
enumerate(['Казань', 'Смоленск', 'Рыбки', 'Чикаго'])
 ↓
[(0, 'Казань'), (1, 'Смоленск'), (2, 'Рыбки'), (3, 'Чикаго')]
Нельзя пройтись дважды

user = ['anna', 'katay', 'jak']
data = list(enumerate(user))
print(data)

List Comprehension
[exp for item in iterable]
[exp for item in iterable (if conditional)]
[exp <if conditional> for item in iterable (if conditional)]



print(' '.join(my_list)) #напечатается ва лодну строкку разделяя элементы пробелами