# s = "()"
# s = "()[]{}"
s = "(]"

roundcnt = 0
curlycnt = 0
squarecnt = 0

for c in s:
    if c == '(':
        roundcnt += 1
    elif c == ')':
        roundcnt -= 1
    elif c == '{':
        curlycnt += 1
    elif c == '[':
        squarecnt += 1
    elif c == ']':
        squarecnt -= 1
    else:
        curlycnt -= 1

if roundcnt or curlycnt or squarecnt:
    print(False)
else:
    print(True)
