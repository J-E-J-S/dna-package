# DNA

## A basic package-in-progress of DNA-related functions.

## Functions

### seq.py
    composition - Returns base composition of nucleotide polymer as dictionary.

    transcribe - Returns transcribed DNA as mRNA.

    reverse_complement - Returns the complementary strand of a DNA polymer.

    gc_content - Returns GC contents of polymer as percentage (%).

    translate - Returns primary sequence of protein polypeptide.

    find_motif - Returns positions of specified motif with sequence. [(start, end), (start, end)...]

### fasta.py
    parse - Returns fasta label and sequence from fasta file containing single sequence

    multi_parse - Returns multiple fasta labels and sequences from fasta file containing multiple sequences
