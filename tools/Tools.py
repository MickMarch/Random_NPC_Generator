from collections import Counter

# create list out of data entries
def lineBreakList(string):
    return string.split("\n")


# find duplicates in data set
def printDuplicates(array):
    counted = Counter(array)
    for k, v in counted.items():
        if v > 1:
            print(v, ": ", k)


# calculate total possibilities
def calculatePossibilities(*args):
    outcome = 1

    for arg in args:
        outcome *= len(arg)

    print(f"{outcome:,}")
