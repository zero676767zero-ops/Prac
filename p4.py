# BIGRAM
def generate_bigrams(text):
    bigrams = []
    for i in range(len(text) - 1):
        bigrams.append(text[i:i+2])   # cleaner slicing
    return bigrams


def calculate_jaccard(set1, set2):
    union = set1 | set2
    intersection = set1 & set2
    return union, intersection


# Input
string1 = "hello"
string2 = "yellow"

bigrams1 = generate_bigrams(string1)
bigrams2 = generate_bigrams(string2)

print("Bigrams of string1:", bigrams1)
print("Bigrams of string2:", bigrams2)

union, intersection = calculate_jaccard(set(bigrams1), set(bigrams2))

print("Union:", union)
print("Intersection:", intersection)

similarity = len(intersection) / len(union)
print(f"Bigram Jaccard Similarity: {similarity:.3f}")

print("-"*80)

# 2) TRIGRAM
def generate_trigrams(text):
    trigrams = []
    for i in range(len(text) - 2):
        trigrams.append(text[i:i+3])
    return trigrams


# Input
string1 = "hello"
string2 = "yellow"

trigrams1 = generate_trigrams(string1)
trigrams2 = generate_trigrams(string2)

print("Trigrams of string1:", trigrams1)
print("Trigrams of string2:", trigrams2)

union = set(trigrams1) | set(trigrams2)
intersection = set(trigrams1) & set(trigrams2)

print("Union:", union)
print("Intersection:", intersection)

similarity = len(intersection) / len(union)
print(f"Trigram Jaccard Similarity: {similarity:.3f}")

print("-"*80)
# Jaccard Coefficent for n-grams
def generate_ngrams(text, n):
    if not isinstance(text, str) or len(text) < n:
        return []
    return [text[i:i+n] for i in range(len(text) - n + 1)]


def jaccard_similarity(text1, text2, n):
    ngrams1 = generate_ngrams(text1.lower(), n)
    ngrams2 = generate_ngrams(text2.lower(), n)

    set1 = set(ngrams1)
    set2 = set(ngrams2)

    intersection = set1 & set2
    union = set1 | set2

    print(f"{n}-grams of text1:", ngrams1)
    print(f"{n}-grams of text2:", ngrams2)
    print("Intersection:", intersection)
    print("Union:", union)

    if len(union) == 0:
        return 0.0

    return len(intersection) / len(union)


# Example
string1 = "hello"
string2 = "yellow"
n = 3

similarity_score = jaccard_similarity(string1, string2, n)
print(f"Jaccard Similarity ({n}-gram): {similarity_score:.3f}")