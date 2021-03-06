# ICREMENTANDO O VALOR DE UM ATRIBUTO COM UM MÉTODO
class Carro():
    """Uma tentativa simples de representar um carro."""
    
    def __init__(self, fabricante, modelo, ano):
        """Inicializa os atributos que descrevem um carro."""
        self.fabricante = fabricante
        self.modelo = modelo
        self.ano = ano
        self.leitura_hodometro = 0


    def nome_descritivo(self):
        """Devolve um nome descritivo, formatado de forma elegante."""
        nome_carro = str(self.ano) + " " + self.fabricante + " " + self.modelo
        return nome_carro.title()


    def ler_hodometro(self):
        """Exibe uma frase que mostra a milhagem do carro."""
        print("Esse carro têm " + str(self.leitura_hodometro) +
            " quilômetros rodados.")


    def atualizar_hodometro(self, quilometragem):
        """
        Define o valor de leitura do hodômetro com valor especificado.
        Rejeita a alteração se a tentativa de definir um valor for
        menor para o hodômetro.
        """
        if quilometragem >= self.leitura_hodometro:
            self.leitura_hodometro = quilometragem
        else:
            print("Não pode fornecer uma quilometragem menor que a atual!")


    def incrementar_hodometro(self, quilometros):
        """Soma a quantidade especificada ao valor de leitura do hodômetro."""
        self.leitura_hodometro += quilometros


meu_carro_usado = Carro(fabricante='subaru', modelo='outback', ano=2013)
print(meu_carro_usado.nome_descritivo())

meu_carro_usado.atualizar_hodometro(quilometragem=23500)
meu_carro_usado.ler_hodometro()

meu_carro_usado.incrementar_hodometro(quilometros=100)
meu_carro_usado.ler_hodometro()