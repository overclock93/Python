velocidade = int(input('Digite a velocidade do veiculo: '))


if velocidade > 110:
    print('Acima da velocidade permitida')
    print('Favor reduzir a sua velocidade')
elif velocidade <= 60:
    print('Por favor dirigir acima de 80 KM/h')
else:
    print('Velocidade OK')
