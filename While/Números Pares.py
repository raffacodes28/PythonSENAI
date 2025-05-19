Par = int(input("Digite um número para saber seu pares"))
quant = 0

print(Par)

while True:
    Par = Par - 1
    if Par % 2 ==0:
        print(Par)
        quant = quant + 1
        
    elif Par <= 0:
        print("A quantidade de número pares é de", 	quant+1)
        
        break
