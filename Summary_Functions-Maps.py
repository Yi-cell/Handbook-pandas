import pandas as pd 
PD_reviews = pd.read_csv('US_politicians_Twitter.csv')
'''Summary functions'''
#Pandas provides many simple "summary functions" (not an official name) which restructure the data in some useful way. For example, consider the describe() method:
# for data type
print(PD_reviews.Age.describe())
# for string data
print(PD_reviews.Name.describe())
# To see the mean of the age allotted
print(PD_reviews.Age.mean())
# To see a list of unique values we can use the unique() function:
print(PD_reviews.Name.unique())

'''Maps'''
#A map is a term, borrowed from mathematics, for a function that takes one set of values and "maps" them to another set of values. In data science we often have a need for creating new representations from existing data, or for transforming data from the format it is in now to the format that we want it to be in later. Maps are what handle this work, making them extremely important for getting your work done!

# map() is the first, and slightly simpler one. For example, suppose that we wanted to remean the scores the wines received to 0. We can do this as follows:

PD_reviews_age_mean = PD_reviews.Age.mean()
print(PD_reviews.Age.map(lambda a: a - PD_reviews_age_mean))

#apply() is the equivalent method if we want to transform a whole DataFrame by calling a custom method on each row.

def remean_age(row):
    row.Age = row.Age - PD_reviews_age_mean
    return row
PD_reviews.apply(remean_age, axis ='columns')

#faster way mapping

PD_reviews_age_mean = PD_reviews.Age.mean()
print(PD_reviews.Age - PD_reviews_age_mean)

#Pandas will also understand what to do if we perform these operations between Series of equal length. For example, an easy way of combining name and age information in the dataset would be to do the following:

print(PD_reviews.Name + ' - ' + PD_reviews.Political_party)

# sample: We'd like to host these wine reviews on our website, but a rating system ranging from 80 to 100 points is too hard to understand - we'd like to translate them into simple star ratings. A score of 95 or higher counts as 3 stars, a score of at least 85 but less than 95 is 2 stars. Any other score is 1 star.

#Also, the Canadian Vintners Association bought a lot of ads on the site, so any wines from Canada should automatically get 3 stars, regardless of points.

#Create a series star_ratings with the number of stars corresponding to each review in the dataset.
'''
def ratings(row):
    if(row['country']=='Canada'):
        return 3
    elif(row['points']>=95):
        return 3
    elif(row['points']>=85 and row['points']<95):
        return 2
    else:
        return 1
star_ratings = reviews.apply(ratings,axis='columns')
'''
