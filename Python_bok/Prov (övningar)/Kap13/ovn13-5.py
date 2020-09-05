class C:
    _total_antal = 0
    def __init__(self):
        C._total_antal += 1

    @ classmethod
    def antal_objekt(cls):
        return cls._total_antal

# Test
c1 = C()
c2 = C()
c3 = C()
print(C.antal_objekt())
