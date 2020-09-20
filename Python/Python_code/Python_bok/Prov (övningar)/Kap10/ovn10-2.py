# Modul för statistik
import math
def medelv(a):
    sum = 0
    for x in a:
        sum += x
    return sum / len(a)

def stdav(a):
    try:
        m = medelv(a)
        sum = 0
        for x in a:
            sum = sum + (x - m) ** 2
        return math.sqrt(sum / len(a))
    except:
        return None

def median(a):
    try:
        b = sorted(a)         # skapa en sorterad kopia
        n = len(b) 
        if n % 2 != 0:
            return b[(n-1)//2]                # udda antal element
        else:
            return (b[n//2-1] + b[n//2]) / 2  # jämnt antal element
    except:
        return None

# Test
a = []
print(median(a))
b = 15
print(stdav(b))

        