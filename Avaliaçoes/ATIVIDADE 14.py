1. O Grau de Obesidade de uma pessoa pode ser obtido através do seu Índice de Massa Corpórea (IMC), conforme a tabela abaixo.
Já o IMC é obtido através da fórmula:
Com base nas informações acima, escreva:
Uma função que receba o peso e a altura de uma pessoa e retorne o seu IMC
Uma função que receba como parâmetro o IMC de uma pessoa e retorne o seu Grau de Obesidade.
Um programa que leia do teclado o nome, o peso e a altura de 30 pessoas e, usando as funções criadas nos dois itens anteriores, calcule e exiba o nome, o IMC e o grau de obesidade dessas pessoas. 

for i in range (30):
  def imc (peso,alt):
    altura = alt * alt
    imc = peso / altura
    return imc

  def grau_obs(imc):
    if imc < 26:
      return 'Normal'
    elif imc < 30:
      return 'Obeso'
    else:
      return 'Obeso Mórbido'

  nome = input('Nome: ')
  peso = float(input('Peso: '))
  alt  = float(input('Altura: '))
  
  a = imc(peso,alt)
  b = grau_obs(a)
  print(f'\nNome: {nome}\nIMC: {a:.2f}\nVocê está {b}\n') 


2. Escreva uma função que receba uma matriz quadrada como parâmetro e retorne um vetor contendo os elementos da diagonal principal dessa matriz.
Escreva também um programa que:
Gere aleatoriamente uma matriz quadrada de ordem N (obs: N será lido);
Imprima a matriz gerada (no formato de matriz);
Usando a função criada, determine e imprima a diagonal principal da matriz.

from random import randint
def matriz(m):
    b = []
    nlc = len(m)
    for i in range (nlc):
      for j in range (nlc):
        if i == j:
          c = m[i][j]
          b.append(c)
    return b

def geraMat(nlc):
    m = [[None] * nlc for i in range(nlc)]
    for i in range(nlc):
        for j in range(nlc):
            m[i][j] = randint(1,101)
    for i in range(nlc):
        for j in range(nlc):
            print(f'{m[i][j]:4}',end='')
        print()
    return m

nlc = int(input('Ordem da matriz: '))
print('\nMatriz quadrada:')
m1 = geraMat(nlc)
c = matriz(m1)
print(f'\nDiagonal principal: \n{c}')
