pessoas = []
while True:
    pessoa = {}
    pessoa['nome'] = str(input("Qual o seu nome? SEM ACENTOS"))
    if not pessoa['nome'].isalpha():
        print("Seu nome não condiz com o cartório")
        continue

    pessoa['turno_de_trabalho'] = str(input("Em qual período você trabalha? (m = Matutino), (v = Vespertino), (n = Noturno) "))
    if pessoa['turno_de_trabalho'] not in ["m", "v", "n"]:
        print("Seu período não condiz com os disponíveis")
        continue

    pessoa['categoria'] = str(input("Você é gerente(g) ou operário(o)? "))
    if pessoa['categoria'] not in ["g", "o"]:
        print("Opção inválida")
        continue

    pessoa['salario'] = 0

    if pessoa['categoria'] == 'g' and pessoa['turno_de_trabalho'] == 'n':
        pessoa['salario'] = 0.1 * 1320
    elif pessoa['categoria'] == 'g' and (pessoa['turno_de_trabalho'] == 'm' or pessoa['turno_de_trabalho'] == 'v'):
        pessoa['salario'] = 0.15 * 1320
    elif pessoa['categoria'] == 'o' and (pessoa['turno_de_trabalho'] == 'n'):
        pessoa['salario'] = 0.09 * 1320
    elif pessoa['categoria'] == 'o' and (pessoa['turno_de_trabalho'] == 'm' or pessoa['turno_de_trabalho'] == 'v'):
        pessoa['salario'] = 0.14 * 1320

    pessoas.append(pessoa)
    resposta = input("Deseja adicionar informações de outra pessoa? (s/n) ")
    if resposta.lower() == 'n':
        break


for pessoa in pessoas:
    print(f"Nome: {pessoa['nome']}, Salário: R${pessoa['salario']:.2f}")