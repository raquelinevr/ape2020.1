QUESTÃO 1:
Faça um programa que, para cada um dos vários alunos de uma turma, leia o
nome e as três notas do aluno (a leitura do nome FIM indica o fim dos dados de
entrada), mostre o nome, a média final e o conceito, sabendo-se que:
 A média final é calculada pela média aritmética das 3 notas;
 O conceito é determinado de com base na tabela abaixo:
  MÉDIA FINAL          CONCEITO
     7,0                  A
     4,0 e < 7,0          B
    < 4,0                  C
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

