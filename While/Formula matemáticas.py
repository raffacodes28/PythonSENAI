numero = 0
quant = 0

print(numero)

while True:
    print("1 - Fatorial")
    print("2 - Quadrado")
    print("3 - Cubo")
    print("4 - Tabuada")
    print("0 - Sair")
    menu = int(input("Qual formula você deseja ultilizar"))
    
    if menu == 1:
        n = int(input("Escolha um número que deseja fatorair"))
        while True:
            math.factorial(n)
            
    elif menu == 2:
        quadrado = int(input("Escolha um número que deseja fazer ao quadrado"))
        valor_quadrado = quadrado * quadrado
        print("O valor ao quadrado é", valor_quadrado)
         
    elif menu == 3:
        cubo = int(input("Escolha um número que deseja para fazer-lo ao cubo"))
        valor_cubo = cubo * cubo * cubo
        print("O valor ao cubo é", valor_cubo)
    
    elif menu == 4:
        numero0 = int(input("Digite um número"))
        resultado_multiplicado = numero0 * 1
        print(resultado_multiplicado)
        
        resultado_multiplicado = numero0 * 2
        print(resultado_multiplicado)
        
        resultado_multiplicado = numero0 * 3
        print(resultado_multiplicado)
        
        resultado_multiplicado = numero0 * 4
        print(resultado_multiplicado)
        
        resultado_multiplicado = numero0 * 5
        print(resultado_multiplicado)
        
        resultado_multiplicado = numero0 * 6
        print(resultado_multiplicado)
        
        resultado_multiplicado = numero0 * 7
        print(resultado_multiplicado)
        
        resultado_multiplicado = numero0 * 8
        print(resultado_multiplicado)
        
        resultado_multiplicado = numero0 * 9
        print(resultado_multiplicado)
        
        resultado_multiplicado = numero0 * 10
        print(resultado_multiplicado)
        
    elif menu == 0:
        print("Você saiu")