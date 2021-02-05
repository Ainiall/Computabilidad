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

 

""" PW-E6: Construir un PW sin macro-tes equivalente a este
 
begin

Z=succ(X)

while (X!=Y) or (Z<T) do

    begin

      Y:=succ(Y);

      Z:=pred(Z);

    end

end
"""


"""
T =(X!=Y) or (Z<T)
          ET = ET1+ET2

T1 =(X!=Y)= (X<Y) or (Y<X)  ET1 =ET11+ET12

T11 =(X<Y)                  ET11 =(Y-X)

T12 =(Y<X)                  ET12 =(X-Y)

T2 = (Z<T)                  ET2 = (T-Z)

"""


def main(X,Y,Z,T):

    Z=succ(X)

    print X,Y,Z,T

    # Quitamos el macro test

    U=resta(Y,X)      # ET11

    V=resta(X,Y)      # ET12

    U=U+V             # ET1

    V=resta(T,Z)      # ET2

    U=U+V             #ET= ET1+ET2

    V=0

    while U!=V:

        print "Dentro Bucle"

        Y=succ(Y)

        Z=pred(Z)

        # Actualizamos condicion del bucle

        U=resta(Y,X)  # ET11

        V=resta(X,Y)  # ET12

        U=U+V         # ET1

        V=resta(T,Z)  # ET2

        U=U+V         #ET= ET1+ET2
 
        V=0


       

main(2,1,1,2) # Entro al bucle



