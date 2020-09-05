class Datum:
    def __init__(self, å, m, d):
        self.å = å
        self.m = m
        self.d = d

    def __str__(self):
        return f'{self.å}-{self.m:02}-{self.d:02d}'

