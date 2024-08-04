# Aula 9

# Desafio 1

count=0
for i in range(5):
    Num = float(input())
    if(Num%2==0):
        count=count+1
print("{} valores pares".format(count))

# Desafio 2

Contador = 0
X = int(input())
while Contador < 12:
    if X % 2 != 0:
        print(X)
    Contador += 1
    X += 1