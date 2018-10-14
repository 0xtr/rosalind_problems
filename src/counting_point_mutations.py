"""
Given two strings s and t of equal length, the Hamming distance between s and t, denoted dH(s,t), is the number of
corresponding symbols that differ in s and t.

Given: Two DNA strings s and t of equal length (not exceeding 1 kbp).
Return: The Hamming distance dH(s,t).
"""

s1 = "CCTGTGCAGCAATCTCACCGGGCAGAACCCTGTGCTGGCATCGCACTACAGAAGGAAAGTTTAAGTAATATTAACTAGCAGCGGGTATTCTTAGGCCAATGGCTGTGAAATGTGCTACAGCGGTGAAAGGTAACATAGCCAGCGAGGACAGATCTCACTCGCCGCCCGATCACCGAGCGTCTAAATTTCGGTGGCGTGATCCTTATGAGCCCTGGGATCTCAGGATCTTCTTTGTAGCCGAATGATTAACCATCAAAGGTTTGTCATATCCCTTATTGGACACGTGTAGTAGAGAAAATATTTGCCGCCCGTAGAGCTTCGTAGACGGAACGGATGGCATGCTTAGGCTTAATCTCGGGCAGAAAACCGTTTTAAAAACTCGGCCCGAATTCGTTTTCAAAGCGCGGCCCTTTTTGTGATCCTTACGCGCGTAATCCCGTCTGTCCACCCTATGATCGAGGTAATGGGGTATGAGGCGGTTTGGTGAGAGCGCTGATTCCCACGCGGGTCAGACGTTTCACCATCCGCCTGTGCTATTTCGTCCTGAGCCTTCTCCGGGGGCGATCAACACTCTTCACTTGCGAGAAGGTCTAAGATCGGCTCATCAAACATTCGCAACAGTGAGCAGATTTGCAAAAGGTAATGTAGCAGATATAACGCCGATCCTCCGATGACAAGCCTCTGGAAATAGTGAGGATTCCGGCGGTCGTCCTAGAATGTTGCCTCTCTCCAAGACACACCGCCCATTCAGTTTTGATATTAGCTGCTTGCGTAGGTTTGCTAAGTCGGGGCCTACCCGCCACAGCTAGTGTAGCCACTGAATGCTCTGCTTTAGTTCAGGTTTCCGGGCGCGAAATCCTATGCAAGATCCAACATACCAAACCGGGCCAAAGCATGGCTCGATAATCTTCGTAAAGGTTGATCAACAGCAGGGGGAATGCACCGGTCTACCCCAGCGCTACTCTCCCCTCCTACCGTCTG"
s2 = "TCACCGTTTCTATATGATAGTGGATACCAGTTTCTGATTCCGCGCAGATTGAATGAAAATTTCAGTAATATTTAAAGGCCTTCGGTCGGCCTACAACTCTTGCGTTGAATTGCCGTACCAAGTATAAAGCAAAAATCAAGAGGGCGGCTTCGTCAATCAGACATTCCATTCATAGACGATCTAAATAACGTTGGAGAGAGACTTAACAGGCTAGTGCTCGTGGTCTTGTCTTCATAACCGAGCCAAGAACCGCCATTCGTTTAGTACACCCGGATGTTGGCGTGTTTTGTAACGAATATATCTGCGATAACTACACAATCGTTTTCGCCACGGAGGACCTCCTTACCAATACTCTGGGCCGGGAAGTGATCTTGTTTATTGGGACCGCAGTTCTGTTCCTACGGTGGTACTTTCGCTGAACCGAATGAGCGCGAGTCAGCCAATCCGCGGGGTCTTCAGGGAAGGAGCCTCCTCGGAGAGTTGCTCAAACCTCGGATTCCGAGGGAGACCAGCTGTGACCCGTTCAGCCTGTGATAGTGAGCCCGTGGACTGCTGCCCAACGGATCCATACATGACACTGGCGAGCAGATTTTACACAGAGCGATCTCTCCGCAGCAACGTTGGGCAAGGTCGCGCGCTGTACGGATAGTGAGTTAAGGCCAACCCTCATAAGACTCCGCTCGGGAAAATGTTAAGATTCTAGCGGTCATCCTTCGATGAAGCCTGAATCCATATGACGGCGGTAACCTACTTAGCGGATTCGCGTTTCGCAGTGTTATCACTCTTCGGGGTTGTCCCCCTATAGCGTGCGGACTGATCGAATGCCCGGGGATAGCGCACAGTACAATGTAGAACTACGTAAACTATAAACATACTGCAAGACGACGCTTCAAAGTGTTTCAGTAAGATTGGACTGTGCTTATCTCCAGCCTTGGAAGTACACCTTTAGATGGAGGAAACGGTGTTCCGCTCTCTGGTTAG "
differences = 0

for x, y in zip(s1, s2):
    if x is not y:
        differences += 1

print(differences)


