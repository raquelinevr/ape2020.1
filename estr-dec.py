1- Verificar se um aluno passou por média;

media=float(input('Digite sua média: '))
if media>=7:
    print('Aprovado(a)')
else:
    print('Reprovado(a)')


2- Verificar se um aluno está aprovado em uma disciplina;

media=float(input('Digite sua média: '))
freq=int(input('Digite a porcentagem da sua frequencia: '))
if media>=7 and freq>=75:
    print('Aprovado(a)')
else:
    print('Reprovado(a)')


3- Verificar se um número é primo;


4- Verificar se uma pessoa pode tirar a CNH no Detran.

idade=int(input('Infome sua idade: '))
aulas=input('Você assistiu todas as aulas téoricas? ')
freqaula=int(input('Digite sua frequencia nas aulas: '))
teste=input('Você foi aprovado em todos os testes? ')

if idade>=18 and (aulas=='sim' or 'Sim') and freqaula>=75 and teste=='sim':
    print('Você está apto.')
else:
    print('reprovado')


5- Verificar a média salarial de uma pessoa.

salario=int(input('Informe seu salario: '))
if salario >=20000:
    print('Seu salario é de',salario,' é você é de classe media alta. ')
if salario >=10000 and salario<=15000:
    print('Seu salario é de',salario,' é você é de classe alta. ')
if salario>=1000 and salario<=5000:
    print('Seu salario é de',salario,' é você é de classe baixa. ')
if salario<1000:
    print('Baixa renda')

    -
    -
    
    mat=int(input('Informe sua matricula: '))
me=int(input('Digite sua média dos exercicios: '))
n1=int(input('Digite sua primeira nota: '))
n2=int(input('Digite sua segunda nota: '))
n3=int(input('Digite sua terceira nota: '))
y=(n1+n2+n3*3)/7
if y>=9.0:
    print(f'Olá {mat} sua média de aproveitamento foi de {y} e seu conceito foi A ')
elif y>=7.5 and y<9.0:
    print(f'Olá {mat} sua média de aproveitamento foi de {y} e seu conceito foi B ')
elif y>=6.0 and y<7.5:
    print(f'Olá {mat} sua média de aproveitamento foi de {y} e seu conceito foi C ')
elif y>=4.0 and y <6.0:
    print(f'Olá {mat} sua média de aproveitamento foi de {y} e seu conceito foi D ')
elif y<4.0:
    print(f'Oi {mat} sua media de aproveitamento foi de {y} e seu conceito foi E' )
    


