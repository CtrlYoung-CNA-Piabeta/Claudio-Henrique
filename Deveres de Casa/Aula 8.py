# Aula 8

# Desafio 1

Num = float(input())
if(Num<0 or Num>100):
     print("Fora de intervalo")
elif(Num>=0 and Num<=25):
     print("Intervalo [0,25]")
elif(Num>25 and Num<=50):
     print("Intervalo (25,50]")
elif (Num>50 and Num<=75):
     print("Intervalo (50,75]")
elif (Num>75 and Num<=100):
     print("Intervalo (75,100]")

# Desafio 2

X,Y=list(map(int,input().split()))
if(X<Y):
    time=Y-X
else:
    time=Y+24-X
print("O jogo durou {} hora(S)".format(time))