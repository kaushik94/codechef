def get_nieghbours(value, l, r):
        nieghbours = []
        if value != -1:
                if l-1 >= L:
                        nvalue = (l-1)^(r)
                        #if nvalue == value+1:
                        nieghbours.append((nvalue, l-1, r))
                if r-1 >= L:
                        nvalue = (r-1)^l
                        #if nvalue == value+1:
                        nieghbours.append((nvalue, l, r-1))
        if l+1 <= R:
                nvalue = (r)^(l+1)
                #if nvalue == value+1:
                nieghbours.append((nvalue, l+1, r))
        if r+1 <= R:
                nvalue = (r+1)^l
                #if nvalue == value+1:
                nieghbours.append((nvalue, l, r+1)) 
        return nieghbours


def paint(L, R):
        matrix = []
        for each in xrange(L,R+1):
                temp = []
                for other in xrange(L, R+1):
                        temp.append(each^other)
                matrix.append(temp)
        for each in matrix:
                print each
def dfs((value, l, r)):
        n = get_nieghbours(value, l, r)
        maximum = 0
        if len(n):
                for nie in n:
                        out = dfs(nie)
                        if out > maximum:
                                maximum = out
                return maximum
        else:return value

def solve(L, R):
        diff = R-L+1
        binary = list(bin(diff)[2:])
        print L, R
        paint(L,R)
        if L == R:
                return 0
        if (R-2) == (L-1) and (R-2)%10 == 0 and (L-1)%10 == 0:
                return 0
        if all(x=='1' for x in binary):
                return diff
        length = len(binary)
        output = 0
        for i in xrange(length-1):
                output += pow(2, i)
        return output
T = input()
for i in xrange(T):
        L, R = map(int, raw_input().split())
        # i, L, R
        a = solve(L, R)
        print a, 0
