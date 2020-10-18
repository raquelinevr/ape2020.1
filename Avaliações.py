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

m=0
f=0
ms2=0
hc3=0
pf=0
pm=0
idm=0

for i in range(5):
    sexo=input('Sexo: [M/F] ').upper()
    idade=int(input('Informe a idade: '))
    estc=input('Estado civil:\nS- SOLTEIRO\nC-CASADO\nV-VIUVO\nD-DIVORCIADO\nOpção:  ').upper()

    if sexo=='F':
        f=f+1
        pf=pf+1
        if idade < 20 and estc=='S':
            ms2=ms2+1
        idm=idm+idade
    else:
        m=m+1
        pm=pm+1
        if estc=='C' and idade>30:
            hc3=hc3+1
        idm=idm+idade

total=pf+pm
percf=pf/total*100
percm=pm/total*100
media=idm/5

print(f'\nPercentual de mulheres: {percf:.2f}% ')
print(f'Percentual de homens: {percm:.2f}% ')
print(f'Média de idade das pessoas: {media} ')
print(f'Mulheres solteiras com idade inferior a 20: {ms2} ')
print(f'Homens casados com idade superior a 30: {hc3} ')


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

sb=0
sd=0
sl=0

for i in range(3):
    nome=input('Informe o nome: ')
    salario=float(input('Informe o salario: '))

    desc=salario*0.12
    saliq=salario-desc

    print('====================')
    print(f'==== CONTRACHEQUE ====')
    print(f'Nome: {nome}')
    print(f'Salário Bruto: R${salario} ')
    print(f'Valor descontado do INSS: R$ {desc:.2f} ')
    print(f'Valor do salário liquído: R$ {saliq:.2f}')
    print('====================')

    sb=sb+salario
    sd=sd+desc
    sl=sl+saliq
print('---------------------------------')
print(f'======= TOTAL =======')
print(f'Total dos salarios brutos: R$ {sb:.2f} ')
print(f'Total dos descontos do INSS: R${sd:.2f} ')
print(f'Total dos salários líquidos: R${sl:.2f} ')

#AVALIAÇÃO 5 

QUESTÃO 1:
Faça um programa que, para cada um dos vários alunos de uma turma, leia o
nome e as três notas do aluno (a leitura do nome FIM indica o fim dos dados de
entrada), mostre o nome, a média final e o conceito, sabendo-se que:
 A média final é calculada pela média aritmética das 3 notas;
 O conceito é determinado de com base na tabela abaixo:
MÉDIA FINAL    CONCEITO
 7,0              A
 4,0 e < 7,0      B
< 4,0              C
Determine e mostre também:
 A quantidade de alunos com conceito A;
 A quantidade de alunos com conceito B;
 A quantidade de alunos com conceito C;
 A quantidade total de alunos da turma.

a=0
b=0
c=0
total=0
cond = 'FIM'
print(f'Olá, informe seu dados. Para encerrar, digite o nome {cond}.')
nome=input('Informe seu nome: ')
nomeUpper=nome.upper()
    
while (nomeUpper != cond):
    n1 = float(input('Primeira nota: '))
    n2 = float(input('Segunda nota: '))
    n3 = float(input('Terceira nota: '))
    media = (n1+n2+n3) / 3
    if media>=7.0:
        a=a+1
        total=total+1
        print(f'Olá {nome} sua media foi {media:.1f} e seu conceito foi A ')
    elif media>=4 and media<7:
        b=b+1
        total=total+1
        print(f'Olá {nome} sua media foi {media:.1f} e seu conceito foi B ')
    else:
        c=c+1
        total=total+1
        print(f'Olá {nome} sua media foi {media:.1f} e seu conceito foi C ')
    nome=input('Informe seu nome: ')
    nomeUpper=nome.upper()
    

print(f'Quantidade de alunos com o conceito A {a}' )
print(f'Quantidade de alunos com o conceito B {b}' )
print(f'Quantidade de alunos com o conceito B {c}' )
print(f'Quantidade de alunos: {total} ')

QUESTÃO 2:
Faça um programa que leia a idade de várias pessoas visitantes de um show (a
leitura da idade 0 indicará o fim dos dados de entrada), calcule e exiba:
 A média de idade do público;
 A porcentagem de pessoas com idade entre 18 e 21 anos;
 Idade do visitante mais jovem.

flag=0
total=0
cont=0
pp=0
print(f'Informe sua idade, para encerrar digite {flag} ')
idade=int(input('Idade: '))
menor=idade

while idade !=flag:
    total=total+idade
    cont=cont+1
    if idade>=18 and idade<=21:
        pp=pp+1
        
    if idade<menor:
        menor=idade
    idade=int(input('Idade: '))
        
media=total/cont
percp=pp/cont*100
print(f'Media de idade do público: {media:.1f} ')
print(f'Porcentagem de pessoas com idade entre 18 e 21 anos: {percp:.1f}% ')
print(f'O visitante mais jovem tem: {menor} anos ')

#AVALIAÇÃO 6


