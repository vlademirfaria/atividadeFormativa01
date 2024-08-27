import json


def lista_json_escrita(lista, nome_arquivo):
    with open(nome_arquivo, "w", encoding='utf-8') as arquivo:
        json.dump(lista, arquivo, ensure_ascii=False, indent=4)


def lista_json_ler(nome_arquivo):
    try:
        with open(nome_arquivo, "r", encoding='utf-8') as arquivo:
            lista = json.load(arquivo)
        return lista
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print(f"Erro ao ler o arquivo {nome_arquivo}. O arquivo pode estar corrompido.")
        return []


def menu_principal():
    print("\nBem-vindo ao menu!")
    print("1. Estudantes")
    print("2. Professores")
    print("3. Disciplinas")
    print("4. Turmas")
    print("5. Matrículas")
    print("0. Sair")
    try:
        opcao = int(input("Digite uma opção válida: "))
        return opcao
    except ValueError:
        print("Entrada inválida. Digite um número.")
        return -1


def menu_secundario():
    print("\n1. Listar")
    print("2. Cadastrar")
    print("3. Atualizar cadastro")
    print("4. Excluir cadastro")
    print("5. Voltar ao menu inicial")
    try:
        subopcao = int(input("Escolha uma opção: "))
        return subopcao
    except ValueError:
        print("Entrada inválida. Digite um número.")
        return -1


def listar_cadastro(nome_arquivo):
    cadastros = lista_json_ler(nome_arquivo)
    if len(cadastros) == 0:
        print("Não há nenhum cadastro.")
    else:
        cadastros_ordenados = sorted(cadastros, key=lambda x: x["codigo"])
        for cadastro in cadastros_ordenados:
            detalhes = [f"Código: {cadastro['codigo']}, Nome: {cadastro['nome']}"]
            if 'cpf' in cadastro:
                detalhes.append(f"CPF: {cadastro['cpf']}")
            print(", ".join(detalhes))


def cadastrar(nome_arquivo, campos_adicionais=None):
    while True:
        cadastros = lista_json_ler(nome_arquivo)
        try:
            codigo = int(input("Digite o código: "))
            if any(cadastro['codigo'] == codigo for cadastro in cadastros):
                print(f"Código {codigo} já existe. Tente um código diferente.")
                continue
            nome = input("Digite o nome completo: ")
            dados = {"codigo": codigo, "nome": nome}
            if campos_adicionais:
                for campo in campos_adicionais:
                    dados[campo] = input(f"Digite o {campo}: ")
            cadastros.append(dados)
            lista_json_escrita(cadastros, nome_arquivo)
            print("Cadastro realizado com sucesso!")
            continuar = input("Deseja realizar outro cadastro? (s/n): ")
            if continuar.lower() == "n":
                return
        except ValueError:
            print("Entrada inválida. Certifique-se de que o código é um número.")


def atualizar_cadastro(nome_arquivo, campos_adicionais=None):
    try:
        cadastros = lista_json_ler(nome_arquivo)
        codigo = int(input("Digite o código do cadastro que deseja atualizar: "))
        cadastro = next((e for e in cadastros if e['codigo'] == codigo), None)
        if cadastro:
            nome = input(f"Digite o novo nome para {cadastro['nome']} (ou pressione Enter para manter): ")
            if nome:
                cadastro['nome'] = nome
            if campos_adicionais:
                for campo in campos_adicionais:
                    valor = input(f"Digite o novo {campo} para {cadastro.get(campo, '')} (ou pressione Enter para manter): ")
                    if valor:
                        cadastro[campo] = valor
            print("Cadastro atualizado com sucesso!")
            lista_json_escrita(cadastros, nome_arquivo)
        else:
            print(f"Nenhum cadastro encontrado com o código {codigo}.")
    except ValueError:
        print("Entrada inválida. Certifique-se de que o código é um número.")


def excluir_cadastro(nome_arquivo):
    try:
        cadastros = lista_json_ler(nome_arquivo)
        codigo = int(input("Digite o código do cadastro que deseja excluir: "))
        cadastro = next((e for e in cadastros if e['codigo'] == codigo), None)
        if cadastro:
            cadastros.remove(cadastro)
            lista_json_escrita(cadastros, nome_arquivo)
            print("Cadastro excluído com sucesso!")
        else:
            print(f"Nenhum cadastro encontrado com o código {codigo}.")
    except ValueError:
        print("Entrada inválida. Certifique-se de que o código é um número.")


def menu_secundario_processar(arquivo_cadastro, tipo_cadastro):
    campos_adicionais = ["cpf"] if tipo_cadastro in {1, 2} else None
    while True:
        subopcao = menu_secundario()
        if subopcao == 1:
            listar_cadastro(arquivo_cadastro)
        elif subopcao == 2:
            cadastrar(arquivo_cadastro, campos_adicionais)
        elif subopcao == 3:
            atualizar_cadastro(arquivo_cadastro, campos_adicionais)
        elif subopcao == 4:
            excluir_cadastro(arquivo_cadastro)
        elif subopcao == 5:
            return
        else:
            print("Digite uma opção válida!")


# Criação dos arquivos JSON
estudantes_cadastro = 'estudantes.json'
professores_cadastro = 'professores.json'
disciplina_cadastro = 'disciplina.json'
turma_cadastro = 'turma.json'
matricula_cadastro = 'matricula.json'

# Entrada do loop
while True:
    opcao_menu_principal = menu_principal()
    if opcao_menu_principal == 1:
        menu_secundario_processar(estudantes_cadastro, opcao_menu_principal)
    elif opcao_menu_principal == 2:
        menu_secundario_processar(professores_cadastro, opcao_menu_principal)
    elif opcao_menu_principal == 3:
        menu_secundario_processar(disciplina_cadastro, opcao_menu_principal)
    elif opcao_menu_principal == 4:
        menu_secundario_processar(turma_cadastro, opcao_menu_principal)
    elif opcao_menu_principal == 5:
        menu_secundario_processar(matricula_cadastro, opcao_menu_principal)
    elif opcao_menu_principal == 0:
        print("Encerrando o sistema... Até mais!")
        break
    else:
        print("Digite uma opção válida!")
