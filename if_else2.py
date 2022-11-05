### Condicional - Elifs

# elif + or

nome = str(input('Digite o nome:'))
if nome == 'Marcello':
  print('Bom dia, {}' .format(nome))
elif nome == 'Maria' or nome =='João' or nome == 'José':
  print('Buenos dias, {}' .format(nome))
else:
  print('Good morning, {}' .format(nome))


# elif + in
nome = str(input('Digite o nome:'))
if nome == 'Marcello':
  print('Bom dia, {}' .format(nome))
elif nome in 'Maria João José':
  print('Buenos dias, {}' .format(nome))
else:
  print('Good morning, {}' .format(nome))

###################################################################################################

### Programa: Emprestimo bancário
# Perguntar valor da casa, salário e anos a pagar, retornar se o emprestimo será aprovado.
# Condição: Prestação mensal não pode exceder 30% do valor do salário

valorcasa = float(input('Digite o valor da casa em R$:'))
w = float(input('Digite o valor do salário em R$:'))
n = int(input('Digite em quantos anos deseja pagar:'))
m = n*12
pm = valorcasa/m

print('='*30)
print(' Valor da casa: R${:.2f} \n Salário mensal: R${:.2f} \n Anos a pagar: {:.0f} \n Meses a pagar: {:.0f} \n Prestação mensal: R$ {:.2f}' .format(valorcasa, w, n, m, pm))
print('='*30)
if pm > 0.3*w:
  print('Empréstimo negado, pois o valor da parcela mensal excede 30% do salário')
elif pm > 0.2*w:
  print('Empréstimo sob aprovação, mediante a comprovação de outras fontes de renda')
else:
  print('Empréstimo aceito')



### Programa: Ler um número e converter ele a partir da escolha do usuário
# Escolhas: Binário, Octal e Hexadecimal

num = int(input('Digite um número:'))
conv = int(input('Digite a base de conversão sendo: 1 para binário; 2 para octal e 3 para hexadecimal:'))
lista = ['binário', 'octal', 'hexadecimal']
if conv  == 1:
  print('A conversão do número {} para {} é {}' .format(num, lista[0], bin(num)[2:]))
elif conv == 2:
  print('A conversão do número {} para {} é {}' .format(num, lista[1], oct(num)[2:]))
elif conv == 3:
  print('A conversão do número {} para {} é {}' .format(num, lista[2], hex(num)[2:]))
else:
  print('O número de escolha digitado não permite realizar conversão.')



### Programa: Ler dois números inteiros e comparar. Mostrar se o 1o ou o 2o valor é o maior ou se são iguais

num1 = int(input('Digite o primeiro número:'))
num2 = int(input('Digite o segundo número:'))

if num1 > num2:
  print('O primeiro número digitado ({}) é maior do que o segundo ({})' .format(num1, num2))
elif num2 > num1: 
  print('O segundo número digitado ({}) é maior do que o primeiro ({})' .format(num2, num1))
else:
  print('O primeiro número digitado ({}) é igual ao segundo ({})' .format(num1, num2))




### Programa: Ler o ano de nascimento e de acordo com a sua idade informar se
# 1) Ainda vai precisar se alistar; 2) Se já é hora de se alistar; 3) Se já passou o tempo de se alistar
# Mostrar o tempo que falta ou que passou do prazo

from datetime import date
anonasc = int(input('Digite o ano de nascimento:'))
anoatual = date.today().year

if anonasc+18 == anoatual:
  print('Você precisa se alistar este ano, pois está com {} anos.' .format(anoatual-anonasc))
elif anonasc+18 > anoatual:
  print('Você ainda não precisa se alistar, só daqui a {} ano(s)' .format(anonasc+18-anoatual))
else:
  print('Você não precisa se alistar mais, pois já passou {} ano(s)' .format(anoatual-anonasc-18))


## Modo mais lógico
from datetime import date
anonasc = int(input('Digite o ano de nascimento:'))
anoatual = date.today().year
genero = str(input('Digite o seu gênero (Masculino ou Feminino):')).strip().upper()
idade = anoatual - anonasc


if genero == 'FEMININO':
  print('Você não tem necessidade de se alistar')
elif idade == 18:
  print('Você deve se alistar imediatamente')
elif idade > 18:
  saldo = idade - 18
  print('Você não precisa se alistar, pois já passou(aram) {} ano(s)' .format(saldo))
  print('Seu alistamento foi em {}' .format(anonasc+18))
else:
  saldo = 18 - idade
  print('Você não precisa se alistar ainda, pois falta(m) {} ano(s)' .format(saldo))
  print('Seu alistamento será em {}' .format(anonasc+18))




