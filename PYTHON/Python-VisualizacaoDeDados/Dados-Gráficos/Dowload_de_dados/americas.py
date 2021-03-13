import pygal

from pygal_maps_world.maps import World

w = World()
w.title = "North, Central and South America"

w.add('North America', ['ca', 'mx', 'us'])
w.add('Central America', ['bz', 'cr', 'gt', 'hn', 'ni', 'pa', 'sv'])
w.add('South America', ['ar', 'bo', 'br', 'cl', 'co', 'ec', 'gf', 'gy',
    'pe', 'py', 'sr', 'uy', 've'])

w.render_to_file('Estudos/PYTHON/Python-VisualizacaoDeDados/Dados-Gráficos/Dowload_de_dados/america.svg')
