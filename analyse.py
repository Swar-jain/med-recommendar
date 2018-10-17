# The main package to help us with our text analysis
from textblob import TextBlob

# For reading input files in CSV format
import csv


# For sorting dictionaries
import operator


# Intialize an empty list to hold all of our tweets
reviews= []


# A helper function that removes all the non ASCII characters
# from the given string. Retuns a string with only ASCII characters.
def strip_non_ascii(string):
    ''' Returns the string without non ASCII characters'''
    stripped = (c for c in string if 0 < ord(c) < 127)
    return ''.join(stripped)




#
# We create a data structure for each review:


with open('sentiment.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    reader.next()
    for row in reader:

        review= dict()
        review['id'] = int(row[0])
        review['patient'] = row[1]
        review['review'] = row[2]

     
        review['clean'] = review['review']

        # Remove all non-ascii characters
        review['clean'] = strip_non_ascii(review['clean'])
    

        # Create textblob object
        review['TextBlob'] = TextBlob(review['clean'])

    
        reviews.append(review)



# DEVELOP MODELS

for review in reviews:
    review['polarity'] = float(review['TextBlob'].sentiment.polarity)
    review['subjectivity'] = float(review['TextBlob'].sentiment.subjectivity)

    if review['polarity'] >= 0.1:
        review['sentiment'] = 'positive'
    elif review['polarity'] <= -0.1:
        review['sentiment'] = 'negative'
    else:
        review['sentiment'] = 'neutral'

reviews_sorted = sorted(reviews, key=lambda k: k['polarity'])


# EVALUATE RESULTS

print "\n\nTOP NEGATIVE REVIEWS"
negative_review = [d for d in reviews_sorted if d['sentiment'] == 'negative']
for review in negative_review[0:100]:
    print "id=%d, polarity=%.2f, review=%s" % (review['id'], review['polarity'], review['review'])

print "\n\nTOP POSITIVE REVIEWS"
positive_review = [d for d in  reviews_sorted if d['sentiment'] == 'positive']
for review in positive_review[-100:]:
     print "id=%d, polarity=%.2f, review=%s" % (review['id'], review['polarity'], review['review'])

print "\n\nTOP NEUTRAL REVIEWS"
neutral_review = [d for d in  reviews_sorted if d['sentiment'] == 'neutral']
for review in neutral_review[0:500]:
 print "id=%d, polarity=%.2f, review=%s" % (review['id'], review['polarity'], review['review'])


