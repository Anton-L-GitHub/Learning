import datetime
dt = datetime.datetime.now()
d = dt.date()
t = dt.time()
print('Dagens datum:', d)
print('Klockan är:', str(t)[:8])