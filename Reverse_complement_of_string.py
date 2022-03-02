def reverse_complement(sequence):
    reverse = ""
    complement_res = complement(sequence)
    reverse += complement_res
    return reverse[::-1]
    
def complement(sequence):
    bases = {"A":"T","T":"A","C":"G","G":"C"}
    complementary_seq = ""
    for i in sequence:
        complementary_seq += bases[i]
    return complementary_seq

with open("rosalind_ba1c.txt","r") as file:
    handle = file.read()
    remove_spaces = handle.rstrip()
    res = reverse_complement(remove_spaces)
    print(res)
