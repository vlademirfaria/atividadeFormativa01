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

def obter_opcao(mensagem):
    while True:
        try:
            opcao = int(input(mensagem))
            return opcao
        except ValueError:
            print("Por favor, digite um número inteiro válido.")

def menu_principal():
    while True:
        exibir_menu_principal()
        opcao = obter_opcao("Digite uma opção válida: ")
        
        if opcao == 0:
            print("Você pediu para sair.")
            break
        elif opcao >= 1 and opcao <= 5:
            print(f"Você escolheu a opção {opcao}.")
            menu_secundario(opcao)
        else:
            print("Você digitou uma opção inválida.")

def menu_secundario(opcao_principal):
    while True:
        exibir_menu_secundario(opcao_principal)
        opcao_secundaria = obter_opcao("Digite uma opção válida: ")
        
        if opcao_secundaria == 5:
            print("Você voltou ao menu anterior.")
            break
        elif opcao_secundaria >= 1 and opcao_secundaria <= 4:
            print(f"Você escolheu a opção {opcao_secundaria}.")
        else:
            print("Você digitou uma opção inválida.")

menu_principal()
