s = input("s= ")


def isPalindrome(string):
    for i in range(len(string)//2):
        if string[i] != string[-(i+1)]:
            return False
    return True


if isPalindrome(s):
    print("Returns= {}".format(len(s)))
else:
    reversedString = s[::-1]

    for char in reversedString[1:]:
        s += char
        if isPalindrome(s):
            break

    print("Returns= {}".format(len(s)))

