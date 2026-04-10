from operator import truediv

idade = 20

maior_idade = idade >= 18
print(maior_idade, type(maior_idade))

#operadores lógicos
# or, and, not

#lógica and

print() # pula linha

verifica_email = True
verifica_senha = False

login = verifica_email and verifica_senha
print(login)

if login:
    print("Entrar no sistema")
if not login:
    print("Presta atenção")

#Notas
nota_final = 6

if nota_final < 4:
    print("Reprovado")
elif nota_final < 6:
    print("Recuperação")
else:
    print("Aprovado")

print("FIM")
