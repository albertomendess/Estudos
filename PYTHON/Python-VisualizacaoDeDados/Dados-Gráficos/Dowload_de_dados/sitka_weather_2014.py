import csv
from datetime import datetime

from matplotlib import pyplot as plt

# Obtém as datas e as temperaturas máximas e mínimas do arquivo.
filename = 'Estudos/PYTHON/Python-VisualizacaoDeDados/Dados-Gráficos/Dowload_de_dados/sitka_weather_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates, highs, lows = [], [], []
    for row in reader:
        dates.append(datetime.strptime(row[0], "%Y-%m-%d"))

        highs.append(int(row[1]))

        lows.append(int(row[3]))


# Faz plotagem dos dados.
fig = plt.figure(dpi=100, figsize=(12, 8))
plt.plot(dates, highs, c='red', alpha=0.5)
plt.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)


# Formata o gráfico.
plt.title("Daily high and low temperatures - 2014", fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()