import re
import os
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
		heapSizeStr = re.search('%s(.*)%s' % ("SemiS", ".txt"), file).group(1)

		# add result to benchmark
		benchmark.makeResult(heapSizeStr, benchmark_name, GCNUM, -1, -1, -1, -1, -1, -1, -1, -1, TotalReclaimed)

		print "****************************" + '\n'

	# add benchmark to experiment
	experiment.addBenchmark(benchmark)


for benchmark in experiment.benchmarks:

	print benchmark.getName()

	for result in benchmark.results:
		#print " ----> bench_id", result.bench_id
		#print " ----> heap_size,", result.getHeapSize()
		#print " ----> ", result.bench_id
		print " ----> ", result.heapSize , " ... GCs: " , result.gcNum