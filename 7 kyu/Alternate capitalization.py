# url: https://www.codewars.com/kata/59cfc000aeb2844d16000075

# Given a string, capitalize the letters that occupy even indexes and odd indexes separately, and return as shown below. Index 0 will be considered even.

# For example, capitalize("abcdef") = ['AbCdEf', 'aBcDeF']. See test cases for more examples.

# The input will be a lowercase string with no spaces.

# Good luck!

def capitalize(s):
    result_1 = ''
    result_2 = ''
    for i in range(0, len(s)):
        if i % 2 == 0:
            result_1 += s[i].capitalize()
        else:
            result_1 += s[i]

    for i in range(0, len(s)):
        if i % 2 != 0:
            result_2 += s[i].capitalize()
        else:
            result_2 += s[i]
    
    return [result_1, result_2]