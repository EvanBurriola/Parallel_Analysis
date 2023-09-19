# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 17:11:53 2023

@author: Evan

Analyzing performance of a parallel LU decomposition algorithm
on Texas A&M's Grace HPRC cluster at different thread counts and 
matrix sizes
"""

import os
import numpy as np
import matplotlib.pyplot as plt

directory = 'data'

threads = {}


for filename in os.listdir(directory):
    fullname = os.path.join(directory,filename)
    
    if(os.path.isfile(fullname)):
        f = open(fullname, "r")
        f.readline()
        f.readline()
        thread_num = int(''.join(filter(str.isdigit, f.readline())))
        mat_size = int(''.join(filter(str.isdigit, f.readline())))
        
        for _ in range(5):
            f.readline()
        
        string_time = f.readline()
        time_list = string_time[string_time.find('0'):-1].split()
        time = float(time_list[1])
        
        if(threads.get(thread_num) == None):
            threads[thread_num] = {}
        
        threads[thread_num][mat_size] = time
        
print(threads)

xpoints = np.array([1,2,4,8,16,32,64,128,256])
ypoints = np.zeros([9])   
for x in range(9):
    ypoints[x] = threads[xpoints[x]][128]
    
plt.plot(xpoints,ypoints,marker = "o")
plt.title("Matrix Size: 128")
plt.xlabel("Number of Threads")
plt.ylabel("Time")
plt.show()    

for x in range(9):
    ypoints[x] = threads[xpoints[x]][1024]

plt.plot(xpoints,ypoints,marker = "o")
plt.title("Matrix Size: 1024")
plt.xlabel("Number of Threads")
plt.ylabel("Time")
plt.show()

for x in range(9):
    ypoints[x] = threads[xpoints[x]][4096]
    
plt.plot(xpoints,ypoints,marker = "o")
plt.title("Matrix Size: 4096")
plt.xlabel("Number of Threads")
plt.ylabel("Time")
plt.show()


