from classes.Curso import Curso
from classes.Campus import Campus

import sys

class SistemaUniversidade:
    def __init__(self):
        self.lista_cursos = []
        self.lista_campus = []
        self._popular_dados_teste()

    def _popular_dados_teste(self):
        c1 = Curso("Engenharia de Software", "4 anos", "Bacharelado", "Presencial")
        c2 = Curso("Design Digital", "4 anos", "Bacharelado", "Hibrido")
        camp1 = Campus("Pici", "001", "Prof. Jose", "60000-000")
        
        self.lista_cursos.extend([c1, c2])
        self.lista_campus.append(camp1)

    def _ler_inteiro(self, mensagem):
        while True:
            try:
                return int(input(mensagem))
            except ValueError:
                print("Erro: Por favor, digite um numero valido.")

    def _buscar_campus(self, codigo):
        return next((c for c in self.lista_campus if c.codigo == codigo), None)

    def iniciar(self):
        while True:
            print("\n===== SISTEMA UNIVERSITARIO =====")
            print("1. Gerenciar Cursos")
            print("2. Gerenciar Campus")
            print("3. Sair")
            
            op = input("Escolha: ")

            if op == "1":
                self.menu_cursos()
            elif op == "2":
                self.menu_campus()
            elif op == "3":
                print("Saindo do sistema...")
                sys.exit()
            else:
                print("Opcao invalida!")

    def menu_cursos(self):
        while True:
            print("\n--- GERENCIAR CURSOS ---")
            print("1. Criar novo curso")
            print("2. Atualizar curso")
            print("3. Listar todos os cursos")
            print("4. Voltar")

            op = input("Escolha: ")

            if op == "1":
                self.criar_curso()
            elif op == "2":
                self.atualizar_curso()
            elif op == "3":
                self.listar_cursos()
            elif op == "4":
                break
            else:
                print("Opcao invalida!")

    def criar_curso(self):
        print("\n--- Novo Curso ---")
        nome = input("Nome: ")
        duracao = input("Duracao: ")
        tipo = input("Tipo: ")
        modalidade = input("Modalidade: ")
        
        novo_curso = Curso(nome, duracao, tipo, modalidade)
        self.lista_cursos.append(novo_curso)
        print("Curso criado com sucesso!")

    def atualizar_curso(self):
        self.listar_cursos()
        if not self.lista_cursos:
            return

        idx = self._ler_inteiro("Digite o NUMERO do curso para atualizar: ") - 1

        if 0 <= idx < len(self.lista_cursos):
            curso = self.lista_cursos[idx]
            print(f"\nEditando '{curso.nome}' (Pressione ENTER para manter o valor atual)")
            
            curso.nome = input(f"Novo Nome [{curso.nome}]: ") or curso.nome
            curso.duracao = input(f"Nova Duracao [{curso.duracao}]: ") or curso.duracao
            curso.tipo = input(f"Novo Tipo [{curso.tipo}]: ") or curso.tipo
            curso.modalidade = input(f"Nova Modalidade [{curso.modalidade}]: ") or curso.modalidade
            
            print("Curso atualizado com sucesso!")
        else:
            print("Numero invalido.")

    def listar_cursos(self):
        print("\n--- Catalogo de Cursos ---")
        if not self.lista_cursos:
            print("Nenhum curso cadastrado.")
        for i, c in enumerate(self.lista_cursos):
            print(f"{i+1}. {c}")

    def menu_campus(self):
        while True:
            print("\n--- GERENCIAR CAMPUS ---")
            print("1. Criar campus")
            print("2. Atualizar campus")
            print("3. Listar campus")
            print("4. Adicionar curso a um campus")
            print("5. Ver cursos de um campus")
            print("6. Voltar")

            op = input("Escolha: ")

            if op == "1":
                self.criar_campus()
            elif op == "2":
                self.atualizar_campus()
            elif op == "3":
                self.listar_campus()
            elif op == "4":
                self.adicionar_curso_campus()
            elif op == "5":
                self.ver_cursos_campus()
            elif op == "6":
                break

    def criar_campus(self):
        print("\n--- Novo Campus ---")
        nome = input("Nome: ")
        codigo = input("Codigo (ID): ")
        
        if self._buscar_campus(codigo):
            print("Erro: Ja existe um campus com este codigo.")
            return

        coord = input("Coordenador: ")
        cep = input("CEP: ")
        
        campus = Campus(nome, codigo, coord, cep)
        self.lista_campus.append(campus)
        print("Campus criado!")

    def atualizar_campus(self):
        codigo = input("Digite o CODIGO do campus para atualizar: ")
        campus = self._buscar_campus(codigo)

        if not campus:
            print("Campus nao encontrado.")
            return

        print(f"\nEditando Campus '{campus.nome}' (Pressione ENTER para manter o valor atual)")
        
        campus.nome = input(f"Novo Nome [{campus.nome}]: ") or campus.nome
        campus.coordenador = input(f"Novo Coordenador [{campus.coordenador}]: ") or campus.coordenador
        campus.cep = input(f"Novo CEP [{campus.cep}]: ") or campus.cep

        print("Campus atualizado com sucesso!")

    def listar_campus(self):
        print("\n--- Lista de Campus ---")
        if not self.lista_campus:
            print("Nenhum campus cadastrado.")
        for c in self.lista_campus:
            print(c)

    def adicionar_curso_campus(self):
        if not self.lista_campus or not self.lista_cursos:
            print("E necessario ter campus e cursos cadastrados antes.")
            return

        self.listar_campus()
        codigo = input("Digite o CODIGO do campus: ")
        campus = self._buscar_campus(codigo)
        
        if not campus:
            print("Campus nao encontrado.")
            return

        self.listar_cursos()
        idx = self._ler_inteiro("Digite o NUMERO do curso para adicionar: ") - 1

        if 0 <= idx < len(self.lista_cursos):
            curso_selecionado = self.lista_cursos[idx]
            campus.adicionarCurso(curso_selecionado)
            print(f"Curso '{curso_selecionado.nome}' vinculado ao campus {campus.nome}!")
        else:
            print("Curso invalido.")

    def ver_cursos_campus(self):
        codigo = input("Digite o CODIGO do campus para visualizar: ")
        campus = self._buscar_campus(codigo)

        if not campus:
            print("Campus nao encontrado.")
            return
        
        print(f"\n--- Cursos no Campus {campus.nome} ---")
        if not campus.cursos:
            print("Nenhum curso ofertado neste campus ainda.")
        
        for c in campus.cursos:
            print(c)
