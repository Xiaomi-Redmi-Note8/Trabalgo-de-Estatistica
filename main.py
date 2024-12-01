import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression


arquivo1 = open("dadosX.txt", "r")
arquivo2 = open("dadosY.txt", "r")
dadosX = []
dadosY = []

dadosX = arquivo1.read().split()
dadosY = arquivo2.read().split()
arquivo1.close()
arquivo2.close()

def muda_float(lista):
    for x in lista:
        i = lista.index(x)
        x = float(x)
        lista[i] = x
    
muda_float(dadosX)
muda_float(dadosY)    
    
dados = pd.DataFrame({
    'X': dadosX,
    'Y': dadosY,
})

x = np.array([[1,1],[1,2],[2,2],[2,3]])
y = np.dot(x, np.array([1,2]))
reg = LinearRegression().fit(dados.X.values.reshape(-1,1), dados.Y)

a = reg.coef_[0]
b = reg.intercept_

fig,ax = plt.subplots() 

ax.set_ylim([90, 100])
ax.scatter(dados.X, dados.Y, color="gray")

X = dados.X.values
Y = a*X + b

ax.plot(X,Y, color="red", linewidth=5)

plt.show()