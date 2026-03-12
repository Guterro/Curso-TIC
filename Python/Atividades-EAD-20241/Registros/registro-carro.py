import numpy as np

print("ATIVIDADE 3 - CARRO\n")

class Carro:
    def __init__(self, ano, quilometragem, modelo):
        self.ano = ano
        self.quilometragem = quilometragem
        self.modelo = modelo

carro1 = Carro(2013, 50000, 'Prisma')

vetor_carros = np.empty(3, dtype=object)
vetor_carros[0] = carro1

print(f"Ano: {vetor_carros[0].ano}")
print(f"Quilometragem: {vetor_carros[0].quilometragem}")
print(f"Modelo: {vetor_carros[0].modelo}")