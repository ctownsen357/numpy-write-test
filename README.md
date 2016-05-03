## numpy-write-test
A test to benchmark Python struct.pack method of write to binary file to store NumPy array vs 
NumPy built in ndarray.tofile method.  For very small arrays the struct.pack method was faster but as soon 
as the arrays get even remotely larger than just a few items in the array, the ndarray.tofile method is 
MUCH faster.  In my application that I did the benchmark for I'm generating VERY LARGE arrays.  

This test generates ~ 20MB binary file and the timings were as follows:
``` bash

python3 numpywrite.py 
Run time for struct was: 3.9031777381896973
Run time for ndarray.tofile was: 0.01241755485534668

```
