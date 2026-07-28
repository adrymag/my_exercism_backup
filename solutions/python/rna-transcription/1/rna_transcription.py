"""RNA Transcription module.

Provides a function to transcribe a DNA strand into its RNA complement
according to the rules of RNA Interference.
"""


def to_rna(dna_strand):
    """Transcribe a DNA strand into its RNA complement.

    Each nucleotide in the DNA strand is replaced by its RNA complement:
        - Guanine (G)  -> Cytosine (C)
        - Cytosine (C) -> Guanine (G)
        - Thymine (T)  -> Adenine (A)
        - Adenine (A)  -> Uracil (U)

    Parameters:
        dna_strand (str): The DNA sequence to transcribe. Valid characters
            are 'G', 'C', 'T', and 'A'. An empty string is also valid.

    Returns:
        str: The RNA complement sequence with the same length as the input.
    """
    # str.maketrans() builds a translation table (a mapping of Unicode
    # ordinals to replacement strings) from the two argument strings.
    # The first string lists the characters to find; the second lists
    # what to replace them with, position by position.
    #   G -> C
    #   C -> G
    #   T -> A
    #   A -> U
    transcription_table = str.maketrans('GCTA', 'CGAU')

    # str.translate() walks through the input string and replaces every
    # character that appears in the translation table. Characters not
    # in the table are left unchanged. This is an O(n) operation and is
    # very efficient. An empty string simply returns an empty string.
    return dna_strand.translate(transcription_table)