s = input('Skriv ett svenskt datum som åååå-mm-dd: ')
månad = s[5:7]
dag = s[8:]
år = s[2:4]
a = månad + '/' + dag + '/' + år
print('Ameriksnskt datum: ' + a)