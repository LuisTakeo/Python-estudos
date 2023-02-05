
def saudacao_pela_manha(nome = 'pessoa', idade = 20):
    print(f'Bom dia {nome}!\n Você nem parece ter {idade} anos')


#def saudacao():
#    print('Boa tarde')

print(__name__)

def soma_e_multi(a, b, x):
    return a + b * x #esse 'a' só esta dentro deste escopo

if __name__ == '__main__':
    saudacao_pela_manha('Ana', 33)