1. Escreva um programa que gere aleatoriamente uma matriz quadrada A (cuja ordem será lida) e gere uma matriz B (da mesma ordem de A), onde cada elemento de B corresponderá ao respectivo elemento de A somado a ele os seus índices, sendo que se o elemento for de alguma diagonal (principal ou secundária) deverá ser colocado 0 (zero).
Veja o exemplo a seguir:

num_lc = int(input("Insira o grau da matriz: "))
matriz_a = [[None] * num_lc for i in range(num_lc)]
matriz_b = [[None] * num_lc for i in range(num_lc)]
for i in range(num_lc):
    for j in range(num_lc):
        matriz_a[i][j]=int(input("Insira um numero: "))
        if i == j:
          matriz_b[i][j] = 0
        
        elif i != j and i + j != (num_lc - 1):
          matriz_b[i][j] = matriz_a[i][j] + i + j
        elif i + j == (num_lc -1):
          
          matriz_b[i][j] = 0
        
for i in matriz_a:
  print(i)

print(20*'*')

for i in matriz_b:
  print(i)
 
 
2. Escreva um programa que:
Crie uma matriz de ordem 20 x 4 e armazene nela as 3 notas dos 20 alunos de uma turma e a média de cada um deles (obs: as notas serão lidas e as médias serão calculadas e armazenadas na 4ª coluna da matriz);
Imprima as notas dos alunos e suas respectivas médias (no formato de matriz);
Calcule e imprima a média geral da turma;
Calcule e imprima o número de alunos com média superior à média geral da turma.

matriz = [[None]* 4 for i in range(20)]
nota1 = 0
nota2 = 0
nota3 = 0
for i in range(20):
  count = 1
  for j in range(4):
    if count < 4:
      matriz[i][j] = float(input(f"Insira a nota do aluno: "))
      if count == 1:
        nota1 = matriz[i][j]
      elif count == 2:
        nota2 = matriz[i][j]
      elif count == 3:
        nota3 = matriz[i][j]
    else:
      matriz[i][j] = round((nota1 + nota2 + nota3)/3,1)
    count += 1

soma2 = 0
count2 = 0
for i in matriz:
  soma2 += i[3]
media = soma2/20

for i in matriz:
  if i[3] > media:
    count2 += 1

for i in matriz:
  print(i)

print(f"Média global: {media:.1f}")
print(f"Quantidade de alunos acima da média global: {count2}")
