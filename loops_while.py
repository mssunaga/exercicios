# Testando a função

for c in range(1,10):
  print(c)
print('Fim')

c = 1
while c < 10:
  print(c)
  c = c + 1
print('Fim')

## Condição de parada >>> Só para quando for 0:
n = 1
while n != 0:
  n = int(input('Digite um valor'))
print('Fim')

r = 'S'
while r == 'S':
  n = int(input('Digite um valor:'))
  r = str(input('Quer continuar? [S/N]')).upper().strip()
print('Fim')


# Exemplo: Estrutura só vai finalizar se usuário digitar 0 e vai retornar quantos números foram digitados(par/impar)

n = 1
par = impar = 0
lista = []
while n != 0:
  n = int(input('Digite um número:'))
  lista.append(n)
  if n != 0:
    if n % 2 == 0:
      par += 1
    else:
      impar += 1
print('Fim. \n{} pares ; {} ímpares' .format(par, impar))
print(lista)


# Exemplo: Usando clausula else para encerrar o loop
x = 0
while x < 10:
  print('O valor de x nesta iteração é', x)
  x += 1

else:
  print('Concluido')


# Exemplo: Loop com pass e break
count = 0
while count < 100:
  if count == 4:
    break
  else:
    pass
  print(count)
  count += 1

# Continue para pular uma condição dentro do loop
for v in 'Python':
  if v == 'h':
    continue
  print(v)



# Exemplo de while e for juntos (verificando numero primo)
for i in range(2,30):
  j = 2
  counter = 0
  while j < i:
    if i % j == 0:
      counter = 1
      j += 1
    else:
      j += 1

  if counter == 0:
    print(f'{i} é um número primo')
    counter = 0
  else:
    counter = 0


# Percorrendo lista dinamicamente
lista = ['Vasco','Flamengo','Botafogo','Fluminense']
for i in range(0, len(lista)):
  print(lista[i])


#########################################################################################################

# Exercícios

### Programa: Programa que leia genero digitado (M ou F) e só pare quando for digitado corretamente
# Bonus: Mostrar quantas vezes erraram até acertar.

genero = ''
log = []
while genero != 'M' and genero != 'F':
  genero = str(input('Digite o gênero [M ou F]:')).upper().strip()[0]
  if genero != 'M' and genero != 'F':
    log += genero
print('Input correto, {}. Houveram {} tentativa(s) errada(s)' .format(genero, len(log)))
print(log)

## Modo aula
# Bonus: Quantas vezes erraram até acertar

count = 0
genero = str(input('Digite o gênero [M ou F]:')).upper().strip()[0]
while genero not in 'MmFf':
  genero = str(input('Dados inválidos. Digite o gênero [M ou F]:')).upper().strip()[0]
  if genero not in 'MmFf':
    count += 1
print('Digitou corretamente, após {} tentativa(s)' . format(count))



### Programa: Computador vai pensar em um número de 0 a 10. Advinhar o número usando while (até acertar)
# Mostrar quantas vezes errou até acertar

## Versão o computador só escolhe o número 1x

import random
ncomputador = random.randint(0,10)
nuser = 0
log = []
while nuser != ncomputador:
  nuser = int(input('Digite o seu número'))
  if nuser < ncomputador:
   print('Mais... Você errou, tente outra vez!')
  elif nuser > ncomputador:
    print('Menos... Você errou, tente outra vez!')
  log.append(nuser)
print('Você acertou! Computador escolheu {} e você {}' .format(ncomputador, nuser))
print('{} chance(s) foi/foram usada(s) para acertar' .format(len(log)))

## Modo aula:
import random
ncomputador = random.randint(0,10)
count = 0
acertou = False
while not acertou:
  nuser = int(input('Digite o seu número'))
  count += 1
  if nuser == ncomputador:
    acertou = True
  else:
    if nuser < ncomputador:
      print('Mais... Você errou, tente outra vez!')
    else:
      print('Menos... Você errou, tente outra vez!')
print('Você acertou! Computador escolheu {} e você {}' .format(ncomputador, nuser))
print('{} chance(s) foi/foram usada(s) para acertar' .format(count))


### Programa: Criar um programa para ler dois valores e mostrar um menu na tela com:
# [1] soma, [2] mult, [3] maior, [4] novos números, [5] sair do programa
n1 = int(input('Digite o primeiro número:'))
print('Primeiro valor: {}' .format(n1))
n2 = int(input('Digite o segundo número:'))
print('Segundo valor: {}' .format(n2))
opcao = 0

