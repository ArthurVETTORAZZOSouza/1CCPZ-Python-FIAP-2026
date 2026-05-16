
temperaturas = [
[28, 31, 34, 33],
 [25, 27, 29, 28],
 [32, 35, 36, 34],
 [24, 26, 25, 27]
]
i = 0
media = 0
criticos = 0
sala_critica = 0
numero_sala_critica = 1
for sala in temperaturas:
    for temperatura in sala:
        if temperatura >= 33:
            criticos +=1

    print(f"Sala: {i+1}")


    media = sum(sala) / len(sala)
    print(f"Média de temperatura: {media}")
    print(f"Número de temperaturas criticas: {criticos}")


    if criticos > sala_critica:
        sala_critica = criticos
        numero_sala_critica = i+1

 
    i+=1
    criticos = 0

    print()


print(f"A sala com maior quantidade de temperatura é: {numero_sala_critica}")
