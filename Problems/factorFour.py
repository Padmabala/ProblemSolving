def isPowerOfFour(num: int) -> bool:
    if (num <= 0):
        return False
    while (num>0):
        if(num == 2):
            return False
        if(((num>>1) & 1 == 1 or num & 1==1) and num != 1):
            return False
        num = num >> 2
    return True
print(isPowerOfFour(5))