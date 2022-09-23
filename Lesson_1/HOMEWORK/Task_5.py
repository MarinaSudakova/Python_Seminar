# Напишите программу, которая 
# принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

ax = float(input('Write x point A: '))
ay = float(input('Write y point A: '))
bx = float(input('Write x point B: '))
by = float(input('Write y point B: '))

import math
dis = round( (math.sqrt((bx - ax)**2 + (by - ay)**2)),4)
print(f'Distanse is {dis}')