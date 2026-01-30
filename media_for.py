# AULA 4 DIA 28 /01 AULA DE LOOP

# exercicio de loop for 

# 10 alunos # usuario vai dar a nota 
# 2 notas de cada aluno 
# fazer media de cada aluno 

# ao usar o for voce usa o range para incluir a lista 
# no for ir de 0 a 9 
# se sabe o limite use o while se nao souber use o for

for i in range(0, 10):
    nota1 = float(input('Digite a primeira nota:  '))
    nota2 = float(input('Digite a segunda nota:  '))

    media = (nota1 + nota2 )/2
    print( f'Aluno {i+1} - Media {media}') # f formatação de string usado muito no print 

