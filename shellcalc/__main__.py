import sys
import operator
inp = "".join(sys.argv[1:])

operators = ['^', '%', '/', '*', '+', '-']
opera = {'/':operator.truediv,'+':operator.add,'-':operator.sub,'*':operator.mul, '^':operator.pow,'%':operator.mod}

def get_numbers(string, left, index):
    num1 = string[left+1:index]
    if left == 0: num1 = string[left:index]
    right = len(string)
    for i in range(index+1,len(string)):
        char = string[i]
        if char in operators:
            right = i
            break
    
    num2 = string[index+1:right]
    str1 = string[:left+1]
    if left ==0 : str1=""
    str2 = string[right:]
    opr = string[index]
    result = opera[opr](float(num1),float(num2))
    right = len(str1+str(result))-2
    return str1+str(result)+str2+" "+str(right)

def main(inp):
    inpcopy = inp
    for op in operators:
        ind = 0
        while ind<len(inpcopy):
            if inpcopy[ind] in operators and inpcopy[ind]!=op:
                left = ind
            if op == inpcopy[ind]:
                index = ind
                ret = get_numbers(inpcopy, left,index).split(" ")
                inpcopy = ret[0]
                right =int(ret[1])
                ind = right
                continue
            ind+=1
        left =0
    print(inpcopy)

main(inp)