# 📩 SMS Spam Detector

This is a simple and stylish web app built with **Streamlit** that detects whether an SMS or email message is spam or not using a Machine Learning model.

![Spam Detector UI](https://github.com/Ayush54555/SMS-Spam-Detector/raw/main/preview.png)

---

## 🚀 Features

- Modern dark-themed UI with gradient accents  
- Real-time text classification using TF-IDF and a trained model  
- Custom text preprocessing using NLTK and stemming  
- Lightweight and fast — no deep learning required  

---

## 🧠 How It Works

1. User enters a message in the text input field.  
2. Text is cleaned: lowercased, tokenized, stopwords removed, and stemmed.  
3. TF-IDF vectorizer transforms the processed text.  
4. The model predicts whether it's Spam (1) or Not Spam (0).

---

## 📁 Project Structure

```
├── app.py             # Streamlit application
├── vectorizer.pkl     # TF-IDF vectorizer object
├── model.pkl          # Trained Machine Learning model
├── requirements.txt   # Python dependencies
└── nltk_data/         # Bundled NLTK resources (optional)
```

---

## ⚙️ Installation

```bash
git clone https://github.com/Ayush54555/SMS-Spam-Detector.git
cd SMS-Spam-Detector
pip install -r requirements.txt
streamlit run app.py
```

---

## 🧾 NLTK Handling (If Needed)

If you run into errors around missing NLTK resources like `punkt` or `stopwords`, run:

```python
import nltk
nltk.download('punkt')
nltk.download('stopwords')
```

For deployment reliability, you can bundle an `nltk_data/` folder locally so the app uses that directory instead of fetching resources at runtime.

---

## 🚀 Deployment

Deploy effortlessly on **Streamlit Cloud**:

- Connect your GitHub repository  
- Set the entry point to `app.py`  
- Let Streamlit install dependencies and run your app

---

## 👤 Author

- [Ayush54555 (GitHub)](https://github.com/Ayush54555)

---

## ⚠️ Disclaimer

This project is for demonstration and educational purposes. It’s not intended for production-level spam filtering systems.tional/demo purposes. It should not be used as a production-grade spam filter.
