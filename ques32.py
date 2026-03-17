from collections import Counter

def firstUniqChar(s):
    count = Counter(s)   # har character ki frequency

    for i in range(len(s)):
        if count[s[i]] == 1:
            return i
    return -1


# Examples
print(firstUniqChar("leetcode"))      # 0
print(firstUniqChar("loveleetcode"))  # 2
print(firstUniqChar("aabb"))          # -1