# Running SpecJVM2008 benchmark on 3 different GCs(using Maxine and HotSpot VM)

We are testing the following 3 Garbage Collectors:

  - Generational Semi-Space(GenSS) on Maxine VM
  - Semi-Space on Maxine VM
  - G1 collector on HotSpot VM

For measuring the performance of each GC we are using the [SPECjvm2008](https://www.spec.org/jvm2008/) benchmark suite, which consists of the following benchmarks :
  (*Startup, Compiler, Compress, Crypto, Derby, Mpegaudio, Scimark, Serial, Sunflow, Xml*)

Each test is performed for all 3 different GCs and for 6 different heap sizes(64 to 2048 MB), which results in **160** 
individual test runs.

### Prerequisites

 - Maxine VM(https://github.com/beehive-lab/Maxine-VM) must be build for testing GenSS and Semi-Space GCs.
 - Oracle's HotSpot must be build for testing G1 collector.
 - Python 2.7

### Creating necessary directories

Specjvm2008 download from [here](https://www.spec.org/download.html)) and placed in the following dir: *src/main/resources/SPEC*. Benchmark run scipts inside:  src/main/python create any other necessary dir inside src/main/resources.

### Running benchmark tests

Inside *src/main/python* each Python script corresponds to a different GC test.

 - eg. running runGenSSBenchmarks.py executes all SPECjvm2008 benchmark tests on Maxine VM using GEnerational Semi-Space garbage
   collector(default GC). Results will be generated inside */src/main/resources/Benchmarks* sorted by each individual test.
   
### Parsing results

  Python parsers are located inside *src/main/python/Parsers*. Again, each script corresponds to a different GC test.
  
  - eg. running genSSParser.py all benchmark results of Maxine's GenSS(located in *src/main/resource/Benchmarks*) are parsed
  and stored in a json format output file.
  
  This file contains all details for the experiment that were executed.
