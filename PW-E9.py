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


"""
PW-E9: 9. Calcule las funciones semanticas unaria y binaria, asi
como la secuencia de computacion con entrada (2,2)

begin
while (X1!=X3) do
    begin
	X1:=pred(X1);
	X3:=succ(X3);
    end
X1:=succ(X3);
while (X1!=X4) do
    begin
	X1:=resta(X1,X2);
	X5:=succ(X5);	
    end
X1:=pred(X5)
end

"""


def main(X1,X2,X3,X4,X5):
    # En el primer bucle se decrementa X1 y se incrementa X3 hasta que X1==X3
    # Si X3 vale 0 y X1 vale 0, y X2 vale 0 --> No entra en el 1er bucle --> bucle infinito en el segundo bucle
    # Si X1 <> 0
    #       Si X1 es impar -> Se queda en el 1er bucle --> bucle infinito
    #       Si X1 es par -> Calcula X1/2
    while (X1!=X3):
        X1=pred(X1) 
        X3=succ(X3)

    # En este segundo bucle parece que lo que hace es X3 div X2, cuenta cuantas veces puede
    # restar X2 a X3 antes de que X3 valga 0
    # Si X1>0 impar --> Bucle infinito en el 1er bucle
    # Si X1>=0 par#
            #Si X2 vale 0 -> Bucle infinito
            #Si X2 >0 --> (X1/2)/X2
    X1=succ(X3) 
    while (X1!=X4):
        X1=resta(X1,X2)
        X5=succ(X5) 
    X1=pred(X5)
    return  X1

# F(X)? Bucle Infinito
#       Si X es impar --> Bucle infinito. (Se queda en el primer bucle)
#       Si X es par --> Bucle infinito. (Calcula X1/2 en el 1er Bucle, y se queda en bucle infinito en el segundo)
print "F(X) -> Bucle infinito"

        
# F(X,Y)? Si X impar --> Bucle infinito. (Se queda en el 1er bucle)
#         Si X par
#               Si Y==0 --> Bucle infinito. (Calcula X1/2 en el 1er bucle, y se queda en bucle infinito en el segundo)
#               Si Y>0  --> (X/2)/y     

print "F(X,Y)"
#print main(5,0,0,0,0) # Bucle infinito
#print main(0,0,0,0,0) # Bucle infinito
##print main(6,0,0,0,0)   # Bucle infinito
print main(0,3,0,0,0) # 1er bucle (0/2=0), 2bucle (0/3=0) -->((X1/2)/X2=0)
print main(6,2,0,0,0) # 1er bucle (6/2=3), 2bucle (3/3=1) -->((X1/2)/X2=1)
print main(16,2,0,0,0) # 1er bucle (16/2=8), 2bucle (8/2=4) -->((X1/2)/X2=4)


"""
Secuencia de computacion (2,2,0,0,0)
a0           A1
(2,2,0,0,0) (X1!=X3) (2,2,0,0,0) X1=pred(X1) (1,2,0,0,0)  X3=succ(X3) (1,2,1,0,0)(X1!=X3) (1,2,1,0,0)
X1=succ(X3) (1,2,1,0,0) (X1!=X4) (1,2,1,0,0)  X1=resta(X1,X2) (0,2,1,0,0) X5=succ(X5) (0,2,1,0,1)
(X1!=X4) (0,2,1,0,1) X1=pred(X5) (0,2,1,0,1)

"""




