# Criação das variáveis para armazenamento dos dados
estudantes = []
professores = []
disciplinas = []
turmas = []
matriculas = []
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
    # Mostrando aos menus secundarios
    try:
        opcao = int(input("Digite uma opção válida: "))
        if opcao == 1:
            while True:
                print("\nMenu de estudantes")
                print("1. Listar estudantes")
                print("2. Cadastrar estudante")
                print("3. Atualizar cadastro")
                print("4. Excluir cadastro")
                print("5. Voltar ao menu inicial")
                subopcao = int(input("Escolha uma opção: "))
                if subopcao == 5:
                    break
                else:
                    print(f"Você escolheu {subopcao} para Estudantes")
                if subopcao == 1:
                    #  condicional que lista os estudantes cadastrados.
                    if len(estudantes) == 0:
                        print("Não há estudantes cadastrados.")
                    else:
                        # coloca em ordem alfabetica
                        estudantes_ordem = sorted(estudantes)
                        for estudante in estudantes_ordem:
                            print(estudante)
                # loop de repetição para cadastro do estudante
                if subopcao == 2:
                    while True:
                        estudante = input("Digite o primeiro nome do estudante (digite sair para finalizar): ")
                        estudantes.append(estudante)
                        if estudante == "sair":
                            break
                if subopcao == 3 or subopcao == 4:
                    print("Em desenvolvimento.")
        elif opcao == 2:
            while True:
                print("\nMenu de professores")
                print("1. Listar professores")
                print("2. Cadastrar professor")
                print("3. Atualizar cadastro")
                print("4. Excluir cadastro")
                print("5. Voltar ao menu inicial")
                subopcao = int(input("Escolha uma opção: "))
                if subopcao == 5:
                    break
                else:
                    print(f"Você escolheu {subopcao} para Professores")
                if subopcao == 1 or subopcao == 2 or subopcao == 3 or subopcao == 4:
                    print("Em desenvolvimento.")
        elif opcao == 3:
            while True:
                print("\nMenu de disciplinas")
                print("1. Listar disciplinas")
                print("2. Cadastrar disciplina")
                print("3. Atualizar disciplina")
                print("4. Excluir disciplina")
                print("5. Voltar ao menu inicial")
                subopcao = int(input("Escolha uma opção: "))
                if subopcao == 5:
                    break
                else:
                    print(f"Você escolheu {subopcao} para Disciplinas")
                if subopcao == 1 or subopcao == 2 or subopcao == 3 or subopcao == 4:
                    print("Em desenvolvimento.")
        elif opcao == 4:
            while True:
                print("\nMenu de turmas")
                print("1. Listar turmas")
                print("2. Cadastrar turma")
                print("3. Atualizar turma")
                print("4. Excluir turma")
                print("5. Voltar ao menu inicial")
                subopcao = int(input("Escolha uma opção: "))
                if subopcao == 5:
                    break
                else:
                    print(f"Você escolheu {subopcao} para Turmas")
                if subopcao == 1 or subopcao == 2 or subopcao == 3 or subopcao == 4:
                    print("Em desenvolvimento.")
        elif opcao == 5:
            while True:
                print("\nMenu de matriculas")
                print("1. Listar matriculas")
                print("2. Cadastrar matricula")
                print("3. Atualizar matricula")
                print("4. Excluir matricula")
                print("5. Voltar ao menu inicial")
                subopcao = int(input("Escolha uma opção: "))
                if subopcao == 5:
                    break
                else:
                    print(f"Você escolheu {subopcao} para Matriculas")
                if subopcao == 1 or subopcao == 2 or subopcao == 3 or subopcao == 4:
                    print("Em desenvolvimento.")
        elif opcao == 0:
            print("Encerando o sistema... Até mais!")
            break
        else:
            print("Digite uma opçao válida!")
    except ValueError:
        print("Digite uma opção válida!")