# Medelvärde, fullständigt program
def medelv (a, b):
  return (a+b)/2
# Här startar exekveringen
x = float(input('Det första talet? '))
y = float(input('Det andra talet? '))
mv = medelv(x, y)
print(f'Medelvärde: {mv:.2f}') 