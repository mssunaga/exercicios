### Iteração -> Laço com variável de controle. Loops

# Estrutura for, contagem simples por repetição
n = int(input('Digite um número:'))
for i in range(0, n+1):
  print(i)
print('Fim')

i = int(input('Inicio:'))
f = int(input('Fim:'))
p = int(input('Passo:'))
for c in range(i, f+1, p):
  print(c)
print('Fim')

# Usando for para ler mais de um input
s = 0
for c in range(0,3):
  n = int(input('Digite o número'))
  s += n
print('O somatório dos números incluídos é {}' .format(s))


# Usando loop direto na string

for c in 'Python':
  print(c, end=' ')
  

# Estrutura for aninhada >> For dentro de for. Comum para matrizes

for i in range(0,5):
  for a in range(0,5):
    print(a, end=' ')


# Percorrer lista e multiplicar cada item gravando em outra variável

lista = [1,2,3,4,5]
soma = 0
for i in lista:
  double = i*2
  soma += double

print(soma)


# Percorrendo listas de listas
listas = [[1,2,3],[4,5,6],[7,8,9]]
for i in listas:
  print(i)



# Escolhendo uma lista dentro da lista
for i in listas[0]:
  print(i)



# Contando número de itens nas listas e colunas
# itens:
listas = [[1,2,3],[4,5,6],[7,8,9]]
lista = listas[0]+listas[1]+listas[2]
count = 0
for i in lista:
  count += 1
print(count)

# Colunas:
primeira_linha = listas[0]
count = 0
for c in primeira_linha:
  count += 1
print(count)


################################################################################################

#### Exercícios

### Programa: Mostrar na tela uma contagem regressiva para estouro de fogos de artifício
# Regra: de 10 a 0 com pausa de 1 segundo entre eles
import emoji
from time import sleep
for i in range(10, -1, -1):
  print(i)
  sleep(1)
print(emoji.emojize(":fire::fire::fire::fire: BOOM! :fire::fire::fire::fire:"))



### Programa: Mostrar na tela todos os números pares que estão no intervalo de 1 a 50
for i in range(0, 51, 2):
  print(i , end=' ')
print('Fim')

## outro modo
for i in range(1, 51):
  if i % 2 == 0:
    print(i, end=' ')
print('Fim')



### Programa: Calcular a soma entre todos os números ímpares que são múltiplos de 3 
# Em um intervalo de 1 a 500
s = 0
cont = 0
for c in range(1, 501, 2):
  if c % 3 == 0:
    s += c
    cont += 1
  else:
    s += 0
    cont += 0
print('O somatório de números ímpares múltiplos de 3 é {}' .format(s))
print('O qtde de números ímpares múltiplos de 3 é {}' .format(cont))



### Programa: Montar uma tabuada com estrutura for
n = int(input('Digite um número para calcular a tabuada'))
for i in range(1, 11):
  print('{} x {} = {}' .format(n, i, n*i))



### Programa: Montar um programa que leia 6 números digitados e leia apenas aqueles que forem PARES
s = 0
for i in range(1,7):
  n = int(input('Digite o número:'))
  if n % 2 == 0:
    s += n
  else:
    s += 0
print('O somatório apenas dos números pares é de {}' .format(s))



### Programa: Ler o primeiro termo e a razão de uma PA. Mostrar os 10 primeiros termos ao final
n = int(input('Digite o primeiro número'))
razao = int(input('Digite a razão da PA (ex.: 1, 2, 5, 10'))
for i in range(n, n+(10*razao), razao):
  print(i, end=' ')
print('Fim')



### Programa: Ler um número inteiro e dizer se é ou não um número primo
n = int(input('Digite um número)'))
mult = 0
for i in range(1, n+1):
  if n % i == 0:
    print('Multiplo de', i)
    mult += 1

if mult == 2:
  print('É primo')
else:
  print('Não é primo')


