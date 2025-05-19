import inputs

def menu_calculadora():    
    print("escolha uma opção")
    print("1 - soma")
    print("2 - subtração")
    print("3-  multiplicação")
    print("4- divisão")
    print("5 - todas as opções")
    
    menu = inputs.input_int("coloque sua escolha aqui")
    
    n1 = inputs.input_int("Digite um número")
            
    n2 = inputs.input_int("Digite outro número")
            
    if menu == "1":
        print(soma(n1, n2))
    elif menu == "2":
        print(subtração(n1, n2))
    elif menu == "3":
        print(multiplicação(n1, n2))
    elif menu == "4":
        print(divisão(n1, n2))
    elif menu == "5":
        resultado(n1 , n2)
    else:
        print("você digitou o numero errado")                                                                                                              
def soma(n1 , n2):		
    return n1 + n2
def subtração(n1, n2):
    return n1 - n2
def multiplicação(n1, n2):
    return n1 * n2
def divisão (n1, n2):
    return n1/n2
           
def resultado(n1 , n2):
    print(soma(n1, n2), "é o resultado da adição!")
    print(subtração(n1, n2), "é o resultado da subtração!")
    print(multiplicação(n1, n2), "é o resultado da multiplicação!")
    print(divisão(n1, n2), "é o resultado da divisão!")

menu_calculadora()