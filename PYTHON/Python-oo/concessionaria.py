"""Um app que mostra informações de carros de uma concessionária"""

class Carro:
    def __init__(self, nome, ano, fabricante):
        self.__nome      = nome.title()
        self.ano         = ano
        self.fabricante  = fabricante
        self.__likes     = 0
        self.__deslikes  = 0




    @property
    def nome(self):
        return self.__nome

    @property
    def likes(self):
        return self.__likes

    @property
    def deslikes(self):
        return self.__deslikes

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome.title()





    def dar_like(self):
        self.__likes += 1

    def dar_deslike(self):
        self.__deslikes += 1





carro_1 = Carro("gol", 2017, 'Volkswagen')
carro_1.dar_like()
carro_1.dar_deslike()
print(f"Carro: {carro_1.nome} \nAno: {carro_1.ano}"
    f"\nFabricante: {carro_1.fabricante}"
    f"\nLikes: {carro_1.likes} \nDeslikes: {carro_1.deslikes}\n")

carro_2 = Carro("fusca", 1997, "Volkswagen")
carro_2.dar_like()
carro_2.dar_like()
carro_2.dar_deslike()
print(f"Carro: {carro_2.nome} \nAno: {carro_2.ano}"
    f"\nFabricante: {carro_2.fabricante}"
    f"\nLikes: {carro_2.likes} \nDeslikes: {carro_2.deslikes}\n")

carro_3 = Carro("palio", 2016, "Fiat")
carro_3.dar_like()
carro_3.dar_deslike()
carro_3.dar_deslike()
print(f"Carro: {carro_3.nome} \nAno: {carro_3.ano}"
    f"\nFabricante: {carro_3.fabricante}"
    f"\nLikes: {carro_3.likes} \nDeslikes: {carro_3.deslikes}\n")