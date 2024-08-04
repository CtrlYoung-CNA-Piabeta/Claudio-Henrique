# Aula 13

# Desafio 1

x = input()
y = input()
z = input()
if x == 'vertebrado' and y == 'ave' and z == 'carnivoro':
    a = 'aguia'
if x == 'vertebrado' and y == 'ave' and z == 'onivoro':
    a = 'pomba'
if x == 'vertebrado' and y == 'mamifero' and z == 'onivoro':
    a = 'homem'
if x == 'vertebrado' and y == 'mamifero' and z == 'herbivoro':
    a = 'vaca'
if x == 'invertebrado' and y == 'inseto' and z == 'hematofago':
    a = 'pulga'
if x == 'invertebrado' and y == 'inseto' and z == 'herbivoro':
    a = 'lagarta'
if x == 'invertebrado' and y == 'anelideo' and z == 'hematofago':
    a = 'sanguessuga'
if x == 'invertebrado' and y == 'anelideo' and z == 'onivoro':
    a = 'minhoca'
print(a)

# Desafio 2

nota_valida = 0
x=0
media=0
while nota_valida!=2:
    x = float(input())
    if x>=0 and x<=10:
        media+=x/2
        nota_valida+=1
    else:
        print('nota invalida')


print('media = %.2f'%(media))