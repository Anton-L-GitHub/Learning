
def division(x, y):
    try:
        result = x / y
        return result
    except ZeroDivisionError as b:
        print(b)
    except Exception as e:
        print(e)
        # print(e.__class__.mro())