while opcao != 5:
  opcao = int(input('Digite a opção desejada:'))
  print('='*11,'Opções','='*11)
  print('''[1] Soma
[2] Multiplicação
[3] Maior número
[4] Digitar novos números
[5] Sair do programa''')
  print('='*30)
  if opcao == 1:
    print('Opção [1], soma.\nA soma de {} + {} é igual a {}' .format(n1, n2, n1+n2))
    print('                                                ')
  elif opcao == 2:
    print('Opção [2], multiplicação.\nA multiplicação de {} x {} é igual a {}' .format(n1, n2, n1*n2))
    print('                                                ')
  elif opcao == 3:
    if n1 > n2:
      print('Opção [3], maior.\nO primeiro número ({}) é maior do que o segundo ({})' .format(n1, n2))
      print('                                                ')
    elif n1 < n2:
      print('Opção [3], maior.\nO primeiro número ({}) é menor do que o segundo ({})' .format(n1, n2))
      print('                                                ')
    else: 
      print('Opção [3], maior.\nO primeiro número ({}) é igual ao segundo ({})' .format(n1, n2))
      print('                                                ')
  elif opcao == 4:
    print('Opção [4], nova consulta com novos valores abaixo:')
    n1 = int(input('Digite novamente o primeiro número:'))
    print('Primeiro valor: {}' .format(n1))
    n2 = int(input('Digite novamente o segundo número:'))
    print('Segundo valor: {}' .format(n2))
  elif opcao == 5:
    print('Opção [5]. O programa foi encerrado')
  else:
    print('Opção [{}]. Esta opção está incorreta' .format(opcao))
    print('                                                ')



### Programa: Ler qualquer número e mostrar o seu fatorial
# Fazer com while e for

### Com While
result = 1
count = 1
n = int(input('Digite o valor para cálculo fatorial:'))

while count <= n:
  result *= count
  count += 1
print('O resultado para !{} é: {}' .format(n, result))


## Outra forma While
n = int(input('Digite o valor para cálculo fatorial:'))
c = n
f = 1
print('Fatorial de !{} é:' .format(n))
while c > 0:
  print('{}' .format(c), end=' ')
  print('x' if c > 1 else '=', end= ' ')
  f *= c
  c -= 1
print(f)



### Com FOR
result = 1
n = int(input('Digite o valor para cálculo fatorial:'))

for i in range(1, n+1):
  result *= i
print('O resultado para !{} é: {}' .format(n, result))



## Com biblio math
from math import factorial
n = int(input('Digite o número para calcular o fatorial:'))
f = factorial(n)
print('O fatorial de {}! é {}' .format(n, f))



### Programa: Ler primeiro termo e a razão de uma PA. Mostrar 10 primeiros termos e usar While
num = int(input('Digite o primeiro termo:'))
razao = int(input('Digite a razão da PA:'))
cont = 1
termo = num
while cont <= 10:
  print('{} ' .format(termo), end='')
  termo += razao
  cont += 1
print('Fim')



### Programa: Melhorar o programa acima, perguntando quantos termos o user quer adicionar
num = int(input('Digite o primeiro termo:'))
razao = int(input('Digite a razão da PA:'))
cont = 1
termo = num
total = 0
mais = 10
while mais != 0:
  total += mais
  while cont <= total:
    print('{} ' .format(termo), end='')
    termo += razao
    cont += 1
  print('Pausa')
  mais = int(input('Digite quantos termos adicionais deseja ver:')) 
print('Fim. {} termo(s) exibido(s)' .format(total))



### Programa: Ler um número N e mostrar N elementos da sequencia de fibonacci
n = int(input('Digite quantos elementos deseja mostrar na sequencia de Fibonacci:'))
# Count é a variável para receber +1 no while até chegar ao valor N digitado no input pelo user.
count = 0
n1, n2 = 0, 1
print('Sequencia de Fibonacci - Elementos escolhidos: {}' .format(n))
while count < n:
  print(n1, end=' ')
  count += 1
  n3 = n1 + n2
  n1 = n2
  n2 = n3

## Modo aula
n = int(input('Digite quantos elementos deseja mostrar na sequencia de Fibonacci:'))
t1 = 0
t2 = 1
cont = 3
print('{} {}' .format(t1, t2), end='')
while cont <= n:
  t3 = t1 + t2
  print(' {}' .format(t3), end='')
  cont += 1
  t1 = t2
  t2 = t3
print(' Fim')



### Programa: Ler vários números e só parar quando o usuário colocar o input 999.
# Ao fim, mostrar quantos números foram digitados e qual foi a soma dos números digitados, desconsiderando o 999
n = s = c = 0
while n != 999:
  n = int(input('Digite o número:'))
  s += n
  c += 1
