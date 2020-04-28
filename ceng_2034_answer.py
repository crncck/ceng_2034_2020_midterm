#! /usr/bin/python3
import os
import platform
import sys
import requests
import threading
import time

#print pid of the program itself
print("PID: %s" % os.getpid())

#print loadavg if the running system is linux
system_name = platform.system()

if system_name == "Linux":
	print("Loadavg values: %s %s %s" % os.getloadavg())

#print 5 min loadavg value
a, b, c = os.getloadavg()
print("5 min loadavg value: %s" % b)

#print cpu core count
cpuCore = os.cpu_count()
print("CPU core count: %s" % cpuCore)

'''
#if the 5 min loadavg value is close to cpu core count then exit script
if cpuCore - b < 1:
	print("Exited from the script")
	sys.exit()
'''

print("\n")

#check if the links in these urls are valid or not
start = time.time()
urls = ['https://api.github.com', 'http://bilgisayar.mu.edu.tr/', 'https://www.python.org/', 'http://akrepnalan.com/ceng2034', 'https://github.com/caesarsalad/wow']

def urlCheck(url):
	try:
		response = requests.head(url)
	except requests.ConnectionError():
		return 2
	else:
		if 200 <= response.status_code <= 299:
			return 1
		else:
			return 0

for url in urls:
	if urlCheck(url) == 1:
		print("Valid URL: " + url)
	elif urlCheck(url) == 2:
		print("Failed: " + url)
	else:
		print("Invalid URL: " + url)

end = time.time()

print("Elapsed time: %s" % (end - start))
print("\n")


#check if the links in these urls are valid or not with threads
start = time.time()

def urlCheck(url):
	try:
		response = requests.head(url)
	except requests.ConnectionError():
		print("Failed: " + url)
	else:
		if 200 <= response.status_code <= 299:
			print("Valid URL: " + url)
		else:
			print("Invalid URL: " + url)

threads = [threading.Thread(target=urlCheck, args=(url,)) for url in urls]

for thread in threads:
	thread.start()
for thread in threads:
	thread.join()

end = time.time()

print("Elapsed time: %s" % (end - start))


