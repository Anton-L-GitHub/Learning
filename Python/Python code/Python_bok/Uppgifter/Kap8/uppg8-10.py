def största(s):
    if len(s) == 0:
        return None
    elif len(s) == 1:
        return s[0]
    else:
        m = största(s[1:])
        if m > s[0]:
            return m
        else:
            return s[0]