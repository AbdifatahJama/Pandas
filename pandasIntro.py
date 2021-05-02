import pandas as pd
# Panda libary is used for data manipulation and analysis
# In partuicular allows manipulation of tables and time serieses
# we will be working the pokemon data set

# df = pd.read_csv('peope_data_set.csv.txt')
# print(df)

df = pd.read_csv('pokemon_data.csv.txt')
print(df.head(4)) # head function returns the first n rows to make big data more manageable
print(df.tail(3)) # tail function returns the last n rows to make big data more manageable


print(df.columns) # returns list of each columns ie: the headers

# We can look at specific columns within the data set
print(df['Name'][1:11]) # and specify how many rows to go down using indexing

# We can specify mutiple columns that should be looked at
print(df[['Name','Type 1','Type 2','Speed']][0:6]) 

# We can also locate a specific row or rows
print('-----------------')
print(df.iloc[[0,1,-1],[1,2,0]]) # returns rows at indexes 0(first row) 1(second row) and -1(last rows)
print('--------------------')
print(df.iloc[0,1]) # returns data set info on 0 row and 0 column

# We can also make the table show it shows all the pokemons with type 1 'Fire'

# print(df.loc[df['']])
print('---------------')
print(df['Type 2'])
print('------------')
print(df.loc[df['Type 1']=='Fire']) # Loc returns all the rows that satify the conditions within it
# Whereas iloc retunrs all rows and specified collum

a = df.describe()
print(a)
print('--------------')

print(a.iloc[[1],[3]])
print(df.iloc[0:,0:])


print(df.iloc[0:,[1,2,3]]) # all rows and 1,2,3 columns
print(df.iloc[0:,[2,3,4]])
print(df.iloc[0:3,1:3]) # 0:3 rows and 1:3 columns
print(df.iloc[0:,[3,4,5]])

# Sorting tables contents columns by alphabetic order or numbering (asceding or descending)

print(df.sort_values(['Name'],ascending = True)) # Name sorted in alphabetical order
print(df.sort_values(['Type 2','HP'],ascending = [1,0])) # columns type 2 and HP sorted, type 2 sorted in ascending order and HP sorted in descending

# Changing data

# Make new columns

df['Total'] = df['HP'] + df['Attack'] + df['Defense'] + df['Sp. Atk'] + df['Sp. Def'] + df['Speed'] # Producing new Total Column
print(df.sort_values(['Total'],ascending = False))

# droping a column

df = df.drop(columns = ['Total','Defense']) # Can drop or mutiple columns via this way
print(df)


a = df.iloc[0:,5]
print(a.sum()) # sum of a column - all graphs normally have axis of 0 as it's considered 2d 

# Better way to make new Total column - NEED TO LEARN HOW TO CHANGE COLUMN ORDER

# df['Total'] = df.iloc[0:,4:10].sum(axis = 1)
# print(df.sort_values(['Total'],ascending = False))

# cols = df.columns
# df[cols[0:4] + [cols[-1]] + cols[4:12]]
# print(df)

# SAVING UPDATED FILE

save_to_csv = df.to_csv('Updated_Pokemon.csv',index = False) # to csv file
save_to_txt = df.to_csv('Updated_Pokemon.txt',index = False,sep = '\t') # to txt file with | acting as separator

# FILTERING DATA IN USEFUL WAYS

# Loc contray to iloc accepts textual/labels and booleans rather than index intergers
# Loc takes in labels meaning indexes or Column names

print(df.loc[1:5,['Name','Type 1']].sort_values(['Name'],ascending =   True))
# print(df.loc[:,'Names'])
print(df.loc[0:,['Name','Type 1']].sort_values(['Name']))
print(df.loc[0:,['Name','Type 2','Type 1','Attack','HP']])

# As well as using loc to format data via labels (indexes and columns) we can use it during condition 

# print(df.loc[df['Attack']])

print(df.loc[0:,['Attack','Type 1']].sort_values(['Attack'],ascending= False))
print(df.loc[df['Attack'] == 30])
print(df.loc[0:500,'Attack'])

a = df.loc[df['Type 1'] == 'Ghost']
print(a)

# filtering data based on mutiple condition using '&' or '|'

# orignal data set
print(df)

data_set = df.loc[(df['Type 1']=='Ghost') & (df['Type 2']=='Poison') &(df['Attack'] > 50)]
print(data_set.reset_index(drop=True).drop(columns=['#'])) # drop attribute in reset_index removes old indexes that were not in order

# Somemore filtering - filtering data that contain a certain word

print(df.loc[0:,'Name'].str.contains('Mega'))

## Conditional changes

# IF a Pokemon has attack greater than 50 then type 2 becomes 'Powerful'

a = df.loc[df['Attack'] >50,'Legendary'] = True # changed so any rows with a pokemon with attack greater than 50 is now considered Legendary
print(df)

# We can also change mutiple rows due to a condition

df.loc[(df['Type 1'] == 'Grass') & (df['Type 2']=='Poison'),['Legendary','Attack']] = [True,55]
print(df)

df.loc[(df['Attack'] + df['Sp. Def'] > 100),'Generation'] = 2
print(df)

## Statistics work on data set

#statistics of a certain column 
# ie: stats of all type 1 data

a = df.groupby(['Type 1']).mean().sort_values(['HP','Sp. Atk'],ascending = False) # mean/average of all type 1 stats pokemon ,then sorts HP from biggest to lowest
print(a)

# groupby mutiple columns

print('------------------------')

b = df.groupby(['Type 1','Speed']).mean() # groups by type and speed and calculates mean of those groups
print(b)


df.loc[df['Type 1'] == 'Grass','Type 1'] = 'Hay'
print(df)













      
















