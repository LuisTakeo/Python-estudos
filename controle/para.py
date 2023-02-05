
for i in range(10):
    print(i, end=' ')

print('')
print('')
for i in range(1, 11):
    print(i, end=' ')

print('')
print('')
for i in range(0, 50, 5):
    print(i, end=' ')

print('')
print('')
for i in range(20, 0, -2):
    print(i, end=' ')

print('')
print('')
nums = [2, 4, 6, 8]

for n in nums:
    print(n, end=' ')

print('')
print('')
texto = 'Python é muito massa!'

for letra in texto:
    print(letra, end=' ')

print('')
print('')

for n in {1, 2, 3, 4, 4, 4}:
    print(n, end=' ')

print('')
print('')

produto = {
    'nome': 'Caneta',
    'preco': 8.80,
    'desc': 0.5
}

for atrib in produto:
    print(f'{atrib}: {produto[atrib]}')

print('')
print('')
for atrib, valor in produto.items():
    print(f'{atrib}==> {valor}')

print('')
print('')
for valor in produto.values():
    print(valor, end=' ')

print('')
print('')
for atrib in produto.keys():
    print(atrib, end=' ')
