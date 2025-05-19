def mostrar_Kelvin(celsius):
    return celsius + 273
def mostrar_Fahrenheit(celsius):
    return celsius * 1.8 + 32

C = int(input("Digite uma temperatura em Celsius"))

print("A temperatura em Kelvin é", mostrar_Kelvin(C))
print("A temperatura em Fahrenheit e", mostrar_Fahrenheit(C))

mostrar_Kelvin(C)
mostrar_Fahrenheit(C)