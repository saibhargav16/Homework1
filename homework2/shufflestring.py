s = "codeleet"                    #values
n = [4,5,6,7,0,2,1,3]
p = "aiohn"
m = [3,1,4,2,0]
q = "aaiougrt"
l = [4,0,2,6,7,3,1,5]
a = "art"
b = [1,0,2]

t1=""                           #create empty varibles
t2=""
t3=""
t4=""

for i in n:                     #for loop to shuffle the strings
    t1 = t1 + s[i]
for j in m:
    t2 = t2 + p[j]
for k in l:
    t3 = t3 + q[k]
for c in b:
    t4 = t4 + a[c]
print(t1)                       #print them all
print(t2)
print(t3)
print(t4)