print('{} número(s) digitado(s)\nA soma foi de {}' .format((c-1), (s-999)))

## Modo aula

n = s = c = 0
n = int(input('Digite o número:'))
while n != 999:
  s += n
  c += 1
  n = int(input('Digite o número:'))
print('{} número(s) digitado(s)\nA soma foi de {}' .format((c), (s)))




### Programa: Ler vários números, perguntar se quer continuar a incluir números ou não. 
# Retornar ao final a média deles, o maior e o menor.
t = 's'
lista = []
s = 0
c = 0
while t in 'Ss':
  n = int(input('Digite o número:'))
  t = str(input('Quer continuar? (S/N)')).strip().lower()[0]
  lista.append(n)
  s += n
  c += 1
print('''Você encerrou o programa. 
O maior valor digitado foi {}, 
o menor foi {} e a média {:.2f}''' .format(max(lista), min(lista), s/c))

## Modo aula
t = 's'
s = c = maior = menor = 0
while t in 'Ss':
  n = int(input('Digite o número:'))
  t = str(input('Quer continuar? (S/N)')).strip().lower()[0]
  s += n
  c += 1
  if c == 1:
    maior = menor = n
  else:
    if n > maior:
      maior = n
    if n < menor:
      menor = n
print('''Você encerrou o programa. 
O maior valor digitado foi {}, 
o menor foi {} e a média {:.2f}''' .format(maior, menor, s/c))

############### Interrompendo repetições WHILE ####################

## Stop: Vai desviar a repetição para encerrar
# Ex.: Tem um IF dentro do While, se verdadeiro, break, vai interromper o While e sair do loop.

n = s = c = 0
while True:
  n = int(input('Digite o número ou 999 para parar:'))
  if n == 999:
    break
  s += n
  c += 1
print(f'A soma é {s} e usou {c} número(s)')


### Programa: Ler vários números inteiros, parar apenas quando o usuário digitar 999. 
# mostrar soma e quantos números foram digitados, desconsiderando o 999
n = s = c = 0
while True:
  n = int(input('Digite um número [999 para finalizar]'))
  if n == 999:
    break
  s += n
  c += 1
print(f'Resultado da soma: {s}.\nQtde. números utilizados: {c}\nMédia: {s/c:.2f}')


### Programa: Mostrar a tabuada de qualquer valor recebido e só parar o programa quando o valor digitado for <0
while True:
  c = 0
  n = int(input('Digite o numero para calcular a tabuada'))
  if n < 0:
    break
  while c < 10:   
    c += 1
    print(f'{n} x {c} = {n*c}')
  print('------------------')
print('Fim')
   
# com estrutura FOR
while True:
  n = int(input('Digite o numero para calcular a tabuada'))
  if n < 0:
    break
  for i in range(1,11):
    print(f'{n} x {i} = {n*i}')
  print('------------------')
print('Fim')


### Programa: Montar um programa para jogar par ou ímpar com o computador. 
# Regra: Interromper o jogo apenas quando o jogador PERDER. 
# Ao final, mostrar quantas vitórias consecutivas o jogador teve.
# Usuário deve fazer input do número (computador fará aleatóriamente) e da opção par ou ímpar.
import random
vitoriacpu = 0
vitoriajogador = 0
while True:
  somajogada = 0
  if vitoriacpu > 0:
    break
  numjogador = int(input('Digite o seu número'))
  escolha = str(input('Par ou ímpar? [P/I]')).strip().lower()[0]
  numcomputador = random.randint(0,10)
  somajogada += numjogador
  somajogada += numcomputador
  print(f'Você jogou {numjogador} e o computador {numcomputador}. Total {somajogada}')
  if somajogada % 2 == 0 and escolha in 'Pp':
    vitoriajogador += 1
    print('Você escolheu par! Você ganhou!')
    print('--------------------------------')
  elif somajogada % 2 == 0 and escolha in 'Ii':
    vitoriacpu += 1
    print('Você escolheu ímpar! Você perdeu!')
    print('--------------------------------')
  elif somajogada % 2 != 0 and escolha in 'Ii':
    print('Você escolheu ímpar! Você ganhou!')
    print('--------------------------------')
    vitoriajogador += 1 
  else:
    vitoriacpu += 1
    print('Você escolheu par! Você perdeu!')
    print('--------------------------------')
print(f'Venceu consecutivamente: {vitoriajogador}x')

