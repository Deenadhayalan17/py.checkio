# In a given string you should reverse every word, but the words should stay in their places.

# Input: A string.

# Output: A string.

# Example:

# backward_string_by_word('') == ''
# backward_string_by_word('world') == 'dlrow'
# backward_string_by_word('hello world') == 'olleh dlrow'
# backward_string_by_word('hello   world') == 'olleh   dlrow'
# 1
# 2
# 3
# 4
# Precondition: The line consists only from alphabetical symbols and spaces.

# def backward_string_by_word(text: str) -> str:
#     # your code here
#     final=''
#     list = text.split()
#     for i in list:
#       if final == '':
        
#           final=  final + (i[::-1])
#       else:
#         final=  final + ' '+ (i[::-1])
        
#     return final
def backward_string_by_word(text: str) -> str:
    # your code here
    
     return " ".join([i[::-1] for i in text.split(" ")])
if __name__ == '__main__':
    print("Example:")
    print(backward_string_by_word(''))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert backward_string_by_word('') == ''
    assert backward_string_by_word('world') == 'dlrow'
    assert backward_string_by_word('hello world') == 'olleh dlrow'
    assert backward_string_by_word('hello   world') == 'olleh   dlrow'
    assert backward_string_by_word('welcome to a game') == 'emoclew ot a emag'
    print("Coding complete? Click 'Check' to earn cool rewards!")
