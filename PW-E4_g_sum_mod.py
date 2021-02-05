def succ(Z):
    return Z + 1
def pred(Z): 
    if Z >= 1:
        return Z - 1
    else:
        return 0
		
# macro resta acotada	
def resta(X,Y):
    Z=0;
    while Z!=Y:
        X=pred(X)
        Z=succ(Z)
    return X


""" PW-E4-g): Construir un PW que compute f(X,Y)=sum_i=1..X(Y mod i). Empleando macros: suma, resta y asignacion """
# Pasar al f como argumento las k varibles (X1, X2, ...Xk)  del programa while k variables construido
def pw(...):


    return X1

def sum_mod(X,Y):
  return print(pw(X,Y,...))


# Para probar el programa, invocar a sum_mod
# Probar que sucede para varios valores de X e Y.
sum_mod(...) 


