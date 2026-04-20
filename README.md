🎬 Review Sentiment Analysis Web App
📌 Overview
This project is a web-based AI application that classifies movie reviews as Positive or Negative using Natural Language Processing (NLP) and Machine Learning.
The model is trained on the IMDB movie reviews dataset, which contains thousands of labeled reviews used for sentiment classification tasks. Such datasets typically include large volumes of text labeled with binary sentiment (positive/negative) to train predictive models.
The application is deployed online using Replit, allowing users to interact with the model through a simple web interface.
🚀 Features
🧠 AI-based sentiment classification
💬 User input for real-time prediction
⚡ Fast and lightweight web app
🌐 Deployed online using Replit
📊 Trained on real-world IMDB dataset
🧩 Tech Stack
Programming Language: Python
Libraries:
Scikit-learn
NLTK
Pandas, NumPy
Machine Learning:
Text preprocessing (cleaning, tokenization, stopword removal)
Feature extraction (TF-IDF / Bag of Words)
Classification model
Web Deployment: Replit
📂 Project Structure
Review_sentiment/
│
├── app.py                # Main web application
├── model/                # Trained model files
├── templates/            # HTML frontend
├── static/               # CSS / assets
├── sentiment_model.pkl   # Saved ML model
├── vectorizer.pkl        # TF-IDF vectorizer
└── README.md
⚙️ How It Works
1. Input
User enters a movie review in the web app.
2. Preprocessing
The input text is cleaned using NLP techniques:
Lowercasing
Removing punctuation
Tokenization
Stopword removal
3. Feature Extraction
Text is converted into numerical format using:
TF-IDF (Term Frequency - Inverse Document Frequency)
4. Prediction
The trained model classifies the review as:
✅ Positive
❌ Negative
5. Output
Result is displayed instantly on the web interface.
🧠 Model Training
The model is trained using supervised machine learning techniques on labeled IMDB reviews.
Typical workflow:
Data preprocessing
Train-test split
Model training
Evaluation (accuracy, confusion matrix)
Common models used in sentiment analysis include:
Logistic Regression
LSTM (Deep Learning)
🌐 Deployment
The project is deployed using Replit, making it accessible online without local setup.
Steps followed:
Upload project files to Replit
Install required dependencies
Run app.py
Generate public web link
🖥️ How to Run Locally
# Clone repository
git clone https://github.com/HeckerG/Review_sentiment.git

# Navigate into folder
cd Review_sentiment

# Install dependencies
pip install -r requirements.txt

# Run application
python app.py
📊 Example
Input:
"This movie was absolutely amazing, I loved it!"
Output:
Positive ✅
🎯 Applications
Movie review analysis
Product review classification
Customer feedback analysis
Social media sentiment tracking
⚠️ Limitations
May struggle with sarcasm or complex language
Accuracy depends on training data quality
Limited to binary classification
🔮 Future Improvements
Add Neutral sentiment
Improve accuracy using deep learning (BERT, LSTM)
Enhance UI design
Add review history/dashboard
Deploy on cloud platforms (AWS / Render)
👨‍💻 Author
Developed by Krish Gulati
