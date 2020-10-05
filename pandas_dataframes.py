import pandas as pd

grades_dict = {'Wally':[87,96,70],'Eva':[100,87,90],'Sam':[94,77,90],'Katie':[100,81,82],'Bob':[83,65,85]}

grades = pd.DataFrame(grades_dict)

grades.index = ['Test1','Test2','Test3']

#print(grades)

#print(grades.Sam)

#print(grades.loc['Test1'])
#print(grades.loc['Test1':'Test3'])          #use a , and it would only give you test 1 and test 3
#print(grades.iloc[0])
#print(grades.iloc[0:2])

#print(grades.loc[['Test1','Test2'],['Eva','Katie']])

#print(grades.iloc[[0,1],[1,3]])

#print(grades)

#print(grades[grades>90])

#print(grades[(grades>=80)&(grades<90)])

#print(grades.at['Test2','Eva'])

grades.at['Test2','Eva'] = 100

#print(grades.at['Test2','Eva'])

#print(grades)

#print(grades.iat[1,2])

grades.iat[1,2] = 87

#print(grades)

#print(grades.describe())        #shows you all the info for each student (count,mean,std,min,25%... ETC.)
pd.set_option('precision',2)     #Makes all the information go to 2 decimal places ^^^


#print(grades.describe())        #shows you all the info for each student (count,mean,std,min,25%... ETC.)
#print(grades.mean())
#print(grades.T.mean())           #Gives you the information for each test
#print(grades)

#print(grades.sort_index(ascending=False))           #Change the order of the tests (from 3-1 instead of 1-3)
#print(grades.sort_index(axis=1))                    #Puts the names in alphabetical order


#print(grades.sort_values(by='Test1', axis=1, ascending=False))


#print(grades.T.sort_values(by='Test1', ascending=False))            #flip the column and rows


print(grades.loc['Test1'].sort_values(ascending=False))


















