

def isPalindrome(s):
        return s == s[::-1]

    s = "racecar"
    num1 = isPalindrome(s)
    if num1:
        print("true")
    else:
        print("false")
