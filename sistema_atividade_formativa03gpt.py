import json

# Funções para leitura e escrita em JSON
def lista_json_escrita(lista, nome_arquivo):
    with open(nome_arquivo, "w", encoding='utf-8') as arquivo:
        json.dump(lista, arquivo, ensure_ascii=False)

def lista_json_ler(nome_arquivo):
    try:
        with open(nome_arquivo, "r", encoding='utf-8') as arquivo:
            lista = json.load(arquivo)
        return lista
    except:
        return []

# Função para exibir o menu principal
def menu_principal():
    print("Bem-vindo ao menu!")
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

# Função para exibir o menu secundário
def menu_secundario():
    print("1. Listar")
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

# Função para listar cadastros
def listar_cadastro(nome_arquivo):
    cadastros = lista_json_ler(nome_arquivo)
    if len(cadastros) == 0:
        print("Não há nenhum cadastro.")
    else:
        for cadastro in sorted(cadastros, key=lambda x: x["codigo"]):
            detalhes = [f"Código: {cadastro['codigo']}", f"Nome: {cadastro['nome']}"]
            for key in ['cpf', 'codigo_professor', 'codigo_disciplina', 'codigo_estudante']:
                if key in cadastro:
                    detalhes.append(f"{key.replace('_', ' ').title()}: {cadastro[key]}")
            print(", ".join(detalhes))

# Função para cadastrar registros genéricos
def cadastrar_registro(nome_arquivo, campos):
    try:
        cadastros = lista_json_ler(nome_arquivo)
        while True:
            novo_cadastro = {}
            for campo in campos:
                novo_cadastro[campo] = input(f"Digite o {campo.replace('_', ' ')}: ")
            novo_cadastro['codigo'] = int(novo_cadastro['codigo'])
            # Verificar se o código é único
            if any(cadastro['codigo'] == novo_cadastro['codigo'] for cadastro in cadastros):
                print(f"Código {novo_cadastro['codigo']} já existe. Tente um código diferente.")
            else:
                cadastros.append(novo_cadastro)
                lista_json_escrita(cadastros, nome_arquivo)
                print("Cadastro realizado com sucesso!")
                continuar = input("Deseja cadastrar outro registro? (s/n): ")
                if continuar.lower() == "n":
                    return
    except ValueError:
        print("Entrada inválida. Certifique-se de que o código é um número.")

# Função para atualizar cadastros
def atualizar_cadastro(nome_arquivo, campos):
    try:
        cadastros = lista_json_ler(nome_arquivo)
        codigo = int(input("Digite o código do cadastro que deseja atualizar: "))
        cadastro = next((e for e in cadastros if e['codigo'] == codigo), None)
        if cadastro:
            for campo in campos:
                valor = input(f"Digite o novo {campo.replace('_', ' ')} (ou pressione Enter para manter): ")
                if valor:
                    cadastro[campo] = valor
            lista_json_escrita(cadastros, nome_arquivo)
            print("Cadastro atualizado com sucesso!")
        else:
            print(f"Nenhum cadastro encontrado com o código {codigo}.")
    except ValueError:
        print("Entrada inválida. Certifique-se de que o código é um número.")

# Função para excluir cadastros
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

# Função para processar o menu secundário
def menu_secundario_processar(nome_arquivo, campos):
    while True:
        subopcao = menu_secundario()
        if subopcao == 1:
            listar_cadastro(nome_arquivo)
        elif subopcao == 2:
            cadastrar_registro(nome_arquivo, campos)
        elif subopcao == 3:
            atualizar_cadastro(nome_arquivo, campos)
        elif subopcao == 4:
            excluir_cadastro(nome_arquivo)
        elif subopcao == 5:
            return
        else:
            print("Digite uma opção válida!")

# Arquivos JSON para cadastros
arquivos_cadastro = {
    1: ('estudantes.json', ['codigo', 'nome', 'cpf']),
    2: ('professores.json', ['codigo', 'nome', 'cpf']),
    3: ('disciplinas.json', ['codigo', 'nome']),
    4: ('turmas.json', ['codigo', 'codigo_professor', 'codigo_disciplina']),
    5: ('matriculas.json', ['codigo', 'codigo_estudante'])
}

# Loop principal do menu
while True:
    menu = menu_principal()
    if menu in arquivos_cadastro:
        nome_arquivo, campos = arquivos_cadastro[menu]
        menu_secundario_processar(nome_arquivo, campos)
    elif menu == 0:
        print("Encerrando o sistema... Até mais!")
        break
    else:
        print("Digite uma opção válida!")
