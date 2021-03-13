import json
import pygal
from pygal_maps_world.maps import World
from country_codes import get_country_code

# Carrega os dados em uma lista
filename = 'Estudos/PYTHON/Python-VisualizacaoDeDados/Dados-Gráficos/Dowload_de_dados/population_data.json'

with open(filename) as f:
    pop_data = json.load(f)

# Constroi um dicinário com dados das populações.
cc_populations = {}
for pop_dict in pop_data:
    if pop_dict['Year'] == '2010':
        country = pop_dict['Country Name']
        population = int(float(pop_dict['Value']))
        code = get_country_code(country)
        if code:
            cc_populations[code] = population

w = World()
w.title = "World population in 2010, by Country"
w.add('2010', cc_populations)

w.render_to_file('Estudos/PYTHON/Python-VisualizacaoDeDados/Dados-Gráficos/Dowload_de_dados/world_population.svg')
