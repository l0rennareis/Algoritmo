termo = 0
while (termo <= 0):
  termo = int(input('Voce quer que a serie de Fibonacci vá ate qual termo? '))
  if (termo <= 0):
    print('O termo deve ser positivo!')


f1 = 1
print (f1)
f2 = 1
for i in range(1, termo):
  print(f2)
  f3 = f1 + f2
  f1 = f2
  f2 = f3
