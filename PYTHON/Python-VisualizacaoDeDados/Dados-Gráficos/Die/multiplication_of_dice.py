import pygal

from die import Die

# Cria dois dados D6
die_1 = Die()
die_2 = Die()


# Faz alguns lançamentos e armazena os reesultados em uma lista
results = []
for roll_num in range(100_000):
    result = die_1.roll() * die_2.roll()
    results.append(result)


# Analiza os resultados
frequencies = []
max_result = die_1.num_sides * die_2.num_sides
for value in range(1, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)


# Vizualiza os resultados
hist = pygal.Bar()


hist.title = "Results of a multiplication of two D6 100 thousand times."
hist.x_labels = [str(x) for x in range(1, max_result+1)]
hist.x_title = "Result"
hist.y_title = "Frequency of Result"


hist.add('D6 x D6', frequencies)
hist.render_to_file('PYTHON/Python-VisualizacaoDeDados/Dados-Gráficos/Die/multiplication_of_dice.svg')
