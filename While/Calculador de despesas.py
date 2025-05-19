valor_total = 0
quant = 0
while True:
    print("0 - Saiu")
    print("1 - Adicionar valor da despesa")
    print("2 - Mostrar a quantidade e o valor total das despesas")
    menu = int(input("Escolha um dos número"))
    
    if menu == 0:
        print("Você saiu")
        break
    elif menu == 1:
        valor_adicional = int(input("Solicite o valor que deseja"))
        valor_total = valor_total + valor_adicional
        quant = quant + 1
    elif menu == 2:
        print("O valor total da despesa é", quant, valor_total)
