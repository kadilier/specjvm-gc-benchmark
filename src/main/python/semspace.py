import re

state = 0
TotalTime = 0
GCNUM = 0
TotalReclaimed = 0

with open("b.txt") as f:
    for line in f:
	if("Start GC" in line):
		state = 1
		GCNUM = GCNUM+1
		continue
	if (state == 1):
		if("reclaimed" in line):
			reclaim = int(re.findall('\d+', line )[2])
			print(reclaim)
			TotalReclaimed = TotalReclaimed + reclaim
			state = 0;
			continue
	if("for all GC" in line):
		TotalTime = int(re.findall('\d+', line )[6])

print "GCTIMES ",GCNUM
print "TOTAL GC TIME ", TotalTime
print "TOTAL RECLAIMED ", TotalReclaimed
