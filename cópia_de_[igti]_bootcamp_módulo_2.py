# -*- coding: utf-8 -*-
"""Cópia de [IGTI] Bootcamp - Módulo 2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1KOEIPf8ZfcN8z4zYCajCCFpYmtbxmtja

## **Numpy**
"""

# importando as bibliotecas
import numpy as np

"""### **Criação de arrays**"""

np.array?

# criação de um array 1D: [1, 2, 3]
l = [1, 2, 3]
x = np.array(l)
print("x:", x)
print("shape:", x.shape)

type(x)

# criação de um array 2D: listas aninhadas
l = [[1, 2], [3, 4]]
x = np.array(l)
print("x:\n", x)
print("shape:", x.shape)

type(x)

help(np.zeros)

# array contendo apenas 0's
dim = (2, 2)  # (linhas, colunas)
x = np.zeros(dim)
print("x:\n", x)
print("shape:", x.shape)

# array contendo apenas 1's
size = (2, 2)  # (linhas, colunas)
x = np.ones(size)
print("x:\n", x)
print("shape:", x.shape)

np.linspace?

# criação de valores dentro de um intervalo
# valores uniformes entre 5 e 15
x_min, x_max = 5, 15
x = np.linspace(start=x_min, stop=x_max, num=6)
print("x:", x)
print("shape:", x.shape)

# criação da matriz identidade
n = 4
x = np.eye(n)
print("x:\n", x)
print("shape:", x.shape)

help(np.random.random)

# criação de valores aleatórios
# np.random.seed(10)
x = np.random.random(size=(2, 3))
print("x:\n", x)
print("shape:", x.shape)

"""### **Indexação de arrays**"""

# os índices no Python vão de 0 a n-1,
# onde n é o tamanho da dimensão
x = np.linspace(start=10, stop=100, num=10)
print("x:", x)
print("shape:", x.shape)

# extração de elementos
print("x:", x)
print("primeiro elemento:", x[0])
print("segundo elemento:", x[1])
print("último elemento:", x[9])
print("último elemento:", x[-1])

x[5]

# slicing: extração de subarrays: 
print("x:", x)
print("dois primeiros elementos:", x[0:2])  # 2 é exclusivo
print("dois primeiros elementos:", x[:2])
print("dois últimos elementos:", x[-2:])

# slicing em arrays 2D (matrizes)
x = x.reshape(2, 5)  # reshape de x para 2 linhas e 5 colunas
print("x:\n", x)

# extração de elementos
print("primeira linha, segunda coluna:", x[0, 1])
print("segunda linha, penúltima coluna:", x[1, -2])
print("última linha, última coluna:", x[1, 4])
print("última linha, última coluna:", x[-1, -1])

# slicing: extração de subarrays
print("x:\n", x)
print("primeira linha inteira: ", x[0, :])
print("primeira linha, segunda a quarta coluna: ", x[0, 1:4])
print("última coluna inteira:\n", x[:, [-1]])

# atenção com compartilhamento de memória em subarrays!!
x = np.array([1, 2, 3])
print("x antes:", x)
y = x[:2]
y[0] = -100  # alteração do valor em y altera o valor de x
print("x depois:", x)

# atenção com compartilhamento de memória em subarrays!!
x = np.array([1, 2, 3])
print("x antes:", x)
y = x[:2].copy()
y[0] = -100  # alteração do valor em y altera o valor de x
print("x depois:", x)

"""### **Funções aritméticas: soma, subtração e divisão**"""

# criação de dois arrays x e y
x = np.ones((2, 2))
y = np.eye(2)
print("x: \n", x)
print("y: \n", y)

# soma
print("soma de dois arrays:\n", x + y)
print("soma com float/int:\n", x + 2.)  # broadcasting

# subtração
print("subtração de dois arrays:\n", x - y)
print("subtração com float/int:\n", x - 2)  # broadcasting

# divisão
print("divisão de dois arrays:\n", x / y)
print("divisão com float/int:\n", x / 2)  # broadcasting

# quando o broadcasting não funciona
# np.array([1, 2, 3]) + np.array([1, 2])

# soma, subtração e divisão
print("combinação de operações: \n", (x+y)/(x-2))

"""### **Funções aritméticas: multiplicação**"""

# multiplicação elemento a elemento
print("x: \n", x)
print("y: \n", y)

# multiplicação
print("multiplicação de dois arrays:\n", x * y)
print("multiplicação com float/int:\n", x * 2)  # broadcasting

# multiplicação matricial
print("multiplicação matricial (np.dot):\n", np.dot(x, y))
print("multiplicação matricial (@):\n", x @ y)
print("multiplicação matricial (.dot):\n", x.dot(y))

