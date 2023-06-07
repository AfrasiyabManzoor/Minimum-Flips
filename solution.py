class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:

        flips = 0
        while a or b or c:
            bit_a = a%2
            bit_b = b%2
            bit_c = c%2
            if bit_a | bit_b != bit_c:
                if bit_c == 1:
                    flips += 1
                else:
                    if bit_a == 1:
                        flips += 1
                    if bit_b == 1:
                        flips += 1
            a //= 2
            b //= 2
            c //= 2
        
        return flips 
