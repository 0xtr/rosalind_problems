"""
The GC-content of a DNA string is given by the percentage of symbols in the string that are 'C' or 'G'. For
example, the GC-content of "AGCTATAG" is 37.5%. Note that the reverse complement of any DNA string has the same
GC-content.

DNA strings must be labeled when they are consolidated into a database. A commonly used method of string labeling is
called FASTA format. In this format, the string is introduced by a line that begins with '>', followed by some
labeling information. Subsequent lines contain the string itself; the first line to begin with '>' indicates the
label of the next string.

In Rosalind's implementation, a string in FASTA format will be labeled by the ID "Rosalind_xxxx", where "xxxx"
denotes a four-digit code between 0000 and 9999.

Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).
Return: The ID of the string having the highest GC-content, followed by the GC-content of that string. Rosalind
allows for a default error of 0.001 in all decimal answers unless otherwise stated; please see the note on absolute
error below.
"""

sample_data = """
>Rosalind_2386
ACCGCACCACCCATTAAGCCGACCAGTCCTACCGCACCAGGATATTCATGGCGAGTAGCT
TTACCCTGGTAGCCGCTCCGCCGAGTATAGTTGCTAAGACTGAAGTTCGGCACTTATCCT
ATTTAGTGGGGCAGGGCTCTAAATAAAAGTGAAGAACACGGGCGGTGTAGTGTGTCCTTC
TACGCCACAGTTGACACAGTCTTTATAGAAATCCTGACTCCTGCTACTAAGACGTTTAAG
CCAGGGGTCTAATACGTACAATATGCCTCGGTAGTTCCCCGGCTCACATGCTTGAATAGC
CTGAACCGGGTGAGTGACCCGCAGGTACCGACCCTCAAGGCACCTAGGGTGACTGGCGCC
CACACATATGTTTCGGCTTAGTTTACAGTCGGCTGGAGACTTCAGGGACCTACAACTAGG
TATACACCTACGAAGTTACGAACTAGCATTACGGTCCCCTGACCCATGTTGACGTAATCA
GGGTCCTGCGTATGTCATGTCTAGACTGCGCACTCACGCAGATAATTTCGGTTTACTGAC
AGGCCCTCGATATATAACTCTAAGGTAAAAATTACCGGCCGTCAGAATAACTGGACACGC
TATAGCTGTCTGGAATTGATCGGCCTCTCTAACAGCTCGCGACACGAATGGCTTGGAGTT
CGTGGGTCGCTATACGTCGATTAACGCCTCATTTCAGATTGTCGGCGTAACTGCTAGCAG
CCATTGCCTAAAGCATAGCCTTCACGTCCGCACAATGGCTGTTACTCTCCAAACACGACC
GGGTAGGAATTTCCGGAACATACTAGCTGTAAAAGGGGC
>Rosalind_8392
AGAGGACATGATCATCCGAGGACTTTAAACTTGTGTTCCGTCTTCCCCTTGGTGCGGGTG
GCCCCACGCGGGATCCGTTGATACGACACTGATGATGAAAAGCGCCGGTATCGTTAAAGA
GCGCATCACCTTCGGAGAATCGAGTCTTGTGTGGGTAGCTTAAAGACGGTGAGTATCCCA
AGCCAAGTCCGCGTACAAATACACTCGTGGGTAAAACCATTAGGGTTACATGCCATCCCC
GGCGACACTCGGTGACTGACACTTACGGTCGAGGGGTATCGGTGGTATCTGTCAACAACG
TGCTAACAGGGCAGGCAGTACTGAGAGGTGTTTGCTCCGGGGTCTTGGCCGGCCGTCAAA
CGCGAACTTCGAATTTAATGACTGACGCTTAAACGGTCCTCTTTGTGAGTCTGACCCACC
TAACGAGGACTCTCGCACCTCGCGTGCAAAGGATCACCGGGTGTAGCCGAGAGCAGGTAG
GAGGGAGCTGACGGTTTGTTGGATAGACCAAGGAGGTCCGGAAGATGGCGTTATTCGTGT
CCAATCGATGTGGCTATTGTGCCCACGTCCCCTAATTCAGGCTCGCAAGAACAGGACTGG
CTGGGAGTTTCGTCCAATCTAGTTATCGCGGTTTGGGATTCTGTCGCCTGTGGGCGCCCA
GGTTTGGCTCCATTTGGATATAGGCGCCCCCGACCACAAGCCTGCGATACTATTGCAATA
CGGTCGGGCAGGACACGTACCGCGGGATAACGACTCCTATCGACATCACATGAGGACCTG
GAGACATATTCATGGTGTGTATCCTGCCTTGTATTCGACGCCTAATTCCAGCCTGGCCGC
CGAAGCATGGGTTCGGAGTGTTTTGATCTATGCACAAAGTGTGCGATCATGGTTCGAATA
CTGAGCAAGTCCACGCAAGCTGACGAGAAGGTCAATAGCCGCGCATAAGAAACGCGCACG
GCTCACCGCGGTTGTCACGCGCGGTCGTCG
>Rosalind_9402
CTTCACCCCAGGAATTCACGGAGTGGGGCCGTACGTCGCACGCGGTCTTTAAATATAATG
AAAGCAGATCCTTTCGTATTAATGCGTTTATTAGACTGTCTAGGCGCACACAGAAGTGGA
CTGCTTCGCTCCTTGAGACTCACGACAGGCCGAGCCCGACCCAACGTCGACTAAGGAGAC
GGGGTGGAAGCCGACCGACTCGGTCTCGATGTGCATTCACCTATACCACATGTCGTGACG
TTTGTGGACTTAAAAATACAAAACGGTTCTCACTGGCGATTGTATGCGAACAACAAGAGA
GCGACAGCTCTTCGATAGTGGTGTAGCACATCAGGCGACCCCAAACGCGCTGATACACCT
TCTGTTCCGGTGAGTACTGTCCATTAGCTACTTAACAATTGCGTAAACGCTTCGGGAGCA
CCCGAGCGGAGACCCAGTTCGGTGCCTACGTACGAGTGAAATTGTCGATGTCAAAAGGGA
TTACCATTACATGCGTAGACGTCACAATGCGAACGGCGCGTAACAAGCCGAGCTGGTATT
TATGATTAACCAGTCAGATTCACATGCACGCCATGTGCCTGTAGTTAAGTGTACTAATGG
GCTCTACACAGAGATGGTCAGCTCCGGAAGCGCTCTCCAAGTATCCCCCCAGTTGTGGAC
GGGAAACGATCGCTAAAGGGGGCCCGCCTGTAGCGGGTATTAACCTAATGTCGTTACTCG
CTTCCTTGCCAGACACTTGTGTTTGCAACGAAGATGGTTCTGGGTTTCATGGTCAAGCGT
AGAACCGTCGAGATTAACGCGCAGAGGGGGCTGTGAGGATACGCAGTGGCCAGTTAAAAG
TGACTGGTGAGACTGCCATGTAGGGAGAGTATCTATCCAATCCCGCACACAAGATTCTAG
TACAG
>Rosalind_6359
TCTCCCTGCCAGTGAGCCGAACGGCTAGCCCGCAAATAAATCTGCGCAAGCCTTGTAATA
CACGCGCTTGCTGAGCACTAGATTCAAACATACAAATCTTTGCCTCCCTGGTACGGATCT
CTATCGAGGACCCCGGTGAGGTGGCGCAAAAAATCCCACGCCCATCTGTTTAAGGGCTTT
AAGAGAATCTATTCATGAAGCAGTAGGTTTTATCGAATCATACAGGGCTGAACCTGTTCC
CGTAAAGGTTTAGACTTTCCGCTGAAGCCGTGGTCCGGTAGGACGTCACTACCTAAGGGG
TCTGCGCCAGCCCCACCGTGGGCTCATTTCTTTAATCGTTATGTTACAAACTCTACAGTG
AGCGTACACTCACTTACGAGGGACAAAGTCTCAAACGCAGTGAGCGACCAGCTCTTACCG
CTTGCCATTGATCTTAGGTCCATGGGCTCATGTGGTGCCTTCATAACGGTAGGCCCTACC
AGGGGGTATCATGCCGCAGAGTCAGTTAAACTAGGTGGTTGCATACAGTGGCACAGACGA
TACCTTCAGTCGTCTCCCCACATTGCGTTTGCAGGGTGTAATCCTGCGGACCTAATAGGT
TTAGTGAACTGGGGGGCAGTGGGTTACCGTCTCCGCCTTGGCGCCCACGCCTAGAGTCTG
CCTTTACCAGCTGATTCTCAGATCCATTTGGTATCTGCCACTAAATAACATGCATGGACA
GAGAGCAGCGGTATACTGCTACAGCTGTAGAATTTCAAGCGTGATCTAATCTGTAATAGT
CAAGATGTCCAAAGAAGTGCACCTGTATCCTCGTAGTGGGGTTAAATTTCCTAAAATTCA
CCACTCTTTATTACTACCAGAATAATGCAAGATGACGCGTACGACTGCCTGGGACCTATG
GTGTGCAACG
>Rosalind_4025
ATGGATCCGTACGTGCGTTGGTCCACTATAAAAGGACCCCCTCTACAATATGTGAAAGGC
CAAGCACTGTAAGGATCTACGGGTCACAACGCCATAAGACACGTTCAAATAATGTACACC
TGAACGTTAGATAGAAGATTATCCTGAGGTTCCTCCGCATCATTCCGCCACAGCAGTGCT
TTGGGGGAACATTGAGAGTCGCGCCAATAAATATACAGATTTCCCAATAAGATCAGAAAC
AACTTGGCTAGCAGATATAGGTAACTGTAGTCGGCCATATTGGCGTTTCACTCCCAGCCG
GAGTGTTCGATGATTGCAGCCGGGTATAGATTCGTAGACCCCCCGCCTTCTTTACCGTAG
ATGAAGCCAAACCGGCGGGTTGATTATCCCAAGCGAACGGGCTACAATGACTGGGGTCGC
GTCCCGACGACCTTCTCGTGGGCACCTTATCTGGAGAATAACCATGGGGAGGCGTTGAGC
CTCGGGCGGATTTTAGCCGGGCTGCGGTCCGAGTTAAAAAGCGTTGAGCGATTGTGTCCA
CCTCCAGATGTCACTCAGCGACGGGGCTTCTACTCGTGGGTAGAGGCTAGGTGGTTTGTT
GTGTCAATCGTTGCGCGGCGCCAAGAACAGTGATCCATTGGAGCATTGGGGTCGTTGACC
TCACGACAATGTTGAGAATAGTCCGCTGTGTATCAAACTGCCCGGCTCAGATCTAGGATG
AGTTATGTTTGTAAATGAGAGTTGGGACCACAGATCGTACGCCTCAGGATACGGCCAGTA
TTCCTTTAGTCGAGACGGAACATCGGTTGGTGGCCAATGCGTCATCG
"""


class DNAString:
    identifier = ''
    GC_content = 0

    def __init__(self, dna):
        if len(dna) > 1:
            fragments = list(filter(lambda x: len(x) > 1, dna.split("\n")))
            self.identifier = fragments[0]
            self.GC_data = ''.join(fragments[1:])
            self.calc_content()

    def calc_content(self):
        length = len(self.GC_data)
        occurrences = self.GC_data.count("C") + self.GC_data.count("G")
        self.GC_content = (occurrences/length) * 100


raw_data_items = list(filter(lambda x: len(x) > 1, sample_data.split(">")))
dna_items = list(map(lambda item: DNAString(item), raw_data_items))
highest = DNAString('')

for dna in dna_items:
    if dna.GC_content > highest.GC_content:
        highest = dna

print(highest.identifier)
print("%.6f" % highest.GC_content)