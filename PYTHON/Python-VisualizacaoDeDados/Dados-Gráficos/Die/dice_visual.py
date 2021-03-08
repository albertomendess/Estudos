from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die


# Cria dois dados D6.
die_1, die_2 = Die(), Die()


# Faz alguns lançamentos e armazena os resultados em uma lista.
results = [die_1.roll() + die_2.roll() for roll_num in range(1000)]


# Analiza os resultados.
max_result = die_1.num_sides + die_2.num_sides
frequencies = [results.count(value) for value in range(2, max_result+1)]


# Visualiza os resultados.
x_values = list(range(2, max_result+1))
data = [Bar(x=x_values, y=frequencies)]


x_axis_config = {'title': 'Result', 'dtick': 1}
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(title="Results of rolling two D6 dice 1000 times.",
    xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, 
    filename='PYTHON/Python-VisualizacaoDeDados/Dados-Gráficos/Die/D6_D6.html')