### Programa: Ler duas notas e calcular a média, mostrando se foi aprovado, reprovado ou ficou de recup.
# < 5.0, reprovado ; 5.0 < x < 6.9, recup. ; >= 7.0, aprovado

n1 = float(input('Digite a primeira nota:'))
n2 = float(input('Digite a segunda nota:'))
media = (n1 + n2)/2

if media < 5.0:
  print('Você está reprovado com nota média {}' .format(media))
elif media >= 5.0 and media < 7.0:
  print('Você está de recuperação com nota média {}' .format(media))
else:
  print('Você está aprovado com nota média {}' .format(media))




### Programa: Ler o ano de nascimento da pessoa e indicar qual categoria ela se encaixa
# Categorias: Até 9 anos MIRIM, até 14 anos INFANTIL, até 19 anos JUNIOR, até 20 anos SENIOR, acima MASTER

ano = int(input('Digite o ano de nascimento:'))
from datetime import date
anoatual = date.today().year

if anoatual - ano <= 9:
  print('Idade atual é de {} ano(s) na categoria Mirim' .format(anoatual-ano))
elif anoatual - ano <= 14:
  print('Idade atual é de {} ano(s) na categoria Infantil' .format(anoatual-ano))
elif anoatual - ano <= 19:
  print('Idade atual é de {} ano(s) na categoria Junior' .format(anoatual-ano))
elif anoatual - ano <= 20:
  print('Idade atual é de {} ano(s) na categoria Senior' .format(anoatual-ano))
else:
  print('Idade atual é de {} ano(s) na categoria Master' .format(anoatual-ano))




### Programa = Ler o comprimento de 3 retas e dizer se pode formar um triângulo
# Complemento: Dizer se é Equilatero (tds lados iguais), Isosceles (dois lados iguais), Escaleno (tds lados dif)
# Propriedade p/ existencia triangulo: Um lado não pode ser maior q a soma dos outros dois

a = float(input('Digite o valor do 1o lado:'))
b = float(input('Digite o valor do 2o lado:'))
c = float(input('Digite o valor do 3o lado:'))
lista = [a,b,c]
print(lista)

if a < b + c and b < a + c and c < a + b and a==b==c:
  print('É possível ter um triângulo e ele é Equilatero')
elif a < b + c and b < a + c and c < a + b and a==c!=b or a==b!=c:
  print('É possível ter um triângulo e ele é Isosceles')
elif a < b + c and b < a + c and c < a + b and a!=c!=b:
  print('É possível ter um triângulo e ele é Escaleno')  
else:
  print('Não é possível ter um triângulo')

## Outro modo

a = float(input('Digite o valor do 1o lado:'))
b = float(input('Digite o valor do 2o lado:'))
c = float(input('Digite o valor do 3o lado:'))
lista = [a,b,c]
print(lista)

if a < b + c and b < a + c and c < a + b:
  print('Os segmentos podem formar um triângulo, ', end='')
  if a == b == c:
    print('Equilátero')
  elif a != b != c != a:
    print('Escaleno')
  else:
    print('Isosceles')
else:
  print('Não é possível ter um triângulo')



### Programa: Desenvolver uma lógica para ler peso e altura, retornando o IMC.
# < 18.5 = Abaixo do peso ; 18.5 < x < 25 = Peso ideal ; 25 < x < 30 = Sobrepeso ; 20 < x < 40 = Obesidade
# > 40 = Obesidade mórbida

peso = float(input('Digite o peso:'))
altura = float(input('Digite a altura:'))
imc = peso/(altura**2)

if imc < 18.5:
  print('Peso: {:.2f}, Altura: {:.2f}, IMC: {:.2f}, abaixo do peso' .format(peso, altura, imc))
elif imc < 25:
  print('Peso: {:.2f}, Altura: {:.2f}, IMC: {:.2f}, peso ideal' .format(peso, altura, imc))
elif imc < 30:
  print('Peso: {:.2f}, Altura: {:.2f}, IMC: {:.2f}, sobrepeso' .format(peso, altura, imc))
elif imc < 40:
  print('Peso: {:.2f}, Altura: {:.2f}, IMC: {:.2f}, obesidade' .format(peso, altura, imc))
else:
  print('Peso: {:.2f}, Altura: {:.2f}, IMC: {:.2f}, obesidade mórbida' .format(peso, altura, imc))



### Programa: Calcular o valor a ser pago por um produto
# Condições: A vista no dinheiro ou cheque: 10% desconto
# A vista no cartão: 5% desconto
# até 2x cartão, sem desconto
# 3x ou mais, 20% de juros

