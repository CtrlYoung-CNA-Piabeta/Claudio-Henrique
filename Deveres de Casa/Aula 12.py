# OBS: Aula 10 é so pra colocar todos os desafios no beecrowd e a Aula 11 colocar no Git Hub

# Aula 12

# Desafio 1

X = int(input('Qual foi a distancia percorrida? '))
Y = float(input('Qual foi o total de combustível gasto? '))
consumo = X / Y
print("%0.3f km/l" %consumo)

# Desafio 2

n = int(input())
print("{}:{}:{}".format(int(n/3600),int(n%3600/60),int(n%60)))