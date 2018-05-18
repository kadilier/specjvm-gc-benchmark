import re
import os, json, operator, csv
from structure import Experiment, Benchmark, Result

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

# structure used for storing results, see structure.py
experiment = Experiment("Exp1", "MaxineVM", "G1")

folders = os.listdir(FILES_PATH)

for folder in folders:

    # create new benchmark, folder corresponds to benchmark name
    benchmark_name = folder
    benchmark = Benchmark(benchmark_name)

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

        # Get heap size from file name and create new Result
        heapSizeStr = re.search('%s(.*)%s' % ("G1_", ".txt"), file).group(1)

        # add result to benchmark
        GCNUM = int(youngNUM) + int(mixedNUM) + int(fullNUM)
        if GCNUM == 0:
            print "zero"
        totalTime = int(youngTotalTime*1000) + int(mixedTotalTime*1000) + int(fullTotalTime*1000)
        reclaimed = int(youngReclaimed) + int(mixedReclaimed) + int(fullReclaimed)

        print "***** "
        benchmark.makeResult(heapSizeStr, benchmark_name, GCNUM, -1, -1, -1, -1, -1, -1, -1, totalTime, reclaimed)


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
