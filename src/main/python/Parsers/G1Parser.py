import re, os

youngNUM = 0
youngTotalTime = 0
youngReclaimed = 0
mixedNUM = 0
mixedTotalTime = 0
mixedReclaimed = 0
fullNUM = 0
fullTotalTime = 0
fullReclaimed = 0


FILES_PATH = "../../resources/Benchmarks/"
folders = os.listdir(FILES_PATH)
for folder in folders:
	if "TODO" in folder:
		continue
	files = os.listdir(FILES_PATH + folder)
	for file in files:
		if("G1" not in file):
			continue
		###################### Initialize variables ######################
		youngNUM = 0
		youngTotalTime = 0
		youngReclaimed = 0
		mixedNUM = 0
		mixedTotalTime = 0
		mixedReclaimed = 0
		fullNUM = 0
		fullTotalTime = 0
		fullReclaimed = 0
		###################### Open each benchmark file ######################
		with open(FILES_PATH + folder + "/" + file) as f:
		#with open("../../resources/Benchmarks/Compiler/G1_64.txt") as f:
			for line in f:
				if("young" in line):
					if("concurrent-root-region-scan-end" in line):
						continue
					if("concurrent-mark-end" in line):
						continue
					before = 0
					after = 0
					time = 0
					youngNUM = youngNUM + 1
					list = line.split()
					if("initial" in line):
						time = float(list[8])
						list2 = list[7].split("-")
						if("M" in list2[0]):
							before = int(re.search(r'\d+', list2[0]).group())
							before = before * 1024
						else:
							before = int(re.search(r'\d+', list2[0]).group())

						list3 = list2[1].split("(")
						if("M" in list3[0]):
							after = int(re.search(r'\d+', list3[0]).group())
							after = after * 1024
						else:
							after = int(re.search(r'\d+', list3[0]).group())

					else:
						time = float(list[7])
						list2 = list[6].split("-")
						if("M" in list2[0]):
							before = int(re.search(r'\d+', list2[0]).group())
							before = before * 1024
						else:
							before = int(re.search(r'\d+', list2[0]).group())

						list3 = list2[1].split("(")
						if("M" in list3[0]):
							after = int(re.search(r'\d+', list3[0]).group())
							after = after * 1024
						else:
							after = int(re.search(r'\d+', list3[0]).group())
					youngTotalTime = youngTotalTime + time
					youngReclaimed = youngReclaimed + (before - after)
					continue

				if("mixed" in line):
					if("warning" in line): continue
					before = 0
					after = 0
					mixedNUM = mixedNUM + 1
					list = line.split()
					time = float(list[7])
					list2 = list[6].split("-")
					if("M" in list2[0]):
						before = int(re.search(r'\d+', list2[0]).group())
						before = before * 1024
					else:
						before = int(re.search(r'\d+', list2[0]).group())

					list3 = list2[1].split("(")
					if("M" in list3[0]):
						after = int(re.search(r'\d+', list3[0]).group())
						after = after * 1024
					else:
						after = int(re.search(r'\d+', list3[0]).group())
					mixedTotalTime = mixedTotalTime + time
					mixedReclaimed = mixedReclaimed + (before - after)
					continue
				if("Full" in line):
					if("System" in line): continue
					before = 0
					after  = 0
					fullNUM = fullNUM +1
					list = line.split()
                                        time = float(list[5])
					list2 = list[4].split("-")
                                        if("M" in list2[0]):
                                                before = int(re.search(r'\d+', list2[0]).group())
                                                before = before * 1024
                                        else:
                                                before = int(re.search(r'\d+', list2[0]).group())

                                        list3 = list2[1].split("(")
                                        if("M" in list3[0]):
                                                after = int(re.search(r'\d+', list3[0]).group())
                                                after = after * 1024
                                        else:
                                                after = int(re.search(r'\d+', list3[0]).group())
                                        fullTotalTime = fullTotalTime + time
                                        fullReclaimed = fullReclaimed + (before - after)
                                        continue

		print "Benchmark:", folder, " file:", file
		print "YOUNG:", youngNUM , " TOTAL TIME:", youngTotalTime , "s TOTAL RECLAIMED:", youngReclaimed/1024, " MB"
		print "MIXED:", mixedNUM , " TOTAL TIME:", mixedTotalTime , "s TOTAL RECLAIMED:", mixedReclaimed/1024, " MB"
		print "FULL", fullNUM, "TOTAL TIME:", fullTotalTime , "s TOTAL RECLAIMED:",fullReclaimed/1024," MB"
		print "----------------------------------------------------------------------"
