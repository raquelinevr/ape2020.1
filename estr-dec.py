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


