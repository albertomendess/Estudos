import csv
from pygal_maps_world.maps import World
from country_codes import get_country_code

# Obtém o país e sua população no ano de 2019.
filename = 'Estudos/PYTHON/Python-VisualizacaoDeDados/Dados-Gráficos/Dowload_de_dados/API_SP.POP.TOTL_DS2_en_csv_v2_2106202.csv'

with open(filename) as f:
    reader = csv.reader(f)
    hearder_row = next(reader)

    countries, populations = [], []
    for row in reader:
        country = row[0]
        countries.append(country)

        try:
            population = int(row[63])
        except ValueError:
            pass
        else:
            populations.append(population)
    
# Exibe a população de cada país em 2019.
cc_populations = {}

world_population = dict(zip(countries, populations))
for name_country, num_population in world_population.items():
    code = get_country_code(name_country)
    if code:
        cc_populations[code] = num_population

world = World()
world.title = "World population in 2019, by Country"
world.add('2019', cc_populations)

world.render_to_file('Estudos/PYTHON/Python-VisualizacaoDeDados/Dados-Gráficos/Dowload_de_dados/world_population_2019.svg')