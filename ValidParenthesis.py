s = "()"
#s = "()[]{}"
#s = "(]"
#s = "]"
#s = "([]){"
#s = "([]"


stackP = []

for c in s:
    flag = False
    if c == '(' or c == '[' or c == '{':
        stackP.append(c)
        flag = False

    elif c == ')':
        if not stackP:
            flag = False
            break
        elif '(' == stackP.pop():
            flag = True
        else:
            flag = False
            break
    elif c == ']':
        if not stackP:
            flag = False
            break
        elif '[' == stackP.pop():
            flag = True
        else:
            flag = False
            break
    elif c == '}':
        if not stackP:
            flag = False
            break
        elif '{' == stackP.pop():
            flag = True
        else:
            flag = False
            break
if stackP:
    flag = False
print(flag)