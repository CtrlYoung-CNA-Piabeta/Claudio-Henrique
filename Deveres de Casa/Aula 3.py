# Aula 3
# Desafio 1

X = []
for i in range(10):
    if i == 0:
        valor = int(input())
        Z = valor
        X.insert(i,valor)
    else:
        Z = Z * 2
        X.insert(i,Z)

for i in range(10):
    print('N[{0}] = {1}'.format(i,X[i]))
# Desafio 2

N = []
Z = []
for i in range(20):
    valor = int(input())
    N.append(valor)
    
j = 19    
for i in range(20):
    Z.append(N[i])
    if i >=10:
        N[i] = Z[j]
    else:
        N[i] = N[j]        
    j-=1

for i in range(20):
    print('N[{0}] = {1}'.format(i,N[i]))