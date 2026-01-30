# instalaras extençoes : jupyter , Pylance , Code Runner ,Error lens ,
# portuguese , python , python debugguer


# Variaveis ( Boas Praticas )
# Nao Pode 
# 1 . iniciar com numeoro 
# 2 . Ter espaço 
# Nao comece comcaractere especial 
# ex : _ab =1 

# Ideal --- Comeecar com letra minuscula 
# ideal --- Usar uma so formatacao 
# obs : Tudo maiosculo indica uma Constatnte 

# FORMATAÇAO
# 1 -- caso da cobra : Underline no lugar do espaço
# ex : Rio_de_janeiro = 'Cuidado'

# 2 -- caso camelo : Onde teria o espaço ,letra minuscula
# ex : rioDeJaneiro = 'Cuidado redobrado'

# 3 -- àscal case  : Usado para classes ( Sempre Inicia a palavra com letra Minuscula)
# Ex RioDeJaneiro = 'a'

# Etapa 1 : Pegar as notas (4)

nota1 = float(input('Digite a primeira nota:  '))
nota2 = float(input('Digite a segunda nota:  '))
nota3 = float(input('Digite a terceira nota:  '))
nota4 = float(input('Digite a quarta nota:  '))

media = ( nota1 + nota2 + nota3 + nota4)/4

print('Media do aluno (a):  ', media)

if media > 7:
    print('Aprovado')
elif media >=5 and media <=7:
    print('Recuperaçao')
else:
    print ('Reprovado')


