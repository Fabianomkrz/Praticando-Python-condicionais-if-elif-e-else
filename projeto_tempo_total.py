# Camila está organizando um projeto e precisa calcular o tempo total necessário para concluir três atividades: A, B e C. No entanto, se alguma atividade tiver um número de dias negativo, o código deve avisar que os valores inseridos são inválidos e não calcular o total.

# Escreva um programa que receba o número de dias de três atividades e exiba o tempo total do projeto. Se algum valor for negativo, mostre uma mensagem informando o erro.

# Recebendo o número de dias de cada atividade

ativ_a = int(input('Digite o tempo da atividade A: '))
ativ_b = int(input('Digite o tempo da atividade B: '))
ativ_c = int(input('Digite o tempo da atividade C: '))

# Comparando a nota das atividades e mostrando o retorno

if ativ_a >= 0 and ativ_b >= 0 and ativ_c >= 0:
    tempo_total = ativ_a + ativ_b + ativ_c
    print(f'O tempo total do projeto foi de {tempo_total} dias!')
else:
    print('Os dias não podem ser negativos!')