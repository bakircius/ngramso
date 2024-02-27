import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.util import ngrams
import string
import sosq
import emek

# Ensure NLTK resources are available (might need to be run separately in an environment where NLTK is fully accessible)
# nltk.download('stopwords')
# nltk.download('punkt')

# Function to preprocess text
def preprocess_text(text):
    # Convert to lowercase, remove punctuation, remove extra spaces, and remove stopwords
    text = str(text).lower()
    text = ''.join(char for char in text if char not in string.punctuation)
    text = ' '.join(text.split())
    stop_words = set(stopwords.words('english'))
    tokens = nltk.word_tokenize(text)
    filtered_tokens = [word for word in tokens if word not in stop_words]
    return ' '.join(filtered_tokens)

# Function to generate n-grams from text
def generate_ngrams(text, n):
    tokens = nltk.word_tokenize(text)
    return list(ngrams(tokens, n))

# Main function to process the data and generate n-grams
def process_and_generate_ngrams(df):
    df.fillna("")

    # Preprocess text columns
    df['title'] = df['title'].apply(preprocess_text)
    df['body'] = df['body'].apply(preprocess_text)

    # Merge text columns
    df['Merged'] = df['title'] + ' ' + df['body']

    # Generate n-grams
    unigrams, bigrams, trigrams = [], [], []
    for text in df['Merged']:
        unigrams.extend(generate_ngrams(text, 1))
        bigrams.extend(generate_ngrams(text, 2))
        trigrams.extend(generate_ngrams(text, 3))

    # Count n-grams
    unigram_counts = pd.Series(unigrams).value_counts().head(5)
    bigram_counts = pd.Series(bigrams).value_counts().head(5)
    trigram_counts = pd.Series(trigrams).value_counts().head(5)

    return unigram_counts, bigram_counts, trigram_counts

# Uncomment the line below to run the function with the file path
# unigrams, bigrams, trigrams = process_and_generate_ngrams(df)
# print("Top 5 unigrams:", unigrams)
# print("Top 5 bigrams:", bigrams)
# print("Top 5 trigrams:", trigrams)
