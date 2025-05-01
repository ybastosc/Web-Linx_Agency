# AULA 1


def imprimir(a, b, c):
    print(a, b, c)


imprimir(1, 2, 3)
imprimir(4, 5, 6)


# AULA 2
def saudacao(nome='Sem nome'):
    print(f'Olá, {nome}!')


saudacao('Yan')
saudacao('Bastos')
saudacao()



# AULA 3
def soma(x, y):
    # Definição
    print(f'{x=} y={y}', '|', 'x + y = ', x + y)

soma(1, 2)
soma(y=2, x=1)

def soma(x, y, z=None):
    if z is not None:
        print(f'{x=} {y=} {z=}', x + y + z)
    else:
        print(f'{x=} {y=}', x + y)

soma(1, 2)
soma(3, 5)
soma(100, 200)
soma(7, 9 ,0)

# AULA 4

x = 1

def escopo ():
    global x
    x = 10

    def outra_funcao():
        global x
        x = 11
        y = 2
        print(x, y)

    outra_funcao()
    print(x)


print(x)
escopo()
print(x)