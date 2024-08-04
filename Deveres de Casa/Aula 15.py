# Aula 15

# Desafio 1

N = int(input())
i = 1
while i <= N:
    print('{0} {1} {2}'.format(i,i*i,i**3))
    i+=1

# Desafio 2

Senha=0000
while (Senha!=2002):
    Senha=int(input())
    if Senha!=2002:
        print("Senha Invalida")
print("Acesso Permitido")