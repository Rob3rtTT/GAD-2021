class Fractie(object):
    def __init__(self, numarator, numitor):
        self.numarator = numarator
        self.numitor = numitor

    def get_numarator(self):
        return self.numarator

    def get_numitor(self):
        return self.numitor

    def set_numitor(self, numitor_nou):
        self.numitor = numitor_nou

    def set_numarator(self, numarator_nou):
        self.numarator = numarator_nou



    def __str__(self):
        return f"{str(self.numarator)}/{str(self.numitor)}"

    def __add__(self, fractie):
        fractie = Fractie(4,6)
        fractie.numitor = self.numitor*fractie.numarator+fractie.numitor*self.numarator
        fractie.numarator = self.numarator*fractie.numarator
        return fractie

    def __sub__(self, fractie):
        fractie = Fractie(4,6)
        fractie.numitor = self.numitor*fractie.numarator-fractie.numitor*self.numarator
        fractie.numarator = self.numarator*fractie.numarator
        return fractie

    def inverse(self):
        return Fractie(self.numitor, self.numarator)
