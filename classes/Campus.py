class Campus:
    def __init__(self, nome, codigo, coordenador, cep):
        self.nome = nome
        self.codigo = codigo
        self.coordenador = coordenador
        self.cep = cep
        self.cursos = []

    def adicionarCurso(self, curso):
        self.cursos.append(curso)

    def removerCurso(self, nomeCurso):
        for c in self.cursos:
            if c.nome == nomeCurso:
                self.cursos.remove(c)
                return True
        return False

    def atualizarCurso(self, nomeAntigo, nomeNovo):
        for c in self.cursos:
            if c.nome == nomeAntigo:
                c.nome = nomeNovo
                return True
        return False

    def listarCursos(self):
        return self.cursos

    def __str__(self):
        return f"Campus {self.codigo}: {self.nome} - Coordenador: {self.coordenador}, CEP: {self.cep}"