from die import Die

import pygal

# Criando dois dados D8
die_1 = Die(8)
die_2 = Die(8)


# Faz alguns lançamentos e aarmazena os resultados em uma lista
results = []
for roll_num in range(100_000):
    result = die_1.roll() + die_2.roll()
    results.append(result)


# Analiza os resultados
frenquencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result+1):
    frenquency = results.count(value)
    frenquencies.append(frenquency)


# Vizualiza os resultados
hist = pygal.Bar()


hist.title = "Results of rolling two D6 dice 100,000 times."
hist.x_labels = [str(x) for x in range(2, max_result+1)]
hist.x_title = "Result"
hist.y_title = "Frequency of Result"


hist.add("D8 + D8", frenquencies)
hist.render_to_file('PYTHON/Python-VisualizacaoDeDados/Dados-Gráficos/Die/dice_D8_visual.svg')