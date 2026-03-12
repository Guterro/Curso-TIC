import numpy as np

print("\nATIVIDADE 2 - CADASTRO DE ALUNO\n")

class Aluno:
  def __init__(self, nome, matricula, mfinal):
    self.nome = nome
    self.matricula = matricula
    self.mfinal = mfinal

aluno = Aluno("", 0, 0)
vetor_alunos = np.empty(10, dtype=object)

mfinal_geral = 0

for i in range(10):
  aluno.nome = str(input("Digite o nome do Aluno(a): "))
  aluno.matricula = int(input(f"Digite a matricula de {aluno.nome}: "))
  aluno.mfinal= float(input(f"Digite a media final de {aluno.nome}: "))
  vetor_alunos[i] = aluno

  mfinal_geral += vetor_alunos[i].mfinal

  print(f"\n Aluno: {vetor_alunos[i].nome}; Matricula {vetor_alunos[i].matricula}; Média Final: {vetor_alunos[i].mfinal}\n")

print(f"A média geral da turma foi de {round(mfinal_geral/10, 2)}")