def succ(Z):
    return Z+1
def pred(Z): 
    if Z>=1:
        return Z-1
    else:
        return 0

"""Esta es la macro de la resta acotada
Si X < Y, X-Y retorna 0
En otro caso X-Y"""
def resta(X,Y):
    Z=0
    while Z!=Y:
        X=pred(X)
        Z=succ(Z)
    return X
 
""" Sesion 8-E5: Calculese para cada caso, la expresion algebraica ET,
tal que tenga valor mayor que 0 cuanto T sea verdadero, y el valor 0 cuando T sea falso.
a)(x!=y) and (z>y)
b)(x<=y) or (z<x)

"""

"""
a) 
T =(X!=Y) and (Z>Y)         ET = ET1*ET2
T1 =(X!=Y)= (X<Y) or (Y<X)  ET1 = ET11+ET12
T11 =(X<Y)                  ET11 = (Y-X)
T12 =(Y<X)                  ET12 = (X-Y)
T2 = (Z>Y)                  ET2 = (Z-Y)

b)
T =((X<=Y) or (Z<X))        ET= ET1+ET2
T1 =(X<=Y)= !(Y<X)          ET1= 1-(X-Y)
T2 = (Z<X)                  ET2 = (X-Z)
"""

def E_test_a(X,Y,Z):
    print "------Quitamos macro-test a)((X!=Y) and (Z>Y))"
    U=resta(Y,X) # ET11
    V=resta(X,Y) # ET12
    U=U+V        # ET1
    V=resta(Z,Y) # ET2
    U=U*V        # ET
    #print X, Y, Z,"a) ", ((X!=Y) and (Z>Y)), " U ", U
    print "a) (",X,"!=", Y,") and (", Z, ">", Y, ")",((X!=Y) and (Z>Y)), ", ET = ", U

def E_test_b(X,Y,Z):
    print "------Quitamos macro-test b)((X<=Y) or (Z<X))"
    U=resta(1,resta(X,Y)) # ET1
    V=resta(X,Z)          #ET2
    U=U+V                 # ET
    #print X, Y, Z,"a) ", ((X<=Y) or (Z<X)), " U ", U
    print "b) (",X,"<=", Y,") or (", Z, "<", X, ")",((X<=Y) or (Z<X)), ", ET = ", U



E_test_a(1,2,3) # true
E_test_a(1,1,3) # falso
E_test_b(1,2,3) # true
E_test_b(5,1,6) # falso
