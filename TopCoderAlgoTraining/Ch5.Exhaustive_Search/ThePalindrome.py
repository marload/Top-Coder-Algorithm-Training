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

'''
Explain
1. 가장 먼저 문자열 s가 회문인지 검사하고 회문이 맞다면 바로 문자열의 길이를 반환
2. 아닐경우 문자열을 뒤집고 뒤집은 문자열의 첫 글자부터 s에 붙여가며 회문인지를 검사함
'''
