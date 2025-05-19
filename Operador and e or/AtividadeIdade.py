Ano = int(input("Solicite o ano de nascimento de uma pessoa"))
Ano_atual = int(input("Solicite o ano de atualmente"))
idade = Ano_atual - Ano
if Ano_atual >= Ano:
    print("A idade da pessoa é", idade)
    if idade >=0 and idade <= 10:
        print("Criança")
    elif idade >= 11 and  17:
        print("Adolecente")
    elif idade >= 18 and idade <= 59:
        print("Adulto")
    elif idade > 60:
        print("Alastor")

