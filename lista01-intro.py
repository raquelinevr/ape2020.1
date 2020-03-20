1.Faça um programa que exiba na tela do computador a mensagem “Bem-vindo ao mundo da programação! ”

print('Bem-vindo ao mundo da programação')

--

2.Escreva um programa que leia um número inteiro e exiba o dobro do mesmo.

n1=int(input('Digite um valor: '))
print('O dobro do numeros digitado é: 'n1*2)

--

3.Faça um programa que leia dois números reais, calcule e exiba a soma deles.

n1=int(input('Digite um valor: '))
n2=int(input('Digite outro valor: '))
print('A soma dos numeros digitados é: ',n1+n2)

--


4.Escreva um programa para calcular e exibir o valor de x elevado a y.

x=int(input('Informe um valor  para ser elevado: '))
y=int(input('Você deseja elevar o número acima a quanto? '))
print(f'O valor de {x} elevado a {y} é de',x**y)

--

5.Escreva um programa para ler o nome e o sobrenome de uma pessoa e escrevê-los na
seguinte forma: sobrenome seguido poruma vírgula e pelo nome.

nome=input('Digite seu primeiro nome: ')
sobrenome=input('Digite seu sobrenome: ')
print(sobrenome,',',nome)

--


6.Escreva um programa para calcular a área de um triângulo, dados os valores debase e altura.

base=int(input('Digite o valor da base: '))
altura=int(input('Digite o valor da altura: '))
area=(base*altura)/2
print('A area do triangulo é de',area)


--

7.Escreva  um programa que  leia  um valor  em  polegadas e  converta-o  para  centímetros.
(1 pol = 2,54 cm)

pol=int(input('Digite o valor em polegadas: '))
c=pol*2,54
print('O valor das polegadas em cm é de',c)

--

8.Faça um programaque efetue a apresentação do valor da conversão em real (R$) de um valor  lido  em  dólar (US$).
O  algoritmo  deverá  solicitar  o  valor  da  cotação  do  dólar  e também a quantidade de dólares disponíveis
com o usuário. 

cot=float(input('Qual a cotação do dólar? '))
qt=float(input('Quantos dólares você tem? '))
dolar=4.47
total=cot*qt
print(f'O seu valor em dólares ({qt}) equivale a {total} em real ')

--

9. O restaurante  a  quilo  Bem-Bão  cobra  R$25,00  por  cada  quilo  de  refeição.  Faça  um programa que 
leia  o  peso  do  prato  montado  pelo  cliente  (em quilos)  e  exiba  o  valor  a pagar. 
Assuma que a balança já desconte o peso do prato. 

prato=int(input('Qual foi o peso do seu prato (em quilos) ? '))
desc=0.400
k=prato*25.00-desc
print(f'O valor a pagar é de {k} ')

ou -

peso=int(input('Informe o valor do seu prato em quilos: '))
quilo=25.00
x=peso
print('O valor do seu prato foi: ',peso*quilo-x) #this

--

10.Faça um programa que leia o nome de um aluno e as notas das três provas que ele obteve no semestre.
No final informar o nome do aluno e a sua média (aritmética). 

nome=input('Digite seu nome: ')
nota1=float(input('Digite sua primeira nota: '))
nota2=float(input('Digite sua segunda nota: '))
nota3=float(input('Digite sua terceira nota: '))
media=(nota1+nota2+nota3)/3
print('Oi',nome,'sua média foi de',media)

--

11.Escreva um programa para calcular e exibir a média ponderada de 2 notas dadas. 
Sabe-se que nota1 possui peso 6 e nota2 possui peso 4.

media1=float(input('Digite sua primeira media: '))
media2=float(input('Digite sua segunda media: '))
x=media1*0.6 + media2*0.4/2
print('Sua média foi de: ',x,)

--

12. Escreva  um programa que  leia  duas  variáveis  inteiras 
e  troque  o  conteúdo  entre  elas, mostrando o resultado.

var1=input('Digite algo: ')
var2=input('Digite outra coisa: ')
print('O conteúdo das variaveis trocadas é de',var2,var1)

--

13. A Companhia de Carros Usados João Honesto paga seus empregados um salário de R$ 1.000,00 por mês
mais uma comissão de R$ 200,00 por cada carro vendido mais 5% do valor da venda.
Faça um programa que leia  o nome, o número de  carros vendidos e o valor total das vendas de um vendedor,
e calcule e exiba o seu salário. 

nome=input('Digite seu nome: ')
cv=int(input('Informe a quantidade de carros que você vendeu: '))
vt=int(input('Informe o valor total das suas vendas: '))
salario=1000
com=200
ad=vt+5.0*5
x=cv*com+salario+ad
print('O seu salario final é de:',x)



--

14.Um motorista anota a marcação do odômetro do seu veículo antes e após uma viagem, bem como o número  de
litros de combustível gastos. Faça um programa que leia os 3 dados acima, 
o preço do litro de combustível, a capacidade do tanque e mostre:
a) Quilometragem rodada.
b) Quantos quilômetros por litro faz o veículo. 
c) Autonomia do veículo. 
d) Custo da viagem.

ant=int(input('Digite a marcação do odometro antes da viagem: '))
dep=int(input('Qual a marcação após a viagem: '))
numl=int(input('Quantos litros de combustivel foram gastos? '))
x=dep-ant
cap=40
print('A quilometragem rodada foi de: ',x,'km')
print('O veículo faz',numl/x,'km por litro')
print('Em um litro o veículo faz',numl/cap)
print('A viagem custou: ',numl,' litros de gasolina')


~~ 

15.Faça  um programa que,  dado  um  número  inteiro  representando  uma  quantidade  de segundos,
calcule quantas horas, minutos e segundos estão contidos nesta quantidade.
Ex: 7.388 segundos = 2 horas, 3 minutos e 8 segundos.
  
tempo=int(input('Digite uma quantidade de segundos: '))
hora=tempo//3600
resto=tempo%3600

minuto=resto//60
resto=resto%60

segundo=resto//1
resto=resto%1

print(hora,'horas' ,minuto,'minutos' ,segundo,'e segundos')


--

16. Cédulas
Escreva  um  programa  para  ler  um  valor  inteiro.
A  seguir,  calcule  o  menor  número  de notas possíveis (cédulas) no qual o valor pode ser decomposto.
As notas consideradas são de 100, 50, 20, 10, 5, 2 e 1.
A seguir mostre o valor lido e a relaçãode notas necessárias. 
Exemplo: 576
5 nota(s) de R$ 100,00
1 nota(s) de R$ 50,00
1 nota(s) de R$ 20,00
0 nota(s) de R$ 10,00
1 nota(s) de R$ 5,00
0 nota(s) de R$ 2,00
1 nota(s) de R$ 1,00

valor=int(input('Digite a quantia: '))
notas100=valor//100
resto=valor%100
notas50=resto//50
resto=resto%50
notas20=resto//20
resto=resto%20
notas10=resto//10
resto=resto%10
notas5=resto//5
resto=resto%5
notas2=resto//2
resto=resto%2
notas1=resto//1
resto=resto%1
print(f'As notas de 100 são: {notas100}\n as notas de 50 são: {notas50}\n as notas de 20 são {notas20}\n as notas de 10 são {notas10}\n as notas de 5 são {notas5}\n as notas de 2 são {notas2} e as notas de 1 são: {notas1} ')

