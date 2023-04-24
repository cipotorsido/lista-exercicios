def verifica_maiuscula(string):
    if not string.isupper():
        raise ValueError("A string deve conter apenas letras maiúsculas.")
    print("A string contém apenas letras maiúsculas.")

try:
    string = input("Digite uma string: ")
    verifica_maiuscula(string)
except ValueError as error:
    print(error)