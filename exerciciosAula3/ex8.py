salario = float(input("Digite o salário do colaborador: "))

if salario <= 280:
    porcentagem = 20
elif salario < 700:
    porcentagem = 15
elif salario < 1500:
    porcentagem = 10
else:
    porcentagem = 5

aumento = salario * (porcentagem / 100)
salarioFinal = salario + aumento

print(f"Salário antes do reajuste: R${salario:.2f}")
print(f"Percentual de aumento: {porcentagem}%")
print(f"Valor do aumento: R${aumento:.2f}")
print(f"Novo salário: R${salarioFinal:.2f}")   