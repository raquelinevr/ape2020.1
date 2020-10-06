# AVALIAÇÃO 2:
QUESTÃO 1:
Escreva um programa para ler uma temperatura
dada na escala Fahrenheit e exibir o equivalente
em Celsius.
 C= 5 
   --- (F-32)
    9 
   
temperatura=float(input('Informe a temperatura em Fahrenheit: '))
cel=(temperatura - 32) * 5/9
print('O valor da temperatura Fahrenheit em Celsius foi: ',cel, '°C')
  
    
QUESTÃO 2:
[URI – 1012 (Adaptada)] Área.
Escreva um programa que leia três
valores: A, B e C.
Em seguida, calcule e mostre:

a) a área do triângulo retângulo que tem A por base e C por
altura.

b) a área do círculo de raio C. (pi = 3.14159)

c) a área do trapézio que tem A e B por bases e C por altura.

d) a área do quadrado que tem lado B.

e) a área do retângulo que tem lados A e B.

a=float(input('Valor do lado A: '))
b=float(input('Valor do lado B: '))
c=float(input('Valor do lado C: '))

print('A area do triângulo que tem A por base e C por altura: ',a*c/2)
print('A área do círculo de raio C: ',2*314159*c)
print('A área do trapézio que tem A e B por bases e C por altura: ',(a+b)/2*c) 
print('A área do quadrado que tem lado B: ',b*b)
print('A área do retângulo que tem lados A e B: ',a*b)


QUESTÃO 3:
Uma certa empresa deseja aumentar o salário
de seus empregados em 20%.
Escrever um programa que leia o nome
e o salário atual de um empregado, e exiba o nome,
o salário atual e o salário reajustado.

nome=input('Seu nome: ')
salario=float(input('Seu salário: '))
sr=salario+(salario*20/100)
print('Olá',nome,'seu salario foi R$',salario,' e com um ajuste de 20% seu salario ficou R$',sr)


QUESTÃO 4:
Considerando a lista de produtos e seus
respectivos preços abaixo, escreva um programa
para ler as quantidades consumidas de cada produto
por um cliente, calcular e exibir o preço total
consumido.
Chocolate R$ 4,00
Refrigerante R$ 5,00
Misto Quente R$ 3,50
Sorvete R$ 3,00

c=int(input('Quantos chocolates você consumiu? '))
r=int(input('Quantos refrigerantes você consumiu? '))
m=int(input('Quantos mistos quentes você consumiu? '))
s=int(input('Quantos sorvetes você consumiu? '))
total=c*4+r*5+m*3.5+s*3

print('Voce consumiu',c, 'chocolate(s) e o preço total foi: R$',c*4)
print('Voce consumiu',r, 'refrigerante(s) e o preço total foi: R$',r*5)
print('Voce consumiu',m, 'misto(s) quente(s) e o preço total foi: R$',m*3.5)
print('Voce consumiu',s, 'sorvete(s) e o preço total foi: R$',s*3)
print('E o seu valor total foi de: R$:',total)


# AVALIAÇÃO 3

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
    print('Olá',matriculaop, 'sua classe foi A e seu salario foi:',salario)
else:
    print('Olá',matriculaop, 'sua classe foi B e seu salario foi: R$',x)


# AVALIAÇÃO 4

QUESTÃO 1:
Em uma pesquisa foram coletados os seguintes dados de um conjunto de 100 pessoas: sexo (M-masculino ou F-feminino), idade e estado civil (S-solteiro, C-casado, V-viúvo ou D-divorciado).
Neste contexto, faça um programa que leia os dados coletados durante a pesquisa, determine e mostre:
a) O percentual de mulheres;
b) O percentual de homens;
c) A média de idade das pessoas;
d) A quantidade de mulheres solteiras com idade inferior a 20 anos;
e) A quantidade de homens casados com idade superior a 30 anos.



QUESTÃO 2:
Faça um programa para ler o nome e o salário bruto dos 80 funcionários de uma determinada empresa.
Para cada funcionário lido, o programa deverá emitir o respectivo contracheque, que deverá conter:

O nome do funcionário;
O valor do salário bruto;
O valor do desconto do INSS (12% do Salário Bruto)
O valor do salário líquido (Salário Bruto - Desconto INSS)
Ao final, o programa deverá mostrar:

A soma total dos salários brutos;
A soma total dos descontos do INSS;
A soma total dos salários líquidos.

