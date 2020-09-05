s = input('Skriv en text: ')
s = s.replace(' ', '')
s = s.lower()
t = s[::-1]
if s == t:
    print('Palindrom')
else:
    print('Inte palindrom')   