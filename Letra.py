import matplotlib . pyplot as plt
import numpy as np

def B ( coorArr , i , j , t ) :
    if j == 0:
        return coorArr [ i ]
    return B ( coorArr , i , j - 1 , t ) * (1 - t ) + B ( coorArr , i + 1 , j - 1 , t ) * t

P = np.array ([[0. , 0.] ,[0. , 10.] , #Recta
    [0. , 8.] , [3.5 ,10.] , #Curva 2º
    [5 , 9.] , #Curva 3º
    [5.5 , 8.] , #Curva 3º
    [6.5, 3.] ,[5.5 , 8.] , #Curva 2º
    [8.5 , 10.] ,[10., 9.] ,[10.5, 8.] , #Repetimos lo que antes
    [11.5, 3.] ,[12.2, 1.7] ,[13.5, 1.]]) #Dos curvas de 3º

fig = plt.figure (1)

#Beizer

#Aquí se marca el grado de la curva:
# 2: 1º grado   3: 2º grado     4: 3º grado

ini =0; fin = 2

for k in range (0 , 2) :
    x = P [ ini : fin ,0]; y = P [ ini : fin ,1]; n = x . size
    xb =[]; yb =[]
    for t in np . linspace (0. ,1. ,25) :
        a = B (x , 0 , n - 1 , t )
        b = B (y , 0 , n - 1 , t )
        xb . append ( a )
        yb . append ( b )
    plt . plot ( xb , yb )
    ini = fin -1
    fin = ini + n


#Añadir nuevos for para nuevas curvas
ini =2; fin = 5

for k in range (0 , 3) :
    x = P [ ini : fin ,0]; y = P [ ini : fin ,1]; n = x . size
    xb =[]; yb =[]
    for t in np . linspace (0. ,1. ,25) :
        a = B (x , 0 , n - 1 , t )
        b = B (y , 0 , n - 1 , t )
        xb . append ( a )
        yb . append ( b )
    plt . plot ( xb , yb )
    ini = fin -1
    fin = ini + n

#Ajustar colores para que se vea algo
plt.plot( P [: ,0] , P [: ,1] , 'ko', P [: ,0] , P [: ,1] , 'c--' , ms =2)
plt.show()