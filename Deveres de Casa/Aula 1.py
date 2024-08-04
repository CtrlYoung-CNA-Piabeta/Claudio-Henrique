# Aula 1
numero = int(input('Qual seu número de funcionário? '))
horas = int(input('Quantas horas trabalhou? '))
valor = float(input('Qual o valor que recebes por hora? '))

salario = valor * horas

print(f"NUMBER = {numero}")
print(f"SALARY = U$ {salario:.2f}")