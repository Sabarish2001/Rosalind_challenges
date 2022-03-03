def pattern_occurences(text,pattern):
    text_len = len(text)
    pattern_len = len(pattern)
    occurences = []
    for i in range(text_len):
        if text[i : i + pattern_len] == pattern:
            occurences.append(i)
    return occurences

genome = input("")
pattern = input("")

res = pattern_occurences(genome,pattern)
for i in res:
    print(i,end=" ")                # answer will be the starting positions of a given pattern in the text
