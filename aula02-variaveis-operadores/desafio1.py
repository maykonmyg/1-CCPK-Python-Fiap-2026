# Desafio 1

nomeProduto = (input("Digite o nome do produto: "))
precoProduto = float(input('Digite o preço do produto: '))
qtdProduto = float(input("Digite a quantidade comprada: "))
descProduto = float(input("Digite o em % o desconto: "))


vlbruto = precoProduto * qtdProduto
print(vlbruto)


valorDesc = precoProduto * (descProduto / 100)
print(valorDesc)

valFinal = vlbruto - valorDesc

print("O valor final é", valFinal)