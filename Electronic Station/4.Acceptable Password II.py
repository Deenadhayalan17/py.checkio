# In this mission you need to create a password verification function.

# Those are the verification conditions:

# the length should be bigger than 6;
# should contain at least one digit.
# Input: A string.

# Output: A bool.

# Example:

# is_acceptable_password('short') == False
# is_acceptable_password('muchlonger') == False
# is_acceptable_password('ashort') == False
# is_acceptable_password('muchlonger5') == True
# is_acceptable_password('sh5') == False
# 1
# 2
# 3
# 4
# 5
# How it’s used: For password verification form. Also it's good to learn how the task can be evaluated.

# Taken from mission Acceptable Password I

def is_acceptable_password(password: str) -> bool:
    # your code here
    if len(password) > 6:
        a = False
        for i in password:
            if i.isdigit():
                a = True
        return a
    else:
        return False


if __name__ == '__main__':
    print("Example:")
    print(is_acceptable_password('short'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert is_acceptable_password('short') == False
    assert is_acceptable_password('muchlonger') == False
    assert is_acceptable_password('ashort') == False
    print("Coding complete? Click 'Check' to earn cool rewards!")


if __name__ == "__main__":
    # These "asserts" are used for self-checking and not for an auto-testing
    assert is_acceptable_password("short") == False
    assert is_acceptable_password("muchlonger") == False
    assert is_acceptable_password("ashort") == False
    assert is_acceptable_password("muchlonger5") == True
    assert is_acceptable_password("sh5") == False
    print("Coding complete? Click 'Check' to earn cool rewards!")
