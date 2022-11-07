### Checando se a palavra ou frase é um palíndromo.
# A versão remove espaços para fazer a verificação

text = str(input('Digite a palavra/texto:'))
ajustedtext = text.lower().replace(' ','')
reversedtext = ''

for i in range(len(ajustedtext), 0, -1):
  reversedtext += ajustedtext[i-1]
if reversedtext == ajustedtext:
  print(f'A palavra "{ajustedtext}" ao contrário é "{reversedtext}". Logo, é um palindromo')
else:
  print(f'A palavra "{ajustedtext}" ao contrário é "{reversedtext}". Logo, não é um palindromo')
