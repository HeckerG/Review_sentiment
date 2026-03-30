from flask import Flask, render_template, request, jsonify
import pickle
import os

app = Flask(__name__)

# Load the model and vectorizer
MODEL_PATH = 'models/knn_model.pkl'
VECTORIZER_PATH = 'models/vectorizer.pkl'

if not os.path.exists(MODEL_PATH) or not os.path.exists(VECTORIZER_PATH):
    print(f"Error: Model files not found. Run 'python Py-Code/train_and_save.py' first.")
    exit(1)

with open(MODEL_PATH, 'rb') as f:
    model = pickle.load(f)

with open(VECTORIZER_PATH, 'rb') as f:
    vectorizer = pickle.load(f)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    review = data.get('review', '')
    
    if not review.strip():
        return jsonify({'error': 'Review cannot be empty'}), 400
    
    # Vectorize and predict
    review_vec = vectorizer.transform([review])
    prediction = model.predict(review_vec)[0]
    distances, indices = model.kneighbors(review_vec)
    
    # Calculate confidence (1 - average distance normalized)
    confidence = max(0, 1 - (distances[0].mean() / 10)) * 100
    
    return jsonify({
        'sentiment': prediction,
        'confidence': round(confidence, 2)
    })

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=False, host='0.0.0.0', port=port)
