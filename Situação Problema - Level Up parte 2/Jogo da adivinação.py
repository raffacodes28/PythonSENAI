import random

n_aleatorio = random.randint(0, 100)

def bem_vindo():
    numero = int(input(""))
    if n_aleatorio > numero:
        print("Seu chute esta menor")
    if n_aleatorio < numero:
        print("Seu chute esta maior")
    if n_aleatorio == numero:
        print("PARABÉNS, Você ganhou")
        print("Você deseja continuar")
        print("1 - CONTINUAR")
        print("2 - SAIR")
        sim_nao = int(input("Digite um dos número se desejar ou não continuar"))
        
        if sim_nao == 1:
            print("Então vamos continuar")
                
        elif sim_nao == 2:
            print("Você saiu ARROMBADO")

print("Seja BEM-VINDO")
print("Você tera que escolher um número de 0 a 100")
print("E tera que adivinhar um número aleatorio")

while True:
    bem_vindo()



