class Stack:
    def _init_(self):
        self.stuff = []

    def isPalindrome(s):
        return s == s[::-1]

    s = "racecar"
    num1 = isPalindrome(s)
    if num1:
        print("true")
    else:
        print("false")

    s = "noon"
    num1 = isPalindrome(s)
    if num1:
        print("true")
    else:
        print("false")

    s = "python"
    num1 = isPalindrome(s)
    if num1:
        print("true")
    else:
        print("false")
    
    s = "madam"
    num1 = isPalindrome(s)
    if num1:
        print("true")
    else:
        print("false")