

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import re

nltk.download("stopwords")
nltk.download("punkt")
nltk.download("wordnet")


def preprocess_text(text):
    # Remove HTML tags and URLs
    text = re.sub('<[^<]+?>', '', text)
    text = re.sub(r'http\S+', '', text)

    # Tokenize text
    tokens = word_tokenize(text)

    # Remove stopwords
    stop_words = set(stopwords.words("english"))
    filtered_tokens = [word for word in tokens if word.lower() not in stop_words]

    # Lemmatization
    lemmatizer = WordNetLemmatizer()
    lemmatized_tokens = [lemmatizer.lemmatize(word) for word in filtered_tokens]

    return " ".join(lemmatized_tokens)


if __name__ == "__main__":
    # Load extracted data (replace this with your actual extracted data)
    extracted_data = [
        {"title": "Title 1", "description": "Description 1", "link": "https://example.com/1"},
        {"title": "Title 2", "description": "Description 2", "link": "https://example.com/2"},
        # Add more extracted data here
    ]

    preprocessed_data = []
    for item in extracted_data:
        preprocessed_title = preprocess_text(item["title"])
        preprocessed_description = preprocess_text(item["description"])
        preprocessed_link = preprocess_text(item["link"])
        preprocessed_data.append({"title": preprocessed_title, "description": preprocessed_description, "link": preprocessed_link})

    # Print preprocessed data
    for item in preprocessed_data:
        print("Preprocessed Title:", item["title"])
        print("Preprocessed Description:", item["description"])
        print("Preprocessed Link:", item["link"])
        print("--------------------")
