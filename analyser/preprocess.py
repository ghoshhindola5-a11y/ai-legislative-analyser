import re
import nltk
from nltk.corpus import stopwords

def clean_text(text):
    text = re.sub(r'\s+', ' ', text)  # remove extra spaces
    text = text.lower()
    tokens = nltk.word_tokenize(text)
    tokens = [t for t in tokens if t not in stopwords.words('english')]
    return " ".join(tokens)
