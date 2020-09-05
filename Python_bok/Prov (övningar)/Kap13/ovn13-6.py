class C:
    _total_antal = 0
    def __init__(self):
        C._total_antal += 1
        self._nr = C._total_antal

    @ classmethod
    def antal_objekt(cls):
        return cls._total_antal

    def id(self):
        return self._nr

# Test
c1 = C()
c2 = C()
c3 = C()
print(C.antal_objekt())
print(c2.id())