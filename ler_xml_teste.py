nomes = ['PEDRO', 'JOÃO', 'LETICIA']
for n in nomes:
  print(n)
print('\n - - -')
cont = 0
for v in range(0, 5):
  print(nomes[v], end=',')
  if (cont % 2 == 1):
    print('')
  cont = cont + 1
