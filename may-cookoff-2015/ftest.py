
def test():
	n = input()
	bmap = {}
	ds = map(int, raw_input().split())
	friendships = 0
	for each in ds:
		if each not in bmap:
			friendships += 1
			bmap[each] = True
	print friendships
T = input()
for _ in xrange(T):
	test()