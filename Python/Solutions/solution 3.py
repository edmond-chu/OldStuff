# Change this file's name to "solution.py" before submitting.

# Implement a basic calculator to evaluate a simple expression string.
# The expression string contains only non-negative integers, +, -, *, / operators and empty spaces.
# The integer division should truncate toward zero.
# Make sure to follow order of operations!

# Note:
# You may not assume that the given expression is always valid. (Return 0 if not valid)
# Do not use the eval built-in library function.

def split(word):
    return [string for string in word]
def isnum(s) :
    return  s == '0' or s == '1' or s == '2' or s == '3' or s == '4' or s == '5' or s == '6' or s == '7' or s == '8' or s == '9'
def isop(s):
    return s == '+' or s == '-' or s == '/' or s == '*'
def calculate(s: str) -> int:
    flag = 0
    if s == "" :
        return 0
    x = split(s)
    i = 0
    fin = []
    ops = []
    #The above splits the string, checks the empty case and creates two arrays
    #one that holds the values, and one that holds the operators

    #below, this nested while loop puts all of the numbers in the array fin, checking for
    #concurrent values so it doesnt split the number 12 into [1,2]
    while i < len(x):
        if x[i].isdigit():
            j = i+1
            if i != len(x)-1 :

                while x[j].isdigit():
                    x[i] = x[i]+x[j]
                    j+=1
                fin.append(x[i])
                i+=1
            else:
                fin.append(x[i])
        i+=1
    q = 0

    #puts the operators into the array ops by using isop helper to check
    #if they are operators. Also checks for illegal characters
    while q < len(x):
        if isop(x[q]):
            if isop(x[q+1]):
                flag = 1
            else:
                ops.append(x[q])
        elif isnum(x[q]) == False:
            flag = 1
        q+=1

    #operations on the multiplication and the division. Basically uses the
    #corresponding indexes of the array and evals the numbers surrounding the
    #operators and puts the final value in the first and pops all the used values
    #out of the list. Divide also checks for division by 0
    while ops.count("*")!=0 or ops.count("/") :
        mul = 0
        mulcount = 0
        newop1 = []
        while mul < len(ops):
            if ops[mul] == '*':

                tmp = int(fin[mul])*int(fin[mul+1])
                fin[mul] = str(tmp)
                ops.pop(mul)
                fin.pop(mul+1)
            elif ops[mul] == '/':
                if fin[mul+1] == "0":
                    flag = 1
                    fin[mul+1] = 4
                else:
                    tmp = int(int(fin[mul])/int(fin[mul+1]))
                    fin[mul] = str(tmp)
                    ops.pop(mul)
                    fin.pop(mul+1)
            else:
                newop1.append(ops[mul])
            mul+=1
    #same concept as above but with addition and multiplication
    while ops.count("+") != 0 or ops.count("-") :
        mul = 0
        mulcount = 0
        newop1 = []
        while mul < len(ops):
            if ops[mul] == '+':

                tmp = int(fin[mul])+int(fin[mul+1])
                fin[mul] = str(tmp)
                ops.pop(mul)
                fin.pop(mul+1)
            elif ops[mul] == '-':

                tmp = int(fin[mul])-int(fin[mul+1])
                fin[mul] = str(tmp)
                ops.pop(mul)
                fin.pop(mul+1)
            else:
                newop1.append(ops[mul])
            mul+=1
    #if the flag went off at any time it returns 0, otherwise it returns an int
    if flag == 0:
        return (int(fin[0]))
    else:
        return 0

    #overall, this program is O(n^2), using multiple nested while loops that
    #traverse to n. Space complexity, it uses two arrays that add
    #up to the size whatever the length of the string is
