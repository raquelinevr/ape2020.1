1. Escreva um programa que preencha duas matrizes (A e B), ambas de ordem 2x3, com valores inteiros fornecidos pelo usuário (ou gerados aleatoriamente).
O programa deverá somar as duas matrizes, armazenando o resultado em uma terceira matriz (C).
Ao final, exiba as 3 matrizes (no formato de matriz). 

nlin = 2  # número de linhas da matriz
ncol = 3  # número de colunas da matriz

# Criação das matrizes
a = [[None]*ncol for i in range(nlin)]
b = [[None]*ncol for i in range(nlin)]
c = [[None]*ncol for i in range(nlin)]

# Leitura da matriz A
print('Digite os elementos da Matriz A:')
for i in range(nlin):
    for j in range(ncol):
        a[i][j] = int(input(f'A[{i}][{j}]: '))

# Leitura da matriz B
print('\nDigite os elementos da Matriz B:')
for i in range(nlin):
    for j in range(ncol):
        b[i][j] = int(input(f'B[{i}][{j}]: '))

# Cálculo da matriz C
for i in range(nlin):
    for j in range(ncol):
        c[i][j] = a[i][j] + b[i][j]

# Impressão da matriz A
print('\nMatriz A:')
for i in range(nlin):
    for j in range(ncol):
        print(f'{a[i][j]:4}',end='')
    print()
      
# Impressão da matriz B
print('\nMatriz B:')
for i in range(nlin):
    for j in range(ncol):
        print(f'{b[i][j]:4}',end='')
    print()

# Impressão da matriz C
print('\nMatriz C:')
for i in range(nlin):
    for j in range(ncol):
        print(f'{c[i][j]:4}',end='')
    print()


2. Escreva um programa que:
Leia (ou gere aleatoriamente) uma matriz quadrada de ordem N contendo elementos inteiros (N será lido);
Exiba a matriz lida (no formato de matriz);
Exiba os elementos da diagonal principal, isto é, os elementos onde I = J.

# Leitura da ordem da matriz quadrada
n = int(input('Digite a ordem da matriz: '))
# Criação da matriz
m = [[None]*n for i in range(n)]
# Leitura da matriz
print('\nDigite os elementos da matriz:')
for i in range(n):
    for j in range(n):
        m[i][j] = int(input(f'm[{i}][{j}]: '))
# Exibição da matriz
print('\nMatriz:')
for i in range(n):
    for j in range(n
                   ):
        print(f'{m[i][j]:4}',end='')
    print()

# Exibição da diagonal principal
print('\nDiagonal Principal:')
for i in range(n):
    for j in range(n):
        if i == j:
            print(f'{m[i][j]:4}',end='')


3. Escreva um programa que gere (aleatoriamente) e imprima (no formato de matriz) uma matriz quadrada onde cada elemento será definido da seguinte forma:
Se i < j, então o elemento será igual ao j;
Se i = j, então o elemento será igual a 0 (zero);
Se i > j, então o elemento será igual ao i.
Obs: a ordem da matriz será lida.

# Leitura da ordem da matriz
n = int(input('Ordem da matriz: '))
# Criação da matriz
m = [[None]*n for i in range(n)]
# Cálculo dos elementos da matriz
for i in range(n):
    for j in range(n):
        if i < j:
            m[i][j] = j
        elif i == j:
            m[i][j] = 0
        else:
            m[i][j] = i

# Impressão da matriz
print('\nMatriz:')
for i in range(n):
    for j in range(n):
        print(f'{m[i][j]:4}',end='')
    print()

Uma matriz transposta é a matriz que se obtém da troca de linhas por colunas de uma dada matriz.
Assim, dada uma matriz C de ordem m x n, a matriz transposta dela será representada por Ct de ordem n x m onde cada elemento de Ct[i,j] = C[j,i].

Escreva um programa que preencha uma matriz 3x5 com valores inteiros fornecidos pelo usuário (ou gerados aleatoriamente) e gere a sua transposta.
Ao final, imprima as duas matrizes (no formato de matriz).

x = 2  # número de linhas da matriz M 
y = 3  # número de colunas da matriz M

# Criação das matrizes
m = [[None]*y for i in range(x)]
t = [[None]*x for i in range(y)]

# Leitura da matriz M
print('Digite os elementos da Matriz M:')
for i in range(x):
    for j in range(y):
        m[i][j] = int(input(f'M[{i}][{j}]: '))

# Geração da matriz T (transposta)
for i in range(y):
    for j in range(x):
        t[i][j] = m[j][i]

# Impressão da matriz M
print('\nMatriz M:')
for i in range(x):
    for j in range(y):
        print(f'{m[i][j]:4}',end='')
    print()
      
# Impressão da matriz T
print('\nMatriz T (transposta):')
for i in range(y):
    for j in range(x):
        print(f'{t[i][j]:4}',end='')
    print()


5. Escreva um programa que preencha uma matriz quadrada de ordem 3 com valores inteiros fornecidos pelo usuário (ou gerados aleatoriamente).
O programa deverá calcular e exibir:
a) A soma dos elementos de cada linha;
b) A soma dos elementos de cada coluna;
c) A soma dos elementos da diagonal principal da matriz;
d) A soma dos elementos da diagonal secundária da matriz;
e) A soma de todos os elementos da matriz.

n = 3  # Ordem da matriz quadrada
# Criação da matriz
m = [[None]*n for i in range(n)]

# Leitura da matriz
'''
print('\nDigite os elementos da matriz:')
for i in range(n):
    for j in range(n):
        m[i][j] = int(input(f'M[{i}][{j}]: '))
'''

# Geração aleatória dos elementos da matriz 
import random
for i in range(n):
    for j in range(n):
        m[i][j] = random.randint(1,10)

# Exibição da matriz
print('\nMatriz:')
for i in range(n):
    for j in range(n):
        print(f'{m[i][j]:4}',end='')
    print()

# Soma das linhas
print('\nSoma de cada linha:')
for i in range(n):
    s = 0
    for j in range(n):
        s += m[i][j]
    print(f'{s:4}')

# Soma das colunas
print('\nSoma de cada coluna:')
for j in range(n):
    s = 0
    for i in range(n):
        s += m[i][j]
    print(f'{s:4}',end='')

# Soma da diagonal principal
print('\n\nSoma da diagonal principal:')
s = 0
for i in range(n):
    for j in range(n):
        if i == j:
            s += m[i][j]
print(f'{s:4}')

# Outra forma para a soma da diagonal principal
'''
print('\n\nSoma da diagonal principal:')
s = 0
for i in range(n):
    s += m[i][i]
print(f'{s:4}')
'''

# Soma da diagonal secundária
print('\nSoma da diagonal secundária:')
s = 0
for i in range(n):
    for j in range(n):
        if i == n-j-1:  # outra condição possível:  i+j == n-1 
            s += m[i][j]
print(f'{s:4}')

# Outra forma para a soma da diagonal secundária
'''
print('\nSoma da diagonal secundária:')
s = 0
for i in range(n):
    s += m[i][n-i-1]
print(f'{s:4}')
'''

# Mais outra forma para a soma da diagonal secundária
'''
print('\nSoma da diagonal secundária:')
s = 0
j = n-1
for i in range(n):
    s += m[i][j]
    j -= 1
print(f'{s:4}')
'''

# Soma de toda a matriz
print('\nSoma de toda a matriz:')
s = 0
for i in range(n):
    for j in range(n):
        s += m[i][j]
print(f'{s:4}')