print('{:=^35}'.format('Loja Loja'))
preco = float(input('Digite o preço do produto: R$'))
print('''Formas de pagamento:
[1] à vista em dinheiro / cheque
[2] à vista no cartão
[3] 2x no cartão
[4] 3x ou mais no cartão''')
opcao = int(input('Digite a opção de pgto:'))

if opcao == 1:
  valor = preco - preco*0.1
  print('O preço do produto é R${}, com desconto fica R${}' .format(preco, valor))
elif opcao == 2:
  valor = preco - preco*0.05
  print('O preço do produto é R${}, com desconto fica R${}' .format(preco, valor))
elif opcao == 3:
  print('O preço do produto é R${}, sem aplicação de desconto' .format(preco))
elif opcao == 4:
  valor = preco*1.2
  print('O preço do produto é R${}, com juros fica R${}' .format(preco, valor)) 
else:
  print('Algum valor pode ter sido digitado incorretamente')


## Enxugando o código

print('{:=^35}'.format('Loja Loja'))
preco = float(input('Digite o preço do produto: R$'))
print('''Formas de pagamento:
[1] à vista em dinheiro / cheque
[2] à vista no cartão
[3] 2x no cartão
[4] 3x ou mais no cartão''')
opcao = int(input('Digite a opção de pgto:'))

if opcao == 1:
  valor = preco - preco*0.1
elif opcao == 2:
  valor = preco - preco*0.05
elif opcao == 3:
  valor = preco
  print('Sua compra será parcelada em 2x de R${:.2f}' .format(preco/2))
elif opcao == 4:
  valor = preco*1.2
  parcelas = int(input('Quantas parcelas?'))
  print('Sua compra será parcelada em {}x de R${:.2f} com juros' .format(parcelas, valor/parcelas))
else:
  valor = preco
  print('Você digitou alguma opção inválida')
print('Sua compra de R${:.2f} vai custar R${:.2f} no final' .format(preco, valor))



### Programa: Computador jogar jokenpô

import random
aleatorio = random.randint(0,2)
lista = ['Pedra', 'Papel', 'Tesoura']
user = str(input('Digite a sua jogada (Pedra, Papel ou Tesoura):'))

from time import sleep
print(' JO')
sleep(1)
print(' KEN')
sleep(1)
print(' PÔ!')
sleep(1)

print('='*30)
if user == lista[aleatorio]:
  print(' Computador escolheu: {} \n Você escolheu: {} \n Empatou!' .format(lista[aleatorio], user))
elif user == 'Pedra' and lista[aleatorio] == 'Tesoura':
  print(' Computador escolheu: {} \n Você escolheu: {} \n Você venceu!' .format(lista[aleatorio], user))
elif user == 'Tesoura' and lista[aleatorio] == 'Papel':
  print(' Computador escolheu: {} \n Você escolheu: {} \n Você venceu!' .format(lista[aleatorio], user))
elif user == 'Papel' and lista[aleatorio] == 'Pedra':
  print(' Computador escolheu: {} \n Você escolheu: {} \n Você venceu!' .format(lista[aleatorio], user))
else:
  print(' Computador escolheu: {} \n Você escolheu: {} \n Você perdeu!' .format(lista[aleatorio], user))
print('='*30)


### Outro modo

import random
aleatorio = random.randint(0,2)
lista = ['PEDRA', 'PAPEL', 'TESOURA']
user = str(input('Digite a sua jogada (Pedra, Papel ou Tesoura):')).strip().upper()

from time import sleep
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!')
sleep(1)

print('='*30)
print('Computador jogou: {}' .format(lista[aleatorio].capitalize()))
print('Usuário jogou: {}' .format(user.capitalize()))
print('='*30)
if lista[aleatorio] == 'PEDRA':
  if user == 'PEDRA':
    print('Empate!')
  if user == 'PAPEL':
    print('Usuário venceu!')
  if user == 'TESOURA':
    print('Computador venceu!')
elif lista[aleatorio] == 'PAPEL':
  if user == 'PEDRA':
    print('Computador venceu!')
  if user == 'PAPEL':
    print('Empate!')
  if user == 'TESOURA':
    print('Usuário venceu!')
elif lista[aleatorio] == 'TESOURA':
  if user == 'PEDRA':
    print('Usuário venceu!')
  if user == 'PAPEL':
    print('Computador venceu!')
  if user == 'TESOURA':
    print('Empate!')
else:
  print('Alguma jogada inválida foi digitada')
print('='*30)


