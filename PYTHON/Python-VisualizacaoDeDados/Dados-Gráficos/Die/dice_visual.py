import pygal

from die import Die

# Cria dois dados D6
die_1 = Die()
die_2 = Die()


# Faz alguns lançamentos e armazena os resultados em uma lista
results = []
for roll_num in range(1000):
    result = die_1.roll() + die_2.roll()
    results.append(result)


# Analiza os resultados
frenquencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result+1):
    frequency = results.count(value)
    frenquencies.append(frequency)


# Vizualiza os resultados
hist = pygal.Bar()


hist.title = "Results of rolling two D6 dice 1000 times."
hist.x_labels = list(range(2, 13))
hist.x_title = "Result"
hist.y_title = "Frequency of Result"


hist.add('D6 + D6', frenquencies)
hist.render_to_file('PYTHON/Python-VisualizacaoDeDados/Dados-Gráficos/Die/dice_visual.svg')
