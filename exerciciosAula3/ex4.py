mat = 5
port = 5
geo = 5
hist = 5

nota = (mat + port + geo + hist) / 4
print(nota)
if( nota < 5):
    print("Reprovado")
else:
    if (nota >= 5 and nota <= 7):
        print("Recuperação")
    else:
        print("Aprovado")

print("Fim")    