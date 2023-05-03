from sklearn.feature_extraction.text import TfidfVectorizer

from Sanitisor import Sanitisor

collection = [
    'This is the JAVA document.',
 ]
filename = Sanitisor('resumes/Java.txt')

# Create a TfidfVectorizer object to calculate TF-IDF scores
vectorizer = TfidfVectorizer()
# Fit the vectorizer to the corpus of documents and transform the documents into TF-IDF vectors
tfidf_matrix = vectorizer.fit_transform(collection)

# Get output feature names for transformation.
print(vectorizer.get_feature_names_out())
# Print the TF-IDF scores of the terms in each document
print(tfidf_matrix.toarray())