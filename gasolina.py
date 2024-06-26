# Bibliotecas usadas para gerar o gráfico.

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Lê o arquivo csv e gera o dataframe.

df = pd.read_csv("gasolina.csv")

# Gera o gráfico de linha definindo x e y.

sns.lineplot(data=df, x="dia", y="venda")

# Nomeia o gráfico e os eixos x e y.

plt.title("Preço da gasolina no mês de Julho/2021")
plt.xlabel("Dia")
plt.ylabel("Preço da gasolina")

# Salva o gráfico como arquivo png.

plt.savefig("gasolina.png")