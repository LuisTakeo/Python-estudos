a = 3
b = 4.4

print(a + b)

texto = "Sua idade é..."
idade = 23

#print(texto + str(idade))
print(f'{texto} {idade}')

saudacao = 'bom dia'
print(3 * saudacao)

PI = 3.14
raio = float(input('Informe o raio da circunferencia? '))
area = PI * pow(raio, 2)

#print(type(raio))
print(f'A área da circunferencia é {area} m2.')
print('A variavel ', area, 'm2.')