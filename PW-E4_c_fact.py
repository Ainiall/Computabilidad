def succ(Z):
    return Z + 1
def pred(Z):
    if Z >= 1:
        return Z - 1
    else:
        return 0

""" PW-E4-c): Construir un PW que compute f(X)=fact(X). Empleando macros: producto y asignacion """
# Pasar al f como argumento las k varibles (X1, X2, ...Xk)  del programa while k variables construido
def pw(X1,X2,X3):
    X2 =1#Calculo el caso especial !0 = 1
    while X3 != X1:
        X3 = succ(X3)
        X2=X2+X2
    X1 = X2

    return X1


def fact(X):
  return print(pw(X,0,0))

# Para probar el programa, invocar a fact
# Probar que sucede para varios valores de X: 0!, 3!, ...
fact(3)

