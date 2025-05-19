#passo passo
#3 Contrua um programa que calcule: Quanto custa encher
# o tanque de um carro que tem 50 litros de capacidade, está com 20 litros de
#combustível atualmenta e o custo do combustível é de R$5,80/litro

#1 - Quanto vai custar o valor ao encher o tanque de um carro com 50 litros

#2 - calcular o valor 1 litro por 30 litros que falta completar

#3 - achar quanto litros faltam para completar 50 litros
# multiplicar a quantidade litros que faltam pelo valor de 1 litro
# Exibir o valor da quantidade de litros que faltam para ter 50 litros


quantidade_total = int(input("Seleciona a quantidade total de litros que precisa no taque"))
quantidade_possui = int(input("selecione a quantidade de litros que possui"))
preco_litros = float(input("selecione o preço de um litro"))
quantidade_faltam = quantidade_total - quantidade_possui
valor_faltam = quantidade_faltam * preco_litros
print("faltam 30 litros para completar 50 e o valor dele é de", valor_faltam, "reais")


