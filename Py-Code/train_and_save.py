import pickle
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

# Load the IMDB dataset
print("Loading IMDB Dataset...")
data = pd.read_csv('IMDB Dataset.csv')

# Preprocess the data
data['label'] = data['sentiment']
data = data[['review', 'label']]

# Handle NaN values
data['review'].fillna('', inplace=True)

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(data['review'], data['label'], test_size=0.2, random_state=42)

# Convert reviews to numerical features
print("Vectorizing text (TF-IDF)...")
vectorizer = TfidfVectorizer(max_features=5000)
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

# Train the KNN model
print("Training KNN model...")
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train_vec, y_train)

# Evaluate
print("Evaluating model...")
predictions = knn.predict(X_test_vec)
accuracy = accuracy_score(y_test, predictions)
print(f'Accuracy: {accuracy:.4f}')
print(classification_report(y_test, predictions))

# Save model and vectorizer
print("Saving model and vectorizer...")
with open('models/knn_model.pkl', 'wb') as f:
    pickle.dump(knn, f)
with open('models/vectorizer.pkl', 'wb') as f:
    pickle.dump(vectorizer, f)

print("Done! Model saved to models/knn_model.pkl and models/vectorizer.pkl")
