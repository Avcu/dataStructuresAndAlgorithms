## Dynamic programming solution to longest palindrome problem. DB has a 2-D array d[i, j] where i and j corresponds to the
## starting and ending indices of the palindrome.

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        len_s = len(s)
        if len_s == 1:
            return s
        else:
            d = [[0 for i in range(len_s)] for j in range(len_s)]
        
            last_seen = 0
            for diff in range(len_s):
                # early stopping
                if diff - 2 > last_seen:
                    break
                
                i = 0
                j = i + diff
                while j<len_s:
                    # diagonal elements are 1
                    if i == j:
                        d[i][j] = 1
                    # find the palindromic strings of size 2
                    elif i+1 == j:
                        if s[i] == s[j]:
                            d[i][j] = 1
                            last_seen = diff
                    else:
                        if (s[i] == s[j]) and (d[i+1][j-1] == 1):
                            d[i][j] = 1
                            last_seen = diff
                    i = i+1
                    j = j+1
                    
            # return the longest string
            for cur_raw in range(len_s):
                i = 0
                j = len_s-cur_raw-1
                while i<len_s and j<len_s:
                    if d[i][j] == 1:
                        return s[i:j+1]
                    i = i+1
                    j = j+1