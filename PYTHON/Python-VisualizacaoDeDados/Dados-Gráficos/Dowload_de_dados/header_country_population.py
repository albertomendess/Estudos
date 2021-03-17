import csv

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
            None
        else:
            populations.append(population)
    
# Exibe a população de cada país em 2019.
world_population = dict(zip(countries, populations))

for name_country, num_population in world_population.items():
    print(f"{name_country}: {str(num_population)}")