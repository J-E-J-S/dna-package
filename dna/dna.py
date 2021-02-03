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

    def transcribe(self):

        return self.sequence.replace('T', 'U')

    def reverse_complement(self):

        paired_sequence = ""

        for base in self.sequence:
            if base == "A":
                paired_sequence += "T"
            if base == "T":
                paired_sequence += "A"
            if base == "G":
                paired_sequence += "C"
            if base == "C":
                paired_sequence += "G"

        return paired_sequence[::1]

    def gc_content(self):

        gc = self.sequence.count('C') + self.sequence.count('G')
        gc_content = (gc / len(self.sequence) * 100)

        return gc_content

    def translate(self):

        # Generate codon table
        bases = "UCAG"
        codons = [a + b + c for a in bases for b in bases for c in bases]
        amino_acids = 'FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG'
        codon_table = dict(zip(codons, amino_acids))

        protein = ''
        count = 0
        while count < len(self.sequence):
            codon = self.sequence[count:count+3]
            try:
                residue = codon_table[codon]
                protein += residue

            except:
                pass

            count += 3

        return protein
