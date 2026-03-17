def isAnagram(s, t):
    if sorted(s) == sorted(t):
        return True
    else:
        return False

# Examples
print(isAnagram("anagram", "nagaram"))  # True
print(isAnagram("rat", "car"))          # False
print(isAnagram("listen", "silent"))    # True