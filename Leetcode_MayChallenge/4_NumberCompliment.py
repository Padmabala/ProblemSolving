import math
class Solution:
    def findComplement(self, num: int) -> int:
        i=1
        j=1
        while(num>=i):
            i=2**j
            j+=1
        i-=1
        n=num^i
        return n
        # number_of_bits = (int)(math.floor(math.log(num) /
        #                                   math.log(2))) + 1;
        #
        # # XOR the given integer with poe(2,
        # # number_of_bits-1 and print the result
        # return ((1 << number_of_bits) - 1) ^ num;
s=Solution()
print(s.findComplement(5))