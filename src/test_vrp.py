import pytest
import math

# Simulação limpa da estrutura de classes do nosso VRP para o ambiente isolado do pytest
class City:
    def __init__(self, id_local, x, y, name, demanda_caixas=0):
        self.id = id_local
        self.x = x
        self.y = y
        self.name = name
        self.demanda_caixas = demanda_caixas

    def distance(self, city):
        return math.sqrt((self.x - city.x)**2 + (self.y - city.y)**2)

class Fitness:
    def __init__(self, distancia_viagem, autonomia_maxima=25, carga_total=0, capacidade_maxima=20):
        self.distancia_viagem = distancia_viagem
        self.autonomia_maxima = autonomia_maxima
        self.carga_total = carga_total
        self.capacidade_maxima = capacidade_maxima

    def verificar_penalidades(self):
        penalidade = 0
        # Hard Constraint: Autonomia
        if self.distancia_viagem > self.autonomia_maxima:
            penalidade += 10000 * (self.distancia_viagem - self.autonomia_maxima)
        # Hard Constraint: Capacidade
        if self.carga_total > self.capacidade_maxima:
            penalidade += 100000
        return penalidade

def test_calculo_distancia_simples():
    # Testa a matemática de distância Euclidiana (Triângulo Pitagórico 3, 4, 5)
    cidade_A = City(0, 0, 0, "Hospital")
    cidade_B = City(1, 3, 4, "Unidade A")
    assert cidade_A.distance(cidade_B) == 5.0

def test_penalidade_autonomia_excedida():
    # Testa se a multa é aplicada estritamente ao passar de 25km
    fit_valido = Fitness(distancia_viagem=20)
    assert fit_valido.verificar_penalidades() == 0

    fit_invalido = Fitness(distancia_viagem=30)
    assert fit_invalido.verificar_penalidades() > 0

def test_penalidade_capacidade_excedida():
    # Testa se a multa é aplicada estritamente ao ultrapassar 20 caixas no veículo
    fit_valido = Fitness(distancia_viagem=10, carga_total=18)
    assert fit_valido.verificar_penalidades() == 0

    fit_invalido = Fitness(distancia_viagem=10, carga_total=25)
    assert fit_invalido.verificar_penalidades() >= 100000
