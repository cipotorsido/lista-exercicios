nome = input("Digite um nome: ")
nota1 = float(input("Digite a nota 1: "))
nota2 = float(input("Digite a nota 2: "))
nota3 = float(input("Digite a nota 3: "))

with open("notas.txt", "a") as arquivo:
    arquivo.write(f"{nome} {nota1} {nota2} {nota3}\n")

with open("notas.txt", "r") as arquivo:
    linhas = arquivo.readlines()

aprovados = []
exame = []
reprovados = []

for linha in linhas:
    valores = linha.strip().split()

    media = sum(float(nota) for nota in valores[1:]) / 3

    if media >= 7:
        aprovados.append(f"{valores[0]}: {media:.2f}")
    elif media >= 5:
        exame.append(f"{valores[0]}: {media:.2f}")
    else:
        reprovados.append(f"{valores[0]}: {media:.2f}")

with open("aprovados.txt", "w") as arquivo:
    arquivo.write("Alunos aprovados:\n")
    for aluno in aprovados:
        arquivo.write(f"{aluno}\n")

with open("reprovados.txt", "w") as arquivo:
    arquivo.write("Alunos reprovados:\n")
    for aluno in reprovados:
        arquivo.write(f"{aluno}\n")