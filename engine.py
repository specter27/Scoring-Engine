from sklearn.feature_extraction.text import TfidfVectorizer

from Extractor import Extractor


uploaded_resume_path = "resumes/Resume.docx"
# uploaded_job_description_path = ""
# 1. extracting & writing the resume content into text file
extracted_resume = Extractor(uploaded_resume_path, True)

print(extracted_resume.get_extracted_resume())

# job_description = []

# Create a TfidfVectorizer object to calculate TF-IDF scores
vectorizer = TfidfVectorizer(stop_words='english')
#
# Fit the vectorizer to the corpus of documents and transform the documents into TF-IDF vectors
tfidf_matrix = vectorizer.fit_transform(extracted_resume.get_extracted_resume())

# Calculate the TF-IDF vector for the query
# query_vector = vectorizer.transform(job_description)

# Get output feature names for transformation.
print(vectorizer.get_feature_names_out())

# Print the TF-IDF scores of the terms in each document
print(tfidf_matrix.toarray())