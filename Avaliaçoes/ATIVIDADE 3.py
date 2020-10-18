QUESTÃO 1:
Faça um programa que leia a altura e o sexo (M-masculino, F-feminino) de uma pessoa, calcule e mostre o seu peso ideal, utilizando uma das seguintes fórmulas:
para homens: (72.7 * altura) - 58.0
para mulheres: (62.1 * altura) - 44.7

altura=float(input('Informe a altura: '))
sexo=int(input('Informe o sexo:\n1-Feminino\n2-Masculino\n'))
pf=(72.7*altura) - 58.0
pm=(62.1*altura) - 44.7
if sexo==1:
    print('Seu peso ideal é de: ',pf)
elif sexo==2:
    print('Seu peso ideal é de: ',pm)
    
 
QUESTÃO 2:
Recomendam-se estudantes para bolsas de estudo em função de seu desempenho.
A natureza das recomendações é baseada na seguinte tabela:
 A - FORTEMENTE RECOMENDADO
 B OU C - RECOMENDADO 
 D - NÃO RECOMENDADO 
Faça um programa que leia o nome e o conceito de um estudante e exiba o nome do estudante e sua respectiva recomendação.

nome=input('Informe seu nome: ')
conceito=input('Informe seu conceito: A, B ou C, D: ')
if conceito == 'A':
    print('Olá',nome, 'sua recomendação foi: "Fortemente recomendado" ')
elif conceito == 'B' or conceito =='C':
    print('Olá',nome, 'sua recomendação foi: "Recomendado" ')
elif conceito == 'D':
    print('Olá',nome, 'sua recomendação foi: "Não recomendado" ')


QUESTÃO 3:
Uma determinada loja está oferecendo um desconto para os seus clientes, de acordo com o valor total de sua compra. O valor do desconto é determinado pela tabela abaixo:
 VALOR DA COMPRA  --- VALOR DESCONTO
   0 - 49,90          NENHUM DESCONTO
   50 - 99,99             R$ 5,00
   100 +                  R$ 20,00
Faça um programa que:

leia o valor da compra de um cliente;
calcule e mostre o valor do seu desconto;
calcule e mostre o valor final a pagar (valor da compra - desconto).

valorc=float(input('Informe o valor da compra: R$ '))
y=valorc-5.00
z=valorc-20.00
if valorc >=0.00 and valorc<=49.99:
    print('O valor final a pagar é: R$',valorc, 'Não houve desconto. ')
elif valorc >= 50.00 and  valorc<= 99.99:
    print('Sua compra foi: R$',valorc, 'Você teve um desconto de R$5,00 e o valor final a pagar foi: R$',y)
elif valorc >=100.00:
    print('Sua compra foi: R$',valorc, 'Você teve um desconto de R$20,00 e o valor final a pagar foi: R$',z)


QUESTÃO 4:
Numa fábrica trabalham homens e mulheres divididos em duas classes:

Classe A: os que fazem até 30 peças por mês;
Classe B: os que fazem mais de 30 peças por mês.
A classe A recebe um salário-mínimo.
A classe B recebe um salário-mínimo e mais R$ 10,00 por cada peça acima das 30 iniciais.
Escreva um programa que leia a matrícula do operário e o número de peças fabricadas por ele no mês.
Como resposta mostre a matrícula do operário, sua classe e o salário que ele deve receber.

matriculaop=int(input('Informe sua matricula: '))
np=int(input('Informe o numero de peças que você fabricou esse mês: '))
salario=1045
b=np-30
x=salario+b*10

if np <=30:
    print('Olá',matriculaop, 'sua classe foi A e seu salario foi: ',salario)
elif np >=30:
    print('Olá',matriculaop, 'sua classe foi B e seu salario foi: R$',x)

22/09/2020 09:55:28
