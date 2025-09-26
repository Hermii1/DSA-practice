class Solution:
    def isAlienSorted(self, words, order):
        alien_order = {char: index for index, char in enumerate(order)}
        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i + 1]
            
            found_difference = False
            for j in range(min(len(word1), len(word2))):
                char1 = word1[j]
                char2 = word2[j]
                
                if char1 != char2:
                    if alien_order[char1] > alien_order[char2]:
                        return False  
                    found_difference = True
                    break  
            
           
            if not found_difference and len(word1) > len(word2):
                return False
        
        return True
        