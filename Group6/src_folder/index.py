import spacy
from fasttext import load_model
import joblib

# Load spaCy English language model
nlp = spacy.load('en_core_web_sm')

# Load FastText sentiment model
sentiment_model = load_model('my_senti_model.bin')

# Load TF-IDF model and Linear Regression model for rating prediction
tfidf = joblib.load('tfidf_model.pkl')
rating_model = joblib.load('rating_model.pkl')

def predict_sentiment_and_rating(text):
    # Process the text with spaCy
    doc = nlp(text)

    # Predict sentiment
    sentiment_label, _ = sentiment_model.predict(text)
    sentiment = 'positive' if '__label__positive' in sentiment_label[0] else 'negative'

    # Predict rating
    transformed_review = tfidf.transform([text])
    predicted_rating = rating_model.predict(transformed_review)

    return sentiment, predicted_rating[0]

while True:
    print("\nOptions:")
    print("1. Predict sentiment and rating")
    print("2. Compare two reviews")
    print("Type 'exit' to quit.")
    choice = input("Please enter your choice: ").strip()

    if choice.lower() == 'exit':
        break

    if choice == "1":
        text = input("Please enter a movie review: ").strip()
        sentiment, rating = predict_sentiment_and_rating(text)
        print(f"This review seems {sentiment} to me!")
        print(f"Predicted rating: {rating:.2f}")

    elif choice == "2":
        review1 = input("Enter first review: ").strip()
        review2 = input("Enter second review: ").strip()

        doc1 = nlp(review1)
        doc2 = nlp(review2)

        similarity_score = doc1.similarity(doc2)
        print(f"Similarity between the two reviews: {similarity_score:.2f}")
