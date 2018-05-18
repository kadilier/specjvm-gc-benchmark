import re
import os, json, operator, csv
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
FILES_PATH = "../../resources/Benchmarks/"

# structure used for storing results, see structure.py
experiment = Experiment("Exp1", "MaxineVM", "GenSS")

folders = os.listdir(FILES_PATH)

for folder in folders:

	# create new benchmark, folder corresponds to benchmark name
	benchmark_name = folder
	benchmark = Benchmark(benchmark_name)

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
			print "TOTAL MINOR RECLAIMED ", minorReclaimed

			print "TOTAL MINOR TIME IN FULL GC", minorTotalTimeinFULLGC
			print "TOTAL FULL GC ",majorNUM
			print "TOTAL MAJOR TIME ",majorTotalTime

			print "TOTAL FULL GC TIME ", minorTotalTimeinFULLGC+majorTotalTime
			print "TOTAL GC TIME ", minorTotalTime+majorTotalTime + minorTotalTimeinFULLGC
			print "TOTAL MAJOR RECLAIMED ", majorReclaimed

			# Get heap size from file name and create new Result
			minorNumNotFull = GCNUM - majorNUM
			heapSizeStr = re.search('%s(.*)%s' % ("GenSS_", ".txt"), file).group(1)
			totalTimeFull =  minorTotalTime+majorTotalTime + minorTotalTimeinFULLGC
			totalTime = minorTotalTime+majorTotalTime + minorTotalTimeinFULLGC

			# add result to benchmark
			print "***** "
			benchmark.makeResult(heapSizeStr, benchmark_name,GCNUM, minorNumNotFull, minorTotalTime, minorReclaimed, minorTotalTimeinFULLGC, majorNUM, majorTotalTime, totalTimeFull, totalTime, majorReclaimed)

			print "****************************" + '\n'

	# add benchmark to experiment
	experiment.addBenchmark(benchmark)


################### Prepare .csv files for plots ###################

outputDir = "../../resources/PlotInput/"
outputMetrics = ["totalTime", "totalPauses", "totalReclaimed", "timePerPause"]

totalTimelst = []
totalPauselst = []
totalReclaimedlst = []
timePerPauselst = []

# sort benchmarks alphabetically
experiment.benchmarks.sort(key=operator.attrgetter('name'))
heapConfigs = [64, 128, 256, 512, 1024]

for i in range(0,5):

	heapConfig = heapConfigs[i]

	for benchmark in experiment.benchmarks:
		time = -1
		gcnum = -1
		reclaim = -1
		timeperpause = -1

		#print benchmark.getName(), ","

		benchmark.results.sort(key=operator.attrgetter('heapSize'))
		for result in benchmark.results:
			if(result.heapSize==heapConfigs[i]):
				time = result.totalTime
				gcnum = result.gcNum
				reclaim = (int(result.minorTotalReclaimed)+int(result.majorTotalReclaimed))/1024 #MB
				timeperpause = int(result.totalTime)/int(result.gcNum)
		if(time!=-1):
			print "totalPauselst FOR HEAP:", heapConfig, benchmark.getName(), "totalPauselst: ", gcnum
			totalTimelst.append(time)
			totalPauselst.append(gcnum)
			totalReclaimedlst.append(reclaim)
			timePerPauselst.append(timeperpause)
		else:
			print "totalPauselst FOR HEAP:", heapConfig, benchmark.getName(), "totalPauselst: 0"
			totalTimelst.append(0)
			totalPauselst.append(0)
			totalReclaimedlst.append(0)
			timePerPauselst.append(0)

	with open(outputDir + str(heapConfig) + "_" + "totalTime.csv","aw+") as file:
		wr = csv.writer(file)
		wr.writerow(totalTimelst)
		totalTimelst = []

	with open(outputDir + str(heapConfig) + "_" + "totalPause.csv","aw+") as file:
		wr = csv.writer(file)
		wr.writerow(totalPauselst)
		totalPauselst = []

	with open(outputDir + str(heapConfig) + "_" + "totalReclaimed.csv","aw+") as file:
		wr = csv.writer(file)
		wr.writerow(totalReclaimedlst)
		totalReclaimedlst = []

	with open(outputDir + str(heapConfig) + "_" + "timePerPause.csv","aw+") as file:
		wr = csv.writer(file)
		wr.writerow(timePerPauselst)
		timePerPauselst = []
