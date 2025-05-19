nomes = []
presentes = []
ausentes = []

while True:
    print("1- Cadastrar dos pais")
    print("2- Exibir o total de pais")
    print("3- Exibir a lista em ordem alfabética")
    print("4- Realizar a confirmação de presença de pais")
    print("5- Exibir um relatorio da chamada")
    print("6- sair")
    opcao = int(input("Digite uma das opções"))
    
    if opcao == 1:
        nome = input("Digite o nome que quer cadastrar")
        if nome in nomes:
            print("Esse nome já esta cadastrado")
        else:
            nomes.append(nome)
            print("Nome cadastrado")
            
    if opcao == 2:
        print("O total de pais cadastrado é", len(nomes), f"pessoas \n")
        
    if opcao == 3:
        nomes.sort()
        for nome in nomes:
            print(nome)
            
    if opcao == 4:
        for nome in nomes:
            print(nome)
            sim_nao = input("O nome esta presente? (s/n)")
            if sim_nao == "s":
                print("Estes nomes estão presente")
                presentes.append(nome)
            else:
                print("Estes nomes estão ausente")
                ausentes.append(nome)
    
    if opcao == 5:
        presentes.sort()
        print("")
        print("Presentes")
        for nome in presentes:
            print(nome)
        ausentes.sort()
        print("")
        print("Ausentes")
        for nome in ausentes:
            print(nome)
            
    if opcao == 6:
        print("Você saiu")
        break
    else:
        print("Opção inexistente")
        
                
            
            
            
            
        