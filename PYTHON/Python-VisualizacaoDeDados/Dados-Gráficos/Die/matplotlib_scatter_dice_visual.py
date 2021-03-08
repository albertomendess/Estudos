from die import Die

import matplotlib.pyplot as plt


# Criando dois dados D6
die_1 = Die()
die_2 = Die()

attempts = 10_000
x_results = range(2, 13)


# Faz alguns lançamentos e armazena os resultados em uma lista
results = []
for roll_num in range(attempts):
    result = die_1.roll() + die_2.roll()
    results.append(result)


# Analiza os resultados
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)


# Criando o Eixo_x e o Eixo_y
plt.scatter(x_results, frequencies,
    c=frequencies,
    cmap=plt.cm.get_cmap("plasma"),
    edgecolor='none',
    s=100)


# Define o título do gráfico e nomeia os eixos
plt.title("Results of rolling tow D6 dice " + str(attempts) + " times.", 
    fontsize=24)
plt.xlabel("Result", fontsize=14)
plt.ylabel("Frequency of Result")


# Define o tamanho dos rótulos das marcações
plt.tick_params(axis='both', labelsize=14)

plt.show()
