import re

"""
Contains structures for the experiment(s):
    Experiment
        -> Benchmark
            -> Result (contains all measurements required for the different configs(heapSize)
"""
class Result:

    def __init__(self, heapSize, bench_id, gcNum, minorNumNotFull, minorTotalTime, minorTotalReclaimed, minorTotalTimeFull, majorTotalNum, majorTotalTime, totalTimeFull, totalTime, majorTotalReclaimed):
        # Configs
        self.heapSize = int(heapSize)
        self.bench_id = bench_id

        # Measurement
        self.gcNum = gcNum
        self.minorNumNotFull = minorNumNotFull
        self.minorTotalTime = minorTotalTime
        self.minorTotalReclaimed = minorTotalReclaimed
        self.minorTotalTimeinFULLGC = minorTotalTimeFull
        self.majorNum = majorTotalNum
        self.majorTotalTime = majorTotalTime
        self.totalTimeFull = totalTimeFull
        self.totalTime = totalTime
        self.majorTotalReclaimed = majorTotalReclaimed

    def getHeapSize(self):
        return self.heapSize

    def getBenchId(self):
        return self.bench_id

    def getTime(self):
        return self.time



class Benchmark:

    def __init__(self, name):
        self.name = name
        self.appTime = -1
        self.results = []

    def makeResult(self, heapSize, bench_id, gcNum, minorNumNotFull, minorTotalTime, minorTotalReclaimed, minorTotalTimeFull, majorTotalNum, majorTotalTime, totalTimeFull, totalTime, majorTotalReclaimed):
        self.results.append(Result(heapSize, bench_id, gcNum, minorNumNotFull, minorTotalTime, minorTotalReclaimed, minorTotalTimeFull, majorTotalNum, majorTotalTime, totalTimeFull, totalTime, majorTotalReclaimed))

    def addResult(self, result):
        self.results.append(result)

    def setAppTime(self, appTime):
        self.appTime = appTime

    def getAppTime(self):
        return self.appTime

    def getName(self):
        return self.name


class Experiment:

    def __init__(self, experiment, jvm, gcType):
        self.experiment = experiment
        self.jvm = jvm
        self.gcType = gcType

        self.benchmarks = []

    def addBenchmark(self, benchmark):
        self.benchmarks.append(benchmark)
