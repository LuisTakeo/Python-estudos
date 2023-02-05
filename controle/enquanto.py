quantidadeNotas = 0
nota = 0
total = 0

while nota != -1:
    nota = float(input('Informe uma nota de 0 a 10 ou -1 para sair '))
    if nota >= 0 and nota <= 10:
        quantidadeNotas += 1
        total += nota
    elif nota == -1:
        print('Calculos encerrados, vamos as notas.')
    else:
        print('Nota invalida. ')


print(f'A média da turma é de {total / quantidadeNotas}')