""" 
Exemplo:
Solução de um sistema de equações:
  1*a + 2*b = 7
  3*a - 2*b = -11
  solução análitica: (a, b) = (-1, 4)
Matricialmente, este problema tem a seguinte forma:
  Ax = c, onde:
  - x = [a, b]
  - A = [[1, 2], [3, -2]]
  - c = [7, -11]
  solução numérica: x = inv(A) @ c, 
"""
 
# definição do problema
A = np.array([[1, 2], [3, -2]])
c = np.array([[7], [-11]])
print("A: \n", A)
print("c: \n", c)

"""Sistema de equações:

$$Ax=c,\\\left[\begin{array}{cc}1&2\\3&-2\end{array}\right]\left[\begin{array}{c}a\\b\end{array}\right] = \left[\begin{array}{c}7\\-11\end{array}\right].$$

Solução:

$$x=A^{-1}c.$$

"""

# solução
x = np.dot(np.linalg.inv(A), c)
# x = np.linalg.inv(A) @ c
print("(a, b):", x.ravel())

"""### **Comparações**"""

# criação dos arrays
x = np.array([[1, 2], [3, 4]])
y = np.array([1.5, 3.5])
print("x: \n", x)
print("y: \n", y)

# comparações ponto a ponto
print("Comparação de um array com um escalar (>): \n", x > 2)  
print("Comparação de um array com um escalar (>=): \n", x >= 2)
print("Comparação de um array com um escalar (<): \n", x < 2)  
print("Comparação de um array com um escalar (<=): \n", x <= 2)
print("Comparação entre arrays (==): \n", x == x)
print("Comparação entre arrays (>): \n", x > x)
print("Comparação entre arrays (>): \n", x > y)  # broadcasting

"""### **Indexação booleana**"""

# indexação booleana
x = np.array([[1, 3, 7],
              [4, 11, 21],
              [42, 8, 9]])
print("x:\n", x)

# indexação boolena: retornar o número de elementos
# maiores que k
k = 10
cond = x > k
print("condição: \n", cond)
print(f"elementos maiores que {k}:", x[cond])
print(f"números de elementos maiores que {k}:", len(x[cond]))

# indexação boolena: extração dos números pares
cond = x % 2 == 0  # números pares
print("condição: \n", cond)
print("números pares:", x[cond])

# indexação boolena: extração dos números ímpares
cond = x % 2 == 1  # números pares
print("condição: \n", cond)
print("números pares:", x[cond])

"""### **Outras operações úteis em numpy**"""

# array
x = np.array([[1, 3, 7],
              [4, 11, 21],
              [42, 8, 9]])
print("x:\n", x)

# reshape: transformar a matriz em um vetor coluna
# (3, 3) vira (9, 1): 3*3 = 9*1 = 9
print("transformação de em um vetor coluna: \n", x.reshape(9, 1))

# transposição de matriz
print("x transposta: \n", x.T)

# np.sum: soma em um dado eixo, axis = {0: linha, 1: coluna}
print("x:\n", x)
print("soma de todos elementos de x:", np.sum(x))
print("soma de x ao longo das linhas:", np.sum(x, axis=0))
print("soma de x ao longo das colunas:", np.sum(x, axis=1))

# np.mean: média em um dado eixo, axis = {0: linha, 1: coluna}
print("x:\n", x)
print("média de todos elementos de x:", np.mean(x))
print("média de x ao longo das linhas:", np.mean(x, axis=0))
print("média de x ao longo das colunas:", np.mean(x, axis=1))

# np.where, indentificação dos índices onde uma dada condição
# é atendida. Uso conjunto com indexação booleana
cond = x % 2 == 0  # números pares
print("condição: \n", cond)
i, j = np.where(cond) # índices x[i, j] = x[cond]
print("índice i (linhas):", i)
print("índice j (colunas):", j)

# indexação booleana e slicing: selecionar as linhas
# de x que possuem algum número par
print("x:\n", x)
cond = x % 2 == 0  # números pares
print("condição: \n", cond)

# # se houver alguma condição True na linha, a soma será > 0
i_row = np.where(np.sum(cond, axis=1))[0]
print("índice das linhas que possuem números pares:", i_row)
print("linhas que possuem número pares: \n", x[i_row, :])

"""### **Regressão linear no numpy**"""

# visualização de dados
import matplotlib.pyplot as plt

# dados
x = [-1., -0.77777778, -0.55555556, -0.33333333, -0.11111111,
     0.11111111, 0.33333333, 0.55555556, 0.77777778, 1.]