## Modo aula
n = int(input('Digite o número:'))
mult = 0
for i in range(1, n+1):
  if n % i == 0:
    print('\033[34m', end=' ')
    mult += 1
  else:
    print('\033[31m', end=' ')
  print('{} '. format(i), end='')
print('\n\033[0mO número {} foi divisível {} vezes' .format(n, mult))
if mult == 2:
  print('Trata-se de um número primo')
else:
  print('Não se trata de um número é primo')




### Programa: Ler uma frase e dizer se ela é um palíndromo
text = str(input('Digite a palavra/texto:'))
textaj = text.lower().replace(' ','')
reverse = ''

for i in range(len(textaj), 0, -1):
  reverse += textaj[i-1]
if reverse == textaj:
  print('A palavra "{}" é um palindromo' .format(text))
else:
  print('A palavra "{}" NÃO é um palindromo' .format(text))


## Modo aula
frase = str(input('Digite a palavra/texto:')).upper().strip()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''

for letra in range(len(junto)-1, -1, -1):
  inverso += junto[letra]
print(inverso)
if inverso == junto:
  print('A palavra {} ao contrário é {}, ela é um palindromo' .format(frase,inverso))
else:
  print('A palavra {} ao contrário é {}, ela NÃO é um palindromo' .format(frase,inverso))

### Sem FOR

frase = str(input('Digite a palavra/texto:')).upper().strip()
inverso = frase[::-1]
if inverso == frase:
  print('A palavra {} ao contrário é {}, ela é um palindromo' .format(frase,inverso))
else:
  print('A palavra {} ao contrário é {}, ela NÃO é um palindromo' .format(frase,inverso))



### Programa: Ler a ano de nascimento de 7 pessoas e mostrar quantas são maior de idade
from datetime import date
atual = date.today().year
maiori = 0
menori = 0
lista = []

for i in range(1,8):
  y = int(input('Digite o ano de nascimento da {}a pessoa' .format(i)))
  lista.append(y)
  if atual - y >= 18:
    maiori += 1
  else:
    menori += 1

print(lista)
print('{} pessoa(s) maior de idade' .format(maiori))
print('{} pessoa(s) menor de idade' .format(menori))



### Programa: Ler peso de 5 pessoas e mostrar qual foi o maior peso e o menor peso
lista = []
for i in range(0,6):
  peso = float(input('Digite o seu peso:'))
  lista.append(peso)
print('O maior peso digitado foi de {}'. format(max(lista)))
print('O menor peso digitado foi de {}'. format(min(lista)))
print(lista)

## modo aula
maior = 0
menor = 0
lista = []
for i in range(0,6):
  peso = float(input('Digite o seu peso:'))
  lista.append(peso)
  if i == 1:
    maior = peso
    menor = peso
  else:
    if peso > maior:
      maior = peso
    if peso < menor:
      menor = peso
print('O maior peso digitado foi de {}'. format(maior))
print('O menor peso digitado foi de {}'. format(menor))
print(lista)



### Programa: Ler nome, idade e genero de 4 pessoas
# Retornar: Média de idade do grupo, nome do homem mais velho e quantas mulheres <20 anos
somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0

for p in range(1, 5):
  nome = str(input('Digite o nome da {}ª pessoa:' .format(p))).strip()
  idade = int(input('Digite a idade da {}º pessoa:' .format(p)))
  genero = str(input('Digite o genero da {}º pessoa [M/F]' .format(p))).strip()
  somaidade += idade
  if p == 1 and genero in 'Mm':
    maioridadehomem = idade
    nomevelho = nome
  if genero in 'Mm' and idade > maioridadehomem:
    maioridadehomem = idade
    nomevelho = nome
  if genero in 'Ff' and idade < 20:
    totmulher20 += 1
    
mediaidade = somaidade / 4
print('A idade média do grupo é {} anos' .format(mediaidade))
print('O homem mais velho tem {} anos e se chama {}' .format(maioridadehomem, nomevelho))
print('Ao todo são {} mulher(es) com menos de 20 anos' .format(totmulher20))

