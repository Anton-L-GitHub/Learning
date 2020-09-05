# Medelvärde, version 2
def medelv(*param):
    sum = 0
    for tal in param:
        sum += tal
    return sum / len(param)