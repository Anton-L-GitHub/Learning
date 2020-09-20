def namnet(rad):
    ord = rad.split()
    namnen = [e for e in ord if not e.isdecimal()]
    namn = ' '.join(namnen)
    return namn.lower()