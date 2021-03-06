import os
import sys
import time


#print('Argument List:', sys.argv)
path = sys.argv[0]
while True:
    print(os.path.exists(path))
    time.sleep(3)