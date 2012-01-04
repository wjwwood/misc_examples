from time import time
import math

times = []
tick = time()
stuff = ''
while True:
    stuff = raw_input()
    if stuff == 'e':
        break
    tock = time()
    diff = tock-tick
    times.append(diff)
    print diff
    tick = tock
    
print "Mean:", sum(times)/len(times)
print "Max:", max(times)
print "Min:", min(times)
mean = sum(times)/len(times)
deviations = [(x-mean)**2 for x in times]
stdev = math.sqrt(sum(deviations)/(len(deviations)-1))
print "STD:",stdev
print "RPS:", len(times)/sum(times)
print "Radians/second: ", (len(times)/sum(times))*2*math.pi

