from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from Extractor import Extractor

def pad_matrix(matrix_to_pad, matrix_to_refer):
    rows = len(matrix_to_refer)
    cols = len(matrix_to_refer[0])
    # creating a initial matrix with 0 as default value
    padded_matrix = [[0 for _ in range(cols)] for _ in range(rows)]
    for i in range(len(matrix_to_pad)):
        for j in range(len(matrix_to_pad[0])):
            padded_matrix[i][j] = matrix_to_pad[i][j]

    return padded_matrix

def sync_resume_vector(resume_vector, resume_tokens, jd_tokens, shape):
    # print(shape)
    synced_resume_vector = []
    missing_tokens = []
    fetched_vector = []
    for token_name in jd_tokens:
        try:
            target_index = resume_tokens.tolist().index(token_name)
            fetched_vector.append(resume_vector.toarray()[0, target_index])
        except ValueError:
            fetched_vector.append(0)
            missing_tokens.append(token_name)

    synced_resume_vector.append(fetched_vector)


    return {'synced_resume_vector': synced_resume_vector, 'missing_tokens': missing_tokens}


# 1. Get uploaded files local path
uploaded_resume_path = "resumes/Resume_RBC.docx"
uploaded_job_description_path = "job_descriptions/jd_extreme-networks.docx"

# 2. Converting Documents to their corresponding term matrix
# 2a_1. extracting & writing the resume content into text file
extracted_resume = Extractor(uploaded_resume_path, True, 0)
# 2a_2. create a TfidfVectorizer object to calculate TF-IDF scores
vectorizer1 = TfidfVectorizer(stop_words='english')
# 2a_3. fit the vectorizer to the corpus of documents and transform the documents into TF-IDF vectors
# resume_vector:- is a type of csr matrix
resume_vector = vectorizer1.fit_transform(extracted_resume.get_sanitised_file())
# 2a_4. extract keywords from resume
resume_tokens = vectorizer1.get_feature_names_out()
print(f"resume_tokens:-{resume_tokens}")

# TODO: Uncomment to code below for debugging purpose only
# print(f"resume vector shape:- {resume_vector.shape}")
# toarray():- method is used to convert a sparse matrix into a dense array
# print(resume_vector.toarray())
# -------------------------------------------------------------------
# TODO: printing the Tdidf matrix with feature names
# df_resumeVect = pd.DataFrame(data = resume_vector.toarray(),index = ['Doc1'], columns = resume_tokens)
# print("\nResume TD-IDF Vectorizer\n")
# print(df_resumeVect)
#---------------------------------------

# 2b_1. extracting & writing the job-description content into text file
extracted_job_description = Extractor(uploaded_job_description_path, True, 1)
# 2b_2. create a TfidfVectorizer object to calculate TF-IDF scores
# set stop_words parameter to 'english' in order
vectorizer2 = TfidfVectorizer(stop_words='english')
# 2b_3. Calculate the TF-IDF vector for the job_description
# jd_vector:- is a type of csr matrix
jd_vector = vectorizer2.fit_transform(extracted_job_description.get_sanitised_file())
# 2c_4. extract keywords from job_description
jd_tokens = vectorizer2.get_feature_names_out()
# print(f"jd_tokens:-{jd_tokens}")
# TODO: Uncomment to code below for debugging purpose only
# print(f"jd vector shape before padding:- {jd_vector.shape}")
# toarray():- method is used to convert a sparse matrix into a dense array
# print(jd_vector.toarray())
# ----------------------------------------------------------------------------

# 3. Padding the jd_vector to match resume_vector dimensions
# padded_jd_vector = pad_matrix(jd_vector.toarray(), resume_vector.toarray())
# print(f"jd vector shape after padding:- rows={len(padded_jd_vector)} columns={len(padded_jd_vector[0])}")
# print(padded_jd_vector)

# 3.
results = sync_resume_vector(resume_vector, resume_tokens, jd_tokens, jd_vector.shape)
# print(f"synced_resume:- {synced_resume}")


# 4. Calculate the cosine similarity between the query and the documents
cosine_similarities = cosine_similarity(results['synced_resume_vector'], jd_vector.toarray())

# 5. Extract the similarity value
cosine_similarity_value = cosine_similarities[0][0]
print("-------------MISSING TOKENS-----------------")
for index, value in enumerate(results['missing_tokens']):
    print(f"{index+1}. {value}")
print("---------------------------------------------")


# Print the cosine similarity values
print(f"MATCH SCORE (based on cosine-similarity of the documents term vectors):- {cosine_similarity_value}")

