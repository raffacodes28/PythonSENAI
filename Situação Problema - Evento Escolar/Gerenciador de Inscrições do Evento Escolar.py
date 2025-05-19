nomes = ["Celio", "Paulini", "Bruno", "Rafael", "Adriano", "Mario", "Lucas"]

while True:
    print("1- Cadastre seu nome")
    print("2- Exibir o total de inscritos")
    print("3- Exibir a lista de nomes em ordem alfabética")
    print("4- Permitir a consulta  de um nome")
    print("5- sair")
    opcao = int(input("Digite sua escolha"))

    if opcao == 1:
        nome = input("Digite o nome que voce quer cadrastrar")
        if nome in nomes:
            print("Nome ja esta cadrastrado")
        else:
            nome.append(nomes)
            print("Nome cadastrado")    
    
    if opcao == 2:
        print("O total de pessoas incristas e de", len(nomes), "pessoas")
        
    if opcao == 3:
        nomes.sort()
        for nome in nomes:
            print(nome)
            
    if opcao == 4:
        nome = input("digite seu nome que quer consultar")
        if nome in nomes:
            vari = input("nome encontrado, você deseja remover da lista? s/n ")
            if vari == "s":
                nomes.remove(nome)
                print("nome removido")
            elif vari == "n":
                print("o nome ainda permanece na lista")
        else:
            vari1 = input("nome não encontrado, deseja adiciona-lo? s/n")
            if vari1 == "s":
                nomes.append(nome)
                print("o nome foi adicionado à lista")
            elif  vari1 == "n":
                print("ok")
            else:
                print("opção inesistente")
    if opcao == 5:
        print("Você saiu")
        break
    else:
        print("Opção inexistente")