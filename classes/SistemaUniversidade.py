from classes.Curso import Curso
from classes.Campus import Campus
from classes.Ufc import UFC

import sys

class SistemaUniversidade:
    def __init__(self):
        self.ufc = UFC()
        self._popular_dados_teste()

    def _popular_dados_teste(self):
        """Popula o sistema com dados de teste"""
        c1 = Curso("Engenharia de Software", "4 anos", "Bacharelado", "Presencial")
        c2 = Curso("Design Digital", "4 anos", "Bacharelado", "Hibrido")
        campus = Campus("Pici", "001", "Prof. Jose", "60000-000")
        campus.adicionarCurso(c1)
        campus.adicionarCurso(c2)
        self.ufc.criarCampus(campus)

    def _buscar_campus(self, codigo):
        """Busca um campus pelo código"""
        return self.ufc.buscarCampus(codigo)

    def iniciar(self):
        """Inicia o sistema com o menu principal"""
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
        """Menu de gerenciamento de cursos"""
        while True:
            print("\n--- GERENCIAR CURSOS ---")
            print("1. Criar novo curso em um campus")
            print("2. Atualizar curso")
            print("3. Listar todos os cursos (de todos os campus)")
            print("4. Remover curso de um campus")
            print("5. Voltar")

            op = input("Escolha: ")

            if op == "1":
                self.criar_curso()
            elif op == "2":
                self.atualizar_curso()
            elif op == "3":
                self.listar_todos_cursos()
            elif op == "4":
                self.remover_curso()
            elif op == "5":
                break
            else:
                print("Opcao invalida!")

    def criar_curso(self):
        """Cria um novo curso e adiciona a um campus"""
        print("\n--- Novo Curso ---")
        
        campus_lista = self.ufc.listarCampus()
        if not campus_lista:
            print("Erro: Nenhum campus cadastrado. Crie um campus primeiro.")
            return
        
        print("\nCampus disponíveis:")
        for c in campus_lista:
            print(f"  {c.codigo} - {c.nome}")
        
        codigo_campus = input("\nCódigo do Campus: ")
        campus = self._buscar_campus(codigo_campus)
        
        if not campus:
            print("Erro: Campus não encontrado.")
            return
        
        nome = input("Nome do curso: ")
        duracao = input("Duração: ")
        tipo = input("Tipo: ")
        modalidade = input("Modalidade: ")
        
        novo_curso = Curso(nome, duracao, tipo, modalidade)
        
        if campus.adicionarCurso(novo_curso):
            print(f"Curso '{nome}' criado e adicionado ao campus {campus.nome} com sucesso!")
        else:
            print("Erro ao adicionar curso.")

    def atualizar_curso(self):
        """Atualiza as informações de um curso existente"""
        print("\n--- Atualizar Curso ---")
        
        # Lista os campus disponíveis
        campus_lista = self.ufc.listarCampus()
        if not campus_lista:
            print("Erro: Nenhum campus cadastrado.")
            return
        
        print("\nCampus disponíveis:")
        for c in campus_lista:
            print(f"  {c.codigo} - {c.nome}")
        
        codigo_campus = input("\nCódigo do Campus onde está o curso: ")
        campus = self._buscar_campus(codigo_campus)
        
        if not campus:
            print("Erro: Campus não encontrado.")
            return
        
        if not campus.listarCursos():
            print("Este campus não possui cursos cadastrados.")
            return
        
        print(f"\nCursos no campus {campus.nome}:")
        for curso in campus.listarCursos():
            print(f"  - {curso.nome}")
        
        nome_curso = input("\nDigite o nome do curso para atualizar: ")
        curso = campus.buscarCurso(nome_curso)
        
        if not curso:
            print("Curso não encontrado neste campus.")
            return
        
        print(f"\nEditando '{curso.nome}' (Pressione ENTER para manter o valor atual)")
        
        novo_nome = input(f"Novo Nome [{curso.nome}]: ") or curso.nome
        nova_duracao = input(f"Nova Duração [{curso.duracao}]: ") or curso.duracao
        novo_tipo = input(f"Novo Tipo [{curso.tipo}]: ") or curso.tipo
        nova_modalidade = input(f"Nova Modalidade [{curso.modalidade}]: ") or curso.modalidade
        
        curso.nome = novo_nome
        curso.duracao = nova_duracao
        curso.tipo = novo_tipo
        curso.modalidade = nova_modalidade
        
        print("Curso atualizado com sucesso!")

    def remover_curso(self):
        """Remove um curso de um campus"""
        print("\n--- Remover Curso ---")
        
        campus_lista = self.ufc.listarCampus()
        if not campus_lista:
            print("Erro: Nenhum campus cadastrado.")
            return
        
        print("\nCampus disponíveis:")
        for c in campus_lista:
            print(f"  {c.codigo} - {c.nome}")
        
        codigo_campus = input("\nCódigo do Campus: ")
        campus = self._buscar_campus(codigo_campus)
        
        if not campus:
            print("Erro: Campus não encontrado.")
            return
        
        if not campus.listarCursos():
            print("Este campus não possui cursos cadastrados.")
            return
        
        print(f"\nCursos no campus {campus.nome}:")
        for curso in campus.listarCursos():
            print(f"  - {curso.nome}")
        
        nome_curso = input("\nDigite o nome do curso para remover: ")
        
        if campus.removerCurso(nome_curso):
            print(f"Curso '{nome_curso}' removido com sucesso!")
        else:
            print("Curso não encontrado.")

    def listar_todos_cursos(self):
        """Lista todos os cursos de todos os campus"""
        print("\n--- Lista de Todos os Cursos ---")
        campus_lista = self.ufc.listarCampus()
        
        if not campus_lista:
            print("Nenhum campus cadastrado.")
            return
        
        tem_cursos = False
        for campus in campus_lista:
            cursos = campus.listarCursos()
            if cursos:
                tem_cursos = True
                print(f"\n{campus.nome} (Código: {campus.codigo}):")
                for curso in cursos:
                    print(f"  - {curso}")
        
        if not tem_cursos:
            print("Nenhum curso cadastrado em nenhum campus.")

    def menu_campus(self):
        """Menu de gerenciamento de campus"""
        while True:
            print("\n--- GERENCIAR CAMPUS ---")
            print("1. Criar campus")
            print("2. Atualizar campus")
            print("3. Listar campus")
            print("4. Ver cursos de um campus")
            print("5. Remover campus")
            print("6. Voltar")

            op = input("Escolha: ")

            if op == "1":
                self.criar_campus()
            elif op == "2":
                self.atualizar_campus()
            elif op == "3":
                self.listar_campus()
            elif op == "4":
                self.ver_cursos_campus()
            elif op == "5":
                self.remover_campus()
            elif op == "6":
                break
            else:
                print("Opcao invalida!")

    def criar_campus(self):
        """Cria um novo campus"""
        print("\n--- Novo Campus ---")
        nome = input("Nome: ")
        codigo = input("Código (ID): ")
        
        if self._buscar_campus(codigo):
            print("Erro: Já existe um campus com este código.")
            return

        coord = input("Coordenador: ")
        cep = input("CEP: ")
        
        campus = Campus(nome, codigo, coord, cep)
        if self.ufc.criarCampus(campus):
            print("Campus criado com sucesso!")

    def atualizar_campus(self):
        """Atualiza as informações de um campus"""
        print("\n--- Atualizar Campus ---")
        
        campus_lista = self.ufc.listarCampus()
        if not campus_lista:
            print("Nenhum campus cadastrado.")
            return
        
        print("\nCampus disponíveis:")
        for c in campus_lista:
            print(f"  {c.codigo} - {c.nome}")
        
        codigo = input("\nDigite o CÓDIGO do campus para atualizar: ")
        campus = self._buscar_campus(codigo)

        if not campus:
            print("Campus não encontrado.")
            return

        print(f"\nEditando Campus '{campus.nome}' (Pressione ENTER para manter o valor atual)")
        
        campus.nome = input(f"Novo Nome [{campus.nome}]: ") or campus.nome
        campus.coordenador = input(f"Novo Coordenador [{campus.coordenador}]: ") or campus.coordenador
        campus.cep = input(f"Novo CEP [{campus.cep}]: ") or campus.cep

        if self.ufc.atualizarCampus(campus):
            print("Campus atualizado com sucesso!")
        else:
            print("Erro ao atualizar campus.")

    def remover_campus(self):
        """Remove um campus"""
        print("\n--- Remover Campus ---")
        
        campus_lista = self.ufc.listarCampus()
        if not campus_lista:
            print("Nenhum campus cadastrado.")
            return
        
        print("\nCampus disponíveis:")
        for c in campus_lista:
            print(f"  {c.codigo} - {c.nome}")
        
        codigo = input("\nDigite o CÓDIGO do campus para remover: ")
        campus = self._buscar_campus(codigo)
        
        if not campus:
            print("Campus não encontrado.")
            return
        
        confirmacao = input(f"Tem certeza que deseja remover o campus '{campus.nome}'? (s/n): ")
        
        if confirmacao.lower() == 's':
            if self.ufc.removerCampus(codigo):
                print(f"Campus '{campus.nome}' removido com sucesso!")
        else:
            print("Operação cancelada.")

    def listar_campus(self):
        """Lista todos os campus"""
        print("\n--- Lista de Campus ---")
        campus_lista = self.ufc.listarCampus()
        
        if not campus_lista:
            print("Nenhum campus cadastrado.")
            return
        
        for c in campus_lista:
            print(f"  {c.codigo} - {c.nome}")
            if c.listarCursos():
                print(f"  Cursos: {len(c.listarCursos())}")

    def ver_cursos_campus(self):
        """Visualiza os cursos de um campus específico"""
        print("\n--- Ver Cursos de um Campus ---")
        
        campus_lista = self.ufc.listarCampus()
        if not campus_lista:
            print("Nenhum campus cadastrado.")
            return
        
        print("\nCampus disponíveis:")
        for c in campus_lista:
            print(f"  {c.codigo} - {c.nome}")
        
        codigo = input("\nDigite o CÓDIGO do campus para visualizar: ")
        campus = self._buscar_campus(codigo)

        if not campus:
            print("Campus não encontrado.")
            return
        
        print(f"\n--- Cursos no Campus {campus.nome} ---")
        cursos = campus.listarCursos()
        
        if not cursos:
            print("Nenhum curso ofertado neste campus ainda.")
        else:
            for curso in cursos:
                print(f"  - {curso}")