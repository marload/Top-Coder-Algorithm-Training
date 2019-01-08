def checkDirectFriend(friendsList, friendsTable):
    for q in friendsList:
        for k in friendsList:
            if q == k:
                continue
            else:
                if friendsTable[q][k]:
                    continue
                else:
                    friendsScore[q] += 1
    return friendsScore


def countMyFriend():
    friendsListOfI = []
    for j, isFriend in enumerate(friendsSeries):
        if isFriend:
            friendsScore[i] += 1
            friendsListOfI.append(j)
    return friendsListOfI


def main():
    friends = ["NYY", "YNY", "YYN"]

    friendsScore = [0 for _ in range(len(friends))]

    friendsTable = [[True if x=='Y' else False for x in list(string)] for string in friends]

    for i, friendsSeries in enumerate(friendsTable):
        friendsListOfI = countMyFriend()
        friendsScore = checkDirectFriend(friendsListOfI, friendsTable)

    print(max(friendsScore))


main()


'''
Explain
1. Graph로 풀음
2. i번째 사람의 직접 친구 수를 score에 더함
3. i번째 사람의 직접 친구가 서로서로 친구라면 계속하고 서로서로 친구가 아니라면 그 직접친구의 score에 1을 더함
'''
