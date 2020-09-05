s = input('Skriv in texten: ')
s = s.lower()
r = ''
i = 0
while i < len(s):
    if s[i]=='a' and i+1<len(s) and s[i+1]=='a':
        r += 'å'
        i += 2
    elif s[i]=='a' and i+1<len(s) and s[i+1]=='e':
        r += 'ä'
        i += 2
    elif s[i]=='o' and i+1<len(s) and s[i+1]=='e':
        r += 'ö'
        i += 2
    else:
        r += s[i]
        i += 1
print(r)