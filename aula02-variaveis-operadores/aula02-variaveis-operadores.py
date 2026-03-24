
print("Vai Corinthians----------------")

print(7 + 4)
print("7 + 4")
print("7"+"4")
'''
comentarios de varias linhas
'''
#variaveis
nome="Arthur" #String
idade=19 #int
peso=80.1 #float
print("O nome, idade e peso sao: ",nome,idade,peso)
print(f"oi,{nome}")

nome = input("Digite sue nome:")
print(nome)
idade = int(input("digite sua idade"))
print(nome, idade)
print(idade + 1)

'''
desafios____________________
'''
#1
nome = input("Digite seu nome:")
print("boas-vindas:" , nome)
#_______________________________

#2
nasc = input("Digite sua data de nascimento: dd/mm/aaaa ")
print("voce nasceu em: " , nasc)
#_______________________________

#3
n1 = int(input("digite o primeiro numero para a soma: "))
n2 = int(input("digite o segundo numero para a soma:  "))

soma = n1 + n2
print("A soma é: ", soma)
#_______________________________

print("Vai Corinthians--------------------------                ")

'''
EXERCICIOS
'''
#1
area = 3.14159 * 5**2
print(f" a area de um circulo com raio 5 é:{area}")

#2
TF = float(input("digite a temperatura em  Fahrenheit:"))
TC = float((TF - 32 ) * 5/9)
print(f"A temperatura em Celcius é: ", TC)

#4
livros  = 25 * 3
canetas = 2  * 5
gasto_total = f"O gasto total da compra de tres livros e duas canetas  foi de: {livros + canetas}R$"
print(gasto_total)

#5
distancia = 150
velom = 60
tempo = distancia/velom
print(f"O tenpo em horas de um percurso de 150km percorrido com velocidade media de 60km é de: {tempo}h")

#6
n1 = float(input("digite a primeira nota: "))
n2 = float(input("digite a segunda nota: "))
ma = ( n1 + n2 ) /2
print(f'a media do aluno foi {ma}')