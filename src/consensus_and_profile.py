"""
http://rosalind.info/problems/cons/
A matrix is a rectangular table of values divided into rows and columns. An m×n matrix has m rows and n columns.
Given a matrix A, we write Ai,j to indicate the value found at the intersection of row i and column j.

Say that we have a collection of DNA strings, all having the same length n . Their profile matrix is a 4×n matrix P
in which P1,j represents the number of times that 'A' occurs in the jth position of one of the strings, P2,
j represents the number of times that C occurs in the jth position, and so on (see below).

A consensus string c is a string of length n formed from our collection by taking the most common symbol at each
position; the jth symbol of c therefore corresponds to the symbol having the maximum value in the j-th column of the
profile matrix. Of course, there may be more than one most common symbol, leading to multiple possible consensus
strings.
"""

# discard FASTA identifiers

dna = []
'''
example:
dna = [
    "ATCCAGCT",
    "GGGCAACT",
    "ATGGATCT",
    "AAGCAACC",
    "TTGGAACT",
    "ATGCCATT",
    "ATGGCACT"
]
'''

f = open("temp_crap/rosalind_cons.txt")
data = f.readlines()
temp_str = ""
in_fasta = False

for d in data:
    if ">" in d:
        if in_fasta is True:
            in_fasta = False
            dna.append(temp_str)
            temp_str = ""
        else:
            in_fasta = True
        continue

    temp_str += d.strip("\n")

f.close()

a = [0] * (len(dna[0]))
c = [0] * (len(dna[0]))
g = [0] * (len(dna[0]))
t = [0] * (len(dna[0]))

for horizontal in range(0, len(dna[0])):
    for vertical in range(0, len(dna)):
        if dna[vertical][horizontal] is "A":
            a[horizontal] += 1

        if dna[vertical][horizontal] is "C":
            c[horizontal] += 1

        if dna[vertical][horizontal] is "G":
            g[horizontal] += 1

        if dna[vertical][horizontal] is "T":
            t[horizontal] += 1

consensus = ""
for r in range(0, len(a)):
    highest = 0
    h_letter = ""

    if a[r] > highest:
        highest = a[r]
        h_letter = "A"
    if c[r] > highest:
        highest = c[r]
        h_letter = "C"
    if g[r] > highest:
        highest = g[r]
        h_letter = "G"
    if t[r] > highest:
        highest = t[r]
        h_letter = "T"

    consensus += h_letter

print(consensus)
