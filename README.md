# 📩 SMS Spam Detector

This is a simple and stylish web app built with **Streamlit** that detects whether an SMS or email message is spam or not using a Machine Learning model.

![Spam Detector UI](https://github.com/Ayush54555/SMS-Spam-Detector/raw/main/preview.png)

---

## 🚀 Features

- 🧼 Clean and modern UI with dark theme and gradients  
- 🧠 Uses a trained ML model with TF-IDF vectorization  
- 🔍 Pre-processing with NLTK: tokenization, stopword removal, stemming  
- ⚡ Real-time prediction using Streamlit  

---

## 🧠 How It Works

1. User enters a message into the text box.  
2. Text is cleaned (lowercased, punctuation and stopwords removed, stemmed).  
3. The cleaned text is converted into a TF-IDF vector.  
4. A pre-trained model classifies the message as **Spam** or **Not Spam**.

---

## 📂 Project Structure

```
├── app.py                # Streamlit web app  
├── vectorizer.pkl        # TF-IDF vectorizer (saved)  
├── model.pkl             # Trained ML model (saved)  
├── requirements.txt      # List of Python packages  
└── nltk_data/ (optional) # Local NLTK downloads (if bundled)  
```

---

## 🛠 Installation

1. **Clone this repository:**

```bash
git clone https://github.com/Ayush54555/SMS-Spam-Detector.git
cd SMS-Spam-Detector
```

2. **Install the dependencies:**

```bash
pip install -r requirements.txt
```

3. **Run the app:**

```bash
streamlit run app.py
```

---

## 🧾 NLTK Setup

If you encounter an error regarding missing NLTK data, run this once:

```python
import nltk
nltk.download('punkt')
nltk.download('stopwords')
```

To avoid issues on deployment, you can download these ahead of time and include them in an `nltk_data` folder.

---

## 🌐 Deployment

You can deploy this app easily on [Streamlit Cloud](https://streamlit.io/cloud):

- Link your GitHub repository  
- Set the app file to `app.py`  
- Done!

---

## 👤 Author

- [Ayush54555](https://github.com/Ayush54555)

---

## ⚠️ Disclaimer

This app is for educational/demo purposes. It should not be used as a production-grade spam filter.
