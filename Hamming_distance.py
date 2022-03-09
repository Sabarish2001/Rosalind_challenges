def Hamming_distance(p, q):   #Function takes 2 parameters p and q which are strings
    string_p = len(p)         #string_p contains the length of string p
    string_q = len(q)         #string_q contains the length of string q

    mismatches = 0            #initializing the variable mismatch to 0. Incremented everytime when a mismatch is found 

    if not string_p == string_q:            #Checking wether strings p and q of equal length
        return "Strings of unequal size"    #If the condition fails, returning the message of unequal size
    else:
        for i in range(string_p):           # taking any of the either string and iterating to the whole length
            if p[i] != q[i]:                # checking 
                mismatches += 1
    return mismatches
