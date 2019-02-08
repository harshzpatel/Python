print("Note: It doesn't works for leap year...")
print()               # just for leaving a line

wholeDate = input("Date- ")

date = wholeDate[0:2]
month = wholeDate[3:5]
year = wholeDate[6:10]

firstTwoYear = year[0:2]
lastTwoYear = year[2:4]

byFour = int(int(lastTwoYear) / 4)




if int(month) == 1:
    month = 1

if int(month) == 2:
    month = 4

if int(month) == 3:
    month = 4

if int(month) == 4:
    month = 0

if int(month) == 5:
    month = 2

if int(month) == 6:
    month = 5

if int(month) == 7:
    month = 0

if int(month) == 8:
    month = 3

if int(month) == 9:
    month = 6

if int(month) == 10:
    month = 1

if int(month) == 11:
    month = 4

if int(month) == 12:
    month = 6





if int(firstTwoYear) == 16:
    firstTwoYear = 6
    
if int(firstTwoYear) == 17:
    firstTwoYear = 4
    
if int(firstTwoYear) == 18:
    firstTwoYear = 2
    
if int(firstTwoYear) == 19:
    firstTwoYear = 0
    
if int(firstTwoYear) == 20:
    firstTwoYear = 6
    
if int(firstTwoYear) == 21:
    firstTwoYear = 4





allAdd = int(date) + int(lastTwoYear) + int(firstTwoYear) + int(byFour) + int(month)

day = allAdd % 7




if day == 0:
    day = "Saturday"

if day == 1:
    day = "Sunday"

if day == 2:
    day = "Monday"

if day == 3:
    day = "Tuesday"

if day == 4:
    day = "Wednesday"

if day == 5:
    day = "Thursday"

if day == 6:
    day = "Friday"


    

print("The day is",day)
