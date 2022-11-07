def count_characters(c):
  count = {}
  for i in c:
    if i in count:
      count[i] += 1
    else:
      count[i] = 1
  print(count)

word = str(input('Digite a frase:'))
print(f'Palavra: {word}\n', count_characters(word))
