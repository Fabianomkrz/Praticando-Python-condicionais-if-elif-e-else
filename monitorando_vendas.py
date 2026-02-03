# Bruno gerencia um pequeno comércio e quer saber qual produto teve o melhor desempenho de vendas no mês passado. Ele registrou a quantidade vendida de dois produtos: maçãs e bananas. Agora, ele precisa escrever um programa que identifique e exiba qual deles teve maior venda.

# Crie um programa que receba o número de vendas dos dois produtos e exiba uma mensagem indicando qual deles vendeu mais. Se as quantidades forem iguais, exiba uma mensagem dizendo que houve empate.

# Recebendo o número de vendas dos produtos

venda_maças = int(input('Digite a quantidade de maças vendidas: '))
venda_bananas = int(input('Digite a quantidade de bananas vendidas: '))

# Comparando as vendas dos produtos e mostrando o retorno

if venda_maças > venda_bananas:
    print('As maças tiveram mais vendas.')
elif venda_bananas > venda_maças:
    print('As bananas tiveram mais vendas.')
else:
    print('Houve um empate na venda')