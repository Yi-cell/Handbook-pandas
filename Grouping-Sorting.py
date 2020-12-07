import pandas as pd
PD_reviews = pd.read_csv('US_politicians_Twitter.csv')
'''
Introduction
Maps allow us to transform data in a DataFrame or Series one value at a time for an entire column. However, often we want to group our data, and then do something specific to the group the data is in.

As you'll learn, we do this with the groupby() operation. We'll also cover some additional topics, such as more complex ways to index your DataFrames, along with how to sort your data.

'''
''' Groupwise analysis'''
# One function we've been using heavily thus far is the value_counts()
print(PD_reviews.groupby('Age').Age.count())

#groupby() created a group of reviews which allotted the same point values to the given wines. Then, for each of these groups, we grabbed the points() column and counted how many times it appeared.  value_counts() is just a shortcut to this groupby() operation.

#We can use any of the summary functions we've used before with this data. For example, to get the cheapest wine in each point value category, we can do the following:

print(PD_reviews.groupby('Political_party').Age.min())

#Using lambda and groupby

print(PD_reviews.groupby('Political_party').apply(lambda df: df.Age.iloc[0]))

#For even more fine-grained control, you can also group by more than one column. For an example, here's how we would pick out the oldest politicians by party and gender.

print(PD_reviews.groupby(['Political_party','Sex']).apply(lambda df: df.Age.iloc[0]))

#Another groupby() method worth mentioning is agg(), which lets you run a bunch of different functions on your DataFrame simultaneously. For example, we can generate a simple statistical summary of the dataset as follows:

print(PD_reviews.groupby(['Political_party']).Age.agg([len,min,max]))

'''Muti-indexes'''
# In all of the examples we've seen thus far we've been working with DataFrame or Series objects with a single-label index. groupby() is slightly different in the fact that, depending on the operation we run, it will sometimes result in what is called a multi-index.
# A multi-index differs from a regular index in that it has multiple levels. For example:
print(PD_reviews.groupby(['Political_party','Sex']).Twitter_username.agg([len]))
A = PD_reviews.groupby(['Political_party','Sex']).Twitter_username.agg([len])

# Multi-indices have several methods for dealing with their tiered structure which are absent for single-level indices. They also require two levels of labels to retrieve a value. Dealing with multi-index output is a common "gotcha" for users new to pandas.

#However, in general the multi-index method you will use most often is the one for converting back a regular index, the reset_index() method:
print(A.reset_index())

'''Sorting'''
# We can see that grouping returns data in index order, not in value order. That is to say, when outputting the result of a groupby, the order of the rows is dependent on the values in the index, not in the data.

PD_sort = A.reset_index()
print(PD_sort.sort_values(by='len'))
#sort_values() defaults to an ascending sort, where the lowest values go first. However, most of the time we want a descending sort, where the higher numbers go first. That goes thusly:
print(PD_sort.sort_values(by='len',ascending=False))
#To sort by index values, use the companion method sort_index(). This method has the same arguments and default order
print(PD_sort.sort_index())
#Finally, know that you can sort by more than one column at a time:
print(PD_sort.sort_values(by=['len','Sex']))