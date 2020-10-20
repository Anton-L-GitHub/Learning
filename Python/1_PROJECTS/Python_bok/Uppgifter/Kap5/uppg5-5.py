# Leta efter det första vita tecknet i en text
s = input("Skriv en text: ")
for i in range(0,len(s)):
    if s[i] == " " or s[i]  == "\t":
        print(f"Första vita tecken finns på plats nr {i:d}")
        break
else:
    print("Inga vita tecken")