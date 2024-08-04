# Aula 2
# Desafio 1
frase = input('Me fale alguma frase: ')
vogais = 0
espacos = 0
for letra in frase:
    if letra == " ":
        espacos += 1
    elif letra in 'aeiou':
        vogais += 1
print("A frase que você enviou tem", vogais, "vogais e", espacos, "espaços vazios.")
# Desafio 2
for x in ("Ctrl+Play "):
   print(x)

nome = str('Ctrl+Play')
vazia = ''
for letra in nome:
    vazia += letra
    print(vazia)

# Desafio 3
nome = input("Digite seu nome completo: ")
cadaPalavra = nome.split()
print("Seu primeiro nome é:", cadaPalavra[0])
print("Seu sobrenome nome é:", cadaPalavra[1])
print("O seu ultimo nome é:", cadaPalavra[len(cadaPalavra) - 1])



