from nltk.tokenize import word_tokenize
import re
import string
from nltk.corpus import stopwords
def clean(word):
    Tword = word_tokenize(word)
    regex = re.compile('[%s]' % re.escape(string.punctuation))
    new_review = []
    for token in Tword:
        new_token = regex.sub(u'', token)
        if not new_token == u'':
            new_review.append(new_token)
    print("review words: ",new_review)

    new_term_vector = []
    for word in new_review:
        if not word in stopwords.words('english'):
            new_term_vector.append(word)
    print("new vector: ",new_term_vector)
