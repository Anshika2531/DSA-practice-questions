from collections import Counter

def first_non_repeating_char(s):
    count = Counter(s)

    for ch in s:
        if count[ch] == 1:
            return ch
    return None


# Example
print(first_non_repeating_char("swiss"))