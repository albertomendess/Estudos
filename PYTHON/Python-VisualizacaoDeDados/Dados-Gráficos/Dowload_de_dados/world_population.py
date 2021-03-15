import json
import pygal
from pygal_maps_world.maps import World
from pygal.style import LightColorizedStyle as LCS, RotateStyle as RS
from country_codes import get_country_code

# Carrega os dados em uma lista.
filename = 'Estudos/PYTHON/Python-VisualizacaoDeDados/Dados-Gráficos/Dowload_de_dados/population_data.json'

with open(filename) as f:
    pop_data = json.load(f)

# Constrói um dicionário com dados das populações.
cc_populations = {}
for pop_dict in pop_data:
    if pop_dict['Year'] == '2010':
        country = pop_dict['Country Name']
        population = int(float(pop_dict['Value']))
        code = get_country_code(country)
        if code:
            cc_populations[code] = population

# Agrupa os países em três níveis populacionais.
cc_pops_1, cc_pops_2, cc_pops_3 = {}, {}, {}
for cc, pop in cc_populations.items():
    if pop < 10_000_000:
        cc_pops_1[cc] = pop
    elif pop < 1_000_000_000:
        cc_pops_2[cc] = pop
    else:
        cc_pops_3[cc] = pop

# Visualiza quantos países estão em cada nível.
print(len(cc_pops_1), len(cc_pops_2), len(cc_pops_3))


w_style = RS('#109008', base_style=LCS)
w = World(style=w_style)
w.title = "World population in 2010, by Country"
w.add('0-10m', cc_pops_1)
w.add('10m-1bn', cc_pops_2)
w.add('>1bn', cc_pops_3)

w.render_to_file('Estudos/PYTHON/Python-VisualizacaoDeDados/Dados-Gráficos/Dowload_de_dados/world_population.svg')
