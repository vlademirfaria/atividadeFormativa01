import json

def lista_json_escrita(lista, nome_arquivo):
    with open(nome_arquivo, "w") as arquivo:
        json.dump(lista, arquivo, indent=4)  # Adicionei indentação para melhor legibilidade

def lista_json_ler(nome_arquivo):
    try:
        with open(nome_arquivo) as arquivo:
            lista = json.load(arquivo)
        return lista
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("Erro ao ler o arquivo JSON. O arquivo está vazio ou corrompido.")
        return []

def menu_principal():
    print("\nBem-vindo ao menu!")
    print("1. Estudantes")
    print("2. Professores")
    print("3. Disciplinas")
    print("4. Turmas")
    print("5. Matriculas")
    print("0. Sair")
    while True:
        try:
            opcao = int(input("Digite uma opção válida: "))
            if opcao in {0, 1, 2, 3, 4, 5}:
                return opcao
            else:
                print("Opção inválida. Digite um número entre 0 e 5.")
        except ValueError:
            print("Entrada inválida. Digite um número.")

def menu_secundario():
    print("1. Listar")
    print("2. Cadastrar")
    print("3. Atualizar cadastro")
    print("4. Excluir cadastro")
    print("5. Voltar ao menu inicial")
    while True:
        try:
            subopcao = int(input("Escolha uma opção: "))
            if subopcao in {1, 2, 3, 4, 5}:
                return subopcao
            else:
                print("Opção inválida. Digite um número entre 1 e 5.")
        except ValueError:
            print("Entrada inválida. Digite um número.")

def listar_estudante(nome_arquivo):
    estudantes = lista_json_ler(nome_arquivo)
    if len(estudantes) == 0:
        print("Não há estudantes cadastrados.")
    else:
        estudantes_ordenados = sorted(estudantes, key=lambda x: x["codigo"])
        for estudante in estudantes_ordenados:
            print(f"Código: {estudante['codigo']}, Nome: {estudante['nome']}, CPF: {estudante['cpf']}")

def cadastrar_estudante(nome_arquivo):
    try:
        while True:
            estudantes = lista_json_ler(nome_arquivo)
            codigo = int(input("Digite o código do estudante: "))
            nome = input("Digite o nome completo do estudante: ")
            cpf = input("Digite o CPF do estudante (no formato 000.000.000-00): ")

            if any(estudante['codigo'] == codigo for estudante in estudantes):
                print(f"Código {codigo} já existe. Tente um código diferente.")
            else:
                estudantes.append({"codigo": codigo, "nome": nome, "cpf": cpf})
                lista_json_escrita(estudantes, nome_arquivo)
                print("Estudante cadastrado com sucesso!") 
                
                continuar = input("Deseja cadastrar outro estudante? (s/n): ").strip().lower()
                if continuar == "n":
                    return None
    except ValueError:
        print("Entrada inválida. Certifique-se de que o código é um número.")

def atualizar_estudante(nome_arquivo):
    try:
        estudantes = lista_json_ler(nome_arquivo)
        codigo = int(input("Digite o código do estudante que deseja atualizar: "))
        estudante = next((e for e in estudantes if e['codigo'] == codigo), None)
        if estudante:
            nome = input(f"Digite o novo nome para {estudante['nome']} (ou pressione Enter para manter): ")
            cpf = input(f"Digite o novo CPF para {estudante['cpf']} (ou pressione Enter para manter): ")
            if nome:
                estudante['nome'] = nome
            if cpf:
                estudante['cpf'] = cpf
            lista_json_escrita(estudantes, nome_arquivo)
            print("Cadastro atualizado com sucesso!")
        else:
            print(f"Nenhum estudante encontrado com o código {codigo}.")
    except ValueError:
        print("Entrada inválida. Certifique-se de que o código é um número.")

def excluir_estudante(nome_arquivo):
    try:
        estudantes = lista_json_ler(nome_arquivo)
        codigo = int(input("Digite o código do estudante que deseja excluir: "))
        estudante = next((e for e in estudantes if e['codigo'] == codigo), None)
        if estudante:
            estudantes.remove(estudante)
            lista_json_escrita(estudantes, nome_arquivo)
            print("Estudante excluído com sucesso!")
        else:
            print(f"Nenhum estudante encontrado com o código {codigo}.")
    except ValueError:
        print("Entrada inválida. Certifique-se de que o código é um número.")

# Criação do arquivo Json
arquivo = 'estudantes.json'
while True:
    menu = menu_principal()
    if menu == 1:
        while True:
            print("\nMenu de estudantes")
            submenu = menu_secundario()
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
    elif menu in {2, 3, 4, 5}:
        print("Em desenvolvimento.")
    elif menu == 0:
        print("Encerrando o sistema... Até mais!")
        break
