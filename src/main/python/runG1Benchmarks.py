import os, sys, json
import subprocess

# Set-up bash commands - Run benchmark

################ G1 inside HotSpotVM test - heap(64 .. 2048)

benchmarks = ['Compiler', 'Compress', 'Crypto', 'Derby', 'Mpegaudio', 'Scimark.large', 'Serial', 'Sunflow', 'Xml']

gc = "G1"
warmUpTime = "60s"
execTime = "120s"

# creating necessary dirs
if not os.path.exists("../resources/Benchmarks"):
    os.makedirs("../resources/Benchmarks")

for benchmark in benchmarks:

    heapSize = 64

    for heapIter in range(1,7):

        heapSizeStr = str(heapSize)

        # creating necessary dir
        if not os.path.exists('../resources/Benchmarks/' + benchmark):
            os.makedirs('../resources/Benchmarks/' + benchmark)

        logfile = open('../resources/../Benchmarks/' + benchmark + '/' + gc + '_' + heapSizeStr + '.txt', 'w+')
        command = "java" + " -Xms" + heapSizeStr + "m" + " -Xmx" + heapSizeStr + "m" +" -XX:+UseG1GC" + " -XX:+PrintGCApplicationConcurrentTime" + " -verbose:gc" +" -Dspecjvm.home.dir=/home/kadilier/MaxineVM/maxineGCBenchmark/SPEC" +  " -jar" + "  /home/kadilier/MaxineVM/maxineGCBenchmark/SPEC/SPECjvm2008.jar" + " -it " + execTime + " -wt " + warmUpTime + " -coe" +" -crf" + " false" + " -ikv" + " " + str.lower(benchmark)
        proc = subprocess.Popen(command.split(), stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        for line in proc.stdout:
            sys.stdout.write(line)
            logfile.write(line)
        proc.wait()
        heapSize = heapSize * 2

        print " ************************* " + gc + " -- " + benchmark + " ended *************************"


print "&&&&&&&&&&&&&&&&&&&& G1 Benchamrks ended &&&&&&&&&&&&&&&&&&&&"


