# Program to Compute the Number of Times a Pattern Appears in a Text Problem

def count(text,pattern):
    text_len = len(text)
    pattern_len = len(pattern)
    count = 0
    for i in range(text_len - pattern_len + 1):
        if text[i:i + pattern_len] == pattern:
            count = count + 1
    return count

res = count("","")
print(res)
