#Visualizing with Pygal
import pygal

from random_walk import RandonWalk


rw = RandonWalk()
rw.fill_walk()


eixo_x = list(range(rw.num_points))


# Analiza os resultados
frequencies = []
for number in (range(rw.num_points+1)):
    frequency = rw.x_values.count(number)
    frequencies.append(frequency)


# Vizualiza os resultados
hist = pygal.Bar()

hist.title = "Results of a random walk."
hist.x_labels = eixo_x
hist.x_title = "Result"
hist.y_title = "Frequency of result"

hist.add('Random', frequencies)

hist.render_to_file('PYTHON/Python-VisualizacaoDeDados/Dados-Gráficos/Random Walk/rw_visual.svg')
