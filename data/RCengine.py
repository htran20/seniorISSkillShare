import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel, cosine_similarity
# from sklearn.cluster import KMeans
from nltk.stem.porter import PorterStemmer
import pickle

# print("hehe")
#
# porter_stemmer = PorterStemmer()
# users = pd.read_excel('/Users/htran20/Desktop/isfile/django-ecommerce/data/mentorData/MentorInformation.xlsx' ,delimiter='\t',encoding='utf-8')
# users['tfidf'] = users['Major'].apply(lambda x: porter_stemmer.stem(x)) + ' ' +  users['Experience'].apply(lambda x: porter_stemmer.stem(x))
# # users['tfidf'] = users['tfidf'].apply(lambda x: porter_stemmer.stem(x))
# filename = './data/users_model.sav'
# pickle.dump(users, open(filename, 'wb'))
#
#
# users = pickle.load(open(filename, 'rb'))
# print(users)

def get_recommendations(description, users):
    porter_stemmer = PorterStemmer()
    stem_description = porter_stemmer.stem(description)
    NewDescription = pd.Series([stem_description])

    data = pd.concat([users['tfidf'], NewDescription], ignore_index=True)
    new_idx = -1

    tf = TfidfVectorizer(analyzer='word', ngram_range=(1, 2), stop_words='english')
    new_tfidf_matrix = tf.fit_transform(data)
    new_cosine_sim = linear_kernel(new_tfidf_matrix, new_tfidf_matrix)
    print(len(new_cosine_sim))
    # print (idx)
    sim_scores = list(enumerate(new_cosine_sim[new_idx]))

    # print (sim_scores)
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    top5_sim_scores = sim_scores[1:5]
    job_indices = []
    for i in top5_sim_scores:
        if i[1] > 0:
            job_indices.append(i[0])
    return users.iloc[job_indices]['Email'].tolist()
#
# a = get_recommendations("education", users)
# print(a)



