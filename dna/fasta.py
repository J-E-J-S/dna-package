class Fasta:

    seq = ''
    label = ''

    def __init__(self, file):
        self.file = file

    def parse(self):

        with open(self.file, 'r') as read_file:
            contents = read_file.readlines()

            sequence = ''
            count = 1
            while count < len(contents):
                sequence += contents[count]
                count += 1

            self.seq = sequence.replace('\n', '')
            self.label = contents[0]

        return self

    def multi_parse(self):

        labels = [] # Holds fasta labels
        seqs = [] # Holds conjugated sequences

        with open(self.file, 'r') as read_file:
            contents = read_file.readlines()
            read_file.close()

        # Bit messy but better error handling and only loop once
        sequence = ''
        for index, value in enumerate(contents):

            # Check if item is the label
            if value.startswith('>') != True:
                sequence += value # Start dynamically creating sequence

                # Adds last sequence (no '>' after)
                if index + 1 == len(contents):
                    seqs.append(sequence.replace('\n', '')) # Replace new line

            # Check again item is label
            if value.startswith('>'):

                # Remove newline formatting
                if value.endswith('\n'):
                    labels.append(value[:-1]) # Better than replace as prevents erroneous removal
                else:
                    labels.append(value)

                # First item will normally be label so don't add un-needed '' to seqs
                if index != 0:
                    seqs.append(sequence.replace('\n', '')) # When get to label, add running sequence to store
                    sequence = '' # Reset running sequence

        self.seq = seqs
        self.label = labels

        return self
