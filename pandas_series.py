import pandas as pd

grades = pd.Series([87, 100, 94,])

#print(grades)

myarray = pd.Series(98.6, range(3))

#print(myarray)

#print(grades[0])

#print(grades.describe())

grades = pd.Series([87,100,94], index = ['Wally', 'Eva', 'Sam'])

#print(grades)

grades = pd.Series({'Wally':87, 'Eva':100, 'Sam':94})

#print(grades)

#print(grades['Eva'])

#print(grades.Wally)

#print(grades[1])

#print(grades.dtype)

#print(grades.values)


hardware = pd.Series(['Hammer','Sam', 'Wrench'])

a = hardware.str.contains('a')

#print(a)

b=hardware.str.upper()

print(b)