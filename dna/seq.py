class Seq:

    def __init__(self, seq):

        self.seq = seq.upper()

        # Check sequence conforms
        for base in self.seq:
            if base not in 'AGCTUN':
                raise NameError('Unrecognized base in sequence.')

                if base == 'N':
                    import warnings
                    warnings.warn("Warning: This sequence contains undefined nucleotides.")


    def composition(self):

        comp = {}
        comp["A"] = self.seq.count("A")
        comp["C"] = self.seq.count("C")
        comp["G"] = self.seq.count("G")
        comp["T"] = self.seq.count("T")
        comp["U"] = self.seq.count("U")

        if comp["U"] == 0:
            comp.pop("U")

        if comp["T"] == 0:
            comp.pop("T")

        return comp

    def transcribe(self):

        # Check sequence is not RNA
        if 'U' in self.seq:
            raise NameError('Sequence is already RNA.')
        if 'N' in self.seq:
            import warnings
            warnings.warn('Warning: This sequence contains ambiguous sequences.')

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

            # reverse_complement intended for DNA, so will warn if RNA seq
            if base == "U":
                paired_seq += "A"
                import warnings
                warnings.warn("Warning: This sequence contains RNA.")

            # Warn if sequence contains undefined nucleotides
            if base == "N":
                paired_seq += "N"
                import warnings
                warnings.warn("Warning: This sequence contains ambiguous sequences.")

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

        if len(self.seq) % 3 != 0:
            import warnings
            warnings.warn('Warning: Sequence is truncated.')

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

            # If codon not recognised, add missing residue '-'
            except:
                protein += '-'
                import warnings
                warnings.warn('Warning: Sequence contains unrecognised codons.')

            count += 3

        self.seq = protein

        return self

    def find_motif(self, motif, type='dna'):

        import re

        length = len(motif)

        # Create regex expression from motif
        if type == 'dna':
            motif = motif.replace('R', '[AG]')
            motif = motif.replace('Y', '[CTU]')
            motif = motif.replace('K', '[GTU]')
            motif = motif.replace('M', '[AC]')
            motif = motif.replace('S', '[CG]')
            motif = motif.replace('W', '[ATU]')
            motif = motif.replace('B', '[^A]')
            motif = motif.replace('D', '[^C]')
            motif = motif.replace('H', '[^G]')
            motif = motif.replace('V', '[^U]')
            motif = motif.replace('N', '[AGUTC]')

        if type == 'protein':
            motif = motif.replace('B', '[DN]')
            motif = motif.replace('J', '[LI]')
            motif = motif.replace('Z', '[EQ]')
            motif = motif.replace('X', '[^\*-]')

        # Finditer with lookahead to allow motif overlap
        positions = [(match.start()+1, match.start()+length)  for match in re.finditer('(?=' + motif + ')', self.seq)]

        return positions

    def ORFs(self):

        """"
        Returns the 6 reading frames for a DNA sequence as a dictionary
        ORFs 1-6: ORF 1-3 = Forward, ORF 4-6 = Reverse
        """
        ORFs = {} # Dictionary to hold frames and ids: 1-6

        frame = 0
        while frame < 3:
            # Forward Frame
            sequence = self.seq # Returns a string
            id = 'ORF-' + str(frame+1) # Re-index
            item = Seq(sequence[frame:]) # Splice sequence to reading frame
            ORFs[id] = item.transcribe().translate().seq # Translate ORF, has to be DNA

            # Reverse Frame
            id = 'ORF-' + str(frame+4)
            item = self.reverse_complement().seq
            item = Seq(item[frame:])
            ORFs[id] = item.transcribe().translate().seq

            frame +=1

        return ORFs
