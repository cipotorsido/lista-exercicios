informacoes = []
contagem_elevadores = {"A": 0, "B": 0, "C": 0}
contagem_periodos = {"M": 0, "V": 0, "N": 0}
contagem_total = 0
while True:
    elevador_frequente = input("Qual elevador você  com mais frequência? (A, B ou C)? ").upper()
    periodo_utilizacao = input("Qual o período em que você utiliza o elevador (M = Matutino, V = Vespertino, N = Noturno)? ").upper()

    if elevador_frequente in ["A", "B", "C"] and periodo_utilizacao in ["M", "V", "N"]:
        informacoes.append((elevador_frequente, periodo_utilizacao))
        contagem_elevadores[elevador_frequente] += 1
        contagem_periodos[periodo_utilizacao] += 1
        contagem_total += 1


    else:
        print("Não coencide. Tente novamente.")

    continuar = input("Deseja inserir mais informações? (S/N)").upper()
    if continuar != "S":
        break

elevador_mais_utilizado = max(contagem_elevadores, key=contagem_elevadores.get)
periodo_maior_fluxo = max(contagem_periodos, key=contagem_periodos.get)
periodo_mais_utilizado = max(contagem_periodos, key=contagem_periodos.get)
mais_usado = contagem_periodos[periodo_mais_utilizado]
menos_usado = min(contagem_periodos.values())
diferenca_percentual = 100 * (mais_usado - menos_usado) / mais_usado




print("Lista de informações coletadas:")
for elevador, periodo in informacoes:
    print("Elevador: ", elevador, "Período de utilização: ", periodo)


print("Elevador mais utilizado: ", elevador_mais_utilizado)
print("Período de maior fluxo: ", periodo_maior_fluxo)
print("Período mais utilizado de todos: ", periodo_mais_utilizado)
print("Diferença percentual entre o mais usado e o menos usado: {:.2f}%".format(diferenca_percentual))