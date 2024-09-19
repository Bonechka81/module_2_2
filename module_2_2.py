first = int(input("Введите первое число: "))
second = int(input("Введите второе число: "))
third = int(input("Введите третье число: "))

if first == second and first == third:
     print( 3, 'Числа равны между собой')
elif first == second or first == third or second == third:
    print(2, 'Числа равны между собой')
else:
    print( 0, 'Не равны между собой')