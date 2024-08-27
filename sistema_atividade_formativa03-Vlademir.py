import json


def lista_json_escrita(lista, nome_arquivo):
    try:
        with open(nome_arquivo, "w") as arquivo:
            json.dump(lista, arquivo)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("Erro ao ler o arquivo JSON. O arquivo está vazio ou corrompido.")
        return []


def lista_json_ler(nome_arquivo):
    try:
        with open(nome_arquivo) as arquivo:
            lista = json.load(arquivo)
        return lista
    except:
        return []


def menu_principal():
    # Mostrando o menu principal
    print("Bem-vindo ao menu!")
    print("1. Estudantes")
    print("2. Professores")
    print("3. Disciplinas")
    print("4. Turmas")
    print("5. Matriculas")
    print("0. Sair")
    opcao = int(input("Digite uma opção válida: "))
    return opcao


def menu_secundario():
    print("1. Listar")
    print("2. Cadastrar")
    print("3. Atualizar cadastro")
    print("4. Excluir cadastro")
    print("5. Voltar ao menu inicial")
    subopcao = int(input("Escolha uma opção: "))
    return subopcao


def listar_estudante(nome_arquivo):
    estudantes = lista_json_ler(nome_arquivo)
    if len(estudantes) == 0:
        print("Não há estudantes cadastrados.")
    else:
        # Listando estudantes em ordem pelo código
        estudantes_ordenados = sorted(estudantes, key=lambda x: x["codigo"])
        for estudante in estudantes_ordenados:
            print(f"Código: {estudante['codigo']}, Nome: {estudante['nome']}, CPF: {estudante['cpf']}")


def cadastrar_estudante(nome_arquivo):
    try:
        while True:
            estudantes = lista_json_ler(nome_arquivo)
            codigo = int(input("Digite o código do estudante: "))
            nome = input("Digite o nome completo do estudante: ")
            cpf = input("Digite o CPF do estudante: (No formato 000.000.000-00) ")
            # Verificando se o código é único
            if any(estudante['codigo'] == codigo for estudante in estudantes):
                print(f"Código {codigo} já existe. Tente um código diferente.")
            else:
                estudantes.append({"codigo": codigo, "nome": nome, "cpf": cpf})
                print("Estudante cadastrado com sucesso!") 
                lista_json_escrita(estudantes, nome_arquivo)                
                continuar = input("Deseja cadastrar outro estudante? (s/n): ")
                if continuar == "n":
                    return None
    except ValueError:
        print("Entrada inválida. Certifique-se de que o código é um número.")


def atualizar_estudante(nome_arquivo):
    try:
        estudantes = lista_json_ler(nome_arquivo)
        codigo = int(input("Digite o código do estudante que deseja atualizar: "))
        estudante = next((e for e in estudantes if e['codigo'] == codigo), None)
        if estudante:  # Se o estudante for encontrado
            nome = input(f"Digite o novo nome para {estudante['nome']} (ou pressione Enter para manter): ")
            cpf = input(f"Digite o novo CPF para {estudante['cpf']} (ou pressione Enter para manter): ")
            if nome:  # Se um novo nome foi fornecido
                estudante['nome'] = nome  # Atualiza o nome
            if cpf:  # Se um novo CPF foi fornecido
                estudante['cpf'] = cpf  # Atualiza o CPF
            print("Cadastro atualizado com sucesso!")  # Confirma a atualização
        else:
            print(f"Nenhum estudante encontrado com o código {codigo}.")
        lista_json_escrita(estudantes, nome_arquivo)
        return None
    except ValueError:
        print("Entrada inválida. Certifique-se de que o código é um número.")


def excluir_estudante(nome_arquivo):
    try:
        estudantes = lista_json_ler(nome_arquivo)
        codigo = int(input("Digite o código do estudante que deseja excluir: "))
        estudante = next((e for e in estudantes if e['codigo'] == codigo), None)
        if estudante:
            estudantes.remove(estudante)  # Remove o estudante da lista
            print("Estudante excluído com sucesso!")  # Confirma a exclusão
            lista_json_escrita(estudantes, nome_arquivo)
            return None
        else:
            print(f"Nenhum estudante encontrado com o código {codigo}.")
    except ValueError:
        print("Entrada inválida. Certifique-se de que o código é um número.")


# Criação do arquivo json
arquivo = 'estudantes.json'
# entrada do loop
while True:  # Loop principal que mantém o programa em execução
    menu = menu_principal()
    try:
        if menu == 1:
            print(f"Você escolheu {menu}!")
            while True:
                print("\nMenu de estudantes")
                # Coleta a opção do usuário para o submenu de estudantes
                submenu = menu_secundario()
                print(f"Você escolheu {submenu}!")
                if submenu == 1:
                    listar_estudante(arquivo)
                elif submenu == 2:
                    cadastrar_estudante(arquivo)
                elif submenu == 3:
                    atualizar_estudante(arquivo)
                elif submenu == 4:
                    excluir_estudante(arquivo)
                elif submenu == 5:
                    break
                else:
                    print("Digite uma opção válida!")
        elif menu in {2, 3, 4, 5}:
            print("Em desenvolvimento.")
        elif menu == 0:  # Sair do sistema
            print("Encerrando o sistema... Até mais!")
            break
        else:  # Opção inválida no menu principal
            print("Digite uma opção válida!")
    except ValueError:
        print("Entrada inválida. Certifique-se de digitar um número.")
