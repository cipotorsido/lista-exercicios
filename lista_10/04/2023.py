import random
paises = []
while True:
    adc_paises = input("Qual país você quer adicionar ?")



    continuar = input("Quer continuar adicionando países?  (S/N)").upper()
    if continuar != "S" :
        break
    else: continue

elemento_aleatorio = random.choice(paises)


def encontrar_posicao(lista, elemento):
    if elemento in lista:
        posicao = lista.index(elemento)
        return posicao
    else:
        return -1
posicao = encontrar_posicao(paises, elemento_aleatorio)

print(posicao)

num_inteiros = []

while True:
    numeros_int = input("Digite numeros inteiros: ")
    num_inteiros.append(int(numeros_int))

    continuar = input("Quer continuar adicionando números? (S/N)").upper()
    if continuar != "S":
        break
num_aleatorio = random.choice(num_inteiros)


def adicionar_numero_na_lista(numeros_inteiros,random ):
    numeros_inteiros.insert(0, num_aleatorio)
    return numeros_inteiros

nova_lista = adicionar_numero_na_lista(num_inteiros, num_aleatorio)
print(nova_lista)
