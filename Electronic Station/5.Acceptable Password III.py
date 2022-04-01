# In this mission you need to create a password verification function.

# Those are the verification conditions:

# the length should be bigger than 6;
# should contain at least one digit, but cannot consist of just digits.
# Input: A string.

# Output: A bool.

# Example:

# is_acceptable_password('short') == False
# is_acceptable_password('muchlonger') == False
# is_acceptable_password('ashort') == False
# is_acceptable_password('muchlonger5') == True
# is_acceptable_password('sh5') == False
# is_acceptable_password('1234567') == False
# Taken from mission Acceptable Password II

# Taken from mission Acceptable Password I

def is_acceptable_password(password: str) -> bool:
    # your code here
    if (password.isdigit()):
        return False
    elif len(password) > 6:
        a = False
        for i in password:
            if i.isdigit():
                a = True
        return a
    else:
        return False
