# Criação das variáveis para armazenamento dos dados
estudantes = []
# entrada do loop
while True:
    # Mostrando o menu principal
    print("\nBem-vindo ao menu!")
    print("1. Estudantes")
    print("2. Professores")
    print("3. Disciplinas")
    print("4. Turmas")
    print("5. Matriculas")
    print("0. Sair")
    # Mostrando os menus secundários
    try:
        opcao = int(input("Digite uma opção válida: "))
        print(f"Você escolheu {opcao}!")
        if opcao == 1:
            while True:
                print("\nMenu de estudantes")
                print("1. Listar estudantes")
                print("2. Cadastrar estudante")
                print("3. Atualizar cadastro")
                print("4. Excluir cadastro")
                print("5. Voltar ao menu inicial")
                # coleta a opção do usuário
                subopcao = int(input("Escolha uma opção: "))
                print(f"Você escolheu {subopcao} para Estudantes")
                if subopcao == 1:
                    # condicional que lista os estudantes cadastrados.
                    if len(estudantes) == 0:
                        print("Não há estudantes cadastrados")
                    else:
                        # coloca em ordem alfabetica
                        estudantes_ordem = sorted(estudantes)
                        for i, estudante in enumerate(estudantes_ordem, start=1):
                            print(f"{i}. {estudante}")
                # loop de repetição para cadastro do estudante
                elif subopcao == 2:
                    while True:
                        estudante = input("Digite o primeiro nome do estudante (digite sair para finalizar): ")
                        if estudante == "sair":
                            break
                        estudantes.append(estudante)
                # opções em desenvolvimento
                elif subopcao == 3 or subopcao == 4:
                    print("Em desenvolvimento")
                # volta ao menu anterior
                elif subopcao == 5:
                    print("Voltando ao menu principal.")
                    break
                else:
                    print("Digite uma opção válida!")
        # opções em desenvolvimento
        elif opcao == 2 or opcao == 3 or opcao == 4 or opcao == 5:
            print("Em desenvolvimento.")
        # encerra o programa
        elif opcao == 0:
            print("Encerando o sistema... Até mais!")
            break
        else:
            print("Digite uma opção válida!")
    except ValueError:
        print("Digite uma opção válida!")