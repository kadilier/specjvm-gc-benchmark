import os, sys, json
import subprocess

from structure import Experiment, Benchmark, Result

JSON_FILE = "../resources/output.json"

# Convert structure to .json file
def jsonDefault(object):
    return object.__dict__

experiment1 = Experiment("exp1", "jvm1", "gc1")

for bench in range(1, 3):

    benchmark = Benchmark("bench" + str(bench))
    for heapSize in range(1, 11):
        benchmark.makeResult(heapSize * 50, bench)

    experiment1.addBenchmark(benchmark)


#print json.dumps(experiment1, default=jsonDefault)

with open(JSON_FILE, 'w+') as output:

    #write json to file
    output.write(json.dumps(experiment1, default=jsonDefault))
