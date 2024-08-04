# Aula 14

# Desafio 1

n = int(input())
calculadora = 1
for i in range(n):
    valor, operacao = input().split()
    valor = int(valor)
    if(operacao == '/'):
        calculadora = calculadora / valor
    else:
        calculadora = calculadora * valor
print("{0:.0f}".format(calculadora))

# Desafio 2

comeco = True
i = 0
j = 0
soma = 0
vet_idade = []
while comeco:
    idade = int(input())
    if idade >= 0:
     vet_idade.append(idade)
    else:
        comeco = False
    i+=1
while j < (i-1):
    soma+=vet_idade[j]
    j+=1
print('{:.2f}'.format(soma/(i-1)))

# Desafio 3

a=int(input())
for i in range(a):
    soma=0
    X=int(input())
    for t in range(1,X):
        if(X%t==0):
            soma=soma+t
            print(t)
    if (soma==X):
        print(X,"é perfeito")
    else:
        print(X,"nao é perfeito")