class Filme:
    def __init__(self, nome, ano, duracao):
        self.__likes = 0
        self.__nome  = nome.title()
        self.ano     = ano
        self.duracao = duracao



    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome.title()

    @property
    def likes(self):
        return self.__likes

    def dar_like(self):
        self.__likes += 1





class Serie:
    def __init__(self, nome, ano, temporadas):
        self.__likes    = 0
        self.__nome     = nome.title()
        self.ano        = ano
        self.temporadas = temporadas



    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome.title()

    @property
    def likes(self):
        return self.__likes




    def dar_like(self):
        self.__likes += 1





vingadores = Filme('vingadores - guerra infinita', 2018, 160)
vingadores.dar_like()
print(f"Nome: {vingadores.nome} \nAno: {vingadores.ano}"
    f"\nDuração: {vingadores.duracao} \nLikes: {vingadores.likes}\n")

atlanta = Serie("atlanta", 2018, 2)
atlanta.dar_like()
atlanta.dar_like()
print(f"Nome: {atlanta.nome} \nAno: {atlanta.ano} "
    f"\nTemporadas: {atlanta.temporadas} \nLikes: {atlanta.likes}\n")