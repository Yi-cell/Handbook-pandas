import pandas as pd 
PD_reviews = pd.read_csv('US_politicians_Twitter.csv')
'''Dtypes'''
#The data type for a column in a DataFrame or a Series is known as the dtype.
#You can use dtype property to grab the type of specific column. For instance, we can get the dtype of the price column in the reviews DataFrame.

print(PD_reviews.Age.dtype)
print(PD_reviews.dtypes)# the dtypes property returns the dtype of every column in the DataFrame
# Data types tell us something about how pandas is storing the data internally. float64 means that is's using a 64-bit floating point number; int64 means a similarly sized integer instead, and so on.
#It's possible to convert a column of one type into another wherever such a conversion makes sense by using the astype() function. For example, we may transform the points column from its existing int64 data type into a float64 data type:
print(PD_reviews.Age.astype('float64'))
# A DataFrame or Series index has its own dtype
print(PD_reviews.index.dtype)

'''Missing Data'''
#Entries missing values are given the value NaN, short for "Not a Number". For technical reasons these NaN values are always of the float64 dtype.

#Pandas provides some methods specific to missing data. To select NaN entries you can use pd.isnull() (or its companion pd.notnull()). This is meant to be used thusly:
print(PD_reviews[pd.isnull(PD_reviews.Age)])
#Replacing missing values is a common operation. Pandas provides a really handy method for this problem: fillna(). fillna() provides a few different strategies for mitigating such data. For example, we can simply replace each NaN with an "Unknown":
PD_reviews.Age.fillna('Unknown')
#Or we could fill each missing value with the first non-null value that appears sometime after the given record in the database. This is known as the backfill strategy.
k =PD_reviews.Political_party.replace('Democratic Party','Devil')
print(k.head())