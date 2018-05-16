# Running SpecJVM2008 benchmark on 3 different GC(using Maxine and HotSpot VM)

We are testing the following 3 different garbage collectors:

  - Generational Semi-Space(GenSS) on Maxine VM.
  - Semi-Space on Maxine VM
  - G1 collector on HotSpot VM

For measuring the performance of each GC we are using the SPECjvm2008 benchmark suite, which consists of the following benchmark-
tests(Startup, Compiler, Compress, Crypto, Derby, Mpegaudio, Scimark, Serial, Sunflow, Xml)

Each test run is performed for 6 different heap sizes (64 to 2048 MB) and for each different garbage collector which results in 90 
total runs.

Running ...

