import pygal

from pygal_maps_world.maps import World

w = World()
w.title = 'Populations of Countries in North America'
w.add('North America', {'ca': 34126000, 'us': 30934900, 'mx': 113423000})

w.render_to_file('Estudos/PYTHON/Python-VisualizacaoDeDados/Dados-Gráficos/Dowload_de_dados/na_populations.svg')
