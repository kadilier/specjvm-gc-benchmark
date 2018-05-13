#maxvm -Xms_m -Xmx_m -XX:+TraceGCTime test.output.GCTest3 | grep Timings

import re


TotalTime = 0
GCNUM = 0


with open("c.txt") as f:
    for line in f:
	if("all GC" in line):
		state = 0
		TotalTime = int(re.findall('\d+', line )[6])
	else:
		GCNUM = GCNUM+1
		continue

print "GCTIMES ",GCNUM
print "TOTAL GC TIME ", TotalTime
