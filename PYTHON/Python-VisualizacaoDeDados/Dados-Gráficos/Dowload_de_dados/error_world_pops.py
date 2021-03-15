import json

from country_codes import get_country_code

# Carrega os dados em uma lista.
file_name = 'Estudos/PYTHON/Python-VisualizacaoDeDados/Dados-Gráficos/Dowload_de_dados/population_data.json'

with open(file_name) as f:
    pop_data = json.load(f)

# Exibe os dados que deram erro de busca.
for pop_dict in pop_data:
    if pop_dict['Year'] == '2010':
        country_name = pop_dict['Country Name']
        population = int(float(pop_dict['Value']))
        code = get_country_code(country_name)
        if code:
            continue
        else:
            print(country_name)