# Let's continue examining words. You are given two strings with words separated by commas. Try to find what is common between these strings. The words in the same string don't repeat.

# Your function should find all of the words that appear in both strings. The result must be represented as a string of words separated by commas in alphabetic order.

# Input: Two arguments as strings.

# Output: The common words as a string.

# Example:

# checkio('hello,world', 'hello,earth') == 'hello'
# checkio('one,two,three', 'four,five,six') == ''
# checkio('one,two,three',
#  'four,five,one,two,six,three') == 'one,three,two'
# 1
# 2
# 3
# 4
# How it is used: Here you can learn how to work with strings and sets. This knowledge can be useful for linguistic analysis.

# Precondition:
# Each string contains no more than 10 words.
# All words separated by commas.
# All words consist of lowercase latin letters.

def checkio(line1: str, line2: str) -> str:
    # your code here

    list1 = line1.split(",")
    list2 = line2.split(",")
    result = []
    for i in list1:
        if i in list2:
            result.append(i)

    return ','.join(sorted(result))
    # list1 = line1.split(",")
    # list2 = line2.split(",")
    # result = ''
    # for i in list1:
    #     if i in list2:
    #         if result == '':

    #             result = result+i
    #         else:
    #             result = result + ','+i
    # return result
    # added sort so that last one satisfies


if __name__ == '__main__':
    print("Example:")
    print(checkio('hello,world', 'hello,earth'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert checkio('hello,world', 'hello,earth') == 'hello'
    assert checkio('one,two,three', 'four,five,six') == ''
    assert checkio('one,two,three',
                   'four,five,one,two,six,three') == 'one,three,two'
    print("Coding complete? Click 'Check' to earn cool rewards!")
