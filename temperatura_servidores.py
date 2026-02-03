# Lucas trabalha em TI e precisa garantir que a temperatura de uma sala de servidores não ultrapasse 25°C. Ele quer um programa que receba a temperatura atual como entrada e, se necessário, exiba uma mensagem de alerta.

# Recebendo a temperatura do servidor

temperatura = float(input('Digite a temperatura atual do servidor: '))

# Comparando a temperatura do servidor e exibindo o retorno

if temperatura > 25:
    print('Alerta! A temperatura está acima do limite permitido!')
else:
    print('Temperatura está dentro do permitido.')