def exibir_menu_principal():
    print("Bem-vindo ao menu!")
    print("1. Estudantes")
    print("2. Professores")
    print("3. Disciplinas")
    print("4. Turmas")
    print("5. Matriculas")
    print("0. Sair")

def exibir_menu_secundario(opcao):
    print(f"Menu de operações - Opção {opcao}")
    print("1. Listar")
    print("2. Criar")
    print("3. Atualizar")
    print("4. Excluir")
    print("5. Voltar ao menu anterior")

def obter_opcao(mensagem, intervalo=None):
    while True:
        try:
            opcao = int(input(mensagem))
            if intervalo is None or opcao in intervalo:
                return opcao
            else:
                print("Opção fora do intervalo permitido.")
        except ValueError:
            print("Por favor, digite um número inteiro válido.")

def menu_principal():
    while True:
        exibir_menu_principal()
        opcao = obter_opcao("Digite uma opção: ", intervalo=range(6))
        
        if opcao == 0:
            print("Você pediu para sair.")
            break
        elif opcao >= 1 and opcao <= 5:
            print(f"Você escolheu a opção {opcao}.")
            menu_secundario(opcao)
        else:
            print("Opção inválida.")

def menu_secundario(opcao_principal):
    while True:
        exibir_menu_secundario(opcao_principal)
        opcao_secundaria = obter_opcao("Digite uma opção: ", intervalo=range(6))
        
        if opcao_secundaria == 5:
            print("Voltando ao menu principal.")
            break
        elif opcao_secundaria >= 1 and opcao_secundaria <= 4:
            print(f"Você escolheu a opção {opcao_secundaria}.")
        else:
            print("Opção inválida.")

menu_principal()