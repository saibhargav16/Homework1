def grade(mark):
    if mark >= 95 and mark<= 100:
        return 'A+'
    elif (mark >= 90 and mark <= 94):
        return 'A'
    elif (mark >= 85 and mark <= 89):
        return 'A-'
    elif (mark >= 80 and mark <= 84):
        return 'B+'
    else:
        return 'Invalid Input'


while(True):
    print('welcome');
    cal = int(input('Enter the value:'))
    if cal == 0:
        break
    else:
        print(grade(cal))
   



