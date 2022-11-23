# Напишите программу для. проверки истинности утверждения 
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат. 
# ⋁ - "Или" ⋀ - "И" ¬ - "Не"

print('Введите значения X,Y,Z = 0 или 1')
a = int(input('X = '))
b = int(input('Y = '))
c = int(input('Z = '))

if a == 1:
    x = True
else:
    x = False

if b == 1:
    y = True
else:
    y = False

if c == 1:
    z = True
else:
    z = False

print(not(x or y or z) == (not x) and (not y) and (not z))   # ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z

