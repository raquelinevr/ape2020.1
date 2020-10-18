1. Em uma pesquisa foram coletados os seguintes dados de um conjunto de 100 pessoas: 
sexo (M-masculino ou F-feminino), idade e estado civil (S-solteiro, C-casado, V-viúvo ou D-divorciado).
Neste contexto, faça um programa que leia os dados coletados durante a
pesquisa, determine e mostre:
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

            
2. Faça um programa para ler o nome e o salário bruto dos 80 funcionários de
uma determinada empresa.
Para cada funcionário lido, o programa deverá emitir o respectivo
contracheque, que deverá conter:
 O nome do funcionário;
 O valor do salário bruto;
 O valor do desconto do INSS (12% do Salário Bruto)
 O valor do salário líquido (Salário Bruto – Desconto INSS)
Ao final, o programa deverá mostrar:
 A soma total dos salários brutos;
 A soma total dos descontos do INSS;
 A soma total dos salários líquidos.

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
