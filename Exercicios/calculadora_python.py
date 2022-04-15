#Calculadora Simples Python
#Com funcão, validações, estruturas de controle e repetição

#Funcões em lambda para as operações da calculadora
from time import sleep

#funcao soma
def soma(a):
    s = 0
    for x in a:
        s+=x
    return print(f'O resultado da soma entre {a[0]} e {a[1]} é {s}')

#funcao subtracao
def subtracao(a):
    sub = 0
    for c,x in enumerate(a):
        if c == 0:
            sub = x - sub
        else:
            sub-=x
    return print(f'O resultado da subtracao entre {a[0]} e {a[1]} é {sub}')

#funcao multiplicacao
def multiplicacao(a):
    m = 1  
    for x in a:
        m*=x
    return print(f'O resultado da soma entre {a[0]} e {a[1]} é {m}')

#funcao divisão
def divisao(a):
    d = a[0] / a[1]
    return print(f'O resultado da divisão entre {a[0]} e {a[1]} é {d}')

#função para solicitar os valores
def valores():
    n1 = int(input('Digite o primeiro valor: '))
    n2 = int(input('Digite o segundo valor:'))
    return n1, n2

codigo = list(range(1,6))

#Tela de inicio
while True:
    sleep(2)
    print('Digite a opção desejada:\n1- Soma\n2- Subtracao\n3- Multiplicação\n4- Divisão\n5- Sair')
    n = int(input('>>'))
    while n not in codigo:
        print('Código inválido! Digite novamente')
        n = int(input('>>'))
    if n == 1:
        soma(valores())
    elif n == 2:
        subtracao(valores())
    elif n == 3:
        multiplicacao(valores())
    elif n == 4:
        divisao(valores())
    else:
        print('Programa finalizado!\nVolte sempre!')
        break
        
    
