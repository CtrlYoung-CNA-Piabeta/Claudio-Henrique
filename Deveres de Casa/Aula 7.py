# Aula 7

# Desafio 1

a,b,c=list(map(int,input().split()))
print("{} é o maior".format(max(a,b,c)))

# Desafio 2

Num = int(input())
Valor = Num
Notas = [100, 50, 20, 10, 5, 2, 1]
Cont = 0
print(Valor)
for i in range(len(Notas)):
    Cont = Num // Notas[i]
    Num %= Notas[i]
    print('{} nota(s) de R$ {},00'.format(Cont, Notas[i]))