from classes.Curso import Curso
from classes.Campus import Campus

lista_cursos = []
lista_campus = []

def menu_cursos():
    while True:
        print("""
===== GERENCIAR CURSOS =====
1. Criar curso
2. Atualizar curso
3. Remover curso
4. Listar cursos
5. Voltar
""")

        op = input("Escolha: ")

        if op == "1":
            criar_curso()
        elif op == "2":
            atualizar_curso()
        elif op == "3":
            remover_curso()
        elif op == "4":
            listar_cursos()
        elif op == "5":
            break
        else:
            print("Opção inválida!\n")


def criar_curso():
    nome = input("Nome do curso: ")
    duracao = input("Duração: ")
    tipo = input("Tipo: ")
    modalidade = input("Modalidade: ")

    curso = Curso(nome, duracao, tipo, modalidade)
    lista_cursos.append(curso)

    print("✔ Curso criado com sucesso!\n")


def atualizar_curso():
    nome = input("Nome do curso que deseja atualizar: ")

    curso = next((c for c in lista_cursos if c.nome == nome), None)

    if not curso:
        print("❌ Curso não encontrado!\n")
        return

    novo_nome = input("Novo nome do curso: ")
    curso.nome = novo_nome

    print("✔ Curso atualizado!\n")


def remover_curso():
    nome = input("Nome do curso para remover: ")

    curso = next((c for c in lista_cursos if c.nome == nome), None)

    if not curso:
        print("❌ Curso não encontrado!\n")
        return

    lista_cursos.remove(curso)
    print("✔ Curso removido!\n")


def listar_cursos():
    print("\n--- LISTA DE CURSOS ---")
    if not lista_cursos:
        print("Nenhum curso cadastrado.\n")
        return

    for c in lista_cursos:
        print(c)
    print()

def menu_campus():
    while True:
        print("""
===== GERENCIAR CAMPUS =====
1. Criar campus
2. Atualizar campus
3. Remover campus
4. Listar campus
5. Adicionar curso ao campus
6. Remover curso do campus
7. Listar cursos do campus
8. Voltar
""")

        op = input("Escolha: ")

        if op == "1":
            criar_campus()
        elif op == "2":
            atualizar_campus()
        elif op == "3":
            remover_campus()
        elif op == "4":
            listar_campus()
        elif op == "5":
            adicionar_curso_ao_campus()
        elif op == "6":
            remover_curso_do_campus()
        elif op == "7":
            listar_cursos_do_campus()
        elif op == "8":
            break
        else:
            print("Opção inválida!\n")


def criar_campus():
    nome = input("Nome do campus: ")
    codigo = input("Código: ")
    coordenador = input("Coordenador: ")
    cep = input("CEP: ")

    campus = Campus(nome, codigo, coordenador, cep)
    lista_campus.append(campus)

    print("✔ Campus criado!\n")


def atualizar_campus():
    codigo = input("Código do campus para atualizar: ")

    campus = next((c for c in lista_campus if c.codigo == codigo), None)

    if not campus:
        print("❌ Campus não encontrado!\n")
        return

    novo_nome = input("Novo nome: ")
    campus.nome = novo_nome

    print("✔ Campus atualizado!\n")


def remover_campus():
    codigo = input("Código do campus para remover: ")

    campus = next((c for c in lista_campus if c.codigo == codigo), None)

    if not campus:
        print("❌ Campus não encontrado!\n")
        return

    lista_campus.remove(campus)
    print("✔ Campus removido!\n")


def listar_campus():
    print("\n--- LISTA DE CAMPUS ---")
    if not lista_campus:
        print("Nenhum campus cadastrado.\n")
        return

    for c in lista_campus:
        print(c)
    print()


def adicionar_curso_ao_campus():
    if not lista_campus:
        print("Não há campus cadastrados!\n")
        return
    if not lista_cursos:
        print("Não há cursos cadastrados!\n")
        return

    codigo = input("Código do campus: ")
    campus = next((c for c in lista_campus if c.codigo == codigo), None)

    if not campus:
        print("❌ Campus não encontrado!\n")
        return

    print("\n--- CURSOS DISPONÍVEIS ---")
    for i, curso in enumerate(lista_cursos):
        print(f"{i+1}. {curso.nome}")

    escolha = int(input("Escolha o número do curso: ")) - 1

    if escolha < 0 or escolha >= len(lista_cursos):
        print("❌ Curso inválido!\n")
        return

    campus.adicionarCurso(lista_cursos[escolha])
    print("✔ Curso adicionado ao campus!\n")


def remover_curso_do_campus():
    codigo = input("Código do campus: ")
    campus = next((c for c in lista_campus if c.codigo == codigo), None)

    if not campus:
        print("❌ Campus não encontrado!\n")
        return

    if not campus.cursos:
        print("Esse campus não possui cursos.\n")
        return

    print("\n--- CURSOS DO CAMPUS ---")
    for i, curso in enumerate(campus.cursos):
        print(f"{i+1}. {curso.nome}")

    escolha = int(input("Escolha qual remover: ")) - 1

    if escolha < 0 or escolha >= len(campus.cursos):
        print("❌ Número inválido!\n")
        return

    removido = campus.cursos.pop(escolha)
    print(f"✔ Curso '{removido.nome}' removido!\n")


def listar_cursos_do_campus():
    codigo = input("Código do campus: ")
    campus = next((c for c in lista_campus if c.codigo == codigo), None)

    if not campus:
        print("❌ Campus não encontrado!\n")
        return

    print(f"\n--- CURSOS DO CAMPUS {campus.nome} ---")
    if not campus.cursos:
        print("Nenhum curso associado.\n")
        return

    for c in campus.cursos:
        print(c)
    print()

def menu_principal():
    while True:
        print("""
===== SISTEMA UNIVERSITÁRIO =====
1. Gerenciar Cursos
2. Gerenciar Campus
3. Sair
""")

        op = input("Escolha: ")

        if op == "1":
            menu_cursos()
        elif op == "2":
            menu_campus()
        elif op == "3":
            print("saindo...")
            break
        else:
            print("Opção inválida!\n")

menu_principal()
