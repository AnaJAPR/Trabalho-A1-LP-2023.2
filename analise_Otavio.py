import limpa_dados as lp
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("IGC_2021.csv")
df = lp.corrige_nomes_df(df)

# analise 1

dados_1 = df.groupby('Organização Acadêmica')

media_curso_por_org = dados_1['Nº de Cursos com CPC no triênio'].mean()
media_curso_por_org.plot(kind='bar', xlabel='Organização Acadêmica', ylabel='Média de Número de Cursos')

plt.title('Número de Cursos por Organização Aadêmica')
plt.show()


# analise 2
    
dados_2 = df.groupby(['Organização Acadêmica', 'Categoria Administrativa'])['Nome da IES'].count().unstack()

dados_2.plot(kind='bar', stacked=True, figsize=(10, 5))

plt.xlabel('Organização Academica')
plt.ylabel('Numero de Instituições')
plt.title('Numero de Inst. por org e categoria adm.')
plt.legend(title='Categoria Administrativa')
plt.show()