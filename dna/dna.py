class Dna:

    def __init__(self, seq):

        self.seq = seq.upper()

        # Check sequence conforms
        for base in self.seq:
            if base not in 'AGCTU':
                raise NameError('Unrecognized base in sequence.')

    def composition(self):

        comp = {}
        comp["A"] = self.seq.count("A")
        comp["C"] = self.seq.count("C")
        comp["G"] = self.seq.count("G")
        comp["T"] = self.seq.count("T")
        comp["U"] = self.seq.count("U")

        if comp["U"] == 0:
            comp.pop("U")

        return comp

    def transcribe(self):

        self.seq = self.seq.replace('T', 'U')

        return self

    def reverse_complement(self):

        paired_seq = ""

        for base in self.seq:
            if base == "A":
                paired_seq += "T"
            if base == "T":
                paired_seq += "A"
            if base == "G":
                paired_seq += "C"
            if base == "C":
                paired_seq += "G"

        self.seq = paired_seq[::-1]

        return self

    def gc_content(self):

        gc = self.seq.count('C') + self.seq.count('G')
        gc_content = (gc / len(self.seq) * 100)

        return gc_content

    def translate(self):

        # Check that seq isn't DNA
        if 'T' in self.seq:
            raise NameError('Sequence is not RNA, chain .transcribe() method to convert DNA --> RNA')

        # Generate codon table
        bases = "UCAG"
        codons = [a + b + c for a in bases for b in bases for c in bases]
        amino_acids = 'FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG'
        codon_table = dict(zip(codons, amino_acids))

        protein = ''
        count = 0
        while count < len(self.seq):
            codon = self.seq[count:count+3]
            try:
                residue = codon_table[codon]
                protein += residue

            # If codon not recognised, add missing residue '_'
            except:
                protein += '_'

            count += 3

        self.seq = protein

        return self
