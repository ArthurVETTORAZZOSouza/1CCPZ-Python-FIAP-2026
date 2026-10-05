class Disciplina:
    def __init__(self, nome, professor):
        self.nome = nome
        self.professor = professor

class Aluno:
    def __init__(self, nome):
        self.nome = nome
        self.disciplinas = []
        self.notas_por_disciplina = {}

    def matricular(self, disciplina):
        if disciplina not in self.disciplinas:
            self.disciplinas.append(disciplina)
            self.notas_por_disciplina.setdefault(disciplina.nome, [])

    def adicionar_nota(self, disciplina, nota):
        if disciplina.nome not in self.notas_por_disciplina:
            self.matricular(disciplina)
        self.notas_por_disciplina[disciplina.nome].append(nota)

d1 = Disciplina('Python', 'Russi')
a1 = Aluno('Carlos')
a1.adicionar_nota(d1, 9.0)
a1.adicionar_nota(d1, 7.0)
print(len(a1.disciplinas), len(a1.notas_por_disciplina['Python']))

# PERGUNTA: Qual será a saída exibida no terminal?