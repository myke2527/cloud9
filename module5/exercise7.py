
spendings = [1346.0, 987.50, 1734.40, 2567.0, 3261.45, 2500.0, 2130, 2987.34, 3120.50, 4069.78, 1000.0]

low = 0
normal = 0
high = 0

for month in spendings:
    if month <1000.0:
        low += 1
    elif month <= 2500.0:
        normal += 1
    else:
        high += 1
        
print('Numbers of months with low speedings: ' +str(low) + ', normal spendings: ' + str(normal) + ', high spendings: ' + str(high) + ',')
