#Write a Python program to find validity of a string of parentheses, '(', ')', '{', '}', '[' and '].
# These brackets must be close in the correct order,for example "()" and "()[]{}" are valid
# but "[)", "({[)]" and "{{{" are invalid
class solution:
  def valid(self):
        str=input("enter the bracket:")
        stack = []
        char = {"(": ")", "{": "}", "[": "]"}
        for p in str:
            if p in char:
                stack.append(p)
            elif (len(stack) == 0 or char[stack.pop()] != p): #char[stack.pop()] will give the last char inserted
                return False
        return len(stack) == 0

print(solution().valid())