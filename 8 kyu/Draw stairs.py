# url: https://www.codewars.com/kata/5b4e779c578c6a898e0005c5

# Given a number n, draw stairs using the letter "I", n tall and n wide, with the tallest in the top left.

# For example n = 3 result in:

# "I\n I\n  I"
# or printed:

# I
#  I
#   I
# Another example, a 7-step stairs should be drawn like this:

# I
#  I
#   I
#    I
#     I
#      I
#       I

def draw_stairs(n):
    result = ''
    for num in range(0 , n-1):
        result += ' ' * num + 'I\n'
    result +=  ' ' * (n-1) + 'I'
    return result