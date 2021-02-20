#Write a function that converts temperature from Fahrenheit to Celsius using formula
#Tc=(5/9)*(Tf-32) 
#To test your answer, 68F = 20C

def convert_c(Tf):
    Tc=(5/9)*(Tf-32)
    print('value is: {:.2f}'.format(Tc))


while(True):
    Tf = int(input('enter temperature: '))
    

    if(Tf == 000):
        break
    else:
        convert_c(Tf)
