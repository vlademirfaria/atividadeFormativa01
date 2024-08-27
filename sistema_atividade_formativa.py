# Mostrando o menu principal
menu_principal = print("Bem-vindo ao menu!")
print("1. Estudantes")
print("2. Professores")
print("3. Disciplinas")
print("4. Turmas")
print("5. Matriculas")
print("0. Sair")
# Coletar a opção escolhida pelo usuário
opcao = int(input("Digite uma opção válida. "))
if opcao >= 1 and opcao <= 5:
    print(f"Você escolheu a opção {opcao}.")
    # Mostrando o menu secundário
    print(f"Menu de operações - Opção {opcao}")
    print("1. Listar")
    print("2. Criar")
    print("3. Atualizar")
    print("4. Excluir")
    print("5. Voltar ao menu anterior")
    # Coletar a opção secundária
    opcao_secundaria = int(input(" Digite uma opção válida. "))
    print(f"Vocês escolheu a opção secundária {opcao_secundaria}.")
    if opcao_secundaria >= 1 and opcao_secundaria <= 4:
        print(f"Você escolheu a opção {opcao}.")
    elif opcao_secundaria == 5:
        print("Você voltara ao menu inicial.")
    else:
        print("Você digitou uma opção secundária inválida.")
elif opcao == 0:
    print("Você pediu pra sair.")
else:
    print("Você digitou uma opção inválida.")