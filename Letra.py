import matplotlib . pyplot as plt
import numpy as np

def B ( coorArr , i , j , t ) :
    if j == 0:
        return coorArr [ i ]
    return B ( coorArr , i , j - 1 , t ) * (1 - t ) + B ( coorArr , i + 1 , j - 1 , t ) * t

P = np.array ([[0. , 0.] ,[0. , 10.] , #Recta
    [0. , 8.] , 
    [1.5 ,9.5], [3.5 ,10.], [5.5, 10.5], [6., 10.], [5.5 , 8.],  
    [4.5 , 7.5], [5. , 7.],
    [6., 3.] ,[5.5 , 8.] , 
    [7. ,9.5], [9. , 10.] ,[11., 10.5], [11.5, 10.], [11. , 8.] ,
    [12.5, 3.] ,[13.2, 1.7] ,[14.5, 1.]]) #Dos curvas de 3º

fig = plt.figure (1)

#Beizer

#Aquí se marca el grado de la curva:
# 2: 1º grado   3: 2º grado     4: 3º grado

P1= np.array([[0. , 0.] ,[0. , 10.]])

ini =0; fin = 2

for k in range (0 , 1) :
    x = P1 [ ini : fin ,0]; y = P1 [ ini : fin ,1]; n = x . size
    xb =[]; yb =[]
    for t in np . linspace (0. ,1. ,25) :
        a = B (x , 0 , n - 1 , t )
        b = B (y , 0 , n - 1 , t )
        xb . append ( a )
        yb . append ( b )
    plt . plot ( xb , yb )
    ini = fin -1
    fin = ini + n


P2= np.array([[0. , 8.] , [1.5 ,9.5], [3.5 ,10.]])

ini =0; fin = 3

for k in range (0 , 2) :
    x = P2 [ ini : fin ,0]; y = P2 [ ini : fin ,1]; n = x . size
    xb =[]; yb =[]
    for t in np . linspace (0. ,1. ,25) :
        a = B (x , 0 , n - 1 , t )
        b = B (y , 0 , n - 1 , t )
        xb . append ( a )
        yb . append ( b )
    plt . plot ( xb , yb )
    ini = fin -1
    fin = ini + n


P3= np.array([[3.5 ,10.], [5.5, 10.5], [6., 10.], [5.5 , 8.]])

ini =0; fin = 4

for k in range (0 , 2) :
    x = P3 [ ini : fin ,0]; y = P3 [ ini : fin ,1]; n = x . size
    xb =[]; yb =[]
    for t in np . linspace (0. ,1. ,25) :
        a = B (x , 0 , n - 1 , t )
        b = B (y , 0 , n - 1 , t )
        xb . append ( a )
        yb . append ( b )
    plt . plot ( xb , yb )
    ini = fin -1
    fin = ini + n

###### ACABAR ESTA, está feucha
P4= np.array([[5.5 ,8.], [4.5 , 7.5], [5. , 7.], [6. ,3.]]) 

ini =0; fin = 4

for k in range (0 , 2) :
    x = P4 [ ini : fin ,0]; y = P4 [ ini : fin ,1]; n = x . size
    xb =[]; yb =[]
    for t in np . linspace (0. ,1. ,25) :
        a = B (x , 0 , n - 1 , t )
        b = B (y , 0 , n - 1 , t )
        xb . append ( a )
        yb . append ( b )
    plt . plot ( xb , yb )
    ini = fin -1
    fin = ini + n

P5= np.array([[5.5 , 8.], [7. ,9.5], [9. , 10.]])

ini =0; fin = 3

for k in range (0 , 2) :
    x = P5 [ ini : fin ,0]; y = P5 [ ini : fin ,1]; n = x . size
    xb =[]; yb =[]
    for t in np . linspace (0. ,1. ,25) :
        a = B (x , 0 , n - 1 , t )
        b = B (y , 0 , n - 1 , t )
        xb . append ( a )
        yb . append ( b )
    plt . plot ( xb , yb )
    ini = fin -1
    fin = ini + n

P6= np.array([[9. , 10.] ,[11., 10.5], [11.5, 10.], [11. , 8.]]) 

ini =0; fin = 4

for k in range (0 , 2) :
    x = P6 [ ini : fin ,0]; y = P6 [ ini : fin ,1]; n = x . size
    xb =[]; yb =[]
    for t in np . linspace (0. ,1. ,25) :
        a = B (x , 0 , n - 1 , t )
        b = B (y , 0 , n - 1 , t )
        xb . append ( a )
        yb . append ( b )
    plt . plot ( xb , yb )
    ini = fin -1
    fin = ini + n


P7= np.array([[11. , 8.] ,[12.5, 3.]]) #Falta aux

P8= np.array([[12.5, 3.] ,[13.2, 1.7] ,[14.5, 1.]])#Falta aux
   

#Ajustar colores para que se vea algo
plt.plot( P [: ,0] , P [: ,1] , 'ko', P [: ,0] , P [: ,1] , 'c--' , ms =2)
plt.show()