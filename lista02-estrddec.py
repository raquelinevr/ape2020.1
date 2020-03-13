1.Escreva um programa que leia um número inteiro e determine se ele é par ou ímpar

n1=int(input('informe um numero: '))
valor=n1%2

if valor==0:
    print('O número é par')
else:
    print('O número é impar')

--

2.Escreva um programa que leia dois números e exiba-os em ordem crescente.

n1=int(input('Informe o primeiro numero: '))
n2=int(input('Informe o segundo numero: '))

if n1>n2:
  print(n2,n1)
else:
  print(n1,n2)

--

3.Escreva um programa que leia 3 números inteiros, determine e mostre o maior deles.

n1=int(input('Informe o primeiro número: '))
n2=int(input('Informe o segundo número: '))
n3=int(input('Informe o terceiro número: '))

if n1>n2 and n1>n3:
  print('O maior número foi', n1)
if n2>n1 and n2>n3:
  print('O maior número foi', n2)
if n3>n1 and n3>n2:
  print('O maior número foi o', n3)
  
--

4.Escreva um programa que leia o nome e o sexo (M ou F) de uma pessoa e exiba a mensagem 
"Olá, Sr. Fulano!" ou "Olá, Sra. Fulana!", de acordo com o sexo da pessoa.
Obs: Fulano e Fulana são nomes exemplos.

nome=input('Informe seu nome: ')
sexo=input('Informe seu sexo [M/F]: ')

if sexo == 'M':
    print('Olá, Sr.',nome)
if sexo == 'F':
     print('Olá, Sra.',nome)
     
--
    
5.A empresa Vende Tudo Ltda paga o salário de cada vendedor com uma comissão de 5% sobre o total
de vendas daquele vendedor, mas essa comissão nunca deve ser inferior ao salário mínimo.
Escreva um algoritmo que leia o valor total das vendas de um vendedor e escreva seu salário. 


6.Escreva um programa para  determinar  as  raízes  de  uma  equação  de  segundo  grau,  dados  os 
seus coeficientes.
Fórmulas: 
Obs: se Δ for negativo, não existem as raízes da equação. Dica: use a função sqrt do módulo math.


7.Escreva um programa que tenha a funcionalidade de uma calculadora simples.
O programa deve solicitar a digitação de dois operandos e um operador (+ - x * / %)
e deve imprimir ao resultado da operação aritmética.
Caso o usuário digite um operador inválido, o programa deve imprimir "Operador desconhecido".

n1=int(input('Informe o primeiro operando: '))
n2=int(input('Informe o segundo operador: '))
op=str(input('Informe o operador: '))
if op=='+':
	print(n1+n2)
elif op=='-':
	print(n1-n2)
elif op=='*':
	print(n1*n2)
elif op=='/':
	print(n1//n2)
elif op=='%':
	x=n1/100
	z=x*n2
	y=z
	print(y)
else: 
    print('Operador desconhecido')
    
--

8.Escreva um programa que solicite a digitação de um número (de 1 a 7) correspondente a um dia da semana
e imprima o nome do dia da semana e se é dia útil (de segunda a sexta) ou final de semana
(sábado e domingo). Considere que o dia 1 é o domingo.

dia=int(input('Informe um numero (de 1 a 7): '))
if dia =='1':
    print('Hoje é domingo. Fim de semana. ')
if dia =='2':
    print('Hoje é segunda. Dia útil. ')
if dia =='3':
    print('Hoje é terça. Dia útil. ')
if dia =='4':
    print('Hoje é quarta. Dia útil. ')
if dia =='5':
    print('Hoje é quinta. Dia útil. ')
if dia =='6':
    print('Hoje é sexta. Dia útil. ')
if dia =='7':
    print('Hoje é sábado. Fim de semana. ') # sem aspas

--

9.Escreva um programa que solicite a digitação de um caractere qualquer do teclado e imprima 
sua classificação: vogal, consoante, número e caractere especial. 

