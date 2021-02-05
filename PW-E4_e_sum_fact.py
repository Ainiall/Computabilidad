def succ(Z):
    return Z+1
def pred(Z): 
    if Z>=1:
        return Z-1
    else: 
        return 0


# Con la macro del producto, y la asignacion
# sum_i=0_X(i!)

def main(X1,X2,X3,X4):
    # X2-> Cuento de i=0 hasta X1
    X3=1 # X3-> Calculo factorial 0!=1
    X4=1 # X4-> Calculo el sumatorio sum_i=0_0(0!)=1
    while X2!=X1:
        X2=succ(X2)
        X3=X3*X2
        X4=X4+X3
    X1=X4
    return X1

def sumatorio_fact(X):
	return main(X,0,0,0)

print sumatorio_fact(3)
