#!/usr/bin/python
import psutil, sys

def getCpuMetrics():
    print("[ CPU metrics ]")
    infoP = psutil.cpu_times_percent(interval = 1, percpu = False)
    print("System cpu   idle: [%s]" % infoP[3])
    print("System cpu   user: [%s]" % infoP[0])
    print("System cpu  guest: [%s]" % infoP[8])
    print("System cpu iowait: [%s]" % infoP[4])
    print("System cpu stolen: [%s]" % infoP[7])
    print("System cpu system: [%s]" % infoP[2])

def getMemMetrics():
    print("[ Memory metrics ]")
    infoP = psutil.virtual_memory()
    print("Virtual  total: [%d]" % infoP[0])
    print("Virtual   used: [%d]" % infoP[3])
    print("Virtual   free: [%d]" % infoP[4])
    print("Virtual shared: [%d]" % infoP[9])
    infoP = psutil.swap_memory()
    print("------------------------------")
    print("Swap 	 total: [%d]" % infoP[0])
    print("Swap  	  used: [%d]" % infoP[1])
    print("Swap  	  free: [%d]" % infoP[2])

def getUsage():
    print("Usage: metrics [ cpu | mem ] \n No args \t Display help. \n cpu \t\t Display CPU metrics information. \n mem \t\t Display MEMORY metrics information.")

def printBorder():
    print("/--------------------------------------------------------/")

argLen = len(sys.argv)
if argLen == 2:
    printBorder()
    if sys.argv[1] == "cpu":
        getCpuMetrics()
    elif sys.argv[1] == "mem":
        getMemMetrics()
    else:
        getUsage()
    printBorder()
else:
    printBorder()
    getUsage()
    printBorder()
    
