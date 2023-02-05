
from functools import reduce

def somar_nota(delta):
    def resultado(nota):
        return nota + delta
    return resultado


notas = [6.4, 7.5, 4.0, 8.1]
notas_finais_1 = list(map(somar_nota(1.5), notas))
notas_finais_2 = list(map(somar_nota(1.6), notas))


print(notas_finais_1)
print(notas_finais_2)

total = 0

#for n in notas:
#    total += n

#print(total)

def soma(a, b):
    return a + b

total = reduce(soma, notas, 0)
print(total)

#for i, nota in enumerate(notas):
#    notas[i] = nota + 1.5

#for i in range(len(notas)):
#    notas[i] += 1.5

