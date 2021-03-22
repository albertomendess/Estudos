import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

def get_response():
    """Faz uma chamada de API e armazena a resposta."""
    url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
    r = requests.get(url)
    return r


def get_repo_dicts(response):
    """Armazena a resposta da API em uma variável."""
    response_dict = r.json()
    repo_dicts = response_dict['items']
    return repo_dicts


def get_names_plot_dicts(repo_dicts):
    names, plot_dicts = [], []
    for repo_dict in repo_dicts:
        names.append(repo_dict['name'])

        plot_dict = {
            'value': repo_dict['stargazers_count'],
            'label': repo_dict['description'] or "Not description provided.",
            'xlink': repo_dict['html_url'],
            }
        plot_dicts.append(plot_dict)
    return names, plot_dicts


def make_visualization(names, plot_dicts):
    """Cria a viazualização."""
    my_style = LS('#222266', base_style=LCS)

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
    chart.title = 'Most-Starred Python Projects on GitHub'
    chart.x_labels = names

    chart.add('', plot_dicts)
    chart.render_to_file('Estudos/PYTHON/Python-Estudos/python_repos.svg')

r = get_response()
repo_dicts = get_repo_dicts(r)
names, plot_dicts = get_names_plot_dicts(repo_dicts)
make_visualization(names, plot_dicts)