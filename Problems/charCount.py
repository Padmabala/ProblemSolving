def countCharOccurences(ipString):
    op = {}
    for char in ipString:
        if (char in op):
            op[char] += 1
        else:
            op[char] = 1
    return op

ipString = input()
print(countCharOccurences(ipString))