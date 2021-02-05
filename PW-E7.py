def succ(Z):
    return Z + 1
def pred(Z):
    if Z >= 1:
        return Z - 1
    else:
        return 0

""" PW-E7: Construyase un programa while equivalente a la siguiente sentencia.
Las unicas macros permitidas son los macro test
if X1!=X2:
    X1=X1+X2
"""

# Pasar al pw como argumento las k varibles (X1, X2, ...Xk) del programa while k variables construido
def pw(X1,X2,X3,X4):
    while X1 !=X3 and X3== 0:
        #quitamos la macro X1 = X1 +X2
        while X4 != X2:
            X1 = succ(X1)
            X4 = succ(X4)
        X4 = 0
        #Al poner X3 a 1, salgo del bucle y este solo se ejecuta una ver cunado X1!= X3
        X3 = succ(X3)
    return X1

def f(X,Y):
	return print(pw(X,Y,0,0))



# Para probar el programa, invocar a f
# Probar que funciona cuando el test (X1!=X2) se evalua a cierto y a falso
f(2,3)

