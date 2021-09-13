a = int(input('Type een geheel getal voor a '))
b = int(input('Type een geheel getal voor b '))
if a > b:
    max = a
    print('a is het grootste getal: '+ str(max))
    print('Het maximum is: '+ str(max))
elif a < b:
    min = a
    print('a is het kleinste getal: '+ str(min))
    print('Het minimum is: '+ str(min))
else:
    print('a is gelijk aan b')