def compute(friends, f, r, n):
	for i in xrange(1, n+1):
		child = f[i]
		if i in friends:
			friends[i].append()
def solve():
	friends = {}
	mappings = {}
	costs = {}
	n = input()
	f = map(int, raw_input().split())
	r = map(int, raw_input().split())
	for i in xrange(n):
		costs[i+1] = r[i]
		mappings[i+1] = f[i]
	# print mappings
	# print costs	
	for each in f:
		friends = compute(each, friends, f, r, n)
	print friends
T = input()
for _ in xrange(T):
	solve()