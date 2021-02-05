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

# Implementamos y div (X mod Y)
def main(X1,X2,X3,X4,X5):
    # X3 = x mod y   
    X1=succ(X1)
    while X1!=X4:
        X3=X1
        # X1=resta(X1,X2) # La quitamos con el codigo de debajo
        X5=0
        while X5!=X2:
            X1=pred(X1)
            X5=succ(X5)
    X3=pred(X3)
    # y div X3
    X2=succ(X2)
    while X2!=X4:
        X1=succ(X1) # reutilizamos la variable X1 que ahora vale 0
        #X2=resta(X2,X3)  # La quitamos con el siguiente codigo
        X5=0
        while X5!=X3:
            X2=pred(X2)
            X5=succ(X5)
    X1=pred(X1)
    return X1

# Definimos un metodo para calcular la funcion semantica binaria asociada al PW
def f(X,Y): return main(X,Y,0,0,0)

print f(8,3)
# Sugerencia: observar lo que ocurre con:
# print f(4,2) #-> Bucle infinito
# print f(8,3) #-> 1
# print f(0,0) #-> Bucle infinito --> Indeterminacion




