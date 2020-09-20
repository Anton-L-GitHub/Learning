def alfa(s):
    s = s.lower()
    v = list(s)
    for i in range(0, len(v)):
        if v[i] == 'ä':
            v[i] = 'å'
        elif v[i] == 'å':
            v[i] = 'ä'
    return v