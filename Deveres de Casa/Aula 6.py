#Aula 6

# Desafio 1

pergunta = input("Informe o DDD a sua escolha: ")
DDD = {
    "61" : "Brasilia",
    "71": "Salvador",
    "11": "São Paulo",
    "21": "Rio de Janeiro",
    "31": "Juiz de Fora",
    "19": "Campinas",
    "27": "Vitoria",
    "31": "Belo Horizonte",
}
if pergunta in DDD:
  print(DDD[pergunta])
else:
  print("DDD não cadastrado")

# Desafio 2

numero = int(input())

X = total_coelhos = NumTotal = TotalRatos = TotalSapos = 0

while X < numero:
    Quantidade,Tipo = input().split(" ")
    Quantidade = int(Quantidade)
    while Quantidade < 1 or Quantidade > 15:
        Quantidade,Tipo = input().split(" ")
        Quantidade = int(Quantidade)
    Tipo = str(Tipo)
    if Tipo == 'C':
        total_coelhos+=Quantidade
    elif Tipo == 'R':
        TotalRatos+=Quantidade
    elif Tipo == 'S':
        TotalSapos+=Quantidade
    NumTotal += Quantidade
    X+=1

PorcenCoelho = PorcenRato = PorcenSapo = 0
PorcenCoelho = (total_coelhos*100.00)/NumTotal
PorcenRato = (TotalRatos*100.00)/NumTotal
PorcenSapo = (TotalSapos*100.00)/NumTotal

print('Total: %d cobaias'%(NumTotal))
print('Total de coelhos: %d'%(total_coelhos))
print('Total de ratos: %d'%(TotalRatos))
print('Total de sapos: %d'%(TotalSapos))
print('Percentual de coelhos: {:.2f} %'.format(PorcenCoelho))
print('Percentual de ratos: {:.2f} %'.format(PorcenRato))
print('Percentual de sapos: {:.2f} %'.format(PorcenSapo))