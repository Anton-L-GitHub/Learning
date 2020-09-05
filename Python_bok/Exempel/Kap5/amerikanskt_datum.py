# Översätt amerikanskt datum till svensk form
a = input('Skriv ett amerikanskt datum som mm/dd/åå: ')
månad = a[:2]
dag = a[3:5]
år = a[6:]
s = '20' + år + '-' + månad + '-' + dag
print('Svenskt datum: ' + s)