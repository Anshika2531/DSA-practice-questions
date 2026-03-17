def countingValleys(steps, path):
    level = 0
    valleys = 0

    for step in path:
        if step == 'U':
            level += 1
            if level == 0:
                valleys += 1
        else:  # step == 'D'
            level -= 1

    return valleys


# Input
steps = 8
path = "UDDDUDUU"

print(countingValleys(steps, path))