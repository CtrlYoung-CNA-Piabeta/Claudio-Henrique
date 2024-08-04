# Aula 4
# Desafio 1

mes = int(input("Digite um Número de 1 a 12 "))
if mes == 1:
  print("Janeiro")
elif mes ==2:
  print("Fevereiro")
elif mes ==3:
  print("Março")
elif mes ==4:
  print("Abril")
elif mes ==5:
  print("Maio")
elif mes ==6:
  print("Junho")
elif mes ==7:
  print("Julho")
elif mes ==8:
  print("Agosto")
elif mes ==9:
  print("Setembro")
elif mes ==10:
  print("Outubro")
elif mes ==11:
  print("Novembro")
elif mes ==12:
  print("Dezembro")
else:
  print("Número Incorreto")
# Desafio 2

lanches = {
   "Cachorro_Quente" : 4.00,
   "X-Salada" : 4.50,
   "X-Bacon" : 5.00,
   "Torrada_simples" : 2.00,
   "Refrigerante" : 1.50,
    }
codigo = int(input())
quantidade = int(input())
if codigo == 1:
    X = 4.00
elif codigo == 2:
    X = 4.50
elif codigo == 3:
    X = 5.00
elif codigo == 4:
    X = 2.00
elif codigo == 5:
    X = 1.50
print("Total:R$", X * quantidade)