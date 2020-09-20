class Konto:
    _räntesats = 0

    @classmethod
    def set_räntesats(cls, p):
        assert p >= 0, ('Negativ ränta', p)
        cls._räntesats = p

    @classmethod
    def get_räntesats(cls):
       return cls._räntesats

    def __init__(self, nr):
        self._nr = nr
        self.kontohavare = None
        self.saldo = 0
        self.intjänad_ränta = 0

    def get_nr(self):
        return self._nr

    def lägg_till_ränta(self):
        self.intjänad_ränta = self.intjänad_ränta + \
                self.saldo * Konto._räntesats / 100 / 365

