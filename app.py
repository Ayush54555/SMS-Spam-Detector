import streamlit as st
import pickle
import string
import nltk
nltk.download('punkt')
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

ps = PorterStemmer()

def transform_text(text):
    text = text.lower()
    text = nltk.word_tokenize(text)
    y = [i for i in text if i.isalnum()]
    y = [i for i in y if i not in stopwords.words('english') and i not in string.punctuation]
    y = [ps.stem(i) for i in y]
    return " ".join(y)

# Load model
tfidf = pickle.load(open('vectorizer.pkl', 'rb'))
model = pickle.load(open('model.pkl', 'rb'))

# Page settings
st.set_page_config(page_title="Spam Detector", page_icon="📩", layout="centered")

# Custom CSS from image reference
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;800&display=swap');

        html, body, .stApp {
            background-color: #000000;
            color: white;
            font-family: 'Poppins', sans-serif;
        }

        .emoji {
            font-size: 2.2rem;
            text-align: center;
            margin-bottom: -1rem;
        }

        .title-text {
            font-size: 3rem;
            font-weight: 800;
            background: linear-gradient(to right, #6a0572, #c71585, #e754b4);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            text-align: center;
            margin-bottom: 0.5rem;
        }

        .subtitle-text {
            font-size: 1.5rem;
            font-weight: 600;
            background: linear-gradient(to right, #6a0572, #c71585);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            text-align: center;
            margin-bottom: 2rem;
        }

        /* Label for input */
        label {
            color: white !important;
            font-family: 'Poppins', sans-serif;
            font-size: 1rem;
            font-weight: 500;
        }

        /* Input box style like your image */
        .stTextInput > div > div > input {
            background-color: #000000;
            border: 1px solid #c71585;
            border-radius: 10px;
            padding: 0.8rem;
            font-size: 1rem;
            font-family: 'Poppins', sans-serif;
            color: white;
            caret-color: white; /* ✅ Added this line */
        }

        /* Placeholder text color */
        .stTextInput > div > div > input::placeholder {
            color: #aaaaaa;
            font-size: 1rem;
        }

        /* Predict button */
        .stButton > button {
            background: linear-gradient(to right, #c71585, #e754b4);
            color: black;
            font-family: 'Poppins', sans-serif;
            text-transform: uppercase;
            font-weight: 700;
            font-size: 1rem;
            padding: 0.75rem 2rem;
            border: none;
            border-radius: 50px;
            box-shadow: none;
            transition: all 0.3s ease-in-out;
        }

        .stButton > button:hover {
            box-shadow: 0 0 15px rgba(231, 84, 180, 0.6);
            transform: scale(1.05);
        }

        .result-box {
            margin-top: 2rem;
            font-size: 1.8rem;
            font-weight: bold;
            text-align: center;
        }

        .spam {
            color: #ff4c4c;
        }

        .not-spam {
            color: #00ff7f;
        }
    </style>
""", unsafe_allow_html=True)

# Interface
st.markdown('<div class="emoji">📩</div>', unsafe_allow_html=True)
st.markdown('<div class="title-text">Spam Detector</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle-text">Check whether your message is Spam or Not</div>', unsafe_allow_html=True)

# Input
input_sms = st.text_input("Enter your message:", placeholder="Your message here...")

# Predict
if st.button("Predict"):
    transform_sms = transform_text(input_sms)
    vector_input = tfidf.transform([transform_sms])
    result = model.predict(vector_input)[0]
    if result == 1:
        st.markdown('<div class="result-box spam">🚨 This is SPAM!</div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="result-box not-spam">✅ This is NOT Spam!</div>', unsafe_allow_html=True)
