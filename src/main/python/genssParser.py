import re
import os
from structure import Experiment, Benchmark, Result

state = 0;

minorNUM = 0
minorTotalTime = 0
minorTotalTimeinFULLGC = 0
minorReclaimed = 0
majorNUM = 0
majorTotalTime = 0
majorReclaimed = 0
GCNUM = 0
timings = 0;
time = 0

# Benchmark files must  be in the following location:
FILES_PATH = "../resources/Benchmarks/"


folders = os.listdir(FILES_PATH)
for folder in folders:

	if "TODO" in folder:
		continue

	files = os.listdir(FILES_PATH + folder)
	for file in files:

		if "GenSS" not in file:
			continue

		###################### Initialize variables ######################
		state = 0;

		minorNUM = 0
		minorTotalTime = 0
		minorTotalTimeinFULLGC = 0
		minorReclaimed = 0
		majorNUM = 0
		majorTotalTime = 0
		majorReclaimed = 0
		GCNUM = 0
		timings = 0;
		time = 0


		###################### Open each benchmark file ######################
		with open(FILES_PATH + folder + "/" + file) as f:

			print "************** " + folder + "/" + file + " **************"
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
							state = 3;
							time = int(re.findall('\d+', line )[1])
							continue
						else:
							Timings=0;
							continue
				if(state==3):
					if("Begin old" in line):
						minorTotalTimeinFULLGC = minorTotalTimeinFULLGC + time;
						state = 5
						continue
					if("After GC" in line):
						minorTotalTime = minorTotalTime + time
						state = 5;
				if(state==4):
					if(Timings==0):
						time = int(re.findall('\d+', line )[1])
						majorTotalTime = majorTotalTime + time
						state = 6;
						continue
					else:
						Timings=0;
						continue
				if(state==5):
					if("End   old generation" in line):
						majorNUM = majorNUM +1
						Timings = 1
						state = 4
						continue

					if("reclaimed" in line):
						reclaimed = int(re.findall('\d+', line )[2])
						#print "minor reclaimed ", reclaimed
						minorReclaimed = minorReclaimed + reclaimed
						state = 1
						continue
				if(state==6):
					if("reclaimed" in line):
						reclaimed = int(re.findall('\d+', line )[2])
						#print "major reclaimed ", reclaimed
						majorReclaimed = majorReclaimed + reclaimed;
						state = 1;
						continue

			###################### Print results ######################
			print "GCTIMES ",GCNUM
			print "TOTAL MINOR NOT IN FULL GC",GCNUM - majorNUM
			print "TOTAL MINOR TIME ",minorTotalTime
			print "TOTAL MONOR RECLAIMED ", minorReclaimed

			print "TOTAL MINOR TIME IN FULL GC", minorTotalTimeinFULLGC
			print "TOTAL FULL GC ",majorNUM
			print "TOTAL MAJOR TIME ",majorTotalTime
			print "TOTAL FULL GC TIME ", minorTotalTimeinFULLGC+majorTotalTime
			print "TOTAL GC TIME ", minorTotalTime+majorTotalTime + minorTotalTimeinFULLGC
			print "TOTAL MAJOR RECLAIMED ", majorReclaimed


			print "****************************" + '\n'






