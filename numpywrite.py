import numpy as np
import struct
import time

def write_struct(x):
	""" replicates the original method I was using to write the binary file """
	fmt = '<hii' #little endian, short, int, int
	with open('tst.bin', 'wb') as fout:
		for row in x: 
			mybin = struct.pack(fmt, row[0], row[1], row[2])
			fout.write(mybin)


def write(x):
	""" write uses the NumPy ndarray.tofile method """
	with open('tst.bin', 'wb') as fout:
		x.tofile(fout)

#create a somewhat representative array (the np arrays I'm creating in the application are MUCH larger)
x = np.array([(1,2,3), (4,5,6)], dtype=('i2,i4,i4'))
for b in range(20):
	x = np.append(x,x)


wall_time_start = time.time()
write_struct(x)
elapsed_wall = (time.time() - wall_time_start)
print("Run time for struct was: {t}".format(t=elapsed_wall))
x = np.fromfile('tst.bin', dtype=('i2,i4,i4'))
print(x.shape)

wall_time_start = time.time()
write(x)
elapsed_wall = (time.time() - wall_time_start)
print("Run time for ndarray.tofile was: {t}".format(t=elapsed_wall))
x = np.fromfile('tst.bin', dtype=('i2,i4,i4'))
print(x.shape)



