import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
# Cristopher Lopez N c 1373 
#crearemos nuestra tabla y la guardaremos con pandas
# tenemos 5 listas de plataforma de streaming con 4 elementos por lista 
# Problema 7: Streaming (Plataforma, suscriptores en millones, opción gratis, lanzamiento)
nfx = ['Netflix', 260, False, 2007]
dis = ['Disney+', 150, False, 2019]
spn = ['Spotify', 602, True, 2008]
ytb = ['YouTube Premium', 100, True, 2014]
hbo = ['Max', 95, False, 2020]

# Creamos una lista de listas (conformando la tabla)
lista_de_plataformas_de_Streaming = [nfx,dis,spn,ytb,hbo]
print(lista_de_plataformas_de_Streaming)
# utilizar pandas para organizar la tabala (data frame o marco de datos)
# a cada columna le ponemos nombre 
df_plataforma_streaming=pd.DataFrame(lista_de_plataformas_de_Streaming,columns=["Nombre","Cantidad","Es_FB","Años"])
print(df_plataforma_streaming)
# cramos el archivo CSV y lo guardamos en CSV 
df_plataforma_streaming.to_csv("plataformasstreaming.csv", index=False)
#crear grafica de lineas 
#donde x es nombre en el eje horizontal 
#donde y es cantidad en el eje vertical 
plt.plot(df_plataforma_streaming["Nombre"],df_plataforma_streaming["Cantidad"])
plt.title("Grafica plataforma de streaming 1374")
plt.xlabel("Nombre de las redes")
plt.ylabel("Cantidad de usuarios")
plt.show()
# Creamos una grafica de puntos 
plt.scatter(df_plataforma_streaming["Nombre"],df_plataforma_streaming["Cantidad"])
plt.show()
# Grafica de barras
plt.bar(df_plataforma_streaming["Nombre"],df_plataforma_streaming["Cantidad"])
# Etiquetas y titulo
plt.title("Grafica plataforma de streaming 1374")
plt.xlabel("Nombre de las redes")
plt.ylabel("Cantidad de usuarios")
# Mostrar grafica
plt.show()
# ordenar la grafica de barras de manera descendente 
# de la mas grande a la mas pequeña
df_rs_ordenar=df_plataforma_streaming.sort_values("Cantidad",ascending=False)
plt.bar(df_rs_ordenar["Nombre"],df_rs_ordenar["Cantidad"])
plt.show()
# coloreando la grafica
df_rs_ordenar=df_plataforma_streaming.sort_values("Cantidad",ascending=False)
plt.bar(df_rs_ordenar["Nombre"],df_rs_ordenar["Cantidad"],
        color=["b","g","c","m","y","r"])
plt.show()

## Grafica de pastel
# plt.plot(df_plataforma_streaming["Nombre"],df_plataforma_streaming["Cantidad"])
plt.pie(df_plataforma_streaming["Cantidad"],labels=df_plataforma_streaming["Nombre"])
plt.show()