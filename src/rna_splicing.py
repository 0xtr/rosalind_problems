"""
After identifying the exons and introns of an RNA string, we only need to delete the introns and concatenate the
exons to form a new string ready for translation.

Given: A DNA string s (of length at most 1 kbp) and a collection of substrings of s acting as introns. All strings
are given in FASTA format.

Return: A protein string resulting from transcribing and translating the exons of s.
(Note: Only one solution will exist for the dataset provided.)
"""

rna_codons = {
    "UUU": "F",
    "CUU": "L",
    "AUU": "I",
    "GUU": "V",
    "UUC": "F",
    "CUC": "L",
    "AUC": "I",
    "GUC": "V",
    "UUA": "L",
    "CUA": "L",
    "AUA": "I",
    "GUA": "V",
    "UUG": "L",
    "CUG": "L",
    "AUG": "M",
    "GUG": "V",
    "UCU": "S",
    "CCU": "P",
    "ACU": "T",
    "GCU": "A",
    "UCC": "S",
    "CCC": "P",
    "ACC": "T",
    "GCC": "A",
    "UCA": "S",
    "CCA": "P",
    "ACA": "T",
    "GCA": "A",
    "UCG": "S",
    "CCG": "P",
    "ACG": "T",
    "GCG": "A",
    "UAU": "Y",
    "CAU": "H",
    "AAU": "N",
    "GAU": "D",
    "UAC": "Y",
    "CAC": "H",
    "AAC": "N",
    "GAC": "D",
    "UAA": "",
    "CAA": "Q",
    "AAA": "K",
    "GAA": "E",
    "UAG": "",
    "CAG": "Q",
    "AAG": "K",
    "GAG": "E",
    "UGU": "C",
    "CGU": "R",
    "AGU": "S",
    "GGU": "G",
    "UGC": "C",
    "CGC": "R",
    "AGC": "S",
    "GGC": "G",
    "UGA": "",
    "CGA": "R",
    "AGA": "R",
    "GGA": "G",
    "UGG": "W",
    "CGG": "R",
    "AGG": "R",
    "GGG": "G"
}

f = open("temp_crap/rosalind_splc.txt")
data = f.readlines()
in_fasta = False
substrings = []
expected = "MVYIADKQHVASREAYGHMFKVCA"
start_pos = 0
end_pos = 3
dna_str = ""
main_str_done = False

for d in data:
    if ">" in d:
        if in_fasta is True:
            in_fasta = False
            main_str_done = True
        else:
            in_fasta = True
    else:
        if main_str_done is False:
            dna_str += d.replace("\n", "")
        else:
            substrings.append(d.strip("\n"))

protein = ""

for sub in substrings:
    dna_str = dna_str.replace(sub, "")

dna_str = dna_str.replace("T", "U")

for i in range(0, int(len(dna_str)/3)):
    chunk = dna_str[start_pos:end_pos]
    start_pos += 3
    end_pos += 3
    protein += rna_codons[chunk]

print(protein)
