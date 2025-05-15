nome = (input('O nome do vendedor:'))

valor_fixo = float (input('o valor fixo do vendedor é:'))
valor_de_vendas = float(input('A quantidade foi:'))
print(valor_fixo)
print(valor_de_vendas)

soma = valor_fixo + (valor_de_vendas * 15 / 100)
print(f'o nome do vendedor é: {nome} é o seu valor fixo é de:{valor_fixo} o seu valor total de vendas foi: {valor_de_vendas} é a soma da porcentagem de 15% da o total de: {soma}')