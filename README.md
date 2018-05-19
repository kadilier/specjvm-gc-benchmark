# Running SpecJVM2008 benchmark on 3 different GCs(using Maxine and HotSpot VM)

We are testing the following 3 Garbage Collectors:

  - Generational Semi-Space(GenSS) on Maxine VM
  - Semi-Space on Maxine VM
  - G1 collector on HotSpot VM

For measuring the performance of each GC we are using the [SPECjvm2008](https://www.spec.org/jvm2008/) benchmark suite, which consists of the following benchmarks :
  (*Startup, Compiler, Compress, Crypto, Derby, Mpegaudio, Scimark, Serial, Sunflow, Xml*)

Each test is performed for all 3 different GCs and for 5 different heap sizes(64 to 1024 MB), which results in **135** 
individual test runs.

### Prerequisites

 - Maxine VM(https://github.com/beehive-lab/Maxine-VM) must be build for testing GenSS and Semi-Space GCs.
 - Oracle's HotSpot must be build for testing G1 collector.
 - Python 2.7

### Creating necessary directories

Specjvm2008 must be downloaded (https://www.spec.org/download.html) and placed in the following dir: *src/main/resources/SPEC*. Benchmark run scipts inside:  src/main/python create any other necessary dir inside src/main/resources.

### Running benchmark tests

Inside *src/main/python* each Python script corresponds to a different GC test.

 - eg. running runGenSSBenchmarks.py executes all SPECjvm2008 benchmark tests on Maxine VM using GEnerational Semi-Space garbage
   collector(default GC). Results will be generated inside */src/main/resources/Benchmarks* sorted by each individual test.
   
   ** each benchmark run may take a lot of time(5-10 hours) depending on the HW characteristics of the host computer.
   
### Parsing results

  Python parsers are located inside *src/main/python/Parsers*. Again, each script corresponds to a different GC test.
  
  - eg. running genSSParser.py all benchmark results of Maxine's GenSS(located in *src/main/resource/Benchmarks*) are parsed
  and the output results are stored: *src/main/resources/PlotInput* as .csv files.
  
 
### Creating plots

  Finally, a Python script(*src/main/python/Parsers/plot.py*) receives as input the .csv files that are were previously generated and creates the final plots of the benchmark results.  
  
####  - Logging GC information
  We use the following arguments:
    - Maxine's GCs : -XX:+TraceGCTime, -XX:+PrintCompilationTime
    - HotSpot G1: -XX:+PrintGCApplicationConcurrentTime, -verbose:gc
    
#### - Running benhcmark cmds
  
  Both Maxine's GCs benchmark tests can be run with the following cmd:
  
    *mx vm -Xms heapSizeInit -Xmx heapSizeMax -XX:+TraceGCTime -XX:+PrintCompilationTime -jar [SPEC_PARAMS]*
   
  HotSpot's G1 can be used with the following cmd:
  
    *java heapSizeInit -Xmx heapSizeMax -XX:+UseG1GC -XX:+PrintGCApplicationConcurrentTime -verbose:gc -jar [SPEC_PARAMS]*
   
