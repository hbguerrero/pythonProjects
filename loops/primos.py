import time
inicio = time.time()

for i in range(0,31):
    conta = 0
    for n in range(1, i+1):
        residue = i%n
        if residue == 0:
            conta = conta + 1
              
    if conta == 2:
        print(f'{i} es un primo')
        
fin = time.time()
print("t = ", (fin - inicio)*1000)