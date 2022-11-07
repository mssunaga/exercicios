### Sequência de fibonacci com while e função

def fibo(n):
  a, b = 0, 1
  while a < n:
    print(a, end=' ')
    a, b = b, a+b
  print()

n = int(input('Digite até qual nº  deseja ver:'))
fibo(n)
