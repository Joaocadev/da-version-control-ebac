# código de geração do gráfico

import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Lê o arquivo csv e gera o dataframe do arquivo.

df = pd.read_csv("gasolina.csv")

# Cria o gráfico de linhas definindo eixo x e y.

sns.lineplot(data=df, x="dia", y="venda")

# Adiciona título ao gráfico e labels.

plt.title("Preço da gasolina de São Paulo nos 10 primeiros dias de Julho 2021")
plt.xlabel("Dia")
plt.ylabel("Preço")

# Salva o gráfico em um arquivo png.

plt.savefig("gasolina.png")
plt.show()