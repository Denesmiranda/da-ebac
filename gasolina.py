# código de geração do gráfico 
import seaborn as sns
import pandas as pd

gasolina = pd.read_csv('./gasolina.csv')

altura  = 10 / 2.54 
largura = 10 / 2.54

with sns.axes_style('whitegrid'):

  gasolina = sns.lineplot(data=gasolina, x="dia", y="venda", palette="pastel")
  gasolina.set(title='Preço médio de venda da gasolina na cidade de São Paulo', xlabel='Dia', ylabel='Preço(R$)')

  altura  = 15 / 2.54
  largura = 15 / 2.54

  gasolina.figure.set_size_inches(w=largura, h=altura)
  figura = gasolina.get_figure()    
  figura.savefig('gasolina.png', dpi=600)