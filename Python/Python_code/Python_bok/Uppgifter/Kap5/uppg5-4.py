# Leta efter det sista vita tecknet i en text
s = input("Skriv en text: ")
i = len(s)-1
while i >= 0:
    if s[i] == " " or s[i]  == "\t":
        break
    i -= 1
if i >= 0:
    print(f"Sista vita tecken finns på plats nr {i:d}")
else:
    print("Inga vita tecken")