from die import Die

import matplotlib.pyplot as plt


# Criando dois dados D6
die_1 = Die()
die_2 = Die()

attempts = 12

# Faz alguns lançamentos e armazena os resultados em uma lista
results = []
for roll_num in range(attempts):
    result = die_1.roll() + die_2.roll()
    results.append(result)


plt.plot(results, linewidth=5)


# Define o título do gráfico e nomeia os eixos
plt.title("Results of rolling tow D6 dice " + str(attempts) + " times.", 
    fontsize=24)
plt.xlabel("Attempt", fontsize=14)
plt.ylabel("Number")


# Define o tamanho dos rótulos das marcações
plt.tick_params(axis='both', labelsize=14)

plt.show()
