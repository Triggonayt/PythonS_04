# Вычислить число ПИ c заданной точностью d
# *Пример:* 
#     - при d = 0.0001, π = 3.1415.    10^-1 ≤ d ≤ 10^-10


# n = float(input('Введите размер списка '))
# n = round(n, 3)
# print(n)


# 2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.


# num = int(input("Введите число: "))
# i = 2 
# lst = []

# while i <= num:
#     if num % i == 0:
#         lst.append(i)
#         num //= i
#         i = 2
#     else:
#         i += 1

# print(lst)


# 3. Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

# lst = list(map(int, input("Введите числа через пробел:\n").split()))
# print(f"Исходный список: {lst}")
# new_lst = []
# [new_lst.append(i) for i in lst if i not in new_lst]
# print(f"Список из неповторяющихся элементов: {new_lst}")



# 5. Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.

# with open('file_1.txt', 'w', encoding='utf-8') as file:
#     file.write('2*x^2 + 5*x^5')
# with open('file_2.txt', 'w', encoding='utf-8') as file:
#     file.write('23*x^4 + 9*x^6')

# with open('file_1.txt','r') as file:
#     poly_1 = file.readline()
#     list_of_poly_1 = poly_1.split()


# with open('file_2.txt','r') as file:
#     poly_2 = file.readline()
#     list_of_poly_2 = poly_2.split()

# print(f'{list_of_poly_1} + {list_of_poly_2}')
# sum_poly = list_of_poly_1 + list_of_poly_2

# with open('sum_fail.txt', 'w', encoding='utf-8') as file:
#     file.write(f'{list_of_poly_1} + {list_of_poly_2}')