### Modo aula >>> Melhor porque tem condições no input que permitem nao digitar coisa errada
import random
countvitoria = 0
rodada = 1
print(f'============= Rodada 1 =============')
while True:
  jogador = int(input('Digite o valor:'))
  computador = random.randint(0, 10)
  total = jogador + computador
  tipo = ' '
  while tipo not in 'PpIi':
    tipo = str(input('Par ou Ímpar? [P/I]')).strip()[0]
  print(f'Você jogou {jogador}, o computador jogou {computador}.\nTotal {total}\n', end='')
  print('Você escolheu par!' if tipo in 'Pp' else 'Você escolheu ímpar!')
  print('Deu par!' if total % 2 == 0 else 'Deu ímpar!')
  rodada += 1
  if tipo in 'Pp':
    if total % 2 == 0:
      print('Você venceu!')
      countvitoria += 1
    else:
      print('Você perdeu!')
      break
  elif tipo in 'Ii':
    if total % 2 != 0:
      print('Você ganhou!')
      countvitoria += 1
    else:
      print('Você perdeu!')
      break
  print(f'============= Rodada {rodada} =============')
print(f'=============== Fim ================')  
print(f'Você venceu {countvitoria}x de forma consecutiva.')



### Programa: Ler idade e genero de várias pessoas
# A cada pessoa cadastrada, perguntar se o user quer permanecer registrando
# Retornar: Qts pessoas > 18 anos; Quantos homens foram cadastrados; Quantas mulheres < 20 anos.
counthomem = 0
countmaior = 0
countmulher20 = 0
while True:
  idade = int(input('Digite a idade:'))
  genero = ' '
  while genero not in 'MF':
    genero = str(input('Digite o genero [M/F]:')).strip().upper()[0]
  if genero == 'M':
    counthomem += 1
  if genero == 'F' and idade < 20:
    countmulher20 += 1
  if idade >= 18:
    countmaior += 1
  resp = ' '
  while resp not in 'SN':
    resp = str(input('Digite se deseja prosseguir no programa [S/N]:')).strip().upper()[0]
  if resp == 'N':
    break
print(f'Maior de 18: {countmaior}\nHomens cadastrados: {counthomem}\nMulheres <20 anos: {countmulher20}')


### Programa: Ler o nome e o preço de vários produtos. O programa pergunta se quer encerrar ou não.
# Ao final, mostrar o total gasto nas compras, quantos produtos > R$ 1000 e nome do produto mais barato.
somacompra = prod1000 = count = menor = 0
nomeprodbarato = ''
listaprod = []
listaprec = []

while True:
  np = str(input('Digite o nome do produto:'))
  p = float(input('Digite o preço do produto R$:'))
  somacompra += p
  count += 1
  listaprod.append(np)
  listaprec.append(p)
  if count == 1 or p < menor:
    menor = p
    nomeprodbarato = np
  if p >= 1000:
   prod1000 += 1
  resp = ' '
  while resp not in 'NS':
    resp = str(input('Deseja incluir um produto na lista? [S/N]')).strip().upper()[0]
  if resp == 'N':
    break
print('===== Extrato =====')
print(f'''Total gasto: R${somacompra}\nProdutos acima de R$1000: {prod1000}\nNome do produto mais barato e preço: {nomeprodbarato}, R${menor}''')
print('===================')
print('Cesta:')
print(listaprod,listaprec)



### Programa: Simular o funcionamento de um caixa eletrônico.
# Perguntar qual o valor a ser sacado.
# Informar quantas cédulas e qual o valor sacado.
# Considerar ter células de: R$ 50, R$ 20, R$ 10 e R$ 1
saque = int(input('Digite o valor para sacar R$:'))
cinquenta = vinte = dez = um = 0
valorsaque = 0

while valorsaque < saque:
    cinquenta = saque // 50
    saque = saque-(cinquenta*50)
    vinte = saque // 20
    saque = saque-(vinte*20)
    dez = saque // 10
    saque = saque-(dez*10)
    um = saque
    valorsaque += cinquenta*50
    valorsaque += vinte*20
    valorsaque += dez*10
    valorsaque += um*1
print(f'Valor a sacar: R${valorsaque}')
print('=====Qtde de cédulas:=====')
print(f'''Cédulas de 50: {cinquenta}
Cédulas de 20: {vinte}
Cédulas de 10: {dez}
Cédulas de 1: {um}''')


### Modo aula
valor = int(input('Digite o valor que quer sacar: R$'))
total = valor
ced = 50
totalced = 0
while True:
  if total >= ced:
    total -= ced
    totalced += 1
  else:
    if totalced > 0:
      print(f'Total de {totalced} cédulas de R${ced}')
    if ced == 50:
      ced = 20
    elif ced == 20:
      ced = 10
    elif ced == 10:
      ced = 1
    totalced = 0
    if total == 0:
      break













