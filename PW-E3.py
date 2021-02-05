def succ(Z):
    return Z + 1
def pred(Z):
    if Z >= 1:
        return Z - 1
    else:
        return 0

""" PW-E3: Construir un PW equivalente a este sin macros
begin
X2=2;
while X3!=0 do
begin
  X2=X2+X4;
  X3=pred(X3);
end
X1=X2;
end
"""

# Pasar a pw como argumento las k varibles (X1, X2, ...Xk) del programa while k variables construido
def pw(X1,X2,X3,X4,X5,X6):
    #Quitar macro X2=2
    X2=0
    X2=succ(X2)
    X2=succ(X2)
    #Quitar el macro test X3 != 0,comparo con X5 que vale 0
    while X3 != X5:
        #Quitar macro X2 = X2 +X4
        while X6 != X4:
            X2 = succ(X2)
            X6 = succ(X6)
        X6 = 0
        X3= pred(X3)

    X1 = succ(X2)
    X1 = pred(X1)
    return X1

# Para probar el programa, invocar el main con k argumentos
print(pw(7,9,2,1,0,0))
