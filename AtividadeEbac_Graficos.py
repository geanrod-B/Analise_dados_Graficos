import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

#       ------ INICIANDO O CODIGO ------

# --    ATIVIDADE EBAC       --
# --    NOME: GEAN RODRIGUES --


# ---- Fazendo a leitura do Arquivo ----
df = pd.read_csv('C:/Users/geanr/Desktop/ecommerce_preparados.csv')
(print(df.head().to_string()))

# ---- Gráfico de Pairplot - Dispersão de Histograma ----
sns.pairplot(df[['N_Avaliações', 'Marca_Cod', 'Material_Cod']])
plt.show()

#---- Gráfico Histograma ----
plt.figure(figsize=(10,8))
plt.hist(df['Desconto'], bins=20, color='#FFA500', edgecolor='black')
plt.title('Distribuição dos Descontos')
plt.xlabel('Desconto')
plt.ylabel('Frequência')
plt.show()


# ---- Gráfico de Dispersão. ----
sns.jointplot(x='Nota', y='N_Avaliações', data=df, kind='scatter')
plt.show()

#---- Mapa de Calor ----

#---- Fazendo a correlação ----
df_corr = df[['Desconto', 'Nota', 'Marca_Cod', 'Material_Cod', 'Temporada_Cod']].corr()

plt.figure(figsize=(10,6))
sns.heatmap(df_corr, annot=True, fmt=".2f", cmap='coolwarm', linewidths=0.5)
plt.title('Mapa de Calor da Correlação entre Variáveis Numéricas')
plt.tight_layout()
plt.show()

#---- Graficos de Barras ----
plt.figure(figsize=(10,6))
df['Nota'].value_counts().plot(kind='bar', color='#90ee70')
plt.title('Avaliação das Vendas')
plt.xlabel('Notas dos Produtos')
plt.ylabel('Quantidades')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# ---- Gráfico de Pizaa ----

# Agrupando desconto médio por materiais.
desconto_material = df.groupby('Material')['Desconto'].mean().sort_values(ascending=False)

# Seleciona os 5 primeiros e agrupa o restante como "Outros"
top_materiais = desconto_material.head(5) #Selecionando os 5 primeiros.
outros_materiais = pd.Series({'Outros': desconto_material[5:].mean()}) #Aqui está criando uma nova linha chamada "Outros" com o valor médio.
desconto_final = pd.concat([top_materiais, outros_materiais]) #Unindo as duas variáveis.


# ---- Fazendo o gráfico ----
plt.figure(figsize=(10,6))
plt.pie(desconto_final,labels=desconto_final.index,autopct='%1.1f%%',startangle=90,colors=plt.cm.Pastel1.colors,wedgeprops={'edgecolor': 'black'})
plt.title('Proporção dos Maiores Descontos Médios por Material (Top 5 + Outros)')
plt.tight_layout()
plt.show()

#---- Gráfico de Regressão ----
sns.regplot(x='Nota', y='N_Avaliações', data=df, color='#278f65', scatter_kws={'alpha': 0.5, 'color': '#34c289'})
plt.title('Regressão de Notas por Avaliações')
plt.xlabel('Nota')
plt.ylabel('N_Avaliações')
plt.show()

# ---- Gráfico de Dispersão ----
plt.hexbin(df['Nota'], df['N_Avaliações'], gridsize=8, cmap='Blues')
plt.colorbar(label='Contagem dentro do bin')
plt.xlabel('Nota')
plt.ylabel('N_Avaliações')
plt.title('Dispersão de Nota e Avaliações')
plt.show()


#       ------ FIM ------