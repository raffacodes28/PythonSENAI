def circulo(raio):
    return 3.14 * raio__

def quadrado(num1):
    return num1 * num1

def retangulo(num1, num2):
    return num1 * num2

def menu_area():
    print("[1] circulo")
    print("[2] quadrado")
    print("[3] retângulo")
    
    opcao = int(input("escolha uma opção:"))
    
    if  opcao == 1:
        raio == float(input("Digite o raio do circulo:"))
        print("Àrea do circulo é", circulo(raio))
    elif opcao == 2:
        lado = float(input("Digite o lado do quadrado:"))
        print("Àrea do quadrado é", quadrado(lado))
    elif opcao == 3:
        base = float(input("Digite a base do retângulo:"))
        altura = float(input("Digite a altura do rentângulo"))
        print("Àrea do retângulo é", retangulo(base, altura))
        
menu_area()