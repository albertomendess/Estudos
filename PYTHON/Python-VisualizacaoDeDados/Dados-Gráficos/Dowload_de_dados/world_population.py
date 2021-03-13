import json

from country_codes import get_country_code

# Carrega os dados em uma lista
filename = 'Estudos/PYTHON/Python-VisualizacaoDeDados/Dados-Gráficos/Dowload_de_dados/population_data.json'

with open(filename) as f:
    pop_data = json.load(f)

# Exibe a população de cada país em 2010.
for pop_dict in pop_data:
    if pop_dict['Year'] == '2010':
        country_name = pop_dict['Country Name']
        population = int(float(pop_dict['Value']))
        print(country_name + ": " + str(population))
        code = get_country_code(country_name)
        if code:
            print(f"{code} : {str(population)}")
        else:
            print(f"ERROR - {country_name}")