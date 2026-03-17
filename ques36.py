def longestCommonPrefix(strs):
    if not strs:
        return ""
    
    prefix = strs[0]
    
    for s in strs[1:]:
        while not s.startswith(prefix):
            prefix = prefix[:-1]
            if prefix == "":
                return ""
    return prefix


# Examples
print(longestCommonPrefix(["flower","flow","flight"]))  # fl
print(longestCommonPrefix(["dog","racecar","car"]))     # ""