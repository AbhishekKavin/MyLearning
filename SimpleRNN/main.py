import numpy as np
import tensorflow as tf
from tensorflow.keras.datasets import imdb
from tensorflow.keras.preprocessing import sequence
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, SimpleRNN, Dense
from tensorflow.keras.callbacks import EarlyStopping
from tensorflow.keras.models import load_model
import streamlit as st

word_index = imdb.get_word_index()
reverse_word_index = {value: key for key,value in word_index.items()}

model = load_model('simple_rnn_imdb.h5',compile = False)

def decode_review(text):
    return ' '.join([reverse_word_index.get(i-3, '?') for i in text])

def preprocess_text(text):
    words = text.lower().split()
    encoded_review = [word_index.get(word, 2) + 3 for word in words]
    padded_review = sequence.pad_sequences([encoded_review], maxlen = 500)
    return padded_review


st.title("IMDB Movie Review Sentiment Analysis")
st.write("Enter a movie review to predict its sentiment (Positive/Negative)")

user_input = st.text_area("Movie Review", "Type your review here...")

if st.button('Classify'):

    preprocessed_input = preprocess_text(user_input)

    sentiment = "Positive" if model.predict(preprocessed_input)[0][0] > 0.5 else "Negative"

    st.write(f"Sentiment: {sentiment}")
    st.write(f"Score: {model.predict(preprocessed_input)[0][0]}")
else:
    st.write("Please enter a review and click 'Classify' to see the sentiment.")