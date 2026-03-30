# Sentiment Analysis Web App

A simple local web application for sentiment analysis using IMDB dataset and KNN classifier.

## Setup & Installation

### 1. Activate the Virtual Environment

```bash
source .venv/bin/activate
```

### 2. Train and Save the Model (First Time Only)

```bash
python Py-Code/train_and_save.py
```

This will:
- Load the IMDB Dataset.csv
- Train a KNN classifier using TF-IDF vectorization
- Save the model to `models/knn_model.pkl`
- Save the vectorizer to `models/vectorizer.pkl`

**Note:** Make sure `IMDB Dataset.csv` is in the root directory.

### 3. Run the Web App

```bash
python app.py
```

You'll see:
```
 * Running on http://127.0.0.1:5000
```

### 4. Open in Browser

Open your browser and go to: **http://127.0.0.1:5000**

You should see a form where you can enter a review and click "Analyze Sentiment" to see if it's positive or negative.

## Project Structure

```
.
├── Py-Code/
│   ├── main.py                 # Original sentiment analysis script
│   └── train_and_save.py       # Training script (creates saved model)
├── app.py                      # Flask web server
├── templates/
│   └── index.html              # Web interface (form + styling)
├── models/                     # Directory for saved model files
│   ├── knn_model.pkl           # Trained KNN model
│   └── vectorizer.pkl          # TF-IDF vectorizer
└── IMDB Dataset.csv            # Dataset (you need to provide this)
```

## How It Works

1. **Training** (`train_and_save.py`):
   - Loads IMDB reviews and their sentiment labels
   - Converts text to TF-IDF vectors
   - Trains a KNN classifier
   - Saves both to disk

2. **Web App** (`app.py` + `index.html`):
   - Flask backend loads the saved model
   - When you submit a review, it's vectorized and sent to the model
   - The model predicts: **positive** or **negative**
   - Result displays on the web page

## Stopping the App

Press `Ctrl+C` in the terminal to stop the server.

## Deactivate Virtual Environment

```bash
deactivate
```

---

**For Class Assignment:** This is a complete local web app. No data is sent anywhere—everything runs on your machine!
