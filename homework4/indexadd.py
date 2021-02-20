arr = [2,7,11,15]
target = 9

def twosum(arr,target):
    values = dict()
    
    for i, elem in enumerate(arr):
        comp = target - elem                 # comp = 9 - 2;  comp = 7

        if comp in values:                    # if 7 in [2,7,11,15]

            return [values[comp], i]          # return [0, 1]

        values[elem] = i

    return []

list =twosum(arr,target)
print(list)
                
