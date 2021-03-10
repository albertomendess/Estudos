import csv
from datetime import datetime

from matplotlib import pyplot as plt

# Obtém as datas, total de casos diários e óbitos na região de São Paulo.
filename = 'PYTHON/Python-VisualizacaoDeDados/Dados-Gráficos/Dowload_de_dados/Dados-covid-19-estado.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates, daily_cases = [], []
    for row in reader:
        current_date = datetime.strptime(row[0], "%Y-%m-%d")
        dates.append(current_date)

        case = int(row[1])
        daily_cases.append(case)


# Faz plotagem dos dados.
fig = plt.figure(dpi=100, figsize=(12, 8))
plt.plot(dates, daily_cases, c='red')


# Formata o gráfico.
plt.title("Number of daily cases in São Paulo - Brasil", fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Cases", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()