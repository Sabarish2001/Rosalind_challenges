#Program to translate mRNA -> Protein

#To translate into Protein we first need to import bring in the codon table(genetic code) 

codon_table = {"UUU": "F","UUC":"F","UUA":"L","UUG":"L",
               "CUU":"L","CUC":"L","CUA":"L","CUG":"L",
               "AUU":"I","AUC":"I","AUA":"I","AUG":"M",
               "GUU":"V","GUC":"V","GUA":"V","GUG":"V",
               "UCU":"S","UCC":"S","UCA":"S","UCG":"S",
               "CCU":"P","CCC":"P","CCA":"P","CCG":"P",
               "ACU":"T","ACC":"T","ACA":"T","ACG":"T",
               "GCU":"A","GCC":"A","GCA":"A","GCG":"A",
               "UAU":"Y","UAC":"Y","UAA":"Stop","UAG":"Stop",
               "CAU":"H","CAC":"H","CAA":"Q","CAG":"Q",
               "AAU":"N","AAC":"N","AAA":"K","AAG":"K",
               "GAU":"D","GAC":"D","GAA":"E","GAG":"E",
               "UGU":"C","UGC":"C","UGA":"Stop","UGG":"W",
               "CGU":"R","CGC":"R","CGA":"R","CGG":"R",
               "AGU":"S","AGC":"S","AGA":"R","AGG":"R",
               "GGU":"G","GGC":"G","GGA":"G","GGG":"G"}


def translate(sequence,codon=3):            #Defining the function translate that will translate mRNA -> Protein
    seq_len = len(sequence)                 #Initializing seq_len variable to length of the sequence
    protein = ""                            #Initializing variable protein to a empty string
    for i in range(0,(seq_len-3),codon):
        if sequence[i: i + codon] in codon_table:
            triplet = sequence[i:i + codon]
            protein += codon_table[triplet]            
        else:
            break
    return protein
