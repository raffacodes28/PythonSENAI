nota1 = int(input("Qual é a nota do 1 aluno"))
nota2 = int(input("Qual a nota do 2 aluno"))
if nota1 > 0 and nota1 < 100 and nota2 > 0 and nota2 < 100:
    print("")
    media = nota1 + nota2
    media1 = media / 2
    if media1 < 70 and media1 > 50:
        print("O Resultado é", media1)
    elif media1 > 70:
        print("Aprovado")
    elif media1 < 50:
        print("Reprovado")
        
