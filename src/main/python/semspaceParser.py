import re
import os
from structure import Experiment, Benchmark, Result

state = 0
TotalTime = 0
GCNUM = 0
TotalReclaimed = 0

# Benchmark files must  be in the following location:
FILES_PATH = "../resources/Benchmarks/"


folders = os.listdir(FILES_PATH)
for folder in folders:

	if "TODO" in folder:
		continue

	files = os.listdir(FILES_PATH + folder)
	for file in files:

		if "SemiSpace" not in file:
			continue

		###################### Initialize variables ######################
		state = 0
		TotalTime = 0
		GCNUM = 0
		TotalReclaimed = 0

		###################### Open each benchmark file ######################
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

		###################### Print results ######################
		print "GCTIMES ",GCNUM
		print "TOTAL GC TIME ", TotalTime
		print "TOTAL RECLAIMED ", TotalReclaimed


