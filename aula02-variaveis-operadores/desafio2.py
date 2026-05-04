# Desafio 2

nomecolab = input('digite seu nome: ')
valortrabalho = float(input('valor hora: '))
hrtrabalho = float(input('horas trabalhadas: '))
bonusfinal = float(input("Digite o valor do bonus"))
descontoLula = float(input("Digite as taxas do amor: "))

salarioBruto = valortrabalho * hrtrabalho + bonusfinal
print(salarioBruto)

desctotal = salarioBruto * (descontoLula / 100)


salarioliquido = salarioBruto - desctotal

print('o salario liquido é igual a', salarioliquido)