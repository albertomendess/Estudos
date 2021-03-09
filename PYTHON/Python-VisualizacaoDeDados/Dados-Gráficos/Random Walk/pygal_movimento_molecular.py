#Visualizing with Pygal
import pygal

from random_walk import RandonWalk


rw = RandonWalk()
rw.fill_walk()


# Vizualiza os resultados
hist = pygal.XY()

hist.title = "Results of a random walk."
rwValues = list(zip(rw.x_values, rw.y_values))

hist.add('Random Walk', rwValues)

hist.render_to_file('PYTHON/Python-VisualizacaoDeDados/Dados-Gráficos/Random Walk/rw_visual.svg')
