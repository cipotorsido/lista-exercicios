import os.path


def calcular_total(rendimentos):
    total = sum(rendimentos)
    print(f"Total de rendimentos: R$ {total:.2f}")


def alterar_rendimento(rendimentos):
    try:
        if len(rendimentos) == 0:
            print("Não há nenhum rendimento registrado.")
            return

        rendimento_atual = rendimentos[-1]
        economia = rendimento_atual * 0.1
        investimento = rendimento_atual * 0.01
        rendimento_novo = rendimento_atual - economia - investimento

        # Remove o rendimento do último mês registrado
        rendimentos.pop()

        # Adiciona o novo rendimento à lista de rendimentos
        rendimentos.append(rendimento_novo)

        # Reordena a lista de rendimentos
        rendimentos.sort()

        with open("rendimento_mensal.txt", "w") as arquivo:
            for rendimento in rendimentos:
                arquivo.write(f"{rendimento}\n")

        print("Rendimento alterado com sucesso!")

    except Exception as e:
        print("Ocorreu um erro ao alterar o rendimento:", e)


def salvar_despesas(despesas):
    try:
        with open("despesas.txt", "w") as arquivo:
            arquivo.write("Descrição\tMês\tValor\n")
            for despesa in despesas:
                arquivo.write(f"{despesa['descricao']}\t{despesa['mes']}\tR$ {despesa['valor']:.2f}\n")
        print("Despesas salvas com sucesso!")
    except Exception as e:
        print("Ocorreu um erro ao salvar as despesas:", e)

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


try:
    mes = int(input("Que mês estamos? "))
    rendimento_do_mes = float(input("Qual o seu rendimento do mês? "))

    rendimentos = []
    if os.path.exists("rendimento_mensal.txt"):
        with open("rendimento_mensal.txt", "r") as arquivo:
            rendimentos = [float(rendimento) for rendimento in arquivo.readlines()]

    rendimentos.append(rendimento_do_mes)

    with open("rendimento_mensal.txt", "w") as arquivo:
        for rendimento in rendimentos:
            arquivo.write(f"{rendimento}\n")

    if len(rendimentos) > 1:
        calcular_total(rendimentos)
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

    despesas = cadastrar_despesas(despesas, mes)
    despesas_por_mes = calcular_despesas_por_mes(despesas)
    for mes in despesas_por_mes:
        despesas_do_mes = despesas_por_mes[mes]
        if despesas_do_mes > rendimento_do_mes:
         print(
            f"Despesas do mês {mes} ({despesas_do_mes:.2f}) são maiores do que o rendimento ({rendimento_do_mes:.2f}).")

    despesas.sort(key=lambda x: x['mes'])
    salvar_despesas(despesas)



except ValueError:
    print(
        "O valor informado é inválido. Certifique-se de que digitou um número para o mês e um número ou decimal para o rendimento.")

except Exception as e:
    print("Ocorreu um erro ao processar a entrada:", e)


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


salvar_despesas(despesas)
excluir_despesa()

# define o caminho do arquivo de despesas
filepath = "despesas.txt"

# verifica se o arquivo de despesas existe
if not os.path.exists(filepath):
    print("O arquivo de despesas não existe!")
else:
    # carrega as despesas do arquivo
    with open(filepath, "r") as f:
        lista_despesa = f.readlines()

    # remove os caracteres de nova linha
    lista_despesa = [d.strip() for d in lista_despesa]

    # cria um dicionário vazio para armazenar as despesas
    despesas = {}

    # itera sobre a lista de despesas e adiciona ao dicionário
    for despesa in lista_despesa:
        try:
            nome, valor = despesa.split(":")
            despesas[nome] = float(valor)
        except ValueError:
            print(f"Erro ao processar despesa: {despesa}")

    # exibe o total das despesas
    total = sum(despesas.values())
    print(f"Total das despesas: R$ {total:.2f}")

    # altera o valor de uma despesa
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

# Crie uma lista vazia para armazenar as despesas
despesas = []

# Defina o diretório onde estão os arquivos txt
diretorio = 'despesas.txt'

import os

# Defina o nome da pasta onde estão os arquivos de despesa
diretorio = 'despesas'

# Inicialize a lista de despesas
despesas = []

# Percorra cada arquivo na pasta
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
# Ordene a lista de despesas por ano e mês
despesas_ordenadas = sorted(despesas, key=lambda x: (int(x['mes'].split('/')[1]), int(x['mes'].split('/')[0])))

# Imprima as despesas ordenadas
for despesa in despesas_ordenadas:
    print(despesa)

    import re

    # diretório contendo os arquivos .txt
    dir_path = "/caminho/para/diretorio"

    # dicionário que irá armazenar as informações agrupadas por mês
    info_by_month = {}

    # percorre todos os arquivos no diretório
    for filename in os.listdir(dir_path):
        if filename.endswith(".txt"):
            filepath = os.path.join(dir_path, filename)

            # extrai o mês presente no nome do arquivo
            month = re.findall(r"\d{4}-(\d{2})", filename)[0]

            # abre o arquivo e lê suas informações
            with open(filepath, "r") as f:
                info = f.read()

            # adiciona as informações ao dicionário correspondente ao mês presente
            if month not in info_by_month:
                info_by_month[month] = [info]
            else:
                info_by_month[month].append(info)

    # ordena as chaves do dicionário por ordem crescente de meses
    info_by_month = dict(sorted(info_by_month.items()))

    # imprime as informações agrupadas por mês
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