cp = 0
while cp < 10:

    if cp == 3 or cp == 5:
        continue
    if cp == 7:
        break
    
    print(f"Produto {cp}")
    cp += 1

i = 4
while i > 0:
    print(i)
    i-= 1