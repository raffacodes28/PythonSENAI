#1- Crie uma lista com os nomes de 5 objetos
objetos = ["lapis", "caneta", "mesa", "estojo", "mochila"]
print('lista de 5 objetos')
#2- Adicione mais um objeto ao final da lista
objetos.append('borracha')
print(objetos[1])
print("Adicione mais um objeto")
#4- Remova um objeto da lista e exiba-o 
variavel = objetos.pop(2)
print(2)
print("Remova um dos objetos na lista")
#5- Exiba o tamanho da lista
print(len(objetos))
print("Retorne o número de elementos na lista")
#6- Mostre todos os itens com o for
for objeto in objetos:
    print(objeto)
print("Mostre todos os itens da lista")
#7- Verifique se 'cadeira' esta na lista. Se sim remova-a, senão adicione
if 'cadeira' in objetos:
    objetos.remove('cadeira')
else:
    objetos.append('cadeira')
print("Veja se a cadeira esta na lista, se estive remova ela, se não adicione ela")

#8- Ordene a lista em ordem alfabética, exiba o antes e o depois
objetos.sort()
print("Você deve organizar a lista em ordem alfabética, e a exiba antes e depois")

#9- Exiba o primeiro e o último objeto e exiba eles
objetos[0]
objetos[4]
print("Você deve exibir o primeiro e o último e tera que exibir eles")

#10- Limpe toda a lista
objetos.clear()
print("Limpe toda a lista caso queira fazer outra")