import re

youngNUM = 0
youngTotalTime = 0
youngReclaimed = 0
mixedNUM = 0
mixedTotalTime = 0
mixedReclaimed = 0



FILES_PATH = "../resources/Benchmarks/"
folders = os.listdir(FILES_PATH)
for folder in folders:
	if "TODO" in folder:
		continue
	files = os.listdir(FILES_PATH + folder)
	for file in files
		if("G1" not in file):
			continue
		###################### Initialize variables ######################
		youngNUM = 0
		youngTotalTime = 0
		youngReclaimed = 0
		mixedNUM = 0
		mixedTotalTime = 0
		mixedReclaimed = 0
		###################### Open each benchmark file ######################
		with open(FILES_PATH + folder + "/" + file) as f:
			for line in f:
				if("young" in line):
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
						#list[6]
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
					before = 0
					after = 0
					mixedNUM = mixedNUM + 1
					list = line.split()
					time = float(list[7])
					''''if("initial" in line):
						#print "initial" + list[7]
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
					else:'''
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
					
print "YOUNG:", youngNUM , " TOTAL TIME:", youngTotalTime , "s TOTAL RECLAIMED:", youngReclaimed/1024, " MB"
print "FULL:", mixedNUM , " TOTAL TIME:", mixedTotalTime , "s TOTAL RECLAIMED:", mixedReclaimed/1024, " MB"

print "YOUNG MB/s ", (youngReclaimed/1024)/youngTotalTime
print "FULL MB/s ",  (mixedReclaimed/1024)/mixedTotalTime

print "YOUNG MB/pause" ,(youngReclaimed/1024)/youngNUM
print "FULL MB/pause" ,(mixedReclaimed/1024)/mixedNUM
