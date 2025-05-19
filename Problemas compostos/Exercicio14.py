#5 construa um programa que calcule: Quantos litros de combustível e
#quantos reais é preciso para fazer uma viagem de 800 quilômetros sendi
#que o carro tem uma autonomia de 7km por litro? O carro ainda tem 10
#litros no tanque e já percorreu 90 quilômetros da viagem e o preço do
#combustivel custa R$6,90

#1 - Achar quantos litros e quantos reais é preciso para fazer a viagem

#2 - Achar  a quantidade de litro em km, os custos e os preço

#3 - Achar o litros em km por subtração
#fazer a divizão para achar o custo atingo e subtrair para achar o novo custo
#Fazer a mutiplicação do novo custo com preço combustivel para achar o novo preço
#Exibir o novo preço e novo custo do combustivel

km_litros = 800 - 90
custo_antigo = km_litros / 7
custo_novo = custo_antigo - 10
antigo_preco = custo_novo * 6.90
print("a viagem teve um gasto total de", antigo_preco, "reais")
print("é preciso", custo_novo, "litros de gasolina para toda a viagem")