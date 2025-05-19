import random

n_aleatorio = random.randint(1,10)

while True:
    print("Ola Bem-Vindo ")
    print("Esta pronto para jogar")
    print("O jogo de impar ou par")
    print("Primeiro escolha um das opções")
    escolha = input("Qual opção você escolhe: impar ou par")
    print("Agora escolha um número aleatório")
    numero = int(input("Agora solicite um número"))
    n_aleatorio = random.randint(1,10)
    print("A máquina escolheu", n_aleatorio)
    soma = n_aleatorio + numero
    print("A soma dos resultados é", soma)
    calculo = soma % 2 == 0
    
    if escolha == "par":
        if calculo:
            print("Você ganhou")
        else:
            print("Você perdeu")

    if escolha == "impar":
        if calculo:
            print("Você ganhou, deseja jogar de novo")
        else:
            print("Você perdeu, deseja jogar de novo")
    while True:
        print("Vai querer jogar novamente")
        print("1 - SIM")
        print("2 - NÃO")
        sim_nao = int(input("Digite um dos número para se deseja ou não continuar"))
        
        if sim_nao == 1:
            print("Então vamos continuar")
        
        elif sim_nao == 2:
            print("Ok então não jogar mais ARROMBADO")
            break
    
    break


