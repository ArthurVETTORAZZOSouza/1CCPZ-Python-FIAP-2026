#script1

nome = input("Insira o nome do produto: ")
preco_uni = float(input("Insira o valor unitário do produto: "))
quant_compra = int(input("Insira a quantidade comprada: "))
percent_desconto = float(input("Insira a porcentagem de desconto: "))/100

valor_bruto = preco_uni * quant_compra
valor_desconto = valor_bruto * percent_desconto
valor_final = valor_bruto - valor_desconto

print(f"Nome do produto: {nome}")
print(f"Valor bruto: R${valor_bruto:.2f}")
print(f"Desconto: R${valor_desconto:.2f}")
print(f"Valor final: R${valor_final:.2f}")


#script2
nome = input("Insira o nome do colaborador: ")
valor_hora = float(input("Insira o valor da hora trabalhada: "))
quant_hora = float(input("Insira a quantidade de horas trabalhadas: "))
bonus = float(input("Insira o valor do bônus: "))
desconto = float(input("Insira o valor descontado do salário: "))

bruto = valor_hora * quant_hora + bonus
liquido = bruto - desconto

print(f"Nome do colaborador(a): {nome}")
print(f"Salário bruto: R${bruto:.2f}")
print(f"Salário líquido: R${liquido:.2f}")