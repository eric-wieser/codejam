import sys

sys.stdin = open('large.in')
sys.stdout = open('large.out', 'w')

t = int(sys.stdin.readline())
for c in range(t):
	n = int(sys.stdin.readline())
	assert n>0
	base=None
	counts=None
	flag=True
	for i in range(n):
		#read s
		s = sys.stdin.readline().strip()
		assert len(s)>0
		for x in s:
			##print '"'+str(x)+'"'
			assert x in 'abcdefghijklmnopqrstuvwxyz'
		#compute base string and counts
		base_string=''
		counts_string=[]
		prev=''
		curr_count=0
		for j in range(len(s)):
			if s[j] != prev:
				base_string=base_string+prev
				counts_string.append(curr_count)
				prev=s[j]
				curr_count=1
			else:
				curr_count+=1
		base_string=base_string+prev
		counts_string.append(curr_count)
		#check if equal to base
		if base==None:
			base=base_string
			counts=[[] for j in range(len(base))]
		if base != base_string:
			flag=False #can't win
		else:
			for j in range(len(base)):
				counts[j].append(counts_string[j+1])
	#flag tells us if winnable
	if flag:
		sum=0
		for j in range(len(base)):
			counts[j].sort()
			##print str(base[j])+": "+str(counts[j])
			for k in range(len(counts[j])):
				sum += abs(counts[j][k]-counts[j][len(counts[j])/2])
		print "Case #"+str(c+1)+": "+str(sum)
	else:
		print "Case #"+str(c+1)+": Fegla Won"
