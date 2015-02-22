def optimised(S, lst):
        l = len(S)
        for each in lst:
                co[each] = [0 for i in xrange(l+2)]
                for other in lst:
                        if each != other:
                                string = each +" "+ other
                                hashmap[string] = [0 for i in xrange(l+2)]
                                
        counts = {i:0 for i in lst}
        count = 1
        for each in S:
                counts[each] += 1
                co[each][count] = 1


def buildmap(S, lst):
	l = len(S)
	co = {}
	ttable = {}
	for each in lst:
		for other in lst:
			if each != other:
				string = each+" "+other
				Mhashmap[string] = []
				if each not in co:
					co[each] = []
				for i in xrange(l+2):
					if each not in ttable:
						co[each].append(0)
					Mhashmap[string].append(0)
				ttable[each] = True
				counter[string] = 0
	counts = {i:0 for i in lst}
	count = 1
	for each in S:
		counts[each] += 1
		co[each][count] = 1
		for other in lst:
			if other != each:
				string = other+" "+each
				counter[string] += counts[other]
				Mhashmap[string][count] = counter[string]
		count += 1
 
	checkmap = {}
	for each in Mhashmap:
		update = Mhashmap[each][0]
		update2 = 0
		done = True
		element = each.split()[0]
		if element not in checkmap:
			done = False
			checkmap[element] = True
		for i in xrange(1, l+1):
			if Mhashmap[each][i] == 0:
				Mhashmap[each][i] = update
			else:
				update = Mhashmap[each][i]
			if not done:
				update2 += co[element][i]
				co[element][i] = update2
		
 
	return co
 
def solve(S, Q):
	co = buildmap(S, lst)
	for i in xrange(Q):
		q = raw_input().split()
		a, b, L, R = q[0], q[1], int(q[2]), int(q[3])
		string = a+" "+b
		doubles = co[a][L-1]*(co[b][R]-co[b][L-1])
		print Mhashmap[string][R] - Mhashmap[string][L-1] - doubles
 
S = list(raw_input())
Q = input()
Mhashmap = {}
hashmap = {}
counts = {}
counter = {}
co = {}
lst = ['c', 'h', 'e', 'f']
#buildmap(S, lst)
solve(S, Q)
