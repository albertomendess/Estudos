from random import choice

class RandonWalk():
    """Uma classe para gerar passeios aleatórios."""

    def __init__(self, num_points=100):
        """Inicia os atributos de um passeio."""
        self.num_points = num_points
        
        # Todos os passeios começam em (0, 0)
        self.x_values = [0]
        self.y_values = [0]


    def get_step(self):
        """Decide a direção a ser seguida e a distância a ser
        percorrida."""
        direction = choice([1, -1])
        distance = choice([0, 1, 2, 3, 4])
        step = direction * distance
        return step


    def fill_walk(self):
        """Calcula todos os pontos do passeio."""

        # Continua dando passos até que o passeio alcance o tamanho
        #desejado
        while len(self.x_values) < self.num_points:

            # Decide a direção e a distância a ser percorrida.
            x_step = self.get_step()
            y_step = self.get_step()

            # Rejeita movimentos que não vão a lugar nenhum.
            if x_step == 0 and y_step == 0:
                continue

            # Calcula os próximos valores de x e de y.
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)
