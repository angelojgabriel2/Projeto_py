# variavesis : potencia , largura , comprimento ,
# numero de lampadas
# 
# a cada M² precisa de 3 watts / / 
# a cada 3m² tem um bocal

import math

potencia = int(input('Dequite a ' \
'potencia da lampada em wattas '))
largura = float(input( 'Digite a largura' \
'do comodo (em metros)'))
comprimento = float(input('Digite o ' \
'comprimento do comodo ( em metros):'))

# etapa dos calculos

area = largura * comprimento 

# saber quantos whatts necessito 

potencia_necessaria = area * 3

# saber quantas lampadas eu preciso para 
# chegar a potencia necessaria
numero_lampadas = \
math.ceil(potencia_necessaria/potencia)

# calcular o numero de bocais disponiveis  
numero_bocais = int ( area/3)

print(10*'-')
print(f'Area do Comodo: {area:.2f}m²')
print(f'Numero de Lamapadas: {numero_lampadas:}')
print(f'Numero de Bocais Estimados:\
       {numero_bocais:}')

if numero_lampadas > numero_bocais :
    print('Numero de Bocais Insuficientes')

