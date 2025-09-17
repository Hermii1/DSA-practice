class Solution(object):
    def freqAlphabets(self, s):
        """
        :type s: str
        :rtype: str
        """
        i = 0
        n = len(s)
        result = []
        while i < n:
        
            if i + 2 < n and s[i + 2] == '#':
                # Extract the two-digit number before #
                num = int(s[i:i + 2])
                result.append(chr(ord('a') + num - 1))
                i += 3  
            else:
                # Single digit number
                num = int(s[i])
                result.append(chr(ord('a') + num - 1))
                i += 1
        return ''.join(result)