# url: https://www.codewars.com/kata/51fd6bc82bc150b28e0000ce
# Write a small function that returns the values of an array that are not odd.

# All values in the array will be integers. Return the good values in the order they are given.


def no_odds(values):
    result = []
    for i in values:
        if i % 2 == 0:
            result.append(i)
    return result