y = [-1.13956201, -0.57177999, -0.21697033, 0.5425699, 0.49406657,
     1.14972239, 1.64228553, 2.1749824, 2.64773614, 2.95684202]

# plot dos dados
plt.figure(figsize=(10, 5))
plt.plot(x, y, 'o', label='dados originais')
plt.legend()
plt.xlabel("x")
plt.ylabel("y")
plt.grid()
plt.show()

"""Regressão linear:

$$X\beta=y,\\\beta=\left[\begin{array}{c}a\\b\end{array}\right] .$$

Solução via minimização do erro quadrático:

$$\beta=(X^TX)^{-1}X^Ty,$$
onde $(X^TX)^{-1}X^T$ é a pseudo-inversa de $X$, facilmente calculada pelo método `np.linalg.pinv(X)`.

"""

"""
Iremos estimar uma função do tipo: y = a*x + b
ou seja, devemos achar quais os valores de a e b
que melhor representam os dados.

Os valores reais de a e b são: (a, b): 2, 1
"""
# transformando para numpy e vetor coluna
x, y = np.array(x).reshape(-1, 1), np.array(y).reshape(-1, 1)

# adicionando bias: para estimar o termo b
X = np.hstack((x, np.ones(x.shape)))

# estimando a e b
beta = np.linalg.pinv(X).dot(y)
print("a estimado:", beta[0][0])
print("b estimado:", beta[1][0])

# plot dos dados
plt.figure(figsize=(10, 5))
plt.plot(x, y, 'o', label='dados originais')
plt.plot(x, X.dot(beta), label='regressão linear')
plt.legend()
plt.xlabel("x")
plt.ylabel("y")
plt.title("Regressão linear com numpy")
plt.grid()
plt.show()



"""## **Pandas**"""

# importando as bibliotecas
import pandas as pd

"""### **Leitura de dados**"""

pd.read_csv?

# leitura dos dados csv
df = pd.read_csv("https://pycourse.s3.amazonaws.com/temperature.csv")
df

# leitura de planilhas excel
# 2 abas (worksheets)

# leitura do arquivo todo
excel_file = pd.ExcelFile("https://pycourse.s3.amazonaws.com/temperature.xlsx")

type(excel_file)

# leitura da primeira aba (Sheet1)
# dados numéricos com separador decimal = '.'
df2 = pd.read_excel(excel_file, sheet_name='Sheet1')
df2

# leitura da segunda aba (Sheet2)
# dados numéricos com separador decimal = ','
df3 = pd.read_excel(excel_file, sheet_name='Sheet2') 
df3['temperatura'] = df3['temperatura'].str.replace(',', '.').astype('float')
df3

# visualizando as primeiras n linhas
n = 3
df.head(n)

# visualizando as últimas n linhas
n = 3
df.tail(n)

# dtypes
df.dtypes

# estatísticas básicas
df.describe()

# dataframe info
df.info()

# nomes das colunas
df.columns

"""### **Indexação**"""

df.head()

# seleção de uma coluna
df['temperatura']

# tipo
type(df['temperatura'])

# seleção de múltiplas colunas
df[['date', 'classification', 'temperatura']]

# tipo
type(df[['date', 'classification']])

# iloc
df.iloc?

# indexação por índice
# selecionado todas as linhas e a coluna 1
# coluna 1: temperatura
a = df.iloc[:, 1]

# indexação por nome
# selecionado todas as linhas e a coluna 1
df.loc[:, 'temperatura']

# indexação por índice de múltiplas colunas
df.iloc[:, 1:]

# indexação por nome de múltiplas colunas
df.loc[:, ['temperatura', 'classification']]

# indexação por nome de múltiplas colunas
df.loc[:, 'temperatura':]

"""### **Indexação booleana**"""

df

# dtype
df.dtypes

# transformando o tipo da coluna date para datetime
df['date'] = pd.to_datetime(df['date'])
df.dtypes

# setando o índice
df = df.set_index('date')

# visualizando o índice 
df

# 5 primeiras linas
df.head()

# indexação booleana
# seleção de exemplos acima de 25 graus
cond = df['temperatura'] >= 25
df[cond]

# indexação booleana considerando datetime
# seleção de entradas até Março de 2020
cond = df.index <= '2020-03-01'
df[cond]

# indexação booleana considerando datetime
# seleção de entradas até Março de 2020 e 
# slice na coluna classification
df.loc[df.index <= '2020-03-01', ['classification']]

# indexação booleana considerando datetime
# seleção de entradas até Março de 2020 e 
# slice na coluna classification
df.iloc[df.index <= '2020-03-01', [-1]]

