import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

my_style = LS('#333366', base_style=LCS)
chart = pygal.Bar(style=my_style, x_label_ratation=45, show_legend=False)

chart.title = 'Python Projects'
chart.x_labels = ['system-design-primer', 'public-apis', 'python-100-days']

plot_dicts = [
    {'value': 124_182, 'label': 'Description of system-design-primer.'},
    {'value': 113_365, 'label': 'Description of public-apis.'},
    {'value': 101_186, 'label': 'Description of python-100-days.'},
    ]

chart.add('', plot_dicts)
chart.render_to_file('Estudos/PYTHON/Python-Estudos/bar_descriptions.svg')
