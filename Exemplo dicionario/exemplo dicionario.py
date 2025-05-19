aluno = {
    "nome": "Rafael",
    "idade": 17,
    "altura": 1.70,
    "matriculado": True
}

filme_lixo = {
    "nome": "Thor: Amor e Trovão",
    "lançamento": 2022,
    "critica": "UM LIXO!",
    "qualidade": "UMA BOSTA",
    "opiniao": "Não deveria ter existido"
}

filme_incrivel = {
    "nome": "Como Treinar o seu Dragão 3",
    "lançamento": 2019,
    "critica": "Maravilhoso",
    "qualidade": "obra prima",
    "opiniao": "melhor filme de animação na minha opinião"
}

filme_incrivel2 ={
    "nome": "Vingadores: Guerra Infinita",
    "lançamento": 2019,
    "critica": "Muito bom",
    "qualidade": "incrivel",
    "opiniao": "Melhor filme da marvel na minha opnião"
}

aluno["peso"] = 70

aluno["idade"] = 17

del aluno ["altura"]

if "altura" in aluno:
    print("Altura existente")
else:
    print("Altura inexistente")
    
for chave, valor in aluno.items():
    print(f"{chave}: {valor}")

#Exibir uma lista de Dicionários
lista_filme = [filme_incrivel, filme_incrivel2, filme_lixo]
    #Escolhendo os campos
for filme in lista_filme:
    print(f"{filme['nome']}")
    
    #Exibindo todos
for filme in lista_filme:
    for chave, valor in filme.items():
         print(f"{chave}: {valor}")
    print()