#Calculating average temperature and finding how many days are above that average.

days = int(input("How many days' temperature?"))
totalTemp = 0

dummy = []

for i in range(days):
    whichDay = int(input("Day " + (str(i+1)) + "'s temperature: "))
    dummy.append(whichDay)
    totalTemp += dummy[i]

avg = round(totalTemp/days, 2)
print(avg)

count = 0 #finding how many days are above average
for i in range(0, len(dummy)):
    if dummy[i] > avg:
        count += 1
print(count)




