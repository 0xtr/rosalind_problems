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
dna_i = [
    "GATTACA",
    "TAGACCA",
    "ATACA"
]
# should be AC

f = open("temp_crap/rosalind_lcsm.txt")
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

#dna = dna_i
#print(dna)

longest_substr_per_frag = {}
all_substrings = []
purge = []

for item in dna:
    everything_but_item = dna.copy()
    everything_but_item.remove(item)
    print(everything_but_item)
    strlen = 1
    start_pos = 0

    for i in range(0, len(dna)):
        for j in range(start_pos, len(item)):
            sub = item[start_pos:start_pos+strlen]
            # create a list of everything excluding this item, check if in that list? might speed it up
            if sub not in everything_but_item:
                print(sub + " not in list")
                start_pos = 0
                strlen = 1
                break

            #print(sub)
            #print(str(j) + " " + str(len(item)))
            if j+1 == len(item):
                #print("len finish")
                start_pos += 1
                strlen = 1
                break

            strlen += 1
            all_substrings.append(sub)

#print(all_substrings)

for fragment in all_substrings:
    #print(fragment)
    for item in dna:
        #print(fragment + " vs " + item + " : match? " + str(fragment in item))
        if fragment not in item:
            #print("purge")
            purge.append(fragment)

all_substrings = [i for i in all_substrings if i not in purge]
#print(len(all_substrings))
#print(len(purge))

longest_substr = ''

for fragment in all_substrings:
    #print(fragment)
    if len(fragment) > len(longest_substr):
        longest_substr = fragment

print("stringy " + longest_substr)
