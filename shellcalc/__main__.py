import sys
import operator
inp = "".join(sys.argv[1:])

operators = ['^', '%', '/', '*', '+', '-']
opera = {'/': operator.truediv, '+': operator.add, '-': operator.sub,
         '*': operator.mul, '^': operator.pow, '%': operator.mod}




'''
TODO: Brackets as []
TODO: next line input as ans
'''

def get_numbers(string, left, index):
    num1 = string[left+1:index]
    if left == 0:
        num1 = string[left:index]
    right = len(string)
    for i in range(index+1, len(string)):
        char = string[i]
        if char in operators:
            right = i
            break

    num2 = string[index+1:right]
    str1 = string[:left+1]
    if left == 0:
        str1 = ""
    str2 = string[right:]
    opr = string[index]
    result = opera[opr](float(num1), float(num2))
    right = len(str1+str(result))-2
    return str1+str(result)+str2,str(right)


def calculate(inp):
    for op in operators:
        index = 0
        left = 0
        while index < len(inp):
            if inp[index] in operators and inp[index] != op:
                left = index
            if op == inp[index]:
                ret = get_numbers(inp, left, index)
                inp = ret[0]
                right = int(ret[1])
                index = right
                continue
            index += 1
        left = 0
    print(inp)


def main():
    right_bracket=[]
    left_bracket=[]
    for i in range(0, len(inp)):
        if inp[i]=='[':
            left_bracket.append(i)
        elif inp[i]==']':
            right_bracket.append(i)
    print(left_bracket,right_bracket)
    right_bracket.sort()
    left_bracket.sort(reverse=True)

    print(left_bracket, right_bracket)


main()