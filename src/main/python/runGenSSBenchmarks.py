import os, sys, json
import subprocess

# Set-up bash commands - Run benchmark

################ GenSS inside MaxineVM - heap(64 .. 2048)

benchmarks = ['Compiler', 'Compress', 'Crypto', 'Derby', 'Mpegaudio', 'Scimark.large', 'Serial', 'Sunflow', 'Xml']

gc = "GenSS"
warmUpTime = "60s"
execTime = "120s"

for benchmark in benchmarks:

    heapSize = 64

    for heapIter in range(1,7):

        heapSizeStr = str(heapSize)

        logfile = open('../resources/../Benchmarks/' + benchmark + '/' + gc + '_' + heapSizeStr + '.txt', 'w+')
        command = "mx" + " vm" + " -Xms" + heapSizeStr + "m" + " -Xmx" + heapSizeStr + "m" + " -XX:+TraceGCTime" +" -XX:+PrintCompilationTime" + " -Dspecjvm.home.dir=/home/kadilier/MaxineVM/maxineGCBenchmark/SPEC" +  " -jar" + "  /home/kadilier/MaxineVM/maxineGCBenchmark/SPEC/SPECjvm2008.jar" + " -it " + execTime + " -wt " + warmUpTime + " -coe" +" -crf" + " false" + " -ikv" + " " + str.lower(benchmark)
        proc = subprocess.Popen(command.split(), stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        for line in proc.stdout:
            sys.stdout.write(line)
            logfile.write(line)
        proc.wait()
        heapSize = heapSize * 2

        print " ************************* " + gc + " -- " + benchmark + " ended *************************"


print "&&&&&&&&&&&&&&&&&&&& GenSS Benchamrks ended &&&&&&&&&&&&&&&&&&&&"

