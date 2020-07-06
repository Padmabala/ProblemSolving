def numJewelsInStones( J: str, S: str) -> int:
    count = 0
    for i in range(len(S)):
        if S[i] in J:
            count = count + 1
    return count
print(numJewelsInStones('z','zzzz'))