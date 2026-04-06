# Cosine similarity focuses on meaningful words, while Jaccard counts all words.
# The result differs because cosine similarity uses vector representation after preprocessing like stopword removal and stemming,
# whereas Jaccard similarity uses raw word sets.
import nltk
import numpy as np
from collections import defaultdict
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer

# Download required resources (run once)
nltk.download("punkt")
nltk.download("stopwords")


def preprocess_text(file_path):
    # Read file
    with open(file_path, "r") as file:
        text = file.read()

    # Tokenization
    tokens = word_tokenize(text.lower())

    # Stemming
    stemmer = PorterStemmer()
    stemmed_words = [stemmer.stem(word) for word in tokens]

    # Remove stopwords
    stop_words = set(stopwords.words("english"))
    filtered_words = [word for word in stemmed_words if word not in stop_words]

    # Word frequency (Term Frequency)
    word_count = defaultdict(int)
    for word in filtered_words:
        word_count[word] += 1

    return word_count


def cosine_similarity(vector1, vector2):
    dot_product = np.dot(vector1, vector2)
    norm1 = np.linalg.norm(vector1)
    norm2 = np.linalg.norm(vector2)

    if norm1 == 0 or norm2 == 0:
        return 0.0

    return dot_product / (norm1 * norm2)


def compute_similarity(dict1, dict2):
    # Unique words 
    all_words = list(set(dict1.keys()).union(set(dict2.keys())))

    # Create vectors
    vector1 = np.zeros(len(all_words), dtype=int)
    vector2 = np.zeros(len(all_words), dtype=int)

    for i, word in enumerate(all_words):
        vector1[i] = dict1.get(word, 0)
        vector2[i] = dict2.get(word, 0)

    return cosine_similarity(vector1, vector2)


# Main
if __name__ == "__main__":
    doc1 = preprocess_text("text1.txt")
    doc2 = preprocess_text("text2.txt")

    similarity = compute_similarity(doc1, doc2)

    print("Similarity between two text documents:", similarity)