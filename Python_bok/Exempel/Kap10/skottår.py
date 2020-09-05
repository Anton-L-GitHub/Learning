# Skottår
def är_skottår(år):
    assert år >= 1754, ('För tidigt årtal', år)
    return (år % 4 == 0 and år % 100 != 0) or år % 400 == 0