def create_headins(heads):
        headins = {head:0 for head in heads}
        power = 1
        for level, index in heads:
                #print level, index
                if power == 0:
                        break
                if level > 1:
                        power = pow_mod(m, level-1, MOD)
                        headins[(level, index)] = power
                else:
                        headins[(level, index)] = 1
        #headins[(0, 0)] = 1
        #print headins
        return headins

def pow_mod(x, y, z):
    "Calculate (x ** y) % z efficiently."
    number = 1
    while y:
        if y & 1:
            number = number * x % z
        y >>= 1
        x = x * x % z
    return number
     
def solvegraph():
        g = headtail.keys()
        g.append((n+1, 0))
        heads = sorted(g)
        tails = sorted(tailhead.keys())
        headins = {}
        headins = create_headins(heads)
        rheads = heads[::-1]
        while tails:
                level, index = tails.pop(0)
                headlist = tailhead[(level, index)]
                newways = 0
                for headlevel, headindex in headlist:
                        newways = (newways%MOD + headins[(headlevel, headindex)]%MOD)%MOD
                for eachlevel, eachindex in rheads:
                        if eachlevel > level:
                                headins[(eachlevel, eachindex)] = (headins[(eachlevel, eachindex)]%MOD + newways*pow_mod(m, eachlevel-level-1, MOD))%MOD
                        if eachlevel == level:
                                if eachindex == index:
                                        headins[(eachlevel, eachindex)] = (headins[(eachlevel, eachindex)]%MOD + newways%MOD)%MOD
                        if eachlevel < level:
                                break
        return headins[(n+1, 0)]%MOD
 
 
def solve():
        for i in xrange(k):
                inp.append(map(int, raw_input().split()))
                curr = inp[-1]
                if (curr[0], curr[1]) in headtail:
                        headtail[(curr[0], curr[1])].append((curr[2], curr[3]))
                else:
                        headtail[(curr[0], curr[1])] = [(curr[2], curr[3])]
                if (curr[2], curr[3]) in tailhead:
                        tailhead[(curr[2], curr[3])].append((curr[0], curr[1]))
                else:
                        tailhead[(curr[2], curr[3])]= [(curr[0], curr[1])]
        return solvegraph()
 
inp = []
headtail = {}
tailhead = {}
MOD = 1000000007
n, m, k = map(int, raw_input().split())
print solve()
