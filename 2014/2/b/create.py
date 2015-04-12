import random

with open('large.fake.in', 'w') as f:
	print >> f, 100
	for i in range(100):
		print >> f, 1000
		print >> f, ' '.join(map(str, random.sample(xrange(10000000), 1000)))