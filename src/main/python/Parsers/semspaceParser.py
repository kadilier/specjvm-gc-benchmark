import re
import os, operator, csv
from structure import Experiment, Benchmark, Result

state = 0
TotalTime = 0
GCNUM = 0
TotalReclaimed = 0

# Benchmark files must  be in the following location:
FILES_PATH = "../../resources/Benchmarks/"

# structure used for storing results, see structure.py
experiment = Experiment("Exp1", "MaxineVM", "SemiS")

folders = os.listdir(FILES_PATH)
for folder in folders:

	# create new benchmark, folder corresponds to benchmark name
	benchmark_name = folder
	benchmark = Benchmark(benchmark_name)

	files = os.listdir(FILES_PATH + folder)
	for file in files:

		if "SemiS" not in file:
			continue

		###################### Initialize variables ######################
		state = 0
		TotalTime = 0
		GCNUM = 0
		TotalReclaimed = 0

		###################### Open each benchmark file ######################
		with open(FILES_PATH + folder + "/" + file) as f:

			print "************** " + folder + "/" + file + " **************"
			for line in f:
				if("Start GC" in line):
					state = 1
					GCNUM = GCNUM+1
					continue
				if (state == 1):
					if("reclaimed" in line):
						reclaim = int(re.findall('\d+', line )[2])
						#print(reclaim)
						TotalReclaimed = TotalReclaimed + reclaim
						state = 0;
						continue
				if("for all GC" in line):
					TotalTime = int(re.findall('\d+', line )[6])

		###################### Print results ######################
		print "GCTIMES ",GCNUM
		print "TOTAL GC TIME ", TotalTime
		print "TOTAL RECLAIMED ", TotalReclaimed

		# Get heap size from file name and create new Result
		heapSizeStr = re.search('%s(.*)%s' % ("SemiS_", ".txt"), file).group(1)

		# add result to benchmark
		benchmark.makeResult(heapSizeStr, benchmark_name, GCNUM, -1, -1, -1, -1, -1, -1, -1, TotalTime, TotalReclaimed)

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

		benchmark.results.sort(key=operator.attrgetter('heapSize'))
		for result in benchmark.results:
			if(result.heapSize==heapConfigs[i]):
				time = result.totalTime
				gcnum = result.gcNum
				reclaim = (int(result.majorTotalReclaimed))/1024 #MB
				timeperpause = int(result.totalTime)/int(result.gcNum)
		if(time!=-1):
			print "totalPauselst FOR HEAP:", heapConfig, benchmark.getName(), "totalPauselst: ", gcnum
			print "%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"
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
