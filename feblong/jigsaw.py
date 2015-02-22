def collectpieces():
        index = 0
        for i in xrange(K):
                count = input()
                index += 1
                pieces[index] = []
                for i in xrange(count):
                        point = tuple(map(int, raw_input().split()))
                        pieces[index].append(point)

def getbest():
        maximum = 0
        best = None
        for each in pieces:
                l = len(pieces[each])
                if l > maximum:
                        maximum = l
                        best = each
        return best
def printtrivial():
        for i in xrange(H):
                for i in xrange(W):
                        print 0,
                print

def solvegreedy(best):
        points = pieces[best]
        pointdict = {point:True for point in points}
        for i in xrange(H):
                for j in xrange(W):
                     if (i+1, j+1) in pointdict:
                        print best,
                     else:
                        print 0,
                print    
def solve():
        collectpieces()
        best = getbest()
        if best is None:
                printtrivial()
        else:
                solvegreedy(best)
pieces = {}
H, W, K = map(int, raw_input().split())
solve()
