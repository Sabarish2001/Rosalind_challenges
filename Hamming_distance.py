def Hamming_distance(p, q):
    string_p = len(p)
    string_q = len(q)

    mismatches = 0

    if not string_p == string_q:
        return "Strings of unequal size"
    else:
        for i in range(string_p):
            if p[i] != q[i]:
                mismatches += 1
    return mismatches
