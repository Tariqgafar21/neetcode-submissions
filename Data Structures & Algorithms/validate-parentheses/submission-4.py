class Solution:
    def isValid(self, s: str) -> bool:
        #initizalize stack
        stack = []
        #hasmaop for matching pairs
        closeToOpen = {")": "(", "]": "[", "}": "{"}
        for c in s:
            if c in closeToOpen:
                #means its a closed bracket, so check if its value(open bracket) matches top of stack
                if stack and stack[-1] == closeToOpen[c]:
                    #pop
                    stack.pop()
                    #if doesnt match return false
                else:
                    return False
                    #if open character instead of closed, append it
            else:
                stack.append(c)
        #at the end return true if stack isnt empty else return false
        return True if not stack else False