import time

# starting time
start = time.time()

# program body starts
def myfunc(*params):
	for x in params:
		print(x)

myfunc("one", 2, 3, 4)

# sleeping for 1 sec to get 10 sec runtime
time.sleep(1)

# program body ends

# end time
end = time.time()

# total time taken
print(f"Runtime of the program is {end - start}")