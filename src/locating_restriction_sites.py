"""
A DNA string is a reverse palindrome if it is equal to its reverse complement. For instance, GCATGC is a reverse
palindrome because its reverse complement is GCATGC. See Figure 2.

Given: A DNA string of length at most 1 kbp in FASTA format.

Return: The position and length of every reverse palindrome in the string having length between 4 and 12. You may
return these pairs in any order.
"""


class SubStr:
    def __init__(self, fragment, pos):
        self.fragment = fragment
        self.pos = pos


f = open("temp_crap/rosalind_revp.txt")
data = f.readlines()
in_fasta = False
dna_str = ""

for d in data:
    if ">" in d:
        if in_fasta is True:
            in_fasta = False
            break
        else:
            in_fasta = True
        continue

    dna_str += d.strip("\n")

all_substrs = []
all_reverses = []

for i in range(0, len(dna_str)):
    for j in range(4, 13):
        if i + j > len(dna_str):
            break
        sub = dna_str[i:i + j]
        all_substrs.append(SubStr(sub, i))


def is_reverse(key):
    reverse = key.replace("A", "0").replace("T", "1").replace("C", "2").replace("G", "3")
    reverse = reverse.replace("0", "T").replace("1", "A").replace("2", "G").replace("3", "C")
    return key == reverse[::-1]


for item in all_substrs:
    if is_reverse(item.fragment) is True:
        all_reverses.append(item)

for item in all_reverses:
    print(str(item.pos + 1) + "\t" + str(len(item.fragment)))
