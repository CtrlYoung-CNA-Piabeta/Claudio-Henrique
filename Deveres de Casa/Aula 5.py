# Aula 5
fibonnaci  = int(input('Escreva um número aqui: '))

x = [0]*fibonnaci

for i in range (0,fibonnaci):
    if i <= 1:
        x[i] = i
    else:
        x[i] = x[i-1] + x[i-2]

    if i==fibonnaci-1:
        print('%d'%(x[i]),end='')
    else:
        print('%d'%(x[i]),end=' ')
    
print()