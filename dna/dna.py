class Dna:

    def __init__(self, sequence):
        self.sequence = sequence.upper()

    def composition(self):

        comp = {}
        comp["A"] = self.sequence.count("A")
        comp["C"] = self.sequence.count("C")
        comp["G"] = self.sequence.count("G")
        comp["T"] = self.sequence.count("T")
        comp["U"] = self.sequence.count("U")

        if comp["U"] == 0:
            comp.pop("U")

        return comp

    
