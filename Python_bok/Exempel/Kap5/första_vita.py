# Leta efter det första vita tecknet i en text
s = input('Skriv en text: ')
i = 0        # i används som räknare
for c in s:
    if c == ' ' or c  == '\t':
        break
    i = i + 1
if i < len(s):
    print(f'Första vita tecken finns på plats nr {i}')
else:
    print('Inget vitt tecken')