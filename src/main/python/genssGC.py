import re

state = 0;
#0 out GC
#1 in GC
#2 in FULL GC
minorNUM = 0
minorTotalTime = 0
majorNUM = 0
majorTotalTime = 0
GCNUM = 0
timings =0;

with open("a.txt") as f:
    for line in f:
        if("Start GC" in line):
		GCNUM = GCNUM+1;
		state = 1
	if("End GC" in line):
		state = 0;


	if(state==1):
		if("End nursery" in line):
			minorNUM = minorNUM +1 
			Timings = 1;
			state = 2;
			continue

	if(state==2):
		if("Timings" in line):
			if(Timings==0):
				state=3;
				time = int(re.findall('\d+', line )[1])
				minorTotalTime = minorTotalTime + time
			else:
				Timings=0;
				continue
	if(state==3):
		if("End   old generation" in line):
			majorNUM = majorNUM +1
			Timings = 1
			state = 4
			continue
	if(state==4):
			if(Timings==0):
                                state=1;
                                time = int(re.findall('\d+', line )[1])
                                majorTotalTime = majorTotalTime + time
                        else:
                                Timings=0;
                                continue

print "GCTIMES ",GCNUM
print "TOTAL MINOR ",minorNUM
print "TOTAL MINOR TIME ",minorTotalTime
print "TOTAL MAJOR ",majorNUM
print "TOTAL MAJOR TIME ",majorTotalTime
print "TOTAL GC TIME ", minorTotalTime+majorTotalTime
