# At this point, I had looked up what sentiment analysis was and how it works.
# This led me to downloading Natural Language Toolkit. I tried to import it into Python.
import nltk
print(nltk.__version__)
# This was done just to make sure I had the most updated version of the Toolkit.
text = open('input.txt').read()
print(text)
lower_case = text.lower()
# This is done because 'Apple' is not equal to 'apple' so all of the words must be lowercase.
# I have cited the sources where I learned these things.
# During this, I was using the YouTube playlist to give me the why of doing the things I do!
print(lower_case)
# It worked!
import string
cleaned_text = lower_case.translate(str.maketrans('','',string.punctuation))
# Translating is similar to converting, and in this case we are converting this lowercase string to into one without punctuation.
# I left the first two strings blank in this case because no characters need to be replaced, only deleted!
print(cleaned_text)
# It worked!
from nltk.tokenize import word_tokenize
tokenize_words = word_tokenize(cleaned_text,"english")
# Since word_tokenize works much faster than split, I used it here! 
# Since nltk also uses many languages, it's important to specify that we're using English!
from nltk.corpus import stopwords
final_words = []
for word in tokenize_words:
    if word not in stopwords.words('english'):
        final_words.append(word)
print(final_words)
from nltk.sentiment.vader import SentimentIntensityAnalyzer
def sentiment_analyse(sentiment_text):
    score = SentimentIntensityAnalyzer().polarity_scores(sentiment_text)
    print (score)
sentiment_analyse(cleaned_text)
def sentiment_analyse(sentiment_text):
    score = SentimentIntensityAnalyzer().polarity_scores(sentiment_text)
    neg = score['neg']
    pos = score['pos']
    if neg > pos:
        print("Negative Sentiment")
    elif pos > neg:
        print("Positive Sentiment")
    else:
        print("Neutral Vibe")
sentiment_analyse(cleaned_text)