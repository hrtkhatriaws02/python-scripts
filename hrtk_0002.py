import math

radius = float(input('Enter radius of circle in cm: ').strip())

area = math.pi * radius ** 2

print(f'The area of circle having {radius} cm = {area:.2f}')