"""### **Ordenação**"""

# df.sort_values
df

# ordenação crescente por uma coluna
df.sort_values(by='temperatura')

# ordenação crescente por uma coluna
df.sort_values(by='classification')

# ordenação crescente por mais de uma coluna
df.sort_values(by=['classification', 'temperatura'])

# ordenação decrescente por uma coluna
df.sort_values(by=['classification', 'temperatura'], ascending=False)

# ordenação crescente pelo índice
df.sort_index()

# ordenação decrescente pelo índice
df.sort_index(ascending=False)

"""### **Visualização**"""

# plot de linhas
df.plot();

# plot de linhas: tamanho
df.plot(figsize=(10, 5));

# plot de linhas: grid
df.plot(figsize=(10, 5), grid=True);

# plot de linhas: style
df.plot(style='-o', figsize=(10, 5), grid=True);
# df.plot(style='--', figsize=(10, 5), grid=True);
# df.plot(style='-.', figsize=(10, 5), grid=True);

# plot de linhas: linewidth
df.plot(style='-o', linewidth=2, figsize=(10, 5), grid=True);

# plot de linhas: color
df.plot(style='-o', linewidth=2.5, color='red', figsize=(10, 5), grid=True);

# plot de linhas: color
df.plot(style='-o', linewidth=2.5, color='#822fb5', figsize=(10, 5), grid=True);

df

# plot de barras
df['classification'].value_counts().plot.bar(figsize=(10, 5),
                                             rot=0);

# plot de barras
df.plot(kind='bar', figsize=(10, 5), rot=30);

# pie plot
df['classification'].value_counts().plot.pie(autopct='%1.1f%%',
                                             shadow=True,
                                             figsize=(10, 7));

"""### **Outras operações úteis no pandas**"""

# dataframe
df.head(6)

# groupby: agrupamento por valores únicos de uma ou mais colunas
df.groupby(by='classification')

# groupby: agrupamento por valores únicos de uma ou mais colunas
df.groupby(by='classification').mean()

# groupby: agrupamento por valores únicos de uma ou mais colunas
df.groupby(by='classification').sum()

# drop: remoção de uma coluna
df.drop('temperatura', axis=1)

df

# cópia de um dataframe: evita compartilhamento de memória
# sem copy(), operações inplace em df2 também alteram df
# df2 = df.copy() 
df2 = df

# argumento inplace
# inplace=True aplica a transformação no próprio objeto
df3 = df2.drop("temperatura", axis=1)

# sem inplace, df2 continua o mesmo
df3.head()

# argumento inplace
# inplace=True aplica a transformação no próprio objeto
df2.drop("temperatura", axis=1, inplace=True)

# com inplace, df2 é alterado
df2.head()

# df
df.head()

"""## **Scikit-learn**

### **Classificação no scikit-learn**
"""

df

# extração de x e y
x, y = df[['temperatura']].values, df[['classification']].values
print("x:\n", x)
print("y:\n", y)

# pré-processamento
from sklearn.preprocessing import LabelEncoder

LabelEncoder?

# conversão de y para valores numéricos
le = LabelEncoder()  # label enconder
y = le.fit_transform(y.ravel())
print("y:\n", y)

# modelo
from sklearn.linear_model import LogisticRegression

# classificador
clf = LogisticRegression()
clf.fit(x, y)

# gerando 100 valores de temperatura
# linearmente espaçados entre 0 e 45
# predição em novos valores de temperatura
x_test = np.linspace(start=0., stop=45., num=100).reshape(-1, 1)

# predição desses valores
y_pred = clf.predict(x_test)

print(y_pred)

# conversão de y_pred para os valores originais
y_pred = le.inverse_transform(y_pred)
# print(y_pred)

# output
output = {'new_temp': x_test.ravel(),
         'new_class': y_pred.ravel()}
output = pd.DataFrame(output)

output.tail()

# estatisticas
output.info()

# estatisticas
output.describe()

# contagem de valores gerados
output['new_class'].value_counts().plot.bar(figsize=(10, 5),
                                            rot=0,
                                            title="# de novos valores gerados");

# distribuição do output produzido
# conseguimos inferir a classificação novas temperaturas
# a partir de um dataset com 6 exemplos
output.boxplot(by='new_class', figsize=(10, 5));

