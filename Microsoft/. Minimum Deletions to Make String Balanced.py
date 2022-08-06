# You are given a string s consisting only of characters 'a' and 'b'​​​​.

# You can delete any number of characters in s to make s balanced. s is balanced if there is no pair of indices (i,j) such that i < j and s[i] = 'b' and s[j]= 'a'.

# Return the minimum number of deletions needed to make s balanced.

class Solution:
    def minimumDeletions(self, s: str) -> int:
        countA = 0
        countB = 0
        balance = 0
        for char in s:
            if char == 'a':
                countA += 1
            else:
                countB += 1
