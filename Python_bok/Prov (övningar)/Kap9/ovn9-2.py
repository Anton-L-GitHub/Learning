# Modulen temperatur (ska ligga i en fil med namnet temperatur.py)
temp = 0.0
tim = 0
min = 0

def observation(uppmätt, t, m):
    global temp, tim, min
    temp = uppmätt
    tim = t
    min = m

def aktuell_temp():
    return temp

def obs_tim():
    return tim

def obs_min():
    return min

# Main-modulen (denna ska ligga i en annan fil)
import temperatur
print('Avsluta med ctrl-c')
while True:
    temp = float(input('Uppmätt temperatur: '))
    ls = input('Tidpunkt(tt:mm): ').split(':')
    tid = [int(e) for e in ls]
    temperatur.observation(temp, tid[0], tid[1])
    temp = temperatur.aktuell_temp()
    tim = temperatur.obs_tim()
    min = temperatur.obs_min()
    print(f'Senaste observation: {temp} Klockan {tim:02d}:{min:02d}')