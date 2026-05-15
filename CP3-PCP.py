
temperaturas = [
[28, 31, 34, 33],
 [25, 27, 29, 28],
 [32, 35, 36, 34],
 [24, 26, 25, 27]
]
i = 0
media = 0
criticos = 0
for sala in temperaturas:
    print(sala)

    for temperatura in sala:
        print(temperatura)
        if temperatura >= 33:
            criticos +=1

    print(f"sala {i+1}")

    media = sum(sala) / len(sala)
    print(media)
    print(criticos)

    i+=1
    criticos = 0

    print()