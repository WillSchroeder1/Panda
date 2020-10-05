import pandas as pd

file_object = open ('Holiday Schedule Ranking 2019.csv','r')

data = pd.read_csv(file_object, index_col = 0).T

print(data)

file_object.close()

file_object = open('Holiday Schedule Ranking 2019.csv', 'r')

schedule = pd.read_csv(file_object, index_col = 0)

for c in schedule.columns:
    schedule[c].values[:] = 0

print(schedule)

data["col_sum"] = data.apply(lambda x:x.sum(), axis = 1)

print(data)

data = data.sort_values(by="col_sum", ascending = False)

data = data.T

print(data)

for date in data.Columns:

    date_series = data[date].nsmallest(5,keep='all')
    slot_count = 0

#if statement saying tp skip someone after 2 days
#slots arent above 3


#finish for loop


#replace with 0
schedule.replace(0,'', inplace=True)
#wrtie the dataframe
schedule.to_csv('final_schedule.csv')

print("done")