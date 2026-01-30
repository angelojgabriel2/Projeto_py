

# Somente notas de 0 a 10

nota = float(input('Digite a nota:  '))

while nota < 0 or nota > 10:
    print ('Valor invalido , Digite novamente ')
    nota = float(input('Digite a nota:  '))

    print(nota)