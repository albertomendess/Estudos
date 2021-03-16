import json
import pygal
from pygal_maps_world.maps import World
from pygal.style import LightColorizedStyle as LCS, RotateStyle as RS
from country_codes import get_country_code

# Carrega os dados em uma lista.
filename = 'Estudos/PYTHON/Python-VisualizacaoDeDados/Dados-Gráficos/Dowload_de_dados/World_PIB.json'
with open(filename) as f:
    pop_data = json.load(f)

# Constrói um dicionário com os dados dos PIBs.
cc_pibs = {}
for pop_dict in pop_data:
    if pop_dict['Year'] == 2016:
        country_name = pop_dict['Country Name']
        country_pib = int(float(pop_dict['Value']))
        code = get_country_code(country_name)
        if code:
            cc_pibs[code] = country_pib

# Agrupando os países pelo seu PIB.
cc_pibs_1, cc_pibs_2, cc_pibs_3 = {}, {}, {}
for cc, pib in cc_pibs.items():
    if pib < 50_000_000_000:
        cc_pibs_1[cc] = pib
    elif pib < 51_000_000_000:
        cc_pibs_2[cc]: pib
    else:
        cc_pibs_3[cc] = pib

# Vizualiza quantos países estão em cada nível.
print(len(cc_pibs_1), len(cc_pibs_2), len(cc_pibs_3))


w_style = RS('#902020', base_style=LCS)
w = World(style=w_style)
w.title = 'PIB Population in 2016, by Country'
w.add('0-50bn', cc_pibs_1)
w.add('>50bn', cc_pibs_3)

w.render_to_file("Estudos/PYTHON/Python-VisualizacaoDeDados/Dados-Gráficos/Dowload_de_dados/PIB_Population.svg")
