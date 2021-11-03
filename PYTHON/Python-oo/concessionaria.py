"""Um app que mostra informações de carros de uma concessionária"""

class Carro:
    def __init__(self, nome, ano, fabricante):
        self.nome        = nome
        self.ano         = ano
        self. fabricante = fabricante


carro_1 = Carro("Gol", 2017, 'Volkswagen')
print(f"Carro: {carro_1.nome} \nAno: {carro_1.ano}"
    f"\nFabricante: {carro_1.fabricante}\n")

carro_2 = Carro("Fusca", 1997, "Volkswagen")
print(f"Carro: {carro_2.nome} \nAno: {carro_2.ano}"
    f"\nFabricante: {carro_2.fabricante}\n")

carro_3 = Carro("Palio", 2016, "Fiat")
print(f"Carro: {carro_3.nome} \nAno: {carro_3.ano}"
    f"\nFabricante: {carro_3.fabricante}\n")