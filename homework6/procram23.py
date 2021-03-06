import shelve 
import time


quotes =['friend in need is friend indeed', 'sun rises in the east', 'small things make big difference'] 

start = time.time()

shelvefile = shelve.open("shelf_file") 
   
shelvefile['quotes']= quotes

end = time.time()

print("time taken shelve: {}".format(end - start))

start = time.time()

dictionary = { 'quotes': quotes }

end = time.time()

print("time taken dictionary: {}".format(end - start))

  
shelvefile.close()