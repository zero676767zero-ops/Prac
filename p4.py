
from nltk.tokenize import sent_tokenize, word_tokenize, RegexpTokenizer, TweetTokenizer
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.corpus import wordnet
import nltk

nltk.download('punkt')
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')

text = input("Enter Text:\n")

sentences = sent_tokenize(text)
print("\nSentence Tokenization:")
print(sentences)

words = word_tokenize(text)
print("\nWord Tokenization:")
print(words)

tokenizer = RegexpTokenizer(r'\w+')
print("\nRegex Tokens:", tokenizer.tokenize(text))

tweet_tokenizer = TweetTokenizer()
print("\nTweet Tokenizer:", tweet_tokenizer.tokenize(text))

stemmer = PorterStemmer()
stemmed_words = [stemmer.stem(word) for word in words]
print("\nStemming:")
print(stemmed_words)

lemmatizer = WordNetLemmatizer()
lemmatized_words = [lemmatizer.lemmatize(word) for word in words]
print("\nLemmatization:")
print(lemmatized_words)

def get_wordnet_pos(word):
    tag = nltk.pos_tag([word])[0][1][0].upper()
    tag_dict = {
        "J": wordnet.ADJ,
        "N": wordnet.NOUN,
        "V": wordnet.VERB,
        "R": wordnet.ADV
    }
    return tag_dict.get(tag, wordnet.NOUN)

lemmatized_with_pos = [lemmatizer.lemmatize(word, get_wordnet_pos(word)) for word in words]
print("\nLemmatization with POS tagging:")
print(lemmatized_with_pos)



# Sentiment
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer

documents = [
    "This is a positive review.",
    "Great product, highly recommend.",
    "Terrible experience, very disappointed.",
    "Not satisfied with the service.",
    "Excellent quality and fast delivery."
]
labels = ["positive", "positive", "negative", "negative", "positive"]
# Convert text to numerical features (word counts)
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(documents)

# Create and train the MultinomialNB model
model = MultinomialNB()
model.fit(X, labels)

new_document = ["This product is amazing!", 
                "I am very disappointed with this movie."]

new_X = vectorizer.transform(new_document)
prediction = model.predict(new_X)

print(f"The new document is classified as: {prediction}")
