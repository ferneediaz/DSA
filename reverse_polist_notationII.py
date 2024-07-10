class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {
            '+': (lambda x, y: x+y),
            '*': (lambda x, y: x*y),
            '/': (lambda x, y: int(x / y)),
            '-': (lambda x, y: x-y),
        }
        i = 0
        while len(tokens)>1:
            if tokens[i] not in operators.keys():
                i+=1
            else:
                right = int(tokens.pop(i-1))
                left = int(tokens.pop(i-2))
                tokens.insert(i-2, operators[tokens[i-2]](left, right))
                tokens.pop(i-1)
                i-=1
        return int(tokens.pop())   