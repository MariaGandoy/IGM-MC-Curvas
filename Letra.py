import matplotlib . pyplot as plt
import numpy as np

def B ( coorArr , i , j , t ) :
    if j == 0:
        return coorArr [ i ]
    return B ( coorArr , i , j - 1 , t ) * (1 - t ) + B ( coorArr , i + 1 , j - 1 , t ) * t


def Curva (ran, ini, fin, P):
    for k in range (0 , ran) :
        x = P [ ini : fin ,0]; y = P [ ini : fin ,1]; n = x . size
        xb =[]; yb =[]
        for t in np . linspace (0. ,1. ,25) :
            a = B (x , 0 , n - 1 , t )
            b = B (y , 0 , n - 1 , t )
            xb . append ( a )
            yb . append ( b )
        plt . plot ( xb , yb, "purple", linewidth = 3)
        ini = fin -1
        fin = ini + n

    plt.plot(  P [: ,0] , P [: ,1] , 'c--', P [: ,0] , P [: ,1] , 'bo', ms =4)

    


P0= np.array([[-2. , 6.],[-0.5 , 10.5],[-5. , 3.5],[0., 9.5]])
Curva(2, 0, 4, P0)    

P1= np.array([[0. , 0.] ,[0. , 9.5]])
Curva(1, 0, 2, P1)

P2= np.array([[0. , 8.] , [1.5 ,9.5], [3.5 ,10.]])
Curva(2, 0, 3, P2)

P3= np.array([[3.5 ,10.], [5.5, 10.5], [6., 10.], [5.5 , 8.]])
Curva(2, 0, 4, P3)

P4= np.array([[5.5 ,8.], [4.5 , 1.], [5.5 ,0.5]]) 
Curva(2, 0, 3, P4)

P5= np.array([[5.5 , 8.], [7. ,9.5], [9. , 10.]])
Curva(2, 0, 3, P5)

P6= np.array([[9. , 10.] ,[11., 10.5], [11.5, 10.], [11. , 8.]]) 
Curva(2, 0, 4, P6)

P7= np.array([[11. , 8.] , [10., 1.], [11., 0.5]]) 
Curva(2, 0, 3, P7)

P8= np.array([[11., 0.5], [13., -0.5] ,[12., 5.] ,[11.5, 3.]])
Curva(2, 0, 4, P8)

plt.show()