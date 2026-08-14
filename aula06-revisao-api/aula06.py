




endpoints = ["/login", "/produtos", "/pedidos"]
status = [
[200, 200, 401, 200, 500],
[200, 200, 200, 200, 200],
[201, 500, 502, 201, 500]
]

# Função que verifica se um codigo HTTP de uma req é sucesso ou não
# 200 -> true
# 401 -> false
def eh_sucesso(codigo):
    return codigo >= 200 and codigo <= 299

# print(eh_sucesso(404))



# FUNÇÃO que verifica se ha dois erros seguidos na lista de requisiçoes (codigo http) de um ENDPOINT
# [200, 200, 401, 200, 500] -> false
# [201, 500, 502, 201, 500] -> true
def verifica_erros(codigos_endpoint):
    for i in range(len(codigos_endpoint) -1 ):
        codigo_atual = codigos_endpoint[i]
        prox_codigo = codigos_endpoint[i+1]

        if not eh_sucesso(codigo_atual) and not eh_sucesso(prox_codigo):
            return True
    return False
print(verifica_erros(status[0]))


