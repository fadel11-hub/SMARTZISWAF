import json
import random
import nltk
import string
import numpy as np
import pickle
import tensorflow as tf
from nltk.stem import WordNetLemmatizer
from tensorflow.keras.preprocessing.sequence import pad_sequences


class ChatBot:
    def __init__(self):
        self.responses = {}
        self.lemmatizer = WordNetLemmatizer()
        self.tokenizer = pickle.load(open('model/tokenizers.pkl', 'rb'))
        self.le = pickle.load(open('model/le.pkl', 'rb'))
        self.model = tf.keras.models.load_model('model/chat_model.h5')
        self.input_shape = 12

        nltk.download('punkt', quiet=True)
        nltk.download('wordnet', quiet=True)

        with open('dataset/IslamicBot.json', encoding="utf-8") as content:
            data = json.load(content)
        for intent in data['intents']:
            self.responses[intent['tag']] = intent['responses']

    def preprocess_text(self, text):
        text = ''.join([char.lower()
                       for char in text if char not in string.punctuation])
        return text

    def vectorize_text(self, text):
        text = self.preprocess_text(text)
        vector = self.tokenizer.texts_to_sequences([text])
        vector = np.array(vector).reshape(-1)
        vector = pad_sequences([vector], self.input_shape)
        return vector

    def predict_response(self, vector):
        output = self.model.predict(vector)
        output = output.argmax()
        response_tag = self.le.inverse_transform([output])[0]
        return response_tag

    def generate_response(self, text):
        vector = self.vectorize_text(text)
        response_tag = self.predict_response(vector)
        answer = random.choice(self.responses.get(response_tag, [
                               'Mohon maaf aku ga dapat memahaminya, tolong kasih pertanyaan yang jelas ya!']))
        return answer


# Contoh penggunaan ChatBot
bot = ChatBot()

# Test
question = "Assalamualaikum"
response = bot.generate_response(question)
print(response)
