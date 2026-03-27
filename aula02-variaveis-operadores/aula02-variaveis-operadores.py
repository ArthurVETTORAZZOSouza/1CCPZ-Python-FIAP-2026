
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

print("EXECICIOS")

print()
#1
area = 3.14159 * 5**2
print(f" a area de um circulo com raio 5 é:{area}")

print()

#2
TF = float(input("digite a temperatura em  Fahrenheit:"))
TC = float((TF - 32 ) * 5/9)
print(f"A temperatura em Celcius é: ", TC)

print()

#4
livros  = 25 * 3
canetas = 2  * 5
gasto_total = f"O gasto total da compra de tres livros e duas canetas  foi de: {livros + canetas}R$"
print(gasto_total)

print()

#5
distancia = 150
velom = 60
tempo = distancia/velom
print(f"O tenpo em horas de um percurso de 150km percorrido com velocidade media de 60km é de: {tempo}h")

print()

#6
n1 = float(input("digite a primeira nota: "))
n2 = float(input("digite a segunda nota: "))
ma = ( n1 + n2 ) /2
print(f'a media aritimetica do aluno foi de: {ma}')

print()

#7
N1 =float(input("digite a primeira nota (peso4): "))
N2 = float(input("digite a segunda nota (peso6): "))
MP = ((N1*4) + (N2*6)) / (4+6)
print (f"A média ponderada do foi de:",MP)

print()

#8
P1= input("Digite o nome da primeira peça: ")
quantP1= int(input(f"Quantas unidades da {P1} o senhor quer?: "))
ValorP1= float(input(f"Qual o valor da {P1}?: "))
pagarP1 = quantP1*ValorP1
print("o pagamento da",P1 ,"foi de: R$",pagarP1)

print()

P2= input("Digite o nome da segunda peça: ")
quantP2= int(input(f"Quantas unidades da {P2} o senhor quer?: "))
ValorP2= float(input(f"Qual o valor da {P2}?: "))
pagarP2 = quantP2*ValorP2
print("o pagamento da",P2 ,"foi de: R$",pagarP2)
print(f"O pagamento total foi de:R$ {pagarP1+pagarP2}")

print()

#9
valorProd = float(input("Digite o valor do produto: R$ "))
valorPago = float(input("Digite o valor pago pelo produto: R$ "))

if valorPago > valorProd:
    troco = valorPago - valorProd
    print(f"O seu troco é de: R$ {troco:}")

elif valorPago == valorProd:
    print("Pagamento exato. Não tem troco.")

else:
    falta = valorProd - valorPago
    print(f"Valor insuficiente ainda faltam: R$ {falta:}")
