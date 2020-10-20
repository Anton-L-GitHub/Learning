t = float(input('Temp? '))
if t < 0:
    print('Det är svinkallt')
    print('Stanna inne')
elif t < 18:
    print('Det är kallt')
    print('Sätt på värmen')
    if t < 12:
        print('Sätt på jackan')
elif t < 30:
    print('Det är varmt')
    if t >= 22:
        print('Stäng av värmen')
else:
    print('Det är ökenhett')
    print('Sätt på AC')
print(f'Det är {t:.1f} grader')