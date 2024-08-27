import json
# Importa o módulo JSON para trabalhar com leitura e escrita de arquivos JSON.

def lista_json_escrita(lista, nome_arquivo):
    with open(nome_arquivo, "w", encoding='utf-8') as arquivo:
        json.dump(lista, arquivo, ensure_ascii=False)
# Função que escreve uma lista em um arquivo JSON.
# Abre o arquivo no modo de escrita ("w") com codificação UTF-8.
# Usa json.dump para salvar a lista no arquivo, desabilitando ensure_ascii para manter caracteres especiais.

def lista_json_ler(nome_arquivo):
    try:
        with open(nome_arquivo, "r", encoding='utf-8') as arquivo:
            lista = json.load(arquivo)
        return lista
    except:
        return []
# Função que lê uma lista de um arquivo JSON.
# Abre o arquivo no modo de leitura ("r") com codificação UTF-8.
# Usa json.load para carregar o conteúdo do arquivo como uma lista.
# Retorna a lista ou, em caso de erro, retorna uma lista vazia.

def menu_principal():
    # Mostrando o menu principal
    print("Bem-vindo ao menu!")
    print("1. Estudantes")
    print("2. Professores")
    print("3. Disciplinas")
    print("4. Turmas")
    print("5. Matriculas")
    print("0. Sair")
    try:
        opcao = int(input("Digite uma opção válida: "))
        return opcao
    except ValueError:
        print("Entrada inválida. Digite um número.")
        return -1
# Função que exibe o menu principal e coleta a opção do usuário.
# Tenta converter a entrada em um inteiro e a retorna.
# Em caso de erro de conversão, imprime uma mensagem de erro e retorna -1.

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
# Função que exibe o menu secundário e coleta a opção do usuário.
# Tenta converter a entrada em um inteiro e a retorna.
# Em caso de erro de conversão, imprime uma mensagem de erro e retorna -1.

def listar_cadastro(nome_arquivo):
    cadastros = lista_json_ler(nome_arquivo)
    if len(cadastros) == 0:
        print("Não há nenhum cadastro.")
    else:
        # Listando cadastro em ordem pelo código
        cadastros_ordenados = sorted(cadastros, key=lambda x: x["codigo"])
        for cadastro in cadastros_ordenados:
            detalhes = [f"Código: {cadastro['codigo']}, Nome: {cadastro['nome']}"]
            if 'cpf' in cadastro:
                detalhes.append(f"CPF: {cadastro['cpf']}")
            print(", ".join(detalhes))
# Função que lista os cadastros de um arquivo JSON.
# Carrega os cadastros do arquivo.
# Se não houver cadastros, imprime uma mensagem.
# Caso contrário, ordena os cadastros pelo código e imprime os detalhes (nome e, se existir, CPF).

def cadastrar_aluno_professor(nome_arquivo):
    try:
        while True:
            cadastros = lista_json_ler(nome_arquivo)
            codigo = int(input("Digite o código: "))
            nome = input("Digite o nome completo: ")
            cpf = input("Digite o CPF: (No formato 000.000.000-00) ")
            # Verificando se o código é único
            if any(cadastro['codigo'] == codigo for cadastro in cadastros):
                print(f"Código {codigo} já existe. Tente um código diferente.")
            else:
                cadastros.append({"codigo": codigo, "nome": nome, "cpf": cpf})
                print("Cadastro realizado com sucesso!")
                lista_json_escrita(cadastros, nome_arquivo)
                continuar = input("Deseja cadastrar outro cadastro? (s/n): ")
                if continuar.lower() == "n":
                    return
    except ValueError:
        print("Entrada inválida. Certifique-se de que o código é um número.")
# Função que cadastra alunos ou professores.
# Lê os cadastros existentes, coleta código, nome e CPF do usuário.
# Verifica se o código é único, adiciona o novo cadastro e salva.
# Pergunta se deseja cadastrar outro, repetindo o loop se necessário.
# Em caso de erro de conversão, imprime uma mensagem de erro.

def cadastrar_turma_disciplina(nome_arquivo):
    try:
        while True:
            cadastros = lista_json_ler(nome_arquivo)
            codigo = int(input("Digite o código: "))
            nome = input("Digite o nome completo: ")
            # Verificando se o código é único
            if any(cadastro['codigo'] == codigo for cadastro in cadastros):
                print(f"Código {codigo} já existe. Tente um código diferente.")
            else:
                cadastros.append({"codigo": codigo, "nome": nome})
                print("Cadastro realizado com sucesso!")
                lista_json_escrita(cadastros, nome_arquivo)
                continuar = input("Deseja cadastrar outro cadastro? (s/n): ")
                if continuar.lower() == "n":
                    return
    except ValueError:
        print("Entrada inválida. Certifique-se de que o código é um número.")
# Função que cadastra turmas ou disciplinas.
# Similar à função anterior, mas não coleta CPF.
# Realiza as mesmas verificações e procedimentos.

