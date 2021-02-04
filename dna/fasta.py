class Fasta:

    seq = ''

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

        return self
