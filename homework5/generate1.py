def generator(start, end, skip):
    x = start
    y = end
    z= skip
    while x<y:
        print(x)
        x+= z
generator(0,5,2)
