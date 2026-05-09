lista_frutas = ["Banana" , "Maçã" ,  "Morango"]

# lista_frutas[0] = "Banana"
# lista_frutas[1] = "Maçã"
# lista_frutas[2] = "Morango"
print(lista_frutas[1])

lista_frutas.append("Uva")
print(lista_frutas[-1])

tamanho = len(lista_frutas)
print(tamanho)
print()

for i in range(tamanho):
    print(lista_frutas[i])

print()

for fruta in lista_frutas:
    print(fruta)

msg  = "Oi Arthur!"

for i in range(len(msg)):
    print(msg[i])


# DESAFIO 1 duplas

Nomes = ["Ana", "joao", "Leo", "Bia", "Arthur", "Jovas", "Brayan", "Alan"]

for Nome in range(len(Nomes)):
    for proxNome in range(Nome+1, len(Nomes)): # i = Nome e j = proxNome, quando Nome for 0 proxNome é 1
        print(Nomes[Nome], Nomes[proxNome])