Utilizando quaisquer dos comandos, funções e operadores vistos até a Semana 8,
faça programas Python para resolver as questões abaixo.

1. Escreva um programa que leia um vetor contendo 100 elementos inteiros,
calcule e exiba:
 A quantidade de elementos pares;
 A quantidade de elementos ímpares;
 A soma de todos os elementos;
 A média dos elementos do vetor.

n = 5
impar = 0
par = 0
soma = 0 
v = [None]*n

for i in range(n):
    v[i]=int(input('Informe o número: '))

    if v[i]% 2 == 0:
        par = par + 1
    else:
        impar = impar + 1
        
    soma=soma+v[i]
    media=soma/n

print(f'Elementos pares: {par} ')
print(f'Elementos ímpares: {impar} ')
print(f'Soma dos elementos: {soma} ')
print(f'Média dos elementos: {media:.1f} ')


2. Escreva um programa que leia um vetor gabarito de 10 elementos.
Cada elemento de gabarito contém a letra A, B, C, D ou E, correspondente as
opções corretas de uma prova objetiva. Em seguida o programa deve ler um outro vetor contendo as respostas de um
aluno. O programa deve comparar os dois vetores e escrever o número de acertos do aluno.

total=0
v=10
gabarito=[None]*v
respostas=[None]*v

print('Informe as respostas do gabarito\n[A] [B] [C] [D] ou [E]')
for i in range(v):
    gabarito[i] = input()

print('\nInforme as respostas do aluno:')
for i in range(v):
    respostas[i]=input()

resp=True
for i in range(v):
    if gabarito[i]==respostas[i]:
        total+=1

print(f'Olá, o(a) aluno(a) acertou {total} questões. ')
