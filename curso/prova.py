produtos = { 
    10: ("Sanduiche", 5.00),
    20: ("Refrigerante", 3.00),
    30: ("Suco", 2.50),
    40: ("Pastel", 4.00)
}
print('Menu de Produtos:')
for codigo, (nome, preco) in produtos.items():
    print(f'{codigo} - {nome} - R${preco:.2f}')

total = 0

while True:
    codigo = int(input('\nDigite o código do produto (ou um valor inválido para encerrar): '))

    if codigo in produtos:
        nome, preco = produtos[codigo]
        total += preco
    else:
        break

print(f'\nVocê deverá pagar R${total:.2f}')        
