# Com map

listaCelsius = [32,30,35,23,35,29,21,10,15,14,16,18]

listaFahrenheit = map(lambda x: (x*(9/5))+32, listaCelsius)

print(list(listaFahrenheit))


# Com list comprehension

celsius = [0, 10, 20.1, 35.4]
fahrenheit = [((9/5) * c + 32) for c in celsius]
fahrenheit
