class Räknare:
    def __init__(self, värde, minsta, största):
        self.minsta = minsta
        self.största = största
        assert(värde >= minsta and värde <= största)
        self.värde = värde

    def öka(self):
        if self.värde < self.största:
            self.värde += 1
        else:
            raise ValueError('Kan inte öka räknare')

    def minska(self):
        if self.värde > self.minsta:
            self.värde -= 1
        else:
            raise ValueError('Kan inte minska räknare')

# Test
r = Räknare(2, 1, 5)
r.minska()
r.minska()

        
