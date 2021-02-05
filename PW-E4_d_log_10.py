def succ(Z):
    return Z+1
def pred(Z): 
    if Z>=1:
        return Z-1
    else:
        return 0

# macro resta acotada	
def resta(X,Y):
    Z=0;
    while Z!=Y:
        X=pred(X)
        Z=succ(Z)
    return X


# Con la macro del producto, la resta y la asignacion
"""
He de contar hasta cuando puedo elevar 10 a un numero sin pasarme de la X
pues log_10(X)=Y, 10^Y<=X
Para ello he de ver a que numero puedo exponenciar el 10 sin pasarme de X
X3<- Calculo la exponenciacion de 10
X4<- Resto X1 a X3
X2<- Cuento las veces que puedo calcular X4, es decir las veces que puedo restar
a X1, X3.
"""
def main(X1,X2,X3,X4,X5,X6):
    
    # log_10(0) indeterminacion --> Bucle infinito
    X6=pred(X1)
    X6=succ(X6)
    while X1!=X6:
        X2=0
		
    """Otra forma de hacerlo sin emplear mas variables
    X2=1;
    X2=resta(X2,X1)
    While X2!=X3:
    X3=0
    """
    

    # X2-> Cuento las veces que puedo restar X4 - X3, logaritmo
    # X3-> Calculo la potencia 10^0=1
    # X4-> Resto
    X1=succ(X1)
    X3=1
    X4=resta(X1,X3)
    while X4!=X5:
        X2=succ(X2)
        X3=X3*10
        X4=resta(X1,X3)
    X1=pred(X2)
    return X1

def log10(X): 
	return main(X,0,0,0,0,0)

print log10(1100) 
print log10(10)
print log10(150) 
print log10(1)
#print log10(0)
