"""
http://rosalind.info/problems/lcsm/

A common substring of a collection of strings is a substring of every member of the collection. We say that a common
substring is a longest common substring if there does not exist a longer common substring. For example,
"CG" is a common substring of "ACGTACGT" and "AACCGTATA", but it is not as long as possible; in this case,
"CGTA" is a longest common substring of "ACGTACGT" and "AACCGTATA".

Note that the longest common substring is not necessarily unique; for a simple example, "AA" and "CC" are both
longest common substrings of "AACC" and "CCAA".

Given: A collection of k (k≤100) DNA strings of length at most 1 kbp each in FASTA format.
Return: A longest common substring of the collection. (If multiple solutions exist, you may return any single solution.)
"""

dna = []
# super simple string check
dna_i = [
    "GATTACA",
    "TAGACCA",
    "ATACA"
] # result should be AC/TA

f = open("temp_crap/rosalind_lcsm.txt")
data = f.readlines()
temp_str = ""
in_fasta = False
num_of_strings = 0

for d in data:
    if ">" in d:
        if in_fasta is True:
            in_fasta = False
            dna.append(temp_str)
            num_of_strings += 1
            temp_str = ""
        else:
            in_fasta = True
        continue

    temp_str += d.strip("\n")

print("fasta strings: " + str(num_of_strings))

all_substrings = []
purge = []

for item in dna:
    everything_but_item = dna.copy()
    everything_but_item.remove(item)
    strlen = 1
    start_pos = 0

    for i in range(0, len(dna)):
        for j in range(start_pos, len(item)):
            sub = item[start_pos:start_pos+strlen]

            if not any(sub in s for s in everything_but_item):
                start_pos = 0
                strlen = 1
                break

            if j+1 == len(item):
                start_pos += 1
                strlen = 1
                break

            strlen += 1
            all_substrings.append(sub)

for fragment in all_substrings:
    count = 0
    for item in dna:
        if fragment not in item:
            purge.append(fragment)
        else:
            count += 1

    print("count " + str(count))
    if count is not num_of_strings:
        purge.append(fragment)

all_substrings = [i for i in all_substrings if i not in purge]
print(len(purge))
print(len(all_substrings))

longest_substr = ''

for fragment in all_substrings:
    if len(fragment) > len(longest_substr):
        longest_substr = fragment

print("stringy " + longest_substr)
