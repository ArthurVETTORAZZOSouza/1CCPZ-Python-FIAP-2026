from model import model_lead
import control

def add_lead():
    name = input("Informe o nome do lead: ")
    email = input("Informe o email do lead: ")
    stage = input("Informe a etapa de vendas: ")

    # validar os dados
    # precisamos modelar os dados (lead) como um dicionario
    # MODELAR -- model
    print(model_lead(name,email,stage))

    #de acordo com os dados modelados (lead como dict)
    #precisamos enviar esse dado do lead para o leads.json
    #control irá nos ajudar nisso
    control.create_leads(model_lead(name,email,stage))

    print("lead adicionado (func)")

def list_leads():
    leads = control.read_leads()
    print(leads)

def mai():
    while True:
        print("\nMini CRM de Leads")
        print("[1] Adicionar lead")
        print("[2] Listar leads")
        print("[0] Sair do programa")

        opt = input("Escolha uma opção: ")
        if opt == "1":
            print("Adicionar lead")
            add_lead()
        elif opt == "2":
            list_leads()
        elif opt == "0":
            print("Até mais...")
            break
        else:
            print("Opção invalida.")
if __name__ == "__main__":
    mai()
