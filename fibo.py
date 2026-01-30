# AULA 4 DIA 28 /01 sequencia de fibonati 

# Construa uma programação que exiba a 
# sequencia de Fibonacci de zero ate dois mil 

# 3 numeros
# 2 anteriores , 1 'atua'

# começar a atualizar pelo anterior - descarta ele 

anterior = 1
atual = 2
proximo = anterior + atual # 3
while proximo <=2000 :
    anterior = atual # ou coloca atual aqui 
    atual = proximo # para antes de 2000
    proximo = atual + anterior 
    print(proximo)


    # fobonacci estilo python

    fibo1, fibo2 = 0, 1

while fibo1 <= 2000:
    print(fibo1)
    fibo1, fibo2 = fibo2, fibo1 + fibo2





