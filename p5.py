import pandas as pd
import numpy as np
import pickle
from sklearn.model_selection import train_test_split
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential, load_model
from tensorflow.keras.layers import Embedding, Dense, LSTM

df = pd.read_csv('Reviews.csv')
df = df[['Text', 'Score']].dropna()

def label_sentiment(score):
    if score >= 4:
        return 'Positive'
    elif score == 3:
        return 'Neutral'
    else:
        return 'Negative'

df['Sentiment'] = df['Score'].apply(label_sentiment)

df_sample = df.sample(n=10000, random_state=42)

texts = df_sample['Text'].values
labels = df_sample['Sentiment'].values

label_dict = {'Negative': 0, 'Neutral': 1, 'Positive': 2}
labels_encoded = np.array([label_dict[label] for label in labels])

tokenizer = Tokenizer(num_words=5000)
tokenizer.fit_on_texts(texts)
sequences = tokenizer.texts_to_sequences(texts)

max_len = 100
padded_sequences = pad_sequences(sequences, maxlen=max_len)

X_train, X_test, y_train, y_test = train_test_split(
    padded_sequences, labels_encoded, test_size=0.2, random_state=42
)

model = Sequential()
model.add(Embedding(5000, 100, input_length=max_len))
model.add(LSTM(128))
model.add(Dense(3, activation='softmax'))

model.compile(loss='sparse_categorical_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])

model.fit(X_train, y_train, epochs=2, batch_size=32,
          validation_data=(X_test, y_test))

model.save('sentiment_model.h5')

with open('tokenizer.pkl', 'wb') as f:
    pickle.dump(tokenizer, f)

model = load_model('sentiment_model.h5')

with open('tokenizer.pkl', 'rb') as f:
    tokenizer = pickle.load(f)

def predict_sentiment(text):
    seq = tokenizer.texts_to_sequences([text])
    padded = pad_sequences(seq, maxlen=max_len)
    pred = model.predict(padded, verbose=0)
    return ['Negative', 'Neutral', 'Positive'][pred.argmax()]

examples = [
    "This product is amazing!",
    "It's okay",
    "Worst product ever"
]

for text in examples:
    print(text, "->", predict_sentiment(text))