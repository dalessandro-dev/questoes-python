class Campus:
    def __init__(self, nome="", codigo="", coordenador="", cep=""):
        self.nome = nome
        self.codigo = codigo
        self.coordenador = coordenador
        self.cep = cep
        self.cursos = []

    def buscarCurso(self, nomeCurso):
        for curso in self.cursos:
            if curso.nome == nomeCurso:
                return curso
        return None

    def adicionarCurso(self, curso):
        self.cursos.append(curso)

    def listarCursos(self):
        return self.cursos

    def removerCurso(self, nomeCurso):
        for c in self.cursos:
            if c.nome == nomeCurso:
                self.cursos.remove(c)
                return True
        return False
