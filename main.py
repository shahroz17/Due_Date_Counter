# This program take maximum 5 data values from the user and show them on the terminal


Numbers = ['first', 'second', 'third', 'fourth', 'fifth']  # List to show the values number on terminal
datetime_data = []  # initializing the list to append date and time together
Val_invalid = 1

Data = int(input('How much data you want to enter in between 1-5?\n'))

if 0 < Data < 6:  # Check if the input data is in required range
    print(Data)
else:
    print("Input Data is not in range")

for x in range(Data):  # Loop to enter Time and date
    Date = input('please enter a date: (Format : TT.MM.YYYY)\n')
    dd, mm, yy = Date.split('.')
    dd = int(dd)
    mm = int(mm)
    if 0 < dd < 32 and 0 < mm < 13 and len(yy) == 4:
        print('Value is valid')
    else:
        Val_invalid = 0
        break
    Time = input('please enter a time:(Format : HH.MM)\n')
    hh, nn = Time.split('.')
    hh = int(hh)
    nn = int(nn)
    if 0 <= hh < 25 and 0 <= nn < 61:
        print('Value is valid')
    else:
        Val_invalid = 0
        break
    datetime_data.append(Date + '-' + Time)

print("Thank you so much. I will notify them! ")
if Val_invalid == 1:
    for x in range(Data):  # loop to print the values on the terminal in their sequence
        print("The " + Numbers[x] + " date has been reached! " + datetime_data[x])
else:
    print('Value is invalid start again')
