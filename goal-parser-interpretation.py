class Solution(object):
    def interpret(self, command):
        stack = []
        result = ""
    
        for char in command:
            if char == 'G':
                result += 'G'
            elif char == '(':
                stack.append(char)
            elif char == ')':
            
                temp = ""
                while stack and stack[-1] != '(':
                    temp = stack.pop() + temp  
            
                stack.pop()  
            
                if temp == "":    
                    result += "o"
                elif temp == "al": 
                    result += "al"
            else:  
                stack.append(char)
    
        return result