def atualizar_cadastro_aluno_professor(nome_arquivo):
    try:
        cadastros = lista_json_ler(nome_arquivo)
        codigo = int(input("Digite o código do cadastro que deseja atualizar: "))
        cadastro = next((e for e in cadastros if e['codigo'] == codigo), None)
        if cadastro:
            nome = input(f"Digite o novo nome para {cadastro['nome']} (ou pressione Enter para manter): ")
            cpf = input(f"Digite o novo CPF para {cadastro['cpf']} (ou pressione Enter para manter): ")
            if nome:
                cadastro['nome'] = nome
            if cpf:
                cadastro['cpf'] = cpf
            print("Cadastro atualizado com sucesso!")
            lista_json_escrita(cadastros, nome_arquivo)
        else:
            print(f"Nenhum cadastro encontrado com o código {codigo}.")
    except ValueError:
        print("Entrada inválida. Certifique-se de que o código é um número.")
# Função que atualiza cadastro de alunos ou professores.
# Lê os cadastros, coleta o código do cadastro a ser atualizado.
# Se encontrado, coleta novos valores para nome e CPF (mantendo antigos se não informados).
# Atualiza e salva os cadastros.
# Em caso de erro de conversão, imprime uma mensagem de erro.

def atualizar_cadastro_turma_disciplina(nome_arquivo):
    try:
        cadastros = lista_json_ler(nome_arquivo)
        codigo = int(input("Digite o código do cadastro que deseja atualizar: "))
        cadastro = next((e for e in cadastros if e['codigo'] == codigo), None)
        if cadastro:
            nome = input(f"Digite o novo nome para {cadastro['nome']} (ou pressione Enter para manter): ")
            if nome:
                cadastro['nome'] = nome
            print("Cadastro atualizado com sucesso!")
            lista_json_escrita(cadastros, nome_arquivo)
        else:
            print(f"Nenhum cadastro encontrado com o código {codigo}.")
    except ValueError:
        print("Entrada inválida. Certifique-se de que o código é um número.")
# Função que atualiza cadastro de turmas ou disciplinas.
# Similar à função anterior, mas não atualiza CPF, apenas nome.
# Segue os mesmos procedimentos de leitura, coleta, verificação e salvamento.

def excluir_cadastro(nome_arquivo):
    try:
        cadastros = lista_json_ler(nome_arquivo)
        codigo = int(input("Digite o código do cadastro que deseja excluir: "))
        cadastro = next((e for e in cadastros if e['codigo'] == codigo), None)
        if cadastro:
            cadastros.remove(cadastro)
            print("Cadastro excluído com sucesso!")
            lista_json_escrita(cadastros, nome_arquivo)
        else:
            print(f"Nenhum cadastro encontrado com o código {codigo}.")
    except ValueError:
        print("Entrada inválida. Certifique-se de que o código é um número.")
# Função que exclui um cadastro.
# Lê os cadastros, coleta o código do cadastro a ser excluído.
# Se encontrado, remove o cadastro da lista e salva.
# Em caso de erro de conversão, imprime uma mensagem de erro.

def menu_secundario_processar(nome_arquivo, menu):
    while True:
        subopcao = menu_secundario()
        if subopcao == 1:
            listar_cadastro(nome_arquivo)
        elif subopcao == 2:
            if menu in {1, 2}:
                cadastrar_aluno_professor(nome_arquivo)
            else:
                cadastrar_turma_disciplina(nome_arquivo)
        elif subopcao == 3:
            if menu in {1, 2}:
                atualizar_cadastro_aluno_professor(nome_arquivo)
            else:
                atualizar_cadastro_turma_disciplina(nome_arquivo)
        elif subopcao == 4:
            excluir_cadastro(nome_arquivo)
        elif subopcao == 5:
            return
        else:
            print("Digite uma opção válida!")
# Função que processa o menu secundário com base no menu principal selecionado.
# Exibe o menu secundário, coleta e processa a subopção.
# Chama funções apropriadas para listar, cadastrar, atualizar ou excluir cadastros.
# Retorna ao menu principal ao selecionar a opção 5.

# Criação dos arquivos JSON
estudantes_cadastro = 'estudantes.json'
professores_cadastro = 'professores.json'
disciplina_cadastro = 'disciplina.json'
turma_cadastro = 'turma.json'
matricula_cadastro = 'matricula.json'
# Define nomes dos arquivos JSON que armazenam cadastros de diferentes categorias.

# Entrada do loop
while True:
    menu = menu_principal()
    if menu == 1:
        menu_secundario_processar(estudantes_cadastro, menu)
    elif menu == 2:
        menu_secundario_processar(professores_cadastro, menu)
    elif menu == 3:
        menu_secundario_processar(disciplina_cadastro, menu)
    elif menu == 4:
        menu_secundario_processar(turma_cadastro, menu)
    elif menu == 5:
        menu_secundario_processar(matricula_cadastro, menu)
    elif menu == 0:
        print("Encerrando o sistema... Até mais!")
        break
    else:
        print("Digite uma opção válida!")
# Loop principal que exibe o menu principal e processa as opções selecionadas.
# Chama menu_secundario_processar com o arquivo JSON apropriado com base na opção selecionada.
# Sai do loop ao selecionar a opção 0.
