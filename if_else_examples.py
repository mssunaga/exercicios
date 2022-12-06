### Programa - Jogo: 
# Fazer o computador pensar em um número inteiro aleatório entre 0 e 5;
# Pedir para o usuário digitar um número entre 0 e 5;
# Exibir se o número escolhido pelo usuário foi o correto comparado ao escolhido pelo computador
from random import randint
ncomputador = randint(0,5)
nhumano = int(input('Digite um número entre 0 e 5:'))
if ncomputador == nhumano:
  print('Parabéns, o número escolhido pelo computador e você foi o {}' .format(nhumano))
else:
  print('Tente outra vez! O computador escolheu o número {} e você escolheu {}' .format(ncomputador, nhumano))



### Programa - Calculador de multa
# Ler a velocidade do carro, se ultrapassar 80km/h, é multado e a multa é R$7,00 por cada KM excedido
velocidade = float(input('Digite a velocidade em KM/h:'))
if velocidade > 80:
  print('A velocidade atingida foi de {}km/h, ocasionando multa no valor de R${}' .format(velocidade, (velocidade-80)*7))
else:
  print('A velocidade atingida foi de {}km/h, não ocasionando em multa.' .format(velocidade))


### Programa - Ler o número e dizer se é par ou impar
numero = int(input('Digite o número'))
if numero % 2 > 0:
  print('O número {} é ímpar' .format(numero))
else:
  print('O número {} é par' .format(numero)) 


### Programa - Perguntar a distância de uma viagem em KM e devolver o preço gasto considerando:
# R$ 0,50 para viagens até 200km ; R$ 0,45 para viagens acima de 200km
kmviagem = float(input('Digite a quantidade de KM da viagem:'))
if kmviagem > 200:
  print('O valor da passagem é de R${}, com custo unitário de R${}' .format(kmviagem*0.45,'R$0,45'))
else:
  print('O valor da passagem é de R${}, com custo unitário de R${}' .format(kmviagem*0.50,'R$0,50'))



### Programa - Ler o ano e indicar se o ano é bissexto ou não
# Um ano bissexto é quando a DEZENA do ano é divisível por 4 (isto é, sem resto de divisão)
ano = int(input('Digite o ano partindo do ano 0:'))
c1 = ano % 4
c2 = ano % 100
c3 = ano % 400
if (c1 == 0 and c2 != 0) or (c1 and c2 and c3 == 0) or (c3 == 0):
  print('O ano de {} é bissexto' .format(ano))
else:
  print('O ano de {} não é bissexto' .format(ano))


### Modo Aula - Com datetime para travar o ano atual se o usuário colocar 0
from datetime import date
ano = int(input('Digite o ano partindo do ano 0:'))
if ano == 0:
  ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
  print('O ano de {} é bissexto' .format(ano))
else:
  print('O ano de {} não é bissexto' .format(ano))


### Programa - Ler três números e dizer qual é o MAIOR e qual é o MENOR

n1 = float(input('Digite o 1o numero:'))
n2 = float(input('Digite o 2o numero:'))
n3 = float(input('Digite o 3o numero:'))
if n1 > n2 and n1 > n3:
  print('O maior número é {}' .format(n1))
elif n2 > n1 and n2 > n3:
  print('O maior número é {}' .format(n2))
else:
  print('O maior número é {}' .format(n3))

if n1 < n2 and n1 < n3:
  print('O menor número é {}' .format(n1))
elif n2 < n1 and n2 < n3:
  print('O menor número é {}' .format(n2))
else:
  print('O menor número é {}' .format(n3))

conj = [n1,n2,n3]
print('O conjunto dos números é', conj)


### Modo aula - Simplificando um pouco o if
n1 = float(input('Digite o 1o numero:'))
n2 = float(input('Digite o 2o numero:'))
n3 = float(input('Digite o 3o numero:'))
conj = [n1,n2,n3]
menor = n1
if n2 < n1 and n2 < n3:
  menor = n2
if n3 < n1 and n3 < n2:
  menor = n3

maior = n1
if n2 > n1 and n2 > n3:
  maior = n2
if n3 > n1 and n3 > n2:
  maior = n3
print(conj)
print('O menor valor é {} e o maior valor é {}' .format(menor, maior))


## Modo alternativo com lista
n1 = int(input('Digite o 1o numero:'))
n2 = int(input('Digite o 2o numero:'))
n3 = int(input('Digite o 3o numero:'))
conj = [n1,n2,n3]
print(conj)
print('O maior valor é {} e o menor valor é {}' .format(max(conj),min(conj)))



### Programa - Digitar o salário e calcular valor do aumento sobre o salário
# 10% para valores acima de R$ 1250, 15% para valores abaixo
w = float(input('Digite o valor do salário:'))
if w > 1250.00:
  print('Valor do salário é R${:.2f}, com o aumento de 10% atualizado é R${:.2f}' .format(w, w*1.1))
else:
  print('Valor do salário é R${:.2f}, com o aumento de 15% atualizado é R${:.2f}' .format(w, w*1.15))



## Programa = Ler o comprimento de 3 retas e dizer se pode formar um triângulo
# Regra: |b-c| < a < (b+c)   ;   |a-c| < b < (a+c)    ;   |a-b| < c < (a+b)

a = float(input('Digite o valor do 1o lado:'))
b = float(input('Digite o valor do 2o lado:'))
c = float(input('Digite o valor do 3o lado:'))

if bool(abs(b-c)<a<(b+c)) == True and bool(abs(a-c)<b<(a+c)) == True and bool(abs(a-b)<c<(a+b)) == True:
  print('É possível ter um triângulo')
else:
  print('Não é possível ter um triângulo')

conj = [a,b,c]
print(conj)

## Modo aula

a = float(input('Digite o valor do 1o lado:'))
b = float(input('Digite o valor do 2o lado:'))
c = float(input('Digite o valor do 3o lado:'))

if a < b + c and b < a + c and c < a + b:
  print('É possível ter um triângulo')
else:
  print('Não é possível ter um triângulo')


