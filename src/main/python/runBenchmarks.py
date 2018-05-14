import os, sys, json
import subprocess

JSON_FILE = "../resources/output.json"

# Set-up bash commands - Run benchmarks

################ Startup - GenSS - heap(50 ... 500)

benchmark_name = "Startup"
gc = "GenSS"
heapSizeInit = 50

for heapIter in range(1,6):

    heapSize = heapIter * heapSizeInit
    heapSizeStr = str(heapSize)

    logfile = open('../Benchmarks/' + benchmark_name + '/' + gc + '_' + heapSizeStr + '.txt', 'w+')
    proc = subprocess.Popen(['maxvm','-Xms' + heapSizeStr + 'm', '-Xmx' + heapSizeStr + 'm', '-XX:+TraceGCTime' ,'-jar', 'SPECjvm2008.jar', '-coe', '--createRawFile', 'false', '--createTextFile' , 'false', '--createHtmlFile' , 'false', '-ikv' ,str.lower(benchmark_name)], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    for line in proc.stdout:
        sys.stdout.write(line)
        logfile.write(line)
    proc.wait()

print " ************************* Startup ended *************************"

################ Compiler - GenSS - heap(50 ... 500)

benchmark_name = "Compiler"
gc = "GenSS"
heapSizeInit = 50

for heapIter in range(1,6):

    heapSize = heapIter * heapSizeInit
    heapSizeStr = str(heapSize)

    logfile = open('../Benchmarks/' + benchmark_name + '/' + gc + '_' + heapSizeStr + '.txt', 'w+')
    proc = subprocess.Popen(['maxvm','-Xms' + heapSizeStr + 'm', '-Xmx' + heapSizeStr + 'm', '-XX:+TraceGCTime' ,'-jar', 'SPECjvm2008.jar', '-coe', '--createRawFile', 'false', '--createTextFile' , 'false', '--createHtmlFile' , 'false', '-ikv' ,str.lower(benchmark_name)], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    for line in proc.stdout:
        sys.stdout.write(line)
        logfile.write(line)
    proc.wait()

print " ************************* Compiler ended *************************"

################ Compress - GenSS - heap(50 ... 500)

benchmark_name = "Compress"
gc = "GenSS"
heapSizeInit = 50

for heapIter in range(1,6):

    heapSize = heapIter * heapSizeInit
    heapSizeStr = str(heapSize)

    logfile = open('../Benchmarks/' + benchmark_name + '/' + gc + '_' + heapSizeStr + '.txt', 'w+')
    proc = subprocess.Popen(['maxvm','-Xms' + heapSizeStr + 'm', '-Xmx' + heapSizeStr + 'm', '-XX:+TraceGCTime' ,'-jar', 'SPECjvm2008.jar', '-coe', '--createRawFile', 'false', '--createTextFile' , 'false', '--createHtmlFile' , 'false', '-ikv' ,str.lower(benchmark_name)], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    for line in proc.stdout:
        sys.stdout.write(line)
        logfile.write(line)
    proc.wait()

print " ************************* Compress ended *************************"


################ Crypto - GenSS - heap(50 ... 500)

benchmark_name = "Crypto"
gc = "GenSS"
heapSizeInit = 50

for heapIter in range(1,6):

    heapSize = heapIter * heapSizeInit
    heapSizeStr = str(heapSize)

    logfile = open('../Benchmarks/' + benchmark_name + '/' + gc + '_' + heapSizeStr + '.txt', 'w+')
    proc = subprocess.Popen(['maxvm','-Xms' + heapSizeStr + 'm', '-Xmx' + heapSizeStr + 'm', '-XX:+TraceGCTime' ,'-jar', 'SPECjvm2008.jar', '-coe', '--createRawFile', 'false', '--createTextFile' , 'false', '--createHtmlFile' , 'false', '-ikv' ,str.lower(benchmark_name)], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    for line in proc.stdout:
        sys.stdout.write(line)
        logfile.write(line)
    proc.wait()

print " ************************* Crypto ended *************************"

################ Derby - GenSS - heap(50 ... 500)

benchmark_name = "Derby"
gc = "GenSS"
heapSizeInit = 50

for heapIter in range(1,6):

    heapSize = heapIter * heapSizeInit
    heapSizeStr = str(heapSize)

    logfile = open('../Benchmarks/' + benchmark_name + '/' + gc + '_' + heapSizeStr + '.txt', 'w+')
    proc = subprocess.Popen(['maxvm','-Xms' + heapSizeStr + 'm', '-Xmx' + heapSizeStr + 'm', '-XX:+TraceGCTime' ,'-jar', 'SPECjvm2008.jar', '-coe', '--createRawFile', 'false', '--createTextFile' , 'false', '--createHtmlFile' , 'false', '-ikv' ,str.lower(benchmark_name)], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    for line in proc.stdout:
        sys.stdout.write(line)
        logfile.write(line)
    proc.wait()

print " ************************* Derby ended *************************"

################ MpegAudio - GenSS - heap(50 ... 500)

benchmark_name = "Mpegaudio"
gc = "GenSS"
heapSizeInit = 50

for heapIter in range(1,6):

    heapSize = heapIter * heapSizeInit
    heapSizeStr = str(heapSize)

    logfile = open('../Benchmarks/' + benchmark_name + '/' + gc + '_' + heapSizeStr + '.txt', 'w+')
    proc = subprocess.Popen(['maxvm','-Xms' + heapSizeStr + 'm', '-Xmx' + heapSizeStr + 'm', '-XX:+TraceGCTime' ,'-jar', 'SPECjvm2008.jar', '-coe', '--createRawFile', 'false', '--createTextFile' , 'false', '--createHtmlFile' , 'false', '-ikv' ,str.lower(benchmark_name)], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    for line in proc.stdout:
        sys.stdout.write(line)
        logfile.write(line)
    proc.wait()

print " ************************* Mpegaudio ended *************************"

################ Xml - GenSS - heap(50 ... 500)

benchmark_name = "Xml"
gc = "GenSS"
heapSizeInit = 50

for heapIter in range(1,6):

    heapSize = heapIter * heapSizeInit
    heapSizeStr = str(heapSize)

    logfile = open('../Benchmarks/' + benchmark_name + '/' + gc + '_' + heapSizeStr + '.txt', 'w+')
    proc = subprocess.Popen(['maxvm','-Xms' + heapSizeStr + 'm', '-Xmx' + heapSizeStr + 'm', '-XX:+TraceGCTime' ,'-jar', 'SPECjvm2008.jar', '-coe', '--createRawFile', 'false', '--createTextFile' , 'false', '--createHtmlFile' , 'false', '-ikv' ,str.lower(benchmark_name)], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    for line in proc.stdout:
        sys.stdout.write(line)
        logfile.write(line)
    proc.wait()

print " ************************* Xml ended *************************"

################ Scimark.large - GenSS - heap(50 ... 500)

benchmark_name = "Scimark.large"
gc = "GenSS"
heapSizeInit = 50

for heapIter in range(1,6):

    heapSize = heapIter * heapSizeInit
    heapSizeStr = str(heapSize)

    logfile = open('../Benchmarks/' + benchmark_name + '/' + gc + '_' + heapSizeStr + '.txt', 'w+')
    proc = subprocess.Popen(['maxvm','-Xms' + heapSizeStr + 'm', '-Xmx' + heapSizeStr + 'm', '-XX:+TraceGCTime' ,'-jar', 'SPECjvm2008.jar', '-coe', '--createRawFile', 'false', '--createTextFile' , 'false', '--createHtmlFile' , 'false', '-ikv' ,str.lower(benchmark_name)], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    for line in proc.stdout:
        sys.stdout.write(line)
        logfile.write(line)
    proc.wait()

print " ************************* Scimark.large ended *************************"



"""
# Convert structure to .json file
def jsonDefault(object):
    return object.__dict__

experiment1 = Experiment("exp1", "jvm1", "gc1")

for bench in range(1, 3):

    benchmark = Benchmark("bench" + str(bench))
    for heapSize in range(1, 11):
        benchmark.makeResult(heapSize * 50, bench)

    experiment1.addBenchmark(benchmark)
"""

#print json.dumps(experiment1, default=jsonDefault)
#with open(JSON_FILE, 'w+') as output:

    #write json to file
    #output.write(json.dumps(experiment1, default=jsonDefault))
