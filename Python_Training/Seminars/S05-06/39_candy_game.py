import random
# 39 Помните игру с конфетами из модуля "Математика и Информатика"? Создайте такую игру для игры человек против человека
# Добавьте игру против бота
# Подумайте как наделить бота "интеллектом"
# intro
# main game
# Game over
# Interface
# Notes
# дается N конфет и задается условие сколько их надо брать X
# если мы берем первыми, то нам надо взять N%X+1 ==
# Если мы берем вторыми, то нужно 
x = int(input('Введите число K: '))
y = int(input('Введите число M: '))
# y += 1
# p = 3
# i = 1
# s = 1
# while x > 0:
#     if p%2:
#         i = x%y
#     else:
#         if s < y-1: s += 1
#         i = s
#     if x < y: i = x
#     x -= i
#     if not p % 2: print("2 игрок "+str(i))
#     else: print("1 игрок "+str(i))
#     p += 1
#     print('Осталось ' + str(x))
for i in range(1,y):
    x = x*i
    print(f"{i} = {x}")