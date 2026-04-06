# Stopword Removal (Direct Text)
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Download resources (run once)
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')

# Input sentence
text = "I went to the park yesterday and enjoyed a beautiful sunny afternoon with my friends."

# Tokenization
tokens = word_tokenize(text)
print("Tokens:", tokens)

# Stopwords
stop_words = set(stopwords.words('english'))

# Remove stopwords
filtered_words = [word for word in tokens if word.lower() not in stop_words]

print("After Stopword Removal:", filtered_words)

# B) Stopword Removal (From File -> Save to file)
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Download resources
nltk.download('punkt')
nltk.download('stopwords')

stop_words = set(stopwords.words('english'))

# Read input file
with open('my_story.txt', 'r') as file:
    text = file.read()

# Tokenize
tokens = word_tokenize(text)

# Remove stopwords
filtered_words = [word for word in tokens if word.lower() not in stop_words]

print("Filtered Words:", filtered_words)

# Write to output file
with open('cleaned_story.txt', 'w') as output_file:
    output_file.write(" ".join(filtered_words))

print("Cleaned text saved to cleaned_story.txt")