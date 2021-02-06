count = 0; higher = 100; lower = 0; guess=50                                         #values initilization
hi = input('Hi, what is your Name: ')                                                #asking user name
print('Hello ' +hi+'!' " Let's play a game!" )                                       #greet the user
print("Think of random number from 1 to 100, and I'll try to guess it!")             
while True:                                                                          #loop
    count += 1                                                                       #count initilization to get attempts
    ans = input('Is your number ' + str(guess) + ': ')                               #asking user whether its 50 or not
    if ans == "no":                                                                  #if 'no' the loop runs to guess the number 
        ans1 = input('is your number larger than '+ str(guess)+'(yes/no): ')         #ask if it is larger than 50(guess)     
        if ans1 == 'yes':                                                            #make if larger
            lower = guess                                                            #make lower to 50
            guess = (higher + guess)//2                                              #make add guess to higher and make it half and ask user guess is the number they think off
        elif ans1 == 'no':                                                           #if lower
            higher = guess                                                           # make the higher equal to guess
            guess = (lower + guess)//2                                               #add guess to lower and make it half and make it as guess and ask user whether is the number they thought off    
    elif ans == "yes":                                                               #if yes
        print('Yay!! I guessed it in '+ str(count) +' attempts')                     #tell them number of guess
        y = input('Do you want to play more(yes/no)?')                               #ask them if they want to play more
        if y == 'yes':                                                               #if yes
            count = 0; higher = 100; lower = 0; guess=50                             #re initilize the values 
            print("Think of random number from 1 to 100, and I'll try to guess it!") #print
        else:                                                                        #else
            print('Bye-bye')                                                         #bye bye
            break                                                                    #break the loop

    