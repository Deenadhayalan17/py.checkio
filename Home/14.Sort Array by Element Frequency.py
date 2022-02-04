# Sort the given iterable so that its elements end up in the decreasing frequency order, that is, the number of times they appear in elements. If two elements have the same frequency, they should end up in the same order as the first appearance in the iterable.

# Input: Iterable

# Output: Iterable

# Example:

# frequency_sort([4, 6, 2, 2, 6, 4, 4, 4]) == [4, 4, 4, 4, 6, 6, 2, 2]
# frequency_sort(['bob', 'bob', 'carl', 'alex', 'bob']) == ['bob', 'bob', 'bob', 'carl', 'alex']
# 1
# 2
# Precondition: elements can be ints or strings


def frequency_sort(items):
    # your code here

    dict1 = {}
    for i in items:
        if not (i in dict1.keys()):
            dict1[i] = items.count(i)

    sort_dict = dict(
        sorted(dict1.items(), key=lambda item: item[1], reverse=True))

    list = []
    for i in sort_dict.keys():
        for y in range(0, sort_dict[i]):
            list.append(i)

    return list


if __name__ == '__main__':
    print("Example:")
    print(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4])) == [
        4, 4, 4, 4, 6, 6, 2, 2]
    assert list(frequency_sort(['bob', 'bob', 'carl', 'alex', 'bob'])) == [
        'bob', 'bob', 'bob', 'carl', 'alex']
    assert list(frequency_sort([17, 99, 42])) == [17, 99, 42]
    assert list(frequency_sort([])) == []
    assert list(frequency_sort([1])) == [1]
    print("Coding complete? Click 'Check' to earn cool rewards!")
