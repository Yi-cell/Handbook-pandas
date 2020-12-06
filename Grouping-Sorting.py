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