try:
    numero = int(input("Digite um número inteiro: "))

    if numero % 2 != 0:
        raise Exception("O número digitado é ímpar. Digite um número par.")
    else:
        print("O número digitado é par.")

except Exception as e:
    print("Ocorreu um erro:", e)