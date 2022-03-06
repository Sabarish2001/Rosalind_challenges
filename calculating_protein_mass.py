monoisotopics_mass_table = {"A": 71.03711,
                            "C": 103.00919,
                            "D": 115.02694,
                            "E": 129.04259,
                            "F": 147.06841,
                            "G": 57.02146,
                            "H": 137.05891,
                            "I": 113.08406,
                            "K": 128.09496,
                            "L": 113.08406,
                            "M": 131.04049,
                            "N": 114.04293,
                            "P": 97.05276,
                            "Q": 128.05858,
                            "R": 156.10111,
                            "S": 87.03203,
                            "T": 101.04768,
                            "V": 99.06841,
                            "W": 186.07931,
                            "Y": 163.06333}

def cal_protein_mass(protein_seq):
    total_weight = 0
    for i in protein_seq:
        total_weight += monoisotopics_mass_table[i]
    return total_weight

with open("rosalind_prtm.txt","r") as f:
    read = f.read().rstrip()
    res = cal_protein_mass(read)
    print("Weight = %5.3f" %res)
