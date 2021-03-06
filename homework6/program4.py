import glob
import time

start = time.time()

print("please enter a path:", end="")
path = input().strip().rstrip('/')
print("please enter a filename:", end="")
filename = input().strip()

files = glob.glob(path + '/**/' + filename, recursive=True)
print(files[0])

end = time.time()

print(f"Runtime of the program is {end - start}")