# sistema automático
def classify_temp():
  """Classifica o input do usuário."""

  ask = True
  while ask:
    # input de temperatura
    temp = input("Insira a temperatura (graus Celsius): ")

    # transformar para numpy array
    temp = np.array(float(temp)).reshape(-1, 1)
    
    # realiza classificação
    class_temp = clf.predict(temp)

    # transformação inversa para retornar a string original
    class_temp =  le.inverse_transform(class_temp)

    # classificação
    print(f"A classificação da temperatura {temp.ravel()[0]} é:", class_temp[0])

    # perguntar
    ask = input("Nova classificação (y/n): ") == 'y'

# rodando programa 
classify_temp()

"""### **Regressão linear no scikit-learn - I**


"""

# dados do segundo capítulo
x = [-1., -0.77777778, -0.55555556, -0.33333333, -0.11111111,
     0.11111111, 0.33333333, 0.55555556, 0.77777778, 1.]
y = [-1.13956201, -0.57177999, -0.21697033, 0.5425699, 0.49406657,
     1.14972239, 1.64228553, 2.1749824, 2.64773614, 2.95684202]

# plot dos dados
plt.figure(figsize=(10, 5))
plt.plot(x, y, 'o', label='dados originais')
plt.legend()
plt.xlabel("x")
plt.ylabel("y")
plt.grid()
plt.show()

# transformando em numpy array
x, y = np.array(x).reshape(-1, 1), np.array(y).reshape(-1, 1)

# modelo
from sklearn.linear_model import LinearRegression

# treinando o modelo: y = a*x + b, valores reais (a, b) = (2, 1)
reg = LinearRegression()
reg.fit(x, y)

# coeficientes a, b estimados:
# valores estimados usando o numpy diretamente
# a estimado no numpy: 2.05414951
# b estimado no numpy: 0.96798926
print("a estimado:", reg.coef_.ravel()[0])
print("b estimado:", reg.intercept_[0])

# predição do modelo
y_pred = reg.predict(x)

# score do modelo
score = reg.score(x, y)
print("score:", score)

# plot dos dados
plt.figure(figsize=(10, 5))
plt.plot(x, y, 'o', label='dados originais')
plt.plot(x, y_pred, label='regressão linear (R2: {:.3f})'.format(score))
plt.legend()
plt.xlabel("x")
plt.ylabel("y")
plt.title("Regressão linear no scikit-learn")
plt.grid()
plt.show()

"""### **Regressão linear no scikit-learn - II**

"""

# plot dos dados
plt.figure(figsize=(10, 5))
plt.plot(x, y, 'o', label='dados originais')
plt.plot(x, y_pred, label='regressão linear (R2: {:.4f})'.format(score))
plt.hlines(y=y.mean(), xmin=x.min(), xmax=x.max(), linestyle='dashed',
           label='Modelo de referência do $R^2$')
plt.legend()
plt.xlabel("x")
plt.ylabel("y")
plt.title("Regressão linear no scikit-learn")
plt.grid()
plt.show()

"""O erro quadrático médio de um modelo de regressão é dado por:

$$MSE_{reg} = \frac{1}{n}\sum_{i=1}^{n} (y_i - \hat{y}_i)^2.$$

O coeficiente de determinação $R^2$ representa o quão melhor um modelo é em relação a um modelo de referência que prevê sempre a média dos pontos, ou seja, o MSE do modelo de referência é dado por:

$$MSE_{ref} = \frac{1}{n}\sum_{i=1}^{n} (y_i - \bar{y})^2,$$

onde $\bar{y}$ representa a média do vetor $y$.

Sendo assim:

$$R^2 = 1 - \frac{MSE_{reg}}{MSE_{ref}}$$
"""

# função para cálculo do MSE
def mse(y_true, y_pred, is_ref = False):

  # mse modelo
  if is_ref:
    mse = ((y_true - y_true.mean())**2).mean()
  else:
    mse = ((y_true - y_pred)**2).mean()

  return mse

# função para cálculo do coeficiente de determinação R2
def r2(mse_reg, mse_ref):
  return 1 - mse_reg/mse_ref

# visualizando y e y_pred
print("y_true:", y.ravel())
print("y_pred:", y_pred.ravel())

# calculando o mse dos modelos
mse_reg = mse(y_true=y, y_pred=y_pred)
print("MSE do modelo de regressão:", mse_reg)
mse_ref = mse(y_true=y, y_pred=y_pred, is_ref=True)
print("MSE do modelo de referência:", mse_ref)

# calculando o R2 score
r2_score = r2(mse_reg=mse_reg, mse_ref=mse_ref)
print("Coeficiente R2 do modelo implementado (calculado):", r2_score)

# score retornado pelo scikit-learn
r2_score_skl = reg.score(x, y)
print("Coeficiente R2 do modelo implementado (scikit-learn):", r2_score_skl)

