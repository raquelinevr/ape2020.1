#C:\Users\Raqueline\AppData\Local\Programs\Python\Python37-32
Utilizando quaisquer dos comandos, funções e operadores vistos até a Semana 6,
faça programas Python para resolver as questões abaixo.

1. Nessa semana ocorrerá a 16a rodada do Brasileirão (Série A). Serão 10 jogos
envolvendo 20 times.
Faça um programa para, em cada um dos 10 jogos dessa rodada, ler os nomes
dos dois times e o placar do jogo (quantidade de gols marcados por cada time
no jogo).
Obs: ao se informar os nomes dos 2 times de cada jogo, o primeiro nome é o
do time “mandante” e o segundo nome é o do time “visitante”.
Ao final, o seu programa deverá calcular e exibir:
 Quantidade de vitórias de mandantes;
 Quantidade de empates;
 Quantidade de vitórias de visitantes;
 Total de gols marcados na rodada.

total = emp = t1 = t2 = 0
for i in range(2):
    time1=input('Primeiro time\nMandante:  ')
    time2=input('Segundo time\nVisitante:  ')
    gol1=int(input('Quantidade de gols do primeiro time: '))
    gol2=int(input('Quantidade de gols do segundo time: '))
    total=total+gol1+gol2
       
    if gol1>gol2:
        t1=t1+1
    if gol2>gol1:
        t2=t2+1
    if gol1==gol2:
        emp=emp+1
        
print('\n===== RESULTADO =====')
print(f'Quantidade de vitórias de mandantes: {t1} ')
print(f'Quantidade de empates: {emp} ')
print(f'Quantidade de vítoria de visitantes: {t2} ')
print(f'Total de gols marcados na rodada: {total} ')


2. Numa determinada festa, os homens tinham que pagar R$ 20,00 pelo ingresso
e as mulheres R$ 10,00. Faça um programa que:
 Leia o nome, a idade e o sexo (M ou F) de cada participante da festa (a
leitura do nome FIM indica o final dos dados de entrada);
 Determine e exiba o nome e a idade do participante mais jovem e do
participante mais velho (suponha que não haja empates);
 Calcule e exiba a média de idade dos participantes da festa;
 Calcule e exiba o total arrecadado com os ingressos da festa.

soma=0
cont=0
m=0
f=0
maior=0
menor=999
nomeJ=0
nomeV=0
while True:
    nome=input('Informe seu nome: ')
    nomeUpper=nome.upper()
    if nomeUpper=='FIM':
        break
    else:
        idade=int(input('Informe a idade: '))
        sexo=input('Informe o sexo: [M/F] ').upper()

        if idade<menor:
            menor=idade
            nomeJ=nome
        if idade>maior:
            maior=idade
            nomeV=nome
        if sexo=='M':
            m=m+1
        if sexo=='F':
            f=f+1
        soma=soma+1
        cont=cont+idade
           
total=f*10+m*20
media=cont/soma

print(f'\n{nomeJ} é o participante mais novo(a) com {menor} anos ')
print(f'{nomeV} é o participante mais velho(a) com {maior} anos ')
print(f'Media de idade dos participantes: {media:.0f} anos')
print(f'Total arrecadado com os ingressos: R$ {total:.2f} ')
