# Excelente para loops dependentes de uma condição
# Publicar um produto com comissão de 10% se for acima de R$ 20,00

valor = int(input('Digite o valor do seu produto em R$: '))

while valor > 20:
    valor = (valor * 1.1)
    print(f'O valor final do seu produto será de R$ {valor}')
    break