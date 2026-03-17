def rotateString(s, goal):
    if len(s) != len(goal):
        return False
    return goal in (s + s)


# Examples
print(rotateString("abcde", "cdeab"))  # True
print(rotateString("abcde", "abced"))  # False