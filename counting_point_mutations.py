#Program to count point mutations(by hamming distance)

def hamming_distance(s,t):
    s_length = len(s)
    t_length = len(t)
    mutations = 0
    if s_length == t_length:
        for i in range(s_length):
            if s[i] !=  t[i]:
                mutations +=1
    return mutations
