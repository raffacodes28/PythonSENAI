num1 = int(input('solicite 1 numero ='))
num2 = int(input('solicite outro numero ='))
num3 = int(input('solicite outro numero ='))

if num1 > num2:
    if num1 > num3:
        print("o primeiro e maior que o segundo e o terceiro")
elif num2 > num1:
    if num2 > num3:
        print("o segundo e maior que o primeiro e o terceiro")
elif num3 > num1:
    if num3 > num2:
        print("o terceiro e maior que o primeiro e o segundo")
