import os.path
from typing import List, Dict


def ler_rendimentos_mensais() -> List[float]:
    """Lê os rendimentos mensais armazenados no arquivo 'rendimento_mensal.txt' e retorna uma lista de floats"""
    rendimentos = []
    if os.path.exists("rendimento_mensal.txt"):
        with open("rendimento_mensal.txt", "r") as arquivo:
            rendimentos = [float(rendimento.strip()) for rendimento in arquivo.readlines() if rendimento.strip()]
    return rendimentos


def salvar_rendimentos_mensais(rendimentos: List[float]) -> None:
    """Salva os rendimentos mensais em um arquivo 'rendimento_mensal.txt'"""
    with open("rendimento_mensal.txt", "w") as arquivo:
        for rendimento in rendimentos:
            arquivo.write(f"{rendimento:.2f}\n")


def calcular_total_rendimentos(rendimentos: List[float]) -> None:
    """Calcula e imprime o total de rendimentos mensais"""
    if not rendimentos:
        print("Não há nenhum rendimento registrado.")
        return

    total = sum(rendimentos)
    print(f"Total de rendimentos: R$ {total:.2f}")


def ler_despesas() -> List[Dict[str, any]]:
    """Lê as despesas armazenadas no arquivo 'despesas.txt' e retorna uma lista de dicionários"""
    despesas = []
    if os.path.exists("despesas.txt"):
        with open("despesas.txt", "r") as arquivo:
            proxima_linha_eh_cabecalho = True
            for linha in arquivo:
                if proxima_linha_eh_cabecalho:
                    proxima_linha_eh_cabecalho = False
                    continue

                campos = linha.strip().split('\t')
                descricao = campos[0]
                mes = int(campos[1])
                valor = float(campos[2])
                despesa = {'descricao': descricao, 'mes': mes, 'valor': valor}
                despesas.append(despesa)
    return despesas


import os


def cadastrar_despesas(despesas, mes):
    descricao = input("Descrição da despesa: ")
    nome = input("Nome da despesa: ")
    valor = float(input("Valor da despesa: "))
    despesa = {'nome': nome, 'descricao': descricao, 'mes': mes, 'valor': valor}
    despesas.append(despesa)
    return despesas


def calcular_despesas_por_mes(despesas):
    despesas_por_mes = {}
    for despesa in despesas:
        mes = despesa['mes']
        if mes not in despesas_por_mes:
            despesas_por_mes[mes] = 0
        despesas_por_mes[mes] += despesa['valor']
    return despesas_por_mes


def calcular_total(rendimentos):
    total_rendimentos = sum(rendimentos)
    print(f"Total dos rendimentos: R$ {total_rendimentos:.2f}")
    return total_rendimentos


def salvar_despesas(despesas):
    with open("despesas.txt", "w") as arquivo:
        arquivo.write("Descrição\tMês\tValor\n")
        for despesa in despesas:
            arquivo.write(f"{despesa['descricao']}\t{despesa['mes']}\t{despesa['valor']}\n")


def excluir_despesa():
    mes = input("Digite o mês em que a despesa foi registrada: ")
    descricao = input("Digite a descrição da despesa que deseja excluir: ")

    try:
        with open("despesas.txt", "r") as arquivo:
            linhas = arquivo.readlines()

        with open("despesas.txt", "w") as arquivo:
            arquivo.write(linhas[0])
            for linha in linhas[1:]:
                if not (mes in linha and descricao in linha):
                    arquivo.write(linha)

        print("Despesa excluída com sucesso!")

    except FileNotFoundError:
        print("O arquivo não existe")

    except Exception as e:
        print("Ocorreu um erro ao excluir a despesa:", e)



salvar_despesas(ler_despesas())
excluir_despesa()


filepath = "despesas.txt"


if not os.path.exists(filepath):
    print("O arquivo de despesas não existe!")
else:

    with open(filepath, "r") as f:
        lista_despesa = f.readlines()


    lista_despesa = [d.strip() for d in lista_despesa]


    despesas = {}


    for despesa in lista_despesa:
        try:
            nome, valor = despesa.split(":")
            despesas[nome] = float(valor)
        except ValueError:
            print(f"Erro ao processar despesa: {despesa}")


    total = sum(despesas.values())
    print(f"Total das despesas: R$ {total:.2f}")


    nome_despesa = input("Digite o nome da despesa que deseja alterar: ")
    novo_valor = input("Digite o novo valor da despesa: ")

    try:
        novo_valor = float(novo_valor)
        if nome_despesa in despesas:
            despesas[nome_despesa] = novo_valor
            print(f"O valor da despesa '{nome_despesa}' foi alterado para R$ {novo_valor:.2f}")
        else:
            print(f"A despesa '{nome_despesa}' não existe!")
    except ValueError:
        print("Valor inválido. Por favor, digite um número válido.")

import os


despesas = []


diretorio = 'despesas.txt'

import os


diretorio = 'despesas'


despesas = []

for arquivo in os.listdir(excluir_despesa()):
    if arquivo.endswith('despesas.txt'):
        # Abra o arquivo em modo de leitura
        with open('despesas.txt', 'r') as f:
            # Leia as informações de cada linha do arquivo
            for linha in f:
                descricao, mes, valor = linha.strip().split(',')
                # Adicione as informações da despesa na lista de despesas
                despesas.append({
                    'descricao': descricao,
                    'mes': mes,
                    'valor': float(valor)
                })

despesas_ordenadas = sorted(despesas, key=lambda x: (int(x['mes'].split('/')[1]), int(x['mes'].split('/')[0])))


for despesa in despesas_ordenadas:
    print(despesa)

    import re


    dir_path = "/caminho/para/diretorio"


    info_by_month = {}


    for filename in os.listdir(dir_path):
        if filename.endswith(".txt"):
            filepath = os.path.join(dir_path, filename)


            month = re.findall(r"\d{4}-(\d{2})", filename)[0]


            with open(filepath, "r") as f:
                info = f.read()


            if month not in info_by_month:
                info_by_month[month] = [info]
            else:
                info_by_month[month].append(info)


    info_by_month = dict(sorted(info_by_month.items()))


    for month, info_list in info_by_month.items():
        print(f"Mês {month}:")
        for info in info_list:
            print(info)

with open('despesas.txt', 'r') as arquivo:
    receita_meta = float(input('Digite a receita meta: '))
    saldo = 0
    for linha in arquivo:
        dados = linha.strip().split(',')
        mes = dados[0]
        receita = float(dados[1])
        despesa = float(dados[2])
        saldo_mes = receita - despesa
        saldo += saldo_mes
        print(f"Mês: {mes}")
        print(f"Receita: {receita:.2f}")
        print(f"Despesa: {despesa:.2f}")
        print(f"Saldo do mês: {saldo_mes:.2f}")
        if saldo_mes >= 0:
            print("Meta batida!")
        else:
            print("Meta não batida!")
        print()
    print(f"Saldo acumulado: {saldo:.2f}")
    if saldo >= receita_meta:
        print("Meta de receita batida!")
    else:
        print("Meta de receita não batida!")