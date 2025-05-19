from datetime import  datetime

def mostrar_nome(nome):
    horario = datetime.now().hour

    if horario >= 0 and horario <= 5:
        print("Boa madrugada", nome) 
    elif horario > 5 and horario <= 12:
        print("Bom dia", nome)
    elif horario > 12 and horario <= 19:
        print("Boa tarde", nome)
    elif horario > 19 and horario <= 24:
        print("Boa noite", nome)
        
nome = input("Digite seu nome")

mostrar_nome(nome)