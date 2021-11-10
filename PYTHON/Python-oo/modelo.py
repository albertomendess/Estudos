class Filme:
    def __init__(self, nome, ano, duracao):
        self.nome    = nome.title()
        self.ano     = ano
        self.duracao = duracao
        self.likes   = 0

    def dar_like(self):
        self.likes += 1


class Serie:
    def __init__(self, nome, ano, temporadas):
        self.nome       = nome.title()
        self.ano        = ano
        self.temporadas = temporadas
        self.likes      = 0

    def dar_like(self):
        self.likes += 1

vingadores = Filme('vingadores - guerra infinita', 2018, 160)
vingadores.dar_like()
print(f"Nome: {vingadores.nome} \nAno: {vingadores.ano}"
    f"\nDuração: {vingadores.duracao} \nLikes: {vingadores.likes}\n")

atlanta = Serie("atlanta", 2018, 2)
atlanta.nome = "atlanda"
atlanta.dar_like()
atlanta.dar_like()
print(f"Nome: {atlanta.nome} \nAno: {atlanta.ano} "
    f"\nTemporadas: {atlanta.temporadas} \nLikes: {atlanta.likes}\n")