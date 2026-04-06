# 1)Retrieve the indexed document no based on the query

import string
from collections import defaultdict

# Preprocessing function
def preprocess_text(text):
    text = text.lower()
    text = text.translate(str.maketrans("", "", string.punctuation))
    return text.split()


# Build inverted index
def build_inverted_index(documents):
    inverted_index = defaultdict(set)

    for doc_id, text in documents.items():
        words = preprocess_text(text)

        for word in words:
            inverted_index[word].add(doc_id)

    return inverted_index


# Search function (AND query)
def search(inverted_index, query):
    query_terms = preprocess_text(query)
    result = None

    for term in query_terms:
        if term not in inverted_index:
            return set()

        if result is None:
            result = inverted_index[term]
        else:
            result = result.intersection(inverted_index[term])

    return result if result else set()


# Documents
documents = {
    1: "Information retrieval is an essential aspect of search engines.",
    2: "The field of information retrieval focuses on algorithms.",
    3: "Search engines use techniques to improve performance.",
    4: "Deep learning models are used for information retrieval tasks."
}

# Build index
index = build_inverted_index(documents)

# Query
query = "retrieval"
result = search(index, query)

print("Documents containing query:", sorted(result))









# 2)Implement an inverted index concept to index
import nltk
from nltk.corpus import stopwords   

nltk.download('stopwords')

# Documents
doc1 = "The quick brown fox jumped over the lazy dog"
doc2 = "The lazy dog slept in the sun"

# Stopwords
stop_words = set(stopwords.words('english'))

# Tokenization
tokens1 = doc1.lower().split()
tokens2 = doc2.lower().split()

# Unique terms
terms = sorted(set(tokens1 + tokens2))

# Build inverted index
inverted_index = {}

for term in terms:
    if term in stop_words:
        continue

    postings = []

    if term in tokens1:
        postings.append(("Document 1", tokens1.count(term)))

    if term in tokens2:
        postings.append(("Document 2", tokens2.count(term)))

    inverted_index[term] = postings

# Display
for term in sorted(inverted_index):
    print(term, "->", inverted_index[term])






# 3) Display the inverted index in alphabetical order of terms.
import string
from collections import defaultdict

def preprocess(text):
    text = text.lower()
    text = text.translate(str.maketrans("", "", string.punctuation))
    return text.split()

def build_index(docs):
    index = defaultdict(set)

    for doc_id, text in docs.items():
        for word in preprocess(text):
            index[word].add(doc_id)

    return index


documents = {
    1: "Information retrieval is important",
    2: "Search engines use retrieval techniques",
    3: "Deep learning improves search"
}

index = build_index(documents)

print("Inverted Index (Alphabetical):")
for term in sorted(index):
    print(term, "->", sorted(index[term]))

print("\nTotal unique terms:", len(index))







# 4)Count and display the total number of unique terms indexed.
import nltk
from nltk.corpus import stopwords

# Download stopwords
nltk.download('stopwords')

# Documents
document1 = "The quick brown fox jumped over the lazy dog"
document2 = "The lazy dog slept in the sun"

# Stopwords
stopWords = stopwords.words('english')

# Tokenization
tokens1 = document1.lower().split()
tokens2 = document2.lower().split()

# Unique terms
terms = list(set(tokens1 + tokens2))

# Inverted index and frequency dictionaries
inverted_index = {}
occ_num_doc1 = {}
occ_num_doc2 = {}

# Build inverted index
for term in terms:
    if term in stopWords:
        continue

    documents = []

    if term in tokens1:
        documents.append("Document 1")
        occ_num_doc1[term] = tokens1.count(term)

    if term in tokens2:
        documents.append("Document 2")
        occ_num_doc2[term] = tokens2.count(term)

    inverted_index[term] = documents

print("\nInverted Index with Term Frequencies (Alphabetical Order):")
for term in sorted(inverted_index.keys()):
    print(term, "->", end=" ")
    for doc in inverted_index[term]:
        if doc == "Document 1":
            print(f"{doc} ({occ_num_doc1.get(term, 0)}),", end=" ")
        else:
            print(f"{doc} ({occ_num_doc2.get(term, 0)}),", end=" ")
    print()

print("\nTotal number of unique terms indexed:", len(inverted_index))


