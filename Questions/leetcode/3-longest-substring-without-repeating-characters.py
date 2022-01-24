class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0 or len(s) == 1:
            return len(s)  
        else:
            my_dict = dict()
            max_len = 1
            start_idx = 0
            for idx in range(len(s)):
                cur_ch = s[idx]
                if cur_ch in my_dict:
                    # find the latest position where the same char is seen
                    start_idx = max(start_idx, my_dict[cur_ch]+1)
                my_dict[cur_ch] = idx
                max_len = max(max_len, idx-start_idx+1)
                
            return max_len