import pandas as pd
PD_reviews = pd.read_csv('US_politicians_Twitter.csv')
print(PD_reviews.head())
#Selecting Name property 
print(PD_reviews.Name)
print(PD_reviews['Name'])
#These are the two ways of selecting a specific Series out of a DataFrame. Neither of them is more or less syntactically valid than the other, but the indexing operator [] does have the advantage that it can handle column names with reserved characters in them (e.g. if we had a country providence column, reviews.country providence wouldn't work).

'''Index-based selection'''
#Pandas indexing works in one of two paradigms. The first is index-based selection: selecting data based on its numerical position in the data. iloc follows this paradigm.
#To select the first row of data in a DataFrame, we may use the following:
print(PD_reviews.iloc[0])
#Both loc and iloc are row-first, column-second. This is the opposite of what we do in native Python, which is column-first, row-second.
print(PD_reviews.iloc[:,0])
#Select the Name column from just the first, second, and third row
print(PD_reviews.iloc[:3,0]) 
# Or
print(PD_reviews.iloc[[0,1,2],0])
# The last five elements of the dataset.
print(PD_reviews.iloc[-5:])

'''Label-based selection'''
#The second paradigm for attribute selection is the one followed by the loc operator: label-based selection. In this paradigm, it's the data index value, not its position, which matters.
#Get the first entry in PD_review
print(PD_reviews.loc[0,'Name'])

#iloc is conceptually simpler than loc because it ignores the dataset's indices. When we use iloc we treat the dataset like a big matrix (a list of lists), one that we have to index into by position. loc, by contrast, uses the information in the indices to do its work. Since your dataset usually has meaningful indices, it's usually easier to do things using loc instead. For example, here's one operation that's much easier using loc:
print(PD_reviews.loc[:,['Name','Twitter_username']])

'''Choosing between loc and iloc'''

#When choosing or transitioning between loc and iloc, there is one "gotcha" worth keeping in mind, which is that the two methods use slightly different indexing schemes.

#iloc uses the Python stdlib indexing scheme, where the first element of the range is included and the last one excluded. So 0:10 will select entries 0,...,9. loc, meanwhile, indexes inclusively. So 0:10 will select entries 0,...,10.

#Why the change? Remember that loc can index any stdlib type: strings, for example. If we have a DataFrame with index values Apples, ..., Potatoes, ..., and we want to select "all the alphabetical fruit choices between Apples and Potatoes", then it's a lot more convenient to index df.loc['Apples':'Potatoes'] than it is to index something like df.loc['Apples', 'Potatoet] (t coming after s in the alphabet).

#This is particularly confusing when the DataFrame index is a simple numerical list, e.g. 0,...,1000. In this case df.iloc[0:1000] will return 1000 entries, while df.loc[0:1000] return 1001 of them! To get 1000 elements using loc, you will need to go one lower and ask for df.loc[0:999].

#Otherwise, the semantics of using loc are the same as those for iloc.

'''Manipulating the index'''
#Label-based selection derives its power from the labels in the index. Critically, the index we use is not immutable. We can manipulate the index in any way we see fit.

#The set_index() method can be used to do the job. Here is what happens when we set_index to the title field:

# -- PD_reviews.set_index('title')

'''Conditional selection'''
# So far we've been indexing various strides of data, using structural properties of the DataFrame itself. To do interesting things with the data, however, we often need to ask questions based on conditions.
# For example, suppose that we're interested specifically in politicians from Democratic party.

print(PD_reviews.Political_party == 'Democratic Party')

#This result can then be used inside of loc to select the relevant data

print(PD_reviews.loc[PD_reviews.Political_party == 'Democratic Party'])

#We can use the ampersand & to bring the two questions together.

print(PD_reviews.loc[(PD_reviews.Political_party == 'Democratic Party')&(PD_reviews.Age >= 50)])
print(PD_reviews.loc[(PD_reviews.Political_party == 'Democratic Party')|(PD_reviews.Age >= 50)])

#The first is isin. isin is lets you select data whose value "is in" a list of values. For example, here's how we can use it to select politicians only from DP or GP:

print(PD_reviews.loc[PD_reviews.Political_party.isin(['Democratic party','Republican Party'])])

#The second is isnull (and its companion notnull). These methods let you highlight values which are (or are not) empty (NaN). 

print(PD_reviews.loc[PD_reviews.Political_party.isnull()])

'''Assigning data'''
# add new column and assigning data
PD_reviews['Republican Party'] = 'red'
print(PD_reviews.head())
# Or with an iterable of values
PD_reviews['index_backwards'] = range(len(PD_reviews),0,-1)
print(PD_reviews.tail())