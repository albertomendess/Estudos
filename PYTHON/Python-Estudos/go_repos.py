import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

# Faz uma chamada de API e armazena a resposta.
url = 'https://api.github.com/search/repositories?q=language:go&sort=stars'
r = requests.get(url)
print("Status code:", r.status_code)

# Armazena a resposta da API em uma variável.
response_dict = r.json()
print("Total repositories:", response_dict['total_count'])

# Explora informações sobre os repositórios.
repo_dicts = response_dict['items']

names, plot_dicts = [], []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])

    plot_dict = {
        'value': repo_dict['stargazers_count'],
        'label': repo_dict['description'] or '',
        'xlink': repo_dict['html_url'],
        }
    plot_dicts.append(plot_dict)

# Cria a visualização.
my_style = LS('#2E8890', base_style=LCS)

my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.title_font_size = 24
my_config.label_font_size = 14
my_config.major_label_font_size = 18
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000

chart = pygal.Bar(my_config, style=my_style)
chart.title = 'Most-Starred Go Projects on GitHub'
chart.x_labels = names

chart.add('', plot_dicts)
chart.render_to_file('Estudos/PYTHON/Python-Estudos/go_repos.svg')