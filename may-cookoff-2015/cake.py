import operator
def cake():
	s = list(raw_input())
	baloons = {}
	for each in s:
		if each in baloons:
			baloons[each] += 1
		else:
			baloons[each] = 1
	string = ''
	while baloons:
		sorted_b = sorted(baloons.items(), key=operator.itemgetter(1), reverse=True)
		if len(sorted_b):
			highest, _ = sorted_b.pop(0)
			baloons[highest] -= 1
			if baloons[highest] == 0:
				del baloons[highest]
			string += highest
		if len(sorted_b):
			second, _ = sorted_b.pop(0)
			baloons[second] -= 1
			if baloons[second] == 0:
				del baloons[second]
			string += second
	check = list(string)
	prev = None
	for c in check:
		if prev == c:
			print -1
			return
		prev = c
	print string
T = input()
for _ in xrange(T):
	cake()