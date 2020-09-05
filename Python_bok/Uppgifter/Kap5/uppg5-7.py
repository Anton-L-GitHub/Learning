a = ' Erik Andersson 990314-2714  '
a = a.strip()        # a blir 'Erik Andersson 990314-2714'
i = a.rfind(' ')+1   # i får värdet 15
j = a.find('-')      # j får värdet 21
b = a[i+4:j] + '/' + a[i+2:i+4]
print(b)