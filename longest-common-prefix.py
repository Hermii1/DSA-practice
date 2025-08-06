class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        
        # Find the smallest string in the array
        smallest_str = min(strs, key=len)
        
        for i, char in enumerate(smallest_str):
            for s in strs:
                if s[i] != char:
                    return smallest_str[:i]
        
        